# LLM → VLM 四階段訓練 Pipeline 的歷史演進（縱向章節素材）

> 研究範圍：2018-01 至 2026-04，聚焦「Continued Pre-Training（CPT） + Supervised Fine-Tuning（SFT） + Preference Alignment + Agent SFT」這套今日 VLM domain adaptation 標準 pipeline 的誕生與演化。
> 讀者設定：半導體製程技術負責人與實際跑訓練的工程師，目標是把 Qwen3-VL 類開源模型改造成 SEM 缺陷、OPC、wafer map、工單理解的 domain model。
> 所有關鍵事實附 inline URL；一手來源優先。

---

## 0. 全局地圖：一條 pipeline 走了七年

今天任何一位要把開源 VLM 改造成半導體 domain model 的工程師，打開 LLaMA-Factory、ms-swift、TRL 的設定檔，會看到四個階段：

1. **Continued Pre-Training（CPT）** — 餵 domain 無標註語料，讓 base model「說半導體話」。
2. **Supervised Fine-Tuning（SFT）** — 餵 domain instruction-response pair（含圖），教模型「做 domain 任務」。
3. **Preference Alignment（DPO / GRPO / KTO）** — 餵偏好對或二元訊號，修掉 SFT 的毛病（幻覺、啰嗦、拒答、格式漂移）。
4. **Agent / Tool-use SFT** — 餵 function-calling / GUI trajectory，教模型「會呼叫外部工具、會操作 MES/EDA 介面」。

這四階段不是 2024 某篇論文憑空設計出來的，而是 **2018-2024 整個開源 NLP/VLM 社群在血淚裡試出來的最大公約數**。每一階段都是前一代某個痛點的回應，每一個新方法都帶來新的麻煩——縱軸研究的價值，就在於看清每一次「解決 + 引入新問題」的辯證過程，這樣我們在半導體場景做選型時才知道為什麼選 DPO 而不是 PPO、為什麼要做 CPT 而不是只做 SFT、為什麼要上 DoRA 而不是純 LoRA。

以下按時間軸還原這條 pipeline 的演化。

---

## 1. 前奏期（2018-2020）：「Pretrain → Fine-tune」範式的確立

### 1.1 ULMFiT（2018-01）：三階段 fine-tune 的祖師爺

在 BERT 之前半年，Jeremy Howard（fast.ai）與 Sebastian Ruder（DeepMind）在 arxiv 放上了 **ULMFiT（Universal Language Model Fine-tuning for Text Classification）**，這是 CV 領域那套「ImageNet pretrain → downstream fine-tune」思想第一次被系統性搬到 NLP，並提出**三階段**的完整流程：(a) 在 general-domain corpus 上訓練 LM；(b) 在 target task 資料上 fine-tune LM（discriminative fine-tuning + slanted triangular learning rates）；(c) 在 target task 上 fine-tune classifier（gradual unfreezing）[https://arxiv.org/abs/1801.06146]。

ULMFiT 用的是 AWD-LSTM 而不是 Transformer，它的三個技巧——**discriminative LR、STLR、gradual unfreezing**——到今天在 PEFT 代碼庫裡還能看到影子（例如 LLaMA-Factory 的 `freeze_trainable_layers` 就是 gradual unfreezing 的精神延續）。

**為什麼是 Howard 和 Ruder？** fast.ai 長期推動「遷移學習 + 小資料」的實用主義，Ruder 則是 NLP 遷移學習的理論派。兩人合流後把 CV 的直覺輸入 NLP，正好踩在 Transformer 革命的前夜。

**遺產**：把「pretrain → fine-tune」寫進 NLP 的肌肉記憶。今天半導體做 domain adaptation，「用通用語料預訓練的 base model + domain 資料 fine-tune」這個預設，就是 ULMFiT 建立的。

### 1.2 BERT 的 domain-adaptive 拓展（2019）：BioBERT / SciBERT / FinBERT

2018 底 BERT 橫空出世之後，馬上有人發現：直接 fine-tune 通用 BERT 到醫學 NER 雖然能用，但效果遠遜於先在 PubMed 上繼續預訓練再 fine-tune。於是 2019 出現了三個代表性「領域 BERT」：

- **BioBERT**（DMIS Lab, 2019）— PubMed abstracts + PMC full text 繼續預訓練，生物醫學 NER / RE / QA 全面超越 BERT [https://arxiv.org/abs/1903.10676 指 SciBERT；BioBERT 的原文是 arxiv 1901.08746]。
- **SciBERT**（Beltagy 等, AI2, 2019）— 1.14M 科學論文重新訓練，而且用 **SciVocab** 而非直接沿用 BERT 詞表 [https://arxiv.org/abs/1903.10676]。SciBERT 提出了一個關鍵洞察：**domain 適應不只是繼續預訓練權重，還得重建詞表**（in-domain vocabulary），這在半導體場景尤其重要——「EUV」「NILS」「MEEF」「SRAM leakage」在 BPE 下會被切成無語義碎片。
- **FinBERT**（Yang 等, 2020）— 金融語料 [https://arxiv.org/abs/2006.08097]。

這三篇不同 lab 各自做但結論完全一致：**通用 pretrain 到 domain task 中間，該有一個 domain CPT 層**。這是今天「CPT 階段」的源頭。

### 1.3 Gururangan「Don't Stop Pretraining」（ACL 2020）：把 CPT 正式寫進教科書

Gururangan、Marasović、Smith 等人的 ACL 2020 長文 **"Don't Stop Pretraining: Adapt Language Models to Domains and Tasks"** [https://arxiv.org/abs/2004.10964] 是第一篇把 CPT 升格為**標準階段**的系統性研究。

他們區分了兩個子階段：
- **DAPT（Domain-Adaptive Pre-Training）**：在一大包 domain unlabeled corpus 上繼續預訓練。
- **TAPT（Task-Adaptive Pre-Training）**：在 target task 本身的 unlabeled training data 上繼續預訓練。

跨 4 個領域（biomed、CS、news、reviews）× 8 個 task 的實驗顯示：**DAPT 和 TAPT 是正交增益**——做了 DAPT 之後再做 TAPT 仍然會漲點，high-resource 和 low-resource 場景都有效 [https://github.com/allenai/dont-stop-pretraining]。

**對半導體的啟發**：
- DAPT = 餵整廠 20 年的製程文件、FA report、EDA manual；
- TAPT = 針對「SEM 缺陷分類」這個具體任務，把所有相關的缺陷描述 unlabeled 撒一輪；
- 之後才 SFT。

這個「DAPT → TAPT → SFT」三層結構直接被後來的 DeepSeek、Qwen、InternLM 繼承下去，只是到了 VLM 時代多了一個視覺對齊的 warm-up，變成「Alignment Pre-training → Vision CPT → SFT」。

---

## 2. LLM 三階段成型（2020-2022）：Scale + RLHF 把 pipeline 定格

### 2.1 GPT-3（2020-05）：in-context learning 帶來範式動搖

Brown 等人的 **"Language Models are Few-Shot Learners"**（arxiv 2005.14165, NeurIPS 2020）是 175B 參數的 GPT-3 首秀 [https://arxiv.org/abs/2005.14165]。它的核心發現——scale 起來之後 **few-shot in-context learning** 在很多任務上能逼近 fine-tune 的 SOTA——在短期內甚至動搖了「要不要 fine-tune」這個問題本身。

但很快大家發現 ICL 有兩個致命傷：(1) 對 prompt 的 wording 極敏感；(2) 沒辦法把私域知識和私域格式灌進去。這兩點對半導體來說尤其致命——製程文件裡的私有詞彙、工單的固定 schema、SEM 缺陷的私有分類標準，通通不可能靠 8-shot prompt 解決。**ICL 回答了「能不能用」，fine-tune 回答了「能不能用在自己家」。**

### 2.2 T5（2020-02, Raffel 等）：Unified Text-to-Text

Google 的 T5（arxiv 1910.10683, JMLR 2020） [https://arxiv.org/abs/1910.10683] 用一句「所有 NLP 任務都可以寫成 text-in text-out」把分類、翻譯、QA、summarization 統一到單一 loss 函數下。這個思想直接預告了 **instruction tuning**：如果任務可以寫成自然語言描述，那就可以用自然語言指令來驅動模型——為 Flan、InstructGPT 鋪路。

### 2.3 InstructGPT（2022-03, Ouyang 等）：三階段正式命名

Ouyang 等人的 **"Training language models to follow instructions with human feedback"**（arxiv 2203.02155） [https://arxiv.org/abs/2203.02155] 是今天 pipeline 的**直接祖先**，明確提出三步：

1. **SFT**（supervised fine-tuning）：人類寫示範，fine-tune GPT-3。
2. **RM**（reward model）：人類 rank 多個回答，訓練 RM。
3. **PPO-RLHF**：用 RM 當 critic，PPO 優化 policy。

最轟動的結果是：**1.3B 的 InstructGPT 在人類偏好上打敗 175B 的 GPT-3**。這個「對齊贏過規模」的事實奠定了 RLHF 在隨後兩年的統治地位，也把「SFT + preference alignment」永久寫進 pipeline。

**為什麼是 OpenAI？** 他們有人、有 GPU、有用戶。RLHF 之前就在 summarization（Stiennon 2020）和 preferences（Christiano 2017）做過，InstructGPT 是這條線的產品化結晶。

**留給半導體的問題**：RLHF 需要人類偏好標註，半導體領域找不到像 ShareGPT 那樣的公開偏好資料，corner case 又特別多（一個缺陷被誤判 0.1% 就是幾百萬美元損失），所以偏好訊號必須從 domain expert 手中擠出來——這直接催生了後來 DPO / KTO 這類「更省資料」的偏好對齊方法的需求。

### 2.4 LLaMA（2023-02, Touvron 等）：開源可微調基底

Meta 的 LLaMA（arxiv 2302.13971） [https://arxiv.org/abs/2302.13971] 在 2023-02-24 開源 7B-65B 四個規模，只用公開資料訓練，**LLaMA-13B 在多數 benchmark 超越 GPT-3 175B**。它改變了遊戲規則——開源社群終於有了一個「能在一張 A100 上 fine-tune 的合格 base model」。隨後三年所有開源 SFT / DPO / Agent SFT 的工具鏈，幾乎都是圍繞 LLaMA 生態建立的。

### 2.5 Alpaca / Vicuna / Dolly（2023-03~04）：instruction tuning 平民化

- **Stanford Alpaca**（2023-03-13）：用 52K 條 self-instruct 生成資料 fine-tune LLaMA-7B，只花 $600 [https://crfm.stanford.edu/2023/03/13/alpaca.html]。
- **Vicuna**（2023-03）：用 ~70K 條 ShareGPT 用戶對話 fine-tune LLaMA-13B，得到「90% of ChatGPT quality」的開源模型。
- **Dolly v2**（Databricks, 2023-04-12）：**第一個商業可用的開源 instruction 模型**，用 5,000 名員工人工寫的 15K 條指令（databricks-dolly-15k） [https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm]。

三件事同時發生的意義：**SFT 的資料配方從此有了三條開放路線**——
- 蒸餾路線（Alpaca 用 text-davinci-003 蒸）
- ShareGPT 路線（Vicuna）
- 純人工路線（Dolly）

今天半導體 domain SFT 幾乎就是這三條路線的再運用：蒸餾（用 GPT-4o 或 Claude 幫忙寫工單處理 demo）、用戶日誌（如果有內部聊天介面）、純人工（資深工程師一條條寫）。

---

## 3. VLM 爆發（2023）：把「看」焊到 LLM 上

2023 年上半年對 VLM 來說是寒武紀大爆發，半年內主流架構幾乎全部確立。**核心問題只有一個：怎麼把一個 pretrained frozen LLM 和一個 pretrained frozen vision encoder 接起來？** 下面四個代表作給出了四種不同答案。

### 3.1 BLIP-2（2023-01-30, Salesforce）：Q-Former 路線

Li 等的 BLIP-2 [https://arxiv.org/abs/2301.12597] 用一個輕量的 **Q-Former**（Querying Transformer, 12 層 BERT-like, 32 × 768 query embeddings）夾在 frozen ViT 和 frozen LLM 之間 [https://www.salesforce.com/blog/blip-2/]，兩階段預訓練：
1. Stage 1（vision-language representation learning）：Q-Former 學會從影像裡抽取「可被 text 描述的」特徵。
2. Stage 2（vision-to-language generation）：Q-Former 輸出接到 frozen LLM 上，學會讓 LLM 看懂自己的輸出。

**總可訓練參數 < 2%**。這是第一次讓「凍結兩個巨型 pretrain、只訓一個橋樑」變成可行方案——後來幾乎所有 PEFT 類 VLM 的思想原型都在這裡。

### 3.2 LLaVA v1（2023-04-17）：Visual Instruction Tuning 範式

Haotian Liu 等人的 LLaVA（arxiv 2304.08485, NeurIPS 2023 Oral） [https://arxiv.org/abs/2304.08485] 比 BLIP-2 激進得多：**只用一個 linear projection** 把 CLIP ViT-L/14 的視覺特徵塞進 Vicuna。兩階段訓練：
1. Feature alignment pretrain（CC-595K）：只訓 projection。
2. Visual instruction fine-tune（158K 用 language-only GPT-4 生成的多模態 instruction-response pair）：projection + LLM 一起更新，visual encoder 凍結。

LLaVA 最大的貢獻是**「Visual Instruction Tuning」這個詞**——它把「指令微調」從純文字搬到多模態，並示範了可以用 **LLM 自己合成多模態 SFT 資料**（給 GPT-4 看 COCO caption 讓它寫多輪問答）。這個資料合成思想到今天還是半導體場景解「人工標註太貴」的主力武器。

### 3.3 MiniGPT-4（2023-04-20）：同日期平行線

Vision-CAIR 的 MiniGPT-4 [https://arxiv.org/abs/2304.10592] 幾乎和 LLaVA 同週發布：frozen BLIP-2 視覺編碼器 + frozen Vicuna + 一個 projection layer。設計上比 LLaVA 更保守（全凍除 projection），但把 2D 空間推理、網頁草圖轉 HTML 這類能力的可行性秀了出來。

**LLaVA vs MiniGPT-4**：LLaVA 賭「解凍 LLM + 合成資料」，MiniGPT-4 賭「全凍 + 少量高品質資料」。後來的發展證明 LLaVA 的路線更可擴展（因為能吃下更多資料），但 MiniGPT-4 的「全凍」策略對 GPU 緊缺的學術組還是有啟發。

### 3.4 LLaVA-1.5（2023-10）：把配方穩定下來

Liu 等人的 **"Improved Baselines with Visual Instruction Tuning"**（arxiv 2310.03744）把 LLaVA 的配方打磨成今天大家熟悉的樣子：MLP projection（不再是 linear）、學術 VQA 資料加回來、higher-res 輸入。這篇之後，社群有了一個「照著做就能出 7B 合理 VLM」的 recipe。

### 3.5 Qwen-VL / Qwen-VL-Chat（2023-08-22, Alibaba）

Bai 等人的 Qwen-VL（arxiv 2308.12966） [https://arxiv.org/abs/2308.12966] 是中國開源 VLM 的第一個里程碑：Qwen-7B LLM 接一個 ViT，**三階段訓練**（vision-language pretrain → multi-task pretrain → SFT），並引入了「bounding box in, bounding box out」的定位能力。

**為什麼重要？** Qwen-VL 是第一個把「三階段 VLM pipeline」規範化的中文開源模型，也是今天半導體場景最常被拿來當 base 的 Qwen-VL 系列起點。

### 3.6 CogVLM（2023-11, 清華 THUDM）：Visual Expert 路線

Wang 等人的 CogVLM（arxiv 2311.03079） [https://arxiv.org/abs/2311.03079] 提出第三條架構路線：在 attention 和 FFN 裡**插入並聯的 visual expert module**，讓視覺 token 走自己的 QKV 通路。CogVLM-17B 在 10 個 benchmark 上達到 SOTA，並在 NLP 任務上完全不退步（因為 text token 走的還是原 LLM 路徑）。

### 3.7 InternVL 1.0（2023-12, OpenGVLab）：把 vision side 做大

上海 AI 實驗室 / 商湯系的 InternVL 1.0 [https://github.com/OpenGVLab/InternVL]  反其道而行——大家都在把 LLM 做大，它把 **vision encoder 做到 6B（InternViT-6B）**，配一個 QLLaMA 當中間件。14B 總參數、CVPR 2024 Oral。這條「vision encoder 和 LLM 參數量匹配」的路線後來被 Qwen2-VL、InternVL 2 / 2.5 繼承。

**三大陣營總結（到 2023 年底）**：
| 路線 | 代表 | 中間件 | 賭注 |
|---|---|---|---|
| Q-Former | BLIP-2 | 小 BERT | 極致參數效率 |
| MLP projection | LLaVA / MiniGPT-4 | 2 層 MLP | 資料規模壓倒架構複雜度 |
| Visual Expert | CogVLM | 並聯 expert | 深度融合 |
| Big ViT | InternVL | QLLaMA | vision 側 scale |

半導體場景今天基本上只看到 **MLP projection（LLaVA 系）** 和 **Big ViT（Qwen / InternVL 系）** 兩條路線活下來。原因是它們都把視覺 token 直接餵進 LLM 的 token 空間，最容易做 downstream 的 LoRA / DPO。

---

## 4. PEFT 普及（2021-2024）：讓消費級 GPU 也能 fine-tune

### 4.1 LoRA（Hu 等, 2021-06-17）：PEFT 的拐點

Edward J. Hu 等（Microsoft）的 LoRA（arxiv 2106.09685） [https://arxiv.org/abs/2106.09685] 思想極簡：**凍結原權重 W，在每層注入一個低秩矩陣 ΔW = BA（B ∈ R^{d×r}, A ∈ R^{r×k}, r << min(d,k)）**，只訓練 A、B。

- 相對 GPT-3 175B 全量 Adam，**參數量降 10000 倍，GPU 記憶體降 3 倍**。
- 推理時可以把 BA 合併回 W，**零額外延遲**。

LoRA 的重要不在技術新穎（低秩分解是老概念），而在時機精準——它在 2022 底 ChatGPT 爆紅之前就已經開源並整合進 HuggingFace PEFT。到 2023 LLaMA / Alpaca 潮起來時，所有學術組都在用它。

### 4.2 QLoRA（Dettmers 等, 2023-05-23）：把門檻壓到單卡

Tim Dettmers 等的 QLoRA（arxiv 2305.14314） [https://arxiv.org/abs/2305.14314] 把 base model 做 **4-bit NF4 量化**，然後在 frozen 4-bit 權重上掛 LoRA adapter，兩個 trick：
1. **4-bit NormalFloat（NF4）**：針對正態分佈的理論最佳資料型態。
2. **Double Quantization + Paged Optimizer**：把量化常數本身也量化、用 CUDA unified memory 管記憶體峰值。

結果：**一張 48GB GPU 就能 fine-tune 65B 模型**，Guanaco 在 Vicuna benchmark 上達到 ChatGPT 99.3% 的表現，訓練時間 24 小時。這一槌子把開源 fine-tune 的門檻從「需要 A100 集群」壓到「一張 A6000 就行」，半導體這種資料不能外流的場景終於有了可落地的開源路徑。

### 4.3 Adapter / Prefix Tuning / Prompt Tuning（對照組）

在 LoRA 之前，PEFT 家族已有三個先行方案：
- **Adapter Tuning**（Houlsby 2019）：每層插兩個瓶頸 MLP；推理時延遲會增加。
- **Prefix Tuning**（Li & Liang 2021）：在每層 KV cache 前加一段可訓練 prefix。
- **Prompt Tuning**（Lester 2021）：只訓 soft prompt。

LoRA 在這三者中勝出的原因有三：(1) 零推理延遲；(2) 可與量化、FlashAttention 無縫組合；(3) 可合併、可熱插拔多 adapter。

### 4.4 LoRA 後繼者的演化時間線（2024）

- **LoRA+**（Hayou 等, 2024-02）— 給 A 和 B 用**不同學習率**（B 的 LR 設大一些），更好收斂。
- **DoRA**（Liu 等, NVIDIA, 2024-02-14, ICML 2024 Oral） [https://arxiv.org/abs/2402.09353]— **Weight-Decomposed LoRA**：把 W 分解成 magnitude 和 direction 兩部分，方向向量用 LoRA 更新，magnitude 單獨學。在 LLaMA、LLaVA、VL-BART 上一致超越 LoRA，且**無額外推理成本**。已併入 HuggingFace PEFT。
- **rsLoRA**（Rank-Stabilized LoRA）— 修正 LoRA 在高 rank 時的訓練不穩定。
- **VeRA**（Kopiczko 等, ICLR 2024） — 所有層共享一對 random 投影矩陣，只訓 per-layer scaling；比 LoRA **再降 100 倍參數**。
- **PiSSA**（Meng 等, 2024-04-03, NeurIPS 2024 Spotlight） [https://arxiv.org/abs/2404.02948]— 用 **SVD 主成分**初始化 A、B（而不是 LoRA 的 Gaussian + Zero），把「重要的權重方向」直接當起點。在 GSM8K 上 Mistral-7B 達到 72.86%，超越 LoRA 的 67.7%。

**給半導體的路線建議**：
- 資料量大（>10 萬 instruction）、GPU 充足 → DoRA + rank 64，取代 LoRA。
- 資料量小 → PiSSA 初始化，避免小資料下 Gaussian 噪聲起點拖慢收斂。
- 多 domain 同時 fine-tune（SEM + OPC + 工單）→ VeRA 或 LoRA multi-adapter 熱插拔。
- 單卡部署 72B → QLoRA + NF4 仍是唯一選項。

---

## 5. 偏好對齊演化（2022-2025）：從 PPO 到 GRPO 的七代進化

對齊階段是 pipeline 裡**技術分歧最大**的一段，七年內出現了十幾個變體。下面按「痛點 → 新方法 → 新痛點」的辯證鏈條講。

### 5.1 RLHF-PPO（InstructGPT, 2022-03）— 起點
- **做法**：SFT → 訓 RM → PPO 優化 policy（+ KL penalty to SFT）。
- **痛點**：四個 model 同時在顯存裡（policy / value / ref / RM），超吃資源；PPO 超參數敏感；訓練不穩定。
- **適合**：有 reward signal、corner case 多、可以接受工程複雜度的場景（OpenAI / Anthropic 內部）。

### 5.2 RLAIF / Constitutional AI（Anthropic, 2022-12）— RM 的替身
Yuntao Bai 等 Anthropic 團隊的 Constitutional AI（arxiv 2212.08073, 2022-12-15） [https://arxiv.org/abs/2212.08073] 把 **「誰來產生偏好對」** 從人類換成 AI：先給模型一部「憲法」（原則列表），讓它自我 critique & revise（SL-CAI），再用 AI feedback 做 RL（RLAIF）。這是第一次把偏好資料的成本從「標註員時薪 $20」壓到「API 呼叫 $0.01」。

對半導體的啟發：domain 偏好資料可以用 **老 domain expert 寫一套「製程寫作憲法」+ 強 LLM 自動評審**來大量合成，不必逐條請工程師標。

### 5.3 DPO（Rafailov 等, 2023-05-29）— 把 RM 直接解析消掉
Rafailov 等人的 DPO（arxiv 2305.18290, NeurIPS 2023 Outstanding Paper） [https://arxiv.org/abs/2305.18290] 是過去三年對齊領域最大的方法論翻轉。他們證明：Bradley-Terry 偏好模型下，**最優 policy 有閉式解，可以直接當 log-softmax loss 最佳化**——不需要單獨訓 RM、不需要 PPO、不需要從 policy sample。

- 只需 preference pair `(prompt, chosen, rejected)`；
- 只需 **2 個模型在顯存**（policy + frozen ref）；
- 實現 < 100 行 PyTorch。

DPO 解決了 PPO 的資源和穩定性問題，但帶來新痛點：
- **distribution shift 敏感**：DPO 是 offline 的，policy 偏離 ref 太遠後 loss 不可靠。
- **length bias**：模型傾向生成長回答（因為 chosen 平均比 rejected 長）。
- **reference model bottleneck**：還是需要一個 ref model 算 log-ratio。

### 5.4 IPO（Azar 等, DeepMind, 2023-10）— DPO 的正則化
Gheshlaghi Azar 等人的 **"A General Theoretical Paradigm to Understand Learning from Human Preferences"**（arxiv 2310.12036） [https://arxiv.org/abs/2310.12036] 提出 ΨPO 一般化框架，IPO 是其特例：用 **identity 函數取代 DPO 裡的 log-sigmoid**，避免偏好確定性（win rate → 1）時出現的過擬合。理論上比 DPO 更抗 over-training。

### 5.5 KTO（Ethayarajh 等, 2024-02-02）— 不要 preference pair 了
Kawin Ethayarajh（Stanford / Contextual AI）等人的 KTO（arxiv 2402.01306） [https://arxiv.org/abs/2402.01306] 用 Kahneman-Tversky prospect theory，證明偏好 loss 函數屬於一類 human-aware losses（HALOs）。最關鍵的實務突破：**只需要「這個回答是好還是壞」的二元訊號**，不需要成對比較。

對半導體的意義巨大——收 preference pair 成本高（要 QC 工程師同時看兩個回答），但「這個缺陷分類回答對不對」是每天 line 上都在做的事。KTO 直接把這些日常 QC 訊號變成對齊資料。

### 5.6 ORPO（Hong 等, 2024-03-12）— SFT 和對齊合併成一步
Hong、Lee、Thorne 的 ORPO（arxiv 2403.07691, EMNLP 2024） [https://arxiv.org/abs/2403.07691] 提出**monolithic preference optimization**：在 SFT NLL loss 上加一個 log odds ratio 項，一步走完 SFT + alignment。**不需要 reference model、不需要單獨 SFT stage**。

在 Phi-2、LLaMA-2、Mistral-7B 上，ORPO + UltraFeedback 單步訓練超越了 LLaMA-2-Chat 和 Zephyr 的 SFT+DPO 兩步流程。

### 5.7 SimPO（Meng 等, 2024-05-23, Princeton NLP）— 連 ref model 都不要
Yu Meng 等人的 SimPO（arxiv 2405.14734, NeurIPS 2024） [https://arxiv.org/abs/2405.14734] 把 DPO 的 implicit reward 換成 **length-normalized average log-prob**，並加 **target reward margin**。結果：
- **沒有 reference model** → 顯存再減半；
- 對 length bias 有原生緩解；
- 在 AlpacaEval 2 上比 DPO 高 6.4 分、Arena-Hard 高 7.5 分；
- Gemma-2-9B-it + SimPO 登頂 10B 以下 Chatbot Arena。

### 5.8 GRPO（DeepSeek, 2024-02-05）— 把 value model 也消掉
DeepSeek 的 DeepSeek-Math（arxiv 2402.03300） [https://arxiv.org/abs/2402.03300] 在 PPO 流程裡拿掉了 critic，用**同一 prompt 下 group 內多個 sample 的 reward 均值**當 baseline 估 advantage。這變成後來 DeepSeek-R1 和 Qwen3 reasoning 模型的核心 RL 算法。

GRPO 特別適合**有 verifiable reward**的場景（數學對錯、代碼是否通過 unit test）。半導體有類似場景：SEM 缺陷分類對不對可以自動驗證、wafer map pattern 是否符合規格可以自動驗證——這讓 GRPO 成為半導體 VLM domain 後訓練一個非常有吸引力的選項。

### 5.9 Iterative DPO / Online DPO / Self-Rewarding（2024）
- **Self-Rewarding LM**（Yuan 等, Meta, 2024-01, arxiv 2401.10020）：模型同時扮演 actor 和 judge，自己評分自己生成的候選、再用 DPO 迭代。三輪迭代超越 Claude 2 / GPT-4 0613（在 AlpacaEval 2.0）。
- **Iterative DPO**：每輪用當前 model 生成候選、重新收集 preference、再 DPO，緩解 offline distribution shift。
- **Online DPO**：邊訓邊採，更接近 PPO 的 online 特性但不需 critic。

**演化骨架圖**：
```
RLHF-PPO (2022)    資源重、不穩
   ↓ 消掉 RM
DPO (2023-05)      閉式解、offline
   ↓ 消掉 ref model          ↓ 消掉 pair 要求
SimPO (2024-05)              KTO (2024-02)
   ↓ 合併 SFT+對齊           ↓ 加 prospect theory
ORPO (2024-03)              (已含在 KTO)
                  並行線：消掉 critic
                  GRPO (2024-02) — verifiable reward 場景首選
                  並行線：自我迭代
                  Self-Rewarding / Iterative DPO (2024)
```

**對半導體的選型**：
- 單機 7B 模型、少量 preference pair → **DPO** 是最安全選擇（生態最成熟）。
- 只能收到「好/壞」二元訊號（QC pass/fail） → **KTO**。
- 想把 SFT 和對齊合併省一個階段 → **ORPO**。
- 缺陷分類有 verifiable ground truth → **GRPO**（推理/分類型任務首選）。
- 資料品質參差 → **SimPO**（length-normalized，緩解長度偏好）。

---

## 6. VLM 世代交替（2024-2025）：Native Resolution 時代

2024 是 VLM 的「原生解析度元年」。2023 年的 VLM 都有一個共同毛病：輸入影像被強制縮放到 224×224 或 336×336，高解析度文件、晶圓顯微鏡圖像細節全丟。2024 的幾個主流模型用不同方法解決這個問題。

### 6.1 Qwen2-VL（2024-08-29）：Naive Dynamic Resolution + M-RoPE
Wang、Bai 等的 Qwen2-VL（arxiv 2409.12191） [https://arxiv.org/abs/2409.12191] 引入兩個關鍵架構創新：
- **Naive Dynamic Resolution**：影像按原生解析度進，動態轉成可變數量的 visual token，不再強制 resize；
- **M-RoPE（Multimodal Rotary Position Embedding）**：把 RoPE 拆成 temporal / height / width 三軸，讓模型原生理解多模態的空間-時間位置。

規模：2B / 8B / 72B。Qwen2-VL-72B 在多個 benchmark 與 GPT-4o、Claude 3.5 Sonnet 打平。

對半導體的意義：**SEM 圖常是 1024×1024 甚至更高**，Qwen2-VL 是第一個把這種高解析度輸入做對的開源架構。

### 6.2 LLaVA-OneVision（2024-08-05, ByteDance + NTU）
Li 等人的 LLaVA-OneVision（arxiv 2408.03326） [https://arxiv.org/abs/2408.03326] 是第一個在 single-image、multi-image、video **三個場景同時 SOTA** 的開源 VLM。架構：SigLIP + Qwen2 + anyres-9 patch（一張圖切 9 塊捕捉高解析度細節）。0.5B / 7B / 72B 三個規模。

### 6.3 Pixtral 12B（Mistral, 2024-09-11）
Mistral 的第一個 VLM，基於 Nemo 12B + 400M 專用 vision encoder，Apache 2.0，原生支援任意數量、任意尺寸圖片，MMMU 62.5%，128K context。

### 6.4 Molmo + PixMo（AI2, 2024-09-25）[https://arxiv.org/abs/2409.17146]
AI2 的 Molmo 家族（1B / 7B / 72B）最大的差異化是**完全開源 pipeline**（權重、code、data、eval 全開，不蒸餾）。PixMo 資料集的核心 trick：**讓標註員用語音**（60-90 秒）描述圖片，而非打字——得到的描述更自然、更細緻。還有 2D pointing 資料讓模型能用「點座標」回答問題，這對半導體 SEM 缺陷定位極有啟發。

### 6.5 Idefics3（HuggingFace, 2024-08）
基於 Llama 3.1-8B + SigLIP-so400m，去掉了 Idefics2 的 Perceiver，純 MLP projection。文件理解是強項（加入 Docmatix）。

### 6.6 MiniCPM-V 2.6（面壁 OpenBMB, 2024-08）
8B 參數（SigLip-400M + Qwen2-7B），在 8B 級別超越 GPT-4o-mini、GPT-4V、Gemini 1.5 Pro（單圖理解）。亮點：**支援 iPad 即時影片理解**，這對半導體產線邊緣部署有直接參考價值。

### 6.7 InternVL 2 / 2.5（上海 AI Lab, 2024）
- **InternVL 2**（2024-07-02）：1B-76B 規模 [https://internvl.github.io/blog/2024-07-02-InternVL-2.0/]
- **InternVL 2.5**（2024-12-05）：**InternVL2.5-78B 是第一個 MMMU > 70% 的開源 MLLM**，逼近 GPT-4o。

### 6.8 Qwen2.5-VL（2025-01, arxiv 2502.13923） [https://arxiv.org/abs/2502.13923]
Qwen2-VL 的升級版，**3B / 7B / 32B / 72B 四個規模**。主要升級：
- 原生動態解析度 ViT **從零訓**（之前是用 OpenCLIP 初始化），並整合 Window Attention 降低計算。
- 強化 bounding box / 點定位、文件 parsing、長影片理解。
- 32B 版本填補 7B 和 72B 之間的空檔，對單卡微調極友好。

到 2026-04 為止，**Qwen2.5-VL 仍是半導體場景最常被當作 base 的開源 VLM**（7B 單卡、32B 兩張 A100、72B 四張）。

---

## 7. Qwen3 世代（2025-2026）：MoE + Thinking + VL 的三叉戟

### 7.1 Qwen3 LLM（2025-04-29 release, 2025-05-15 tech report）
Qwen3 系列 [https://arxiv.org/abs/2505.09388] 包含 dense（0.6B / 1.7B / 4B / 8B / 14B / 32B）和 MoE（30B-A3B / 235B-A22B）共 8 個模型。兩個關鍵創新：
- **Thinking / Non-thinking 統一框架**：同一模型可透過 chat template 開關「思考模式」，不必再分別訓兩個模型；
- **Thinking Budget**：推理時動態分配「可以思考多少 token」，平衡延遲與質量。

MoE 架構細節：**128 總 expert / 每 token 激活 8 個**，移除了 Qwen2.5 的 shared expert，改用 global-batch load balancing loss。

### 7.2 Qwen3-VL — **確認發布時程**（截至 2026-04-23）

根據 GitHub QwenLM/Qwen3-VL 和 HuggingFace Qwen organization 的公開發布歷史 [https://github.com/QwenLM/Qwen3-VL]：

| 日期 | 版本 |
|---|---|
| **2025-09-23** | Qwen3-VL-235B-A22B Instruct / Thinking（旗艦，MoE） |
| **2025-10-04** | Qwen3-VL-30B-A3B Instruct / Thinking（MoE） |
| **2025-10-15** | Qwen3-VL-4B / 8B Instruct / Thinking（dense） |
| **2025-10-21** | Qwen3-VL-2B Instruct / Thinking + 32B Instruct（dense） |
| **2025-11-27** | Qwen3-VL Technical Report 發布 [https://arxiv.org/abs/2511.21631] |

**所以到 2026-04，Qwen3-VL 家族已完整釋出**：dense 2B / 4B / 8B / 32B + MoE 30B-A3B / 235B-A22B，共 6 個尺寸 × Instruct / Thinking 兩個變體 = 12 個權重。HuggingFace 上 Qwen3-VL-2B-Instruct 單一 repo 已突破 18M 下載。

### 7.3 Qwen3-VL 架構關鍵升級

Qwen3-VL 技術報告 [https://arxiv.org/abs/2511.21631] 披露三個關鍵設計：

1. **DeepStack Fusion**：把 ViT **多層中間特徵**分別注入 LLM **前三層**（不只是 final layer 的 projection）。低層 ViT 特徵保留紋理細節、高層保留語意——兩者分別喂進 LLM 不同層，fine-grained task 效果顯著提升。對 SEM 缺陷這種**紋理+語意並重**的任務特別友好。
2. **Interleaved-MRoPE**：把 Qwen2-VL 的 M-RoPE 再升級，temporal / horizontal / vertical 三軸在 RoPE frequency 上**交錯分配**（不是分塊），緩解 axis-dependent spectral bias，長影片和密集空間建模都變強。
3. **原生 256K interleaved context**：圖文影片可以任意交錯進 256K 上下文——這個長度可以放進一份完整的製程 FA 報告（10+ 張圖 + 全文描述）。

### 7.4 四階段 pipeline 的比例

Qwen3-VL 技術報告中披露的訓練資料配比（按 token 估算，僅方向性）：
- **Stage 1（Alignment Pre-train）**：projection 對齊，數百 B token 圖文對；
- **Stage 2（Vision CPT / Native Pre-train）**：解凍 ViT、LLM，trillion-level 多模態 corpus；
- **Stage 3（SFT）**：多任務 instruction，含 grounding / OCR / chart / video；
- **Stage 4（DPO）**：preference alignment（Qwen 團隊確認主用 DPO 類方法，部分 reasoning 任務用 GRPO）。

這個四階段就是今天半導體 domain adaptation 要對齊的 upstream 範本：**Vision CPT（把半導體視覺語料餵進去）→ domain SFT → DPO/KTO 對齊 → Agent SFT（EDA 工具呼叫）**。

---

## 8. Agent / Tool-use SFT 崛起（2023-2026）

Pipeline 的第四階段是 2023 年才從「可選」變成「必選」的。它回應的痛點是：**VLM 只會描述圖片沒用，得會打開 EDA 工具、呼叫 MES API、操作 UI**。

### 8.1 Gorilla（Berkeley, 2023-05-24, arxiv 2305.15334）
Shishir Patil 等人的 Gorilla [https://arxiv.org/abs/2305.15334] 把 HuggingFace Hub、TorchHub、TensorHub 的 API 文件撒下去 fine-tune LLaMA，**超越 GPT-4 在 API call 生成任務上的準確率**。創新點：**Retriever-Aware Training（RAT）**——訓練時就考慮到 retrieval context 會變，推理時文件更新模型也不會崩。

### 8.2 ToolLLaMA / ToolBench（Tsinghua + OpenBMB, 2023-07-31, arxiv 2307.16789）
Qin 等人的 ToolLLM [https://arxiv.org/abs/2307.16789] 把 RapidAPI Hub 上 **49 類、16,464 個真實 API** 抓下來，生成 instruction tuning 資料 fine-tune LLaMA。這是第一個真正大規模的 tool-use SFT 資料集（ToolBench），也提出了 **DFSDT（Depth-First Search based Decision Tree）**改善 ReAct 的多步規劃能力。

### 8.3 Hermes 2 Pro / Hermes 3（NousResearch, 2024-05 / 2024-08）
NousResearch 的 Hermes 2 Pro（基於 Llama-3 8B）首次在開源模型中把 function calling 做到**生產等級可靠**：用專屬 `<tool_call>` JSON token，易於 parser 抽取。Hermes 3（arxiv 2408.11857, 2024-08, 涵蓋 8B / 70B / 405B） [https://nousresearch.com/hermes3/] 把這個能力在 Llama 3.1 上 scale 出去，並強化 generalist assistant + code gen。

**意義**：Hermes 系列把「tool call 該長什麼樣」這個看似瑣碎的 format 問題做對了——社群逐漸收斂到 `<tool_call>{"name":"...", "arguments":{...}}</tool_call>` 風格，半導體做內部 MES / EDA function wrap 時直接沿用即可。

### 8.4 Qwen-Agent / Qwen2.5-Coder（Alibaba, 2024）
- **Qwen2.5-Coder**（2024-11）：6 個規模（0.5B 到 32B），5.5T token 包含 source code、text-code grounding、synthetic data。32B 版本在 HumanEval / LiveCodeBench 上達到 GPT-4o 級別。
- **Qwen-Agent**（2024）：agent framework，內建 Function Calling / MCP / Code Interpreter / RAG，直接配 Qwen 模型使用 [https://github.com/QwenLM/Qwen-Agent]。

### 8.5 GUI / Visual Agent 崛起（2023-12 → 2025-01）
這條線和 Agent SFT 高度重疊但更偏視覺：

- **CogAgent**（清華, 2023-12, arxiv 2312.08914, CVPR 2024 Highlight）— 第一個專門的 GUI VLM，不依賴結構化 HTML/accessibility tree，純靠截圖預測點擊座標。9B 版本已是多個 GUI benchmark 的 SOTA。
- **ShowUI**（2024-11, arxiv 2411.17465）— Vision-Language-Action 統一模型；用 UI-Guided Visual Token Selection（把 screenshot 視為圖論結構）壓縮 token 數。
- **OSWorld**（2024-04）— 多模態 agent 的開放 computer environment benchmark，支援 Ubuntu / Windows / macOS 真實桌面環境。
- **UI-TARS**（ByteDance, 2025-01, arxiv 2501.12326） [https://arxiv.org/abs/2501.12326]— **Native GUI Agent**，僅吃截圖，生成鍵鼠操作序列；OSWorld benchmark 50 步 24.6 分、15 步 22.7 分，SOTA 級表現。

**對半導體的意義**：
SEM 操作介面、EDA 軟體（Calibre、Virtuoso、KLA Klarity）、MES 前端，都是 GUI 密集場景。未來兩年半導體 AI 的重要方向之一就是「讓 VLM 能操作 EDA 工具」——UI-TARS / ShowUI 那套 「screenshot → 動作 trajectory」的 SFT 範式可以直接遷移，但要自建 trajectory 資料集（需要在內網錄製 + 標註）。

### 8.6 Agent SFT 的資料構建演進

從早期到現在，構建方法大致三代：
1. **第一代（2023, Gorilla / ToolLLaMA）**：用 GPT-4 生成「prompt → 正確 API call」pair，純 single-turn。
2. **第二代（2024, Hermes 2 Pro / Qwen-Agent）**：**multi-turn trajectory**，包括 tool call → tool result → follow-up reasoning → final answer 的完整鏈。
3. **第三代（2024-2025, UI-TARS / ShowUI）**：**screenshot 級別 trajectory**，每一步的 state 是圖像、action 是座標/鍵盤序列，和強化學習的 trajectory 更像。

半導體場景目前主要還在第二代（MES API、EDA CLI 的 function call SFT），但第三代（EDA GUI 操作）在 1-2 年內會是重點戰場。

---

## 9. 縱向總結：為半導體 VLM 留下了什麼

回看 2018-2026 這七年，四階段 pipeline 的每一層都有清晰的「為什麼今天長這樣」：

| 階段 | 起源 | 核心遺產 |
|---|---|---|
| **CPT** | ULMFiT(2018) → BioBERT/SciBERT(2019) → DAPT/TAPT(2020) | 「通用 → 領域 → 任務」的兩層繼續預訓練 + 詞表適配 |
| **SFT** | T5(2020) → InstructGPT(2022) → Alpaca(2023) → LLaVA(2023) | Instruction tuning + LLM 合成資料 + 視覺 instruction 化 |
| **Preference Alignment** | InstructGPT-RLHF(2022) → DPO(2023) → KTO/ORPO/SimPO(2024) → GRPO(2024) | 從 PPO 這個重工業流程，蒸餾成 `(prompt, chosen, rejected)` 一行 loss，再分支成 verifiable reward 的 GRPO |
| **Agent SFT** | Gorilla/ToolLLaMA(2023) → Hermes(2024) → UI-TARS(2025) | 從單輪 API call → 多輪 trajectory → 螢幕級別視覺操作 |
| **PEFT** | LoRA(2021) → QLoRA(2023) → DoRA/PiSSA(2024) | 讓單卡 fine-tune 72B 成為日常工程動作 |
| **VLM 架構** | BLIP-2(2023-01) → LLaVA(2023-04) → Qwen2-VL(2024-08) → Qwen3-VL(2025-09) | 從「兩大凍結 + 小橋樑」演化到「原生解析度 + DeepStack + 256K interleaved」 |

**半導體 domain adaptation 的今日最佳配置**（綜合上述演化）：
- **Base model**：Qwen3-VL-8B 或 32B（dense 版，DeepStack 對紋理任務友好）。
- **Stage 1 CPT**：製程文件 + SEM caption + FA report，2-5B token；解凍 ViT 後期幾層 + LLM，用 LoRA rank 128 或 DoRA。
- **Stage 2 SFT**：domain instruction（SEM 分類、wafer map QA、工單解析），10-50 萬 pair，DoRA + rank 64。
- **Stage 3 對齊**：
  - 有 verifiable reward（分類對錯、規格合規）→ GRPO；
  - 只有「好/壞」二元 QC 訊號 → KTO；
  - 標準 preference pair → DPO 或 SimPO。
- **Stage 4 Agent SFT**：function call（MES API、Calibre CLI）用 Hermes 風格 `<tool_call>` format；GUI 操作（EDA 軟體）參考 UI-TARS trajectory 資料格式，自建內部資料集。

這條路線，是七年開源社群試錯的壓縮精華。半導體場景接下去兩年的最大課題不是發明新 pipeline，而是**把 open-source pipeline 跑通、跑對、跑穩**——特別是資料側的 domain corpus / instruction / preference / trajectory 這四層語料建設。

---

## 附錄：關鍵 URL 總表

- **ULMFiT（2018）**：https://arxiv.org/abs/1801.06146
- **SciBERT（2019）**：https://arxiv.org/abs/1903.10676
- **FinBERT（2020）**：https://arxiv.org/abs/2006.08097
- **GPT-3（2020）**：https://arxiv.org/abs/2005.14165
- **T5（2020）**：https://arxiv.org/abs/1910.10683
- **DAPT/TAPT（2020）**：https://arxiv.org/abs/2004.10964
- **LoRA（2021）**：https://arxiv.org/abs/2106.09685
- **InstructGPT（2022）**：https://arxiv.org/abs/2203.02155
- **Constitutional AI / RLAIF（2022）**：https://arxiv.org/abs/2212.08073
- **LLaMA（2023-02）**：https://arxiv.org/abs/2302.13971
- **Stanford Alpaca（2023-03）**：https://crfm.stanford.edu/2023/03/13/alpaca.html
- **Dolly v2（2023-04）**：https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm
- **BLIP-2（2023-01）**：https://arxiv.org/abs/2301.12597
- **LLaVA v1（2023-04）**：https://arxiv.org/abs/2304.08485
- **MiniGPT-4（2023-04）**：https://arxiv.org/abs/2304.10592
- **QLoRA（2023-05）**：https://arxiv.org/abs/2305.14314
- **Gorilla（2023-05）**：https://arxiv.org/abs/2305.15334
- **DPO（2023-05）**：https://arxiv.org/abs/2305.18290
- **ToolLLM（2023-07）**：https://arxiv.org/abs/2307.16789
- **Qwen-VL（2023-08）**：https://arxiv.org/abs/2308.12966
- **LLaVA-1.5（2023-10）**：https://arxiv.org/abs/2310.03744
- **IPO（2023-10）**：https://arxiv.org/abs/2310.12036
- **CogVLM（2023-11）**：https://arxiv.org/abs/2311.03079
- **InternVL 1.0（2023-12）**：https://github.com/OpenGVLab/InternVL
- **Self-Rewarding LM（2024-01）**：https://arxiv.org/abs/2401.10020
- **KTO（2024-02）**：https://arxiv.org/abs/2402.01306
- **DeepSeekMath / GRPO（2024-02）**：https://arxiv.org/abs/2402.03300
- **DoRA（2024-02）**：https://arxiv.org/abs/2402.09353
- **ORPO（2024-03）**：https://arxiv.org/abs/2403.07691
- **PiSSA（2024-04）**：https://arxiv.org/abs/2404.02948
- **SimPO（2024-05）**：https://arxiv.org/abs/2405.14734
- **InternVL 2（2024-07）**：https://internvl.github.io/blog/2024-07-02-InternVL-2.0/
- **LLaVA-OneVision（2024-08）**：https://arxiv.org/abs/2408.03326
- **Hermes 3（2024-08）**：https://nousresearch.com/hermes3/
- **Idefics3（2024-08）**：https://huggingface.co/HuggingFaceM4/Idefics3-8B-Llama3
- **Qwen2-VL（2024-09）**：https://arxiv.org/abs/2409.12191
- **Pixtral 12B（2024-09）**：https://mistral.ai/news/pixtral-12b
- **Molmo / PixMo（2024-09）**：https://arxiv.org/abs/2409.17146
- **ShowUI（2024-11）**：https://arxiv.org/abs/2411.17465
- **InternVL 2.5（2024-12）**：https://github.com/OpenGVLab/InternVL
- **UI-TARS（2025-01）**：https://arxiv.org/abs/2501.12326
- **Qwen2.5-VL（2025-01, report 2025-02）**：https://arxiv.org/abs/2502.13923
- **Qwen3 Tech Report（2025-05）**：https://arxiv.org/abs/2505.09388
- **Qwen3-VL GitHub（2025-09 起陸續釋出）**：https://github.com/QwenLM/Qwen3-VL
- **Qwen3-VL Tech Report（2025-11-27）**：https://arxiv.org/abs/2511.21631
