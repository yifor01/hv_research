# 橫向分析：VLM 四階段訓練 Pipeline — 主流方法與工具鏈全景對比

> 面向：半導體業技術負責人 + 訓練工程師
> 情境：以 Qwen3-VL 為基底，對半導體製程領域做路線選型
> 更新日期：2026-04

本章節回答一個核心問題：**當你要把一個通用 VLM 變成「看得懂 SEM 影像、讀得懂製程工單、會呼叫廠內 MES 工具」的領域模型時，從 CPT → SFT → Preference Alignment → Agent SFT 的每一步，該選哪個方法、用哪套工具？**

所有對比不是為了列菜單，而是為了回答一個實際問題：**選型的真實理由是什麼？**

---

## A. CPT 階段：你到底要不要做預訓練？

### A.1 核心爭議：Full-param CPT vs. LoRA-based CPT

這是 CPT 階段最根本的分歧。Meta 的 "LoRA Learns Less and Forgets Less"（arxiv 2405.09673）給了一個很誠實的結論：**在程式與數學這類結構化知識的 continued pretraining 上，full-param FT 比 LoRA 更精準、更 sample-efficient；但 LoRA 忘得少**（[LoRA Learns Less and Forgets Less](https://arxiv.org/html/2405.09673v2)）。這就是工程上的兩難：你要領域知識長得快，還是要通用能力退得慢？

對半導體這種「子領域很窄但 base model 通用能力不能丟」的場景，LoRA-based CPT 看起來誘人，但有個常被忽略的細節：**LoRA 在 CPT 的 domain-specific insight 學習能力是有天花板的**。"Learning Beyond the Surface"（arxiv 2501.17840）直接測了這件事，結論是 LoRA 適合學表面模式（文風、格式、簡單記憶），但對於需要深層推理重組的領域知識（例如製程參數與良率之間的隱性因果），full-param CPT 還是必要的（[Learning Beyond the Surface](https://arxiv.org/html/2501.17840v1)）。

**對半導體場景的啟示**：SEM 缺陷分類、wafer map pattern 這類「新視覺分佈」，full-param CPT 幾乎是必要的（至少 vision encoder + projector 要解凍）；但製程工單的語言風格學習，LoRA-CPT 就夠。

### A.2 LLaMA-Pro Block Expansion：第三條路

LLaMA-Pro（arxiv 2401.02415）提出一個很巧妙的折衷：**只擴展新的 transformer blocks，且只訓練新擴的 blocks**。原始 LLaMA-Pro 從 LLaMA2-7B 擴成 8.3B，在 code 和 math corpus 上訓練，幾乎沒有 catastrophic forgetting（[LLaMA Pro: Progressive Block Expansion](https://www.emergentmind.com/papers/2401.02415)）。這個思路在 2025 的 domain-adaptive pretraining 圈子很紅 — MS-SWIFT、LLaMA-Factory 都支援 `llama_pro` 訓練模式。

### A.3 PiSSA-CPT 與 LoRA-FA

PiSSA（Principal Singular values and Singular vectors Adaptation）是 LoRA 初始化的優化：用原權重 SVD 的主奇異值初始化 adapter，不是 Kaiming 隨機初始化。在長序列 CPT 場景下，PiSSA 收斂速度遠快於原生 LoRA，且量化誤差遠小於 QLoRA（[Advanced LoRA Fine-Tuning](https://kaitchup.substack.com/p/advanced-lora-fine-tuning-how-to)）。LoRA-FA 則是把 A 矩陣凍結、只訓 B，激進削減記憶體但犧牲表達能力，業界實戰很少人用。

### A.4 VLM 特有議題：Vision Encoder 要不要解凍？

Qwen2.5-VL technical report（arxiv 2502.13923）揭露了一個 Qwen 團隊的具體做法：**vision encoder 在不同訓練階段有不同凍結策略**。在 Stage 1 純視覺對齊階段，LLM 凍結、只訓 ViT + Projector；Stage 2 多模態 pretraining 才全解凍；Stage 3 SFT 時根據任務選擇性凍結（[Qwen2.5-VL Technical Report](https://arxiv.org/pdf/2502.13923)）。

**凍結 ViT 的代價**：如果你要做 SEM / TEM grayscale 高解析度影像，原始 ViT 是在 RGB 自然影像上預訓練的，特徵空間根本不覆蓋灰階高頻紋理。凍結 ViT = 你的缺陷檢測永遠只會看到「長得像狗毛邊緣」的 token，精度卡死在 ViT 原生表達能力。Qwen2-VL 引入 Native Dynamic Resolution（NaViT-style）後這點好一些，但半導體影像仍要解凍 ViT。

**解凍的代價**：train loss 會抖、MMLU 會退、general 視覺能力會往你的窄分佈飄。緩解方法是 **replay ratio** — Gururangan 2020 的經典 DAPT 論文就強調 general:domain ≈ 1:1 到 1:3 是黃金比例；Qwen2 tech report 內部披露的混合比約為 **1 份 domain + 2-4 份 general**（語言 + 視覺 + 通用 instruction）。

### A.5 Catastrophic Forgetting 指標

"Examining Forgetting in Continual Pre-training"（arxiv 2401.03129）給了可操作的監測清單：MMLU、HELM、GSM8K、HumanEval 四項做基線，CPT 前後差異超過 3% 就要警惕（[Examining Forgetting](https://arxiv.org/html/2401.03129v1)）。VLM 則加上 MMMU、OCRBench、ChartQA、MMBench 作為視覺側的遺忘指標。CURLoRA（arxiv 2408.14572）和 TIES-merging 是兩個 2025 常見的遺忘緩解方案。

---

## B. SFT 階段：表面上人人都會，細節決定成敗

### B.1 Vanilla SFT 的三個隱藏殺手

**Sample packing**：把多個短 sample 拼成同一個長序列以提升 GPU 利用率，是 SFT 的標配。但 naive packing 會讓 attention 跨 sample 洩漏（"Threshold Filtering Packing" arxiv 2408.09327 記錄了這問題）。正確做法是 packing + correct attention mask（block-diagonal mask）。LLaMA-Factory、Axolotl、TRL 都已支援，但 Axolotl 的實作被公認最成熟（[Enhancing Training Efficiency Using Packing](https://arxiv.org/html/2407.09105v1)）。

**Loss masking（assistant-only loss）**：TRL SFTTrainer 的 `assistant_only_loss=True` 是 2025 後成為預設（[TRL SFTTrainer docs](https://huggingface.co/docs/trl/en/sft_trainer)）。若不做 loss masking，user turn 的 token 也會進 loss，你其實是在教模型「怎麼當個好用戶」，這是很多開源 finetune 模型「說話怪怪的」的根因。

**NEFTune**：arxiv 2310.05914 提出的 noisy embedding trick，對 embedding 注入小幅雜訊作正則化。LLaMA-2-7B 在 Alpaca 上從 29.79% 直接拉到 64.69% AlpacaEval（[NEFTune paper](https://arxiv.org/abs/2310.05914)）。幾乎零成本、零風險，2025 預設啟用。

### B.2 Chat Template 戰爭

每個模型家族都有自己的 chat template，混用會翻車：
- **ChatML**（OpenAI 風格，Qwen / Mistral 系）
- **LLaMA template**（Llama-2/3 系，有 `[INST]` `[/INST]` 奇特標記）
- **Qwen template**（擴展 ChatML 加 tool_call 特殊 token）
- **Alpaca**（老式 `### Instruction:` `### Response:`，現已淘汰）

Qwen3 的 template 特別要注意：它在 Qwen2 基礎上**額外插入了 `<think>...</think>` reasoning token 與 hermes-style tool_call 標籤**（[Function Calling and Tool Use - DeepWiki](https://deepwiki.com/QwenLM/Qwen3/4.3-function-calling-and-tool-use)）。若你用 LLaMA-Factory / MS-SWIFT 做 Qwen3-VL SFT，一定要指定 `--template qwen3_vl`，否則 tool-call 能力會退化。

### B.3 VLM 特有：資料格式與多圖/影片輸入

Qwen3-VL 系統設定以 `<image>` placeholder + 原生動態解析度輸入為主：圖片不被 resize 到固定 448，而是保留原解析度並轉 variable token 數。這對半導體 SEM 圖（常見 1024×1024、16-bit grayscale）極為重要。**凡是要處理 SEM/TEM 的 pipeline，Qwen2-VL 以下的基座就不要考慮**，即使有 patch resize trick 也會丟失細微缺陷紋理。

多圖輸入方面，Qwen3-VL 原生支援 32 張以上 interleaved image，wafer map + 製程配方圖並列分析的場景可直接做。影片則走 T-RoPE + FPS sampling，Qwen2.5-VL 之後成熟，以半導體產線的時序影像（如 CVD 反應艙監控）可直接用。

### B.4 LIMA 啟示：Data 品質遠大於數量

LIMA（arxiv 2305.11206）用 1000 筆精選資料 fine-tune LLaMA-65B，在 43% 的對比中擊敗 GPT-4（[LIMA: Less Is More](https://arxiv.org/abs/2305.11206)）。這對半導體場景的啟示極為關鍵：**與其洗 10 萬筆粗糙的工單摘要，不如讓 10 位資深製程工程師合寫 1000 筆高品質 Q&A**。這 1000 筆的 ROI 遠大於前者。

---

## C. Preference Alignment：這章決定你產品的「氣質」

### C.1 PPO（Proximal Policy Optimization）：為何難訓

RLHF 的原生路線。流程是：先訓 reward model (RM)，再用 PPO on-policy 探索。難訓的原因是**四模型同台**（policy + ref policy + RM + value）、**on-policy 採樣貴**、**KL 爆掉就崩**、**reward hacking 無處不在**。2023 的 alignment tax 論文更指出：PPO 會讓模型某些能力（尤其 math）降級。工程上除非你有 DeepMind / OpenAI 級的基礎設施與 reward model，否則不要作為首選。

### C.2 DPO（arxiv 2305.18290）：如何幹掉 Reward Model

Rafailov 的 DPO 核心洞察：**LLM 本身就是 reward model**。透過貝氏定理推導，可以把 RM + PPO 兩步合併為一個 simple classification loss：

```
L_DPO = -log σ(β · [log π(y_w|x)/π_ref(y_w|x) - log π(y_l|x)/π_ref(y_l|x)])
```

簡單一句話：**讓 chosen 的機率比 ref 高、rejected 的機率比 ref 低**（[Direct Preference Optimization](https://arxiv.org/abs/2305.18290)）。DPO 2023 年底迅速統一半壁江山，幾乎所有開源 alignment 都改投 DPO。但三個已知問題：(1) 容易 overfit（Azar et al. 證明），(2) chosen 和 rejected 同時被推低（counterintuitive log-prob decrease），(3) 需要保留 ref model（記憶體負擔 2x）。

### C.3 IPO（Azar 2023, arxiv 2310.12036）：解 DPO 的 overfitting

IPO 指出 DPO 會讓 π(y_w)→1、π(y_l)→0 的退化，這在資料雜訊高時毒性極大（[A General Theoretical Paradigm](https://arxiv.org/abs/2310.12036)）。IPO 用 identity mapping 代替 sigmoid，並強化 KL 正則。業界評估：IPO 在**偏好資料髒**的情境特別有用（例如 RLAIF 用 GPT-4 打分的自動標註），但在乾淨的人工偏好資料上與 DPO 差異有限。

### C.4 KTO（Ethayarajh 2024, arxiv 2402.01306）：單樣本偏好

KTO 最大突破：**不需要 pairwise 資料**。只要你有「這則回覆好 / 不好」的單點標籤，就能訓練。對半導體場景，這是個巨大實用優勢 — 要求製程工程師給 pair 排序成本極高，但給 thumbs up/down 很便宜（[KTO paper](https://arxiv.org/abs/2402.01306)）。KTO 從 Kahneman-Tversky prospect theory 推導，把 loss 拆成「得到正樣本的 utility」 + 「避免負樣本的 utility」，且兩邊有不對稱權重（loss aversion）。**實戰評價**：在 binary feedback 場景勝 DPO；但在精細 pairwise 場景不如 DPO。

### C.5 ORPO（Hong 2024, arxiv 2403.07691）：SFT + Alignment 合併

ORPO 的野心：**把 SFT 與 alignment 合併成單一階段**。公式加一項 log(odds ratio) 的 penalty：

```
L_ORPO = L_SFT + λ · log σ(log odds(y_w) - log odds(y_l))
```

不需要 ref model，從 base model 直接訓出 aligned model（[ORPO paper](https://arxiv.org/abs/2403.07691)）。工程優勢巨大：記憶體少一份 ref model、pipeline 少一個階段、小模型（1-7B）收斂快。但大模型（> 30B）上未如 DPO 穩定，且需要同時有好 SFT data + 好偏好 data，很多團隊現有資料不符。

### C.6 SimPO（Meng 2024, arxiv 2405.14734）：去 Reference Model

SimPO 進一步把 DPO 簡化到極致：**完全丟掉 ref model，用平均 log prob 當 implicit reward**：

```
L_SimPO = -log σ(β/|y_w| · log π(y_w|x) - β/|y_l| · log π(y_l|x) - γ)
```

其中 γ 是 margin 項，強制 winning 與 losing 有安全距離（[SimPO paper](https://arxiv.org/abs/2405.14734)）。SimPO 在 AlpacaEval 2 比 DPO 高 6.4 分、Arena-Hard 高 7.5 分，且記憶體省一半。**但**：缺 ref model 的約束下，SimPO 對 beta 與 gamma 超敏感，hyperparameter 不對就崩。社群已形成共識：SimPO 適合小團隊打榜，不適合生產部署。

### C.7 GRPO（DeepSeek 2024, arxiv 2402.03300）：本文重點

GRPO 是 2024-2026 這兩年最重要的 RL 創新，DeepSeek-Math 提出、DeepSeek-R1 發揚光大、Qwen3 全線採用（[DeepSeekMath paper](https://arxiv.org/abs/2402.03300)）。核心機制：**對每個 prompt 採樣一組（通常 8-16 個）response，組內相對 reward 當 advantage，完全丟掉 value / critic model**。

```
A_i = (r_i - mean(r)) / std(r)
```

記憶體省一份 value model，訓練穩定性大幅提升（因為 advantage 有天然 normalize）。但 GRPO 真正改變遊戲的是與 **verifiable reward**（RLVR）結合 — DeepSeek-R1 用「最終答案正不正確」這種硬 reward 就能訓出強推理能力，完全不需要 reward model。

**GRPO 對半導體場景的啟示**：如果你要訓一個「能算 CD bias、能驗證 layout design rule、能計算製程窗口」的 agent，GRPO + verifiable reward（程式自動驗算結果）是極有吸引力的路線。不用標註員、不用 reward model，只要有驗算器即可。

GRPO 的變體爆炸：**DAPO**（字節 2025 SOTA，AIME 50 分）、**DrGRPO**（去 reward shaping）、**GSPO**（Qwen 的 group sequence variant，稍優於 GRPO）、**KL_Cov / Clip_Cov**（控爆解法）。verl 框架原生支援全套（[verl GitHub](https://github.com/volcengine/verl)）。

### C.8 Iterative DPO / Online DPO：bridging 離線與在線

Iterative DPO：用當前 model 自採樣 → 用 RM 或 LLM-as-Judge 標偏好 → 重新 DPO → 再採樣。形成「自我對弈式」改進循環，介於 DPO 的離線穩定與 PPO 的在線探索能力之間。Llama 3 post-training 重度使用這條路（論文披露有 6 輪迭代）。TRL 2025 Q3 新增 OnlineDPOTrainer 直接支援此範式（[TRL VLM Alignment Blog](https://huggingface.co/blog/trl-vlm-alignment)）。

### C.9 RLAIF vs. RLHF：標註員還是 GPT-4？

Google 2023 年的 RLAIF 論文證明：用 LLM 打分可達 RLHF 同等效果且成本降 10x。但**領域專業性不能假設**。半導體製程的對錯判斷，GPT-4 不比大學生強多少，用 RLAIF 標 reward 等於標廢數據。折衷方案：domain expert 標 seed 數據（500-1000 筆）→ 訓小型 domain-specific reward model → 用這個 RM 做 RLAIF。這是 2025 業界驗證過的可行路線。

### C.10 VLM 對齊特有問題

Visual hallucination 是 VLM 的結構性毛病：模型會「幻想」圖中不存在的物件。RLHF-V（CVPR 2024）收集 fine-grained segment-level 人工修正，dense DPO 訓練（[RLHF-V](https://openaccess.thecvf.com/content/CVPR2024/papers/Yu_RLHF-V_Towards_Trustworthy_MLLMs_via_Behavior_Alignment_from_Fine-grained_Correctional_CVPR_2024_paper.pdf)）。V-DPO（arxiv 2411.02712）改良為 vision-guided DPO，讓 preference 對應到具體視覺區域（[V-DPO paper](https://arxiv.org/abs/2411.02712)）。VLFeedback 是 80k 筆 GPT-4V 打分的偏好資料，2025 成為標配（[V-DPO on ACL](https://aclanthology.org/2024.findings-emnlp.775.pdf)）。

**對半導體場景**：缺陷檢測的視覺幻覺尤其致命（「有 particle 但模型說沒」和「沒 particle 但模型說有」後果都嚴重）。建議直接 follow V-DPO 範式，在缺陷標註 bbox 層級收集 fine-grained preference。

---

## D. Agent / Tool-use SFT

### D.1 Function-calling 格式戰爭

四大流派，格式互不兼容：

1. **OpenAI format**：JSON Schema `"tools":[{...}]` + `"tool_calls":[...]` 的結構化字段。最乾淨但完全靠 API 解析，不在 prompt 裡。
2. **Hermes format**：Nous Research 提出，用 `<tool_call>...</tool_call>` XML-like 標籤內嵌 JSON。Qwen3 / QwQ 預設格式，vLLM `--tool-call-parser hermes` 原生支援（[Qwen docs - Function Calling](https://qwen.readthedocs.io/en/latest/framework/function_call.html)）。
3. **Qwen-Agent format**：Hermes 變體，附加 `<reasoning>` 等擴展。Qwen3 SFT 要訓這種格式最方便。
4. **XML-style (Claude/Anthropic)**：`<tool_use>` tag，語義化但解析最費工。

**選型建議**：以 Qwen3-VL 為基座 → 直接 follow Hermes 格式，一來 Qwen3 chat template 已內建，二來 vLLM / SGLang inference 側 parser 現成，三來 Qwen-Agent 框架可直接跑。

### D.2 ReAct vs. 原生 function call

ReAct（Thought → Action → Observation 循環，純 prompt engineering）曾是 2023 主流，但 token 消耗大、延遲高、易錯格式。**2025 後基本被原生 function call 替代**。但 ReAct 的思路活在 tool-use 訓練資料的 CoT 部分 — 讓模型先輸出 reasoning、再決定 tool call，保留了 ReAct 的可解釋性優點，規避了全靠 prompt 的脆弱性。

### D.3 Multi-turn tool-use 訓練資料構建

難點：一個完整 agent trace 可能跨 5-10 輪 tool call，每輪 output 要可序列化、要能恢復、token 要能 loss mask。開源資料代表：**Glaive-v2 function calling**、**ToolBench**、**API-Bank**、**APIGen 系列**。但對半導體場景幾乎都不直接可用，**必須自己合成** — 常見做法是用 GPT-4 根據你的內部 tool API schema 合成 conversation，再由 engineer QC 過濾。

### D.4 Agentic Visual Tasks：GUI Agent 四大家

- **CogAgent**（智譜，arxiv + CogAgent-9B-20241220）— 純視覺 GUI agent 最早代表作
- **ShowUI**（arxiv + code）— UI-Guided Visual Token Selection 降低 token 成本
- **OS-Atlas**（arxiv 2410.23218）— Windows/Linux/macOS/Android/Web 跨平台，首創 13M GUI element 開源資料（[OS-ATLAS](https://arxiv.org/html/2410.23218v1)）
- **UI-TARS**（ByteDance, arxiv 2501.12326）— end-to-end 本體 GUI agent，跨 10+ benchmark SOTA。UI-TARS-2（arxiv 2509.02544）引入 multi-turn RL 進一步拉開差距

對半導體：若目標是做「能操作廠內 MES / APC 介面的 agent」，直接以 UI-TARS-2 或 OS-Atlas 為基座再微調，比從 Qwen3-VL 從零訓 GUI 知識快 3 倍以上。

---

## E. 工具鏈對比矩陣（本章最重要）

### E.1 完整矩陣

| 工具 | GitHub URL | Stars (2026 Q2) | VLM 支援 | 支援方法 | 分散式 | 記憶體優化 | 學習曲線 | 最適情境 |
|------|-----------|----------------|---------|---------|--------|----------|---------|---------|
| **LLaMA-Factory** | [hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | ~65K | 最廣（Qwen3-VL, InternVL, LLaVA, Pixtral...）| CPT/SFT/DPO/KTO/ORPO/PPO/GRPO | DeepSpeed/FSDP | 接入 unsloth | 低（Web UI） | 快速 PoC、教學、Web UI 需求 |
| **MS-SWIFT** | [modelscope/ms-swift](https://github.com/modelscope/ms-swift) | ~10K+ | 最廣 300+ MLLM（Qwen 原生）| CPT/SFT/DPO/GRPO 全家族 | Megatron TP/PP/CP/EP | 多款 | 中 | Qwen 生態、大規模 full FT、Megatron 需求 |
| **Axolotl** | [axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl) | ~11K (v0.29) | VLMs 完整 | SFT/DPO/IPO/KTO/ORPO/GRPO/GDPO | DeepSpeed/FSDP | Flash Attn 2/3 | 中（YAML config） | 嚴謹研究、複雜 config、歐美社群 |
| **unsloth** | [unslothai/unsloth](https://github.com/unslothai/unsloth) | 高 | Qwen3-VL / Gemma / Llama-V | SFT/DPO/GRPO/GSPO | 單卡為主（2026 Q1 多卡 beta） | 2-5x 速度、90% VRAM 節省 | 低 | 單卡 / 消費級 GPU、快速實驗 |
| **TRL** | [huggingface/trl](https://github.com/huggingface/trl) | 高 | VLM DPO / GRPO / Online DPO | 全家族最底層 | Accelerate/DeepSpeed | 依賴 PEFT | 高（需寫 code） | 研究、客製化 trainer、算法開發 |
| **OpenRLHF** | [OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) | 高 | VLM RL 支援 | PPO/DAPO/REINFORCE++/GRPO | Ray + vLLM | Ray async | 高 | 大規模 PPO / Agentic RL |
| **verl** | [volcengine/verl](https://github.com/volcengine/verl) | 高 | VLM GRPO / DAPO | PPO/GRPO/GSPO/DAPO/DrGRPO 最全 | FSDP+Megatron+vLLM/SGLang | Hybrid CPU/GPU | 高 | 大規模 RL、671B 可擴、工業級 |
| **DeepSpeed** | Microsoft | — | — | 基礎設施 | ZeRO 1/2/3 + offload | CPU offload | 中 | 通用分散式後端 |
| **FSDP** | PyTorch | — | — | 基礎設施 | Fully Sharded Data Parallel | activation ckpt | 中 | PyTorch 原生、簡潔 |
| **ColossalAI** | hpcaitech | ~38K | VLM 支援 | SFT/DPO/PPO | 全家族並行 | Zero Redundancy | 中 | 中國大廠、節省成本 |
| **Megatron-LM** | NVIDIA | ~13K | VLM 支援 (v0.7+) | Pretraining 為主 | TP/PP/CP/EP 最強 | MoE 優化 | 極高 | 超大規模預訓練、100B+ |

### E.2 幾個關鍵觀察（這才是工程師選型時真正在意的）

**LLaMA-Factory 的定位變了**：從 2023 的「最易用 framework」進化成 2025 的「集大成整合器」。它不再和 unsloth 競爭，而是**直接把 unsloth 包成 `--use_unsloth` flag**，這讓它同時擁有 unsloth 的速度和 LLaMA-Factory 的 VLM 廣度（[EVAL #003 fine-tuning 2026](https://dev.to/ultraduneai/eval-003-fine-tuning-in-2026-axolotl-vs-unsloth-vs-trl-vs-llama-factory-2ohg)）。

**MS-SWIFT 是 Qwen 生態的親兒子**：阿里 ModelScope 團隊和 Qwen 團隊同屬一個大部門。新的 Qwen3-VL / Qwen3-Omni 第一個 day-0 可訓框架永遠是 MS-SWIFT。若你鎖定 Qwen 基座，這條路線 learning curve 最低、支援最及時（[Qwen3-VL Best Practices](https://swift.readthedocs.io/en/latest/BestPractices/Qwen3-VL-Best-Practice.html)）。

**Axolotl 的 YAML 配置美學**：在歐美社群有忠實用戶，尤其是研究型團隊。好處是**每次 run 的 hyperparameter 都可版本化**（一份 yaml 就是一份 experiment record）。弱點：小樣本上手成本高，YAML 欄位上百個、文件散落。

**unsloth 的「單卡怪獸」定位**：2-5x 速度、90% VRAM 節省是真的，但**只有單卡場景最吃香**。2025 Q4 多卡版本仍處於 beta。若你有 8× H100，unsloth 的優勢就消失了（因為 FSDP + Flash Attn 3 本身就很快）。**unsloth 的真實價值**：讓「一個消費級 GPU 也能 finetune 70B」這件事從 meme 變成現實。

**TRL 是所有人的爹**：真實世界中，Axolotl / LLaMA-Factory / MS-SWIFT 的 DPO/GRPO trainer **底層都是 TRL**（或 fork 自 TRL）。2025 起，TRL 本身就是第一個官方支援 VLM DPO / VLM GRPO / Online DPO 的框架（[TRL VLM Alignment](https://huggingface.co/blog/trl-vlm-alignment)）。

**verl 是 2025-2026 的大型 RL 新王**：字節出品，HybridFlow 被 EuroSys 2025 接收。技術亮點是 **FSDP + Megatron + vLLM/SGLang 異構混合**，inference 端用 vLLM 做 rollout、training 端用 FSDP 做更新、state 端用 Megatron 並行，三者無縫切換。DAPO 在 Qwen2.5-32B 上 AIME 50 分就是 verl 訓的（[verl GitHub](https://github.com/volcengine/verl)）。若你要做 GRPO / agentic RL 到 70B+ scale，verl 現在是唯一嚴肅的選擇。

**OpenRLHF vs. verl 的微妙競爭**：OpenRLHF 更早（2023 底）、社群更國際化、Ray 原生。verl 晚半年但工程更硬、字節內部實打實訓過 Qwen-32B 到 o1 等級。業界 split：學術偏 OpenRLHF，工業界大廠偏 verl。

**Megatron-LM 是最後的終極武器**：除非你要做 100B+ 從零預訓練，否則你應該用別人包裝好的 Megatron。Megatron-Core v0.7 以後才真正好用，MFU 可達 47% on H100。Megatron-Bridge（NeMo 體系）提供 HuggingFace 雙向轉換，這是 2025 開始 Megatron 進入主流工作流的關鍵（[Megatron-Bridge](https://github.com/NVIDIA-NeMo/Megatron-Bridge)）。

### E.3 選型決策樹（給半導體場景）

- **情境 1：想最快跑通 Qwen3-VL SFT + LoRA，一個工程師兩週內交差** → **LLaMA-Factory**（Web UI + Qwen3-VL 原生 + 中文文件）
- **情境 2：要做嚴謹的 DPO / 投論文 / 細緻調 hyperparameter** → **Axolotl**（YAML 可版控）或 **TRL 直寫**（最大控制權）
- **情境 3：要 scale 到 Qwen3-VL-72B full FT + 4 機 32 卡** → **MS-SWIFT with Megatron backend** 或直接 **Megatron-Bridge**
- **情境 4：要做 GRPO / RLVR / 工具使用 RL** → **verl**（大規模）或 **TRL GRPOTrainer**（中等規模）或 **unsloth**（單卡實驗）
- **情境 5：手上只有 1 張 4090 要試點** → **unsloth** 無懸念
- **情境 6：要訓 GUI agent 操作廠內 MES** → **verl + UI-TARS-2 基座**

---

## F. LoRA 變體矩陣

| 方法 | 原理一句話 | 訓練速度 | 記憶體 | 收斂品質 | 2025-2026 業界定位 |
|------|----------|---------|--------|---------|------------------|
| **LoRA** | 低秩分解 ΔW = BA | 基準 | 基準 | 基準 | 仍是事實標準 |
| **QLoRA** | base model 4-bit NF4 + LoRA FP16 | 略慢（反量化） | -75% | ≈ LoRA | 消費級 GPU 首選 |
| **DoRA** | 拆 magnitude + direction，只 LoRA direction | -5% | +5% | **+3-4%** accuracy | 2025 business default |
| **LoRA+** | A / B 用不同 learning rate | = | = | +1-2% | 幾乎零成本小改，建議啟用 |
| **PiSSA** | SVD 主奇異值初始化 adapter | = | = | 收斂快 2-3x | CPT 長序列場景首選 |
| **rsLoRA** | alpha 除以 sqrt(r) 而非 r | = | = | 高 rank (>64) 時才顯著 | 僅在 r > 64 時啟用 |
| **VeRA** | AB 共享、只訓對角縮放 | = | -90% (param) | 略降 | 小眾，超窄場景 |
| **AdaLoRA** | 動態分配 rank 預算 | 略慢 | = | +1-2% | 理論好但實作複雜，淡出 |

**2025-2026 業界預設配方**（[LoRA Complete Guide](https://medium.com/@abhi-84/lora-qlora-dora-rslora-the-complete-guide-to-7-production-ready-fine-tuning-variants-283ff3e574a3)）：

```yaml
peft_type: lora
r: 16          # style/instruction-following；domain adaptation 上 32-64
lora_alpha: 32
target_modules: all-linear    # 不要只 Q/V，all-linear 差異實測明顯
use_dora: true                # +3-4% 準確率，為何不用
use_rslora: false             # 僅當 r > 64 才開
init_lora_weights: pissa      # 比 Kaiming 初始化收斂快
```

一個重要的最新研究警告：Kaitchup 2026 的 "Learning Rate Matters"（arxiv 2602.04998 — 注意這筆是 2026 最新 preprint）指出：**一旦 learning rate 調對，所有 LoRA 變體的峰值性能幾乎相同**，只是不同方法對應不同的 best lr range。**別被變體名稱唬住，真正的超參在 learning rate**。

---

## G. 半導體相關特殊考量

### G.1 SEM / TEM 影像：Native Dynamic Resolution 是必要條件

SEM 影像典型規格：1024×1024 或 2048×2048，16-bit grayscale，16 bit depth。傳統 VLM（CLIP-ViT 224 / 448）會先 resize + 8-bit 量化 + RGB tri-channel 填充，**三重資訊損失**。Qwen2-VL 引入的 NaViT-style Native Dynamic Resolution 直接保留原尺寸；Qwen3-VL 更進一步可接到 4K 級輸入。

**對工具鏈的影響**：你的訓練 pipeline 必須支援 variable image token length + dynamic patch size。LLaMA-Factory / MS-SWIFT 已內建；unsloth 在 2025 Q3 之後也 OK；但 Axolotl 早期版本對 variable length packing 有 issue，建議 ≥ v0.28。

### G.2 Wafer Map：小解析度 + 高 class imbalance

Wafer map 典型 128×128 或 256×256，缺陷類型 30-50 類但長尾嚴重（某些 defect pattern 一年只出現 10 次）。這意味著：

- VLM 的高解析度能力用不上（直接 downsample 到 448 也 OK）
- **嚴重 imbalance 下 vanilla SFT 會崩**，需要 focal loss / class-weighted loss / synthetic oversampling
- 最小樣本類別建議用 **few-shot in-context learning** 而非微調，否則過擬合

### G.3 製程工單：長 context

製程工單 / 批次 recipe / FMEA 報告動輒 30-50K token。這對基座模型的 context length 要求極高：

- Qwen3-VL 原生支援 128K（用 YaRN / NTK scaling 可到 256K）
- 訓練時必須用 **long-context stage**（通常 SFT 最後一階段專門用 128K 長樣本訓）
- 工具鏈須支援 **sequence parallel (CP)** — verl / Megatron / MS-SWIFT 支援；Axolotl / LLaMA-Factory 較受限

### G.4 對工具選型的實際影響

- **SEM/TEM 為主 → Qwen3-VL + MS-SWIFT**（原生 VLM 支援最全）
- **Wafer map 分類為主 → 小 VLM (3B/7B) + LLaMA-Factory + 強 augmentation**
- **長工單 RAG / agent → Qwen3-VL-72B + verl GRPO + 128K context，vLLM inference**

---

## 資料缺口與誠實標註

1. **半導體 VLM benchmark 稀缺**：公開的 domain-specific benchmark 極少（僅有 SEMICON DEPT 2024 的 SemanticSegmentation demo dataset）。絕大多數選型依據來自通用 VLM benchmark，對半導體的預測能力有限。
2. **Qwen3-VL 的 RLHF 配比未公開**：Qwen3 tech report 披露了 LLM 側的 alignment 細節，但 VLM 側的 RL 過程只有「用了 GRPO + GSPO」這種籠統描述。
3. **verl 中文 / 半導體場景實測稀缺**：verl 社群以字節內部案例為主，外部複現在 32B 以下模型有成功案例，70B+ 的外部案例極少。
4. **MS-SWIFT 英文社群弱**：Github issue 和 Twitter 上英文討論少、事故排障資源遠不如 LLaMA-Factory。這點對外商子公司團隊要權衡。
5. **GRPO hyper-parameter 的 off-the-shelf 預設還不成熟**：group size、KL coefficient、reward shaping 三者交互作用極複雜，**沒有單一「推薦預設」**，是當前社群最大的痛點之一。

---

## Reference URL 列表（供報告引用）

- Qwen3 Technical Report: https://arxiv.org/pdf/2505.09388
- Qwen2.5-VL Technical Report: https://arxiv.org/pdf/2502.13923
- Qwen2-VL: https://arxiv.org/html/2409.12191v1
- Open-Qwen2VL: https://arxiv.org/abs/2504.00595
- DPO: https://arxiv.org/abs/2305.18290
- IPO / General Theoretical Paradigm: https://arxiv.org/abs/2310.12036
- KTO: https://arxiv.org/abs/2402.01306
- ORPO: https://arxiv.org/abs/2403.07691
- SimPO: https://arxiv.org/abs/2405.14734
- GRPO / DeepSeekMath: https://arxiv.org/abs/2402.03300
- LIMA: https://arxiv.org/abs/2305.11206
- NEFTune: https://arxiv.org/abs/2310.05914
- LLaMA-Pro: https://www.emergentmind.com/papers/2401.02415
- LoRA Learns Less and Forgets Less: https://arxiv.org/html/2405.09673v2
- Learning Beyond the Surface: https://arxiv.org/html/2501.17840v1
- Examining Forgetting in CPT: https://arxiv.org/html/2401.03129v1
- CURLoRA: https://arxiv.org/html/2408.14572v1
- RLHF-V: https://openaccess.thecvf.com/content/CVPR2024/papers/Yu_RLHF-V_Towards_Trustworthy_MLLMs_via_Behavior_Alignment_from_Fine-grained_Correctional_CVPR_2024_paper.pdf
- V-DPO: https://arxiv.org/abs/2411.02712
- UI-TARS: https://arxiv.org/html/2501.12326v1
- UI-TARS-2: https://arxiv.org/html/2509.02544v1
- OS-Atlas: https://arxiv.org/html/2410.23218v1
- LLaMA-Factory: https://github.com/hiyouga/LLaMA-Factory
- MS-SWIFT: https://github.com/modelscope/ms-swift
- Axolotl: https://github.com/axolotl-ai-cloud/axolotl
- unsloth: https://github.com/unslothai/unsloth
- TRL: https://github.com/huggingface/trl
- OpenRLHF: https://github.com/OpenRLHF/OpenRLHF
- verl: https://github.com/volcengine/verl
- Megatron-LM: https://github.com/NVIDIA/Megatron-LM
- Megatron-Bridge: https://github.com/NVIDIA-NeMo/Megatron-Bridge
- Unsloth Vision RL: https://www.unsloth.ai/blog/vision-rl
- Qwen3-VL Best Practices (SWIFT): https://swift.readthedocs.io/en/latest/BestPractices/Qwen3-VL-Best-Practice.html
- TRL VLM Alignment Blog: https://huggingface.co/blog/trl-vlm-alignment
- Qwen Function Calling: https://qwen.readthedocs.io/en/latest/framework/function_call.html
- Post-Training in 2026 (LLM-stats): https://llm-stats.com/blog/research/post-training-techniques-2026
- Modern Post-Training Stack: https://medium.com/@fahey_james/dpo-isnt-enough-the-modern-post-training-stack-simpo-orpo-kto-and-beyond-d82e52a1ee6c
- EVAL #003 Fine-Tuning in 2026: https://dev.to/ultraduneai/eval-003-fine-tuning-in-2026-axolotl-vs-unsloth-vs-trl-vs-llama-factory-2ohg
- Advanced LoRA Fine-Tuning Guide: https://kaitchup.substack.com/p/advanced-lora-fine-tuning-how-to
- GRPO Primer (Wolfe): https://cameronrwolfe.substack.com/p/grpo
