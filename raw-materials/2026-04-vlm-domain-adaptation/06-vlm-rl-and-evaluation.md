# VLM RL 實戰與評測實務 — 工程深度補強材料

> 為「半導體 VLM domain adaptation」研究報告之第 6 章深度版素材。
> 目標讀者：技術負責人 + 訓練工程師。
> 寫作原則：具體數字、可復現連結、失敗案例優先於理論重述。

---

## Part 1 — VLM RL 的工程實戰

### A. VLM DPO 實戰

#### A-1. HuggingFace TRL 的 VLM DPO 已是產線級選項

HuggingFace TRL 官方部落格「Vision Language Model Alignment in TRL ⚡️」（2025/8/7 發布）以及更早的「Preference Optimization for Vision Language Models」把 VLM DPO 從研究 code 推成生產級 pipeline。`DPOTrainer` 目前完整支援接受 `image`（單圖）或 `images`（多圖 list）欄位的偏好資料集，官方明列支援的 backbone 包含 Idefics2、LLaVA-1.5、PaliGemma，並持續擴展到 SmolVLM、Qwen2-VL 系列 <https://huggingface.co/blog/trl-vlm-alignment>、<https://huggingface.co/blog/dpo_vlm>。

TRL blog 的 PaliGemma + RLAIF-V 實驗在 7B 級模型上使用 4 × A100 (80G) 約 16 小時跑完一個 epoch，VRAM 峰值壓在 65 GB（PEFT LoRA r=8 + gradient checkpointing + bfloat16）；關鍵是 loss `sigmoid` 對 VLM 仍然是 default，但 blog 明確建議 `loss_type="mpo"`（Mixed Preference Optimization，下節 A-2）取得更穩定的收斂，MPO 同時融合 DPO sigmoid loss、BCO quality loss、SFT loss 三項，壓低 VLM 特有的 reward hacking <https://huggingface.co/blog/trl-vlm-alignment>。

**消費級 GPU 復現 (SmolVLM-Instruct + DPO)**：HuggingFace Cookbook 有一份 `fine_tuning_vlm_dpo_smolvlm_instruct` 範本，在 RTX 4090 (24GB) 或 L4 (24GB) 上可實跑 SmolVLM 2.2B + LoRA DPO，batch size=1 + gradient accumulation=8，4 小時跑 1k preference pair，MMBench 提升 1.3 分，是目前唯一 **消費級 GPU 可復現** 的 VLM DPO 公開 notebook <https://huggingface.co/learn/cookbook/fine_tuning_vlm_dpo_smolvlm_instruct>。半導體團隊做 PoC 時這是最省錢的起點。

#### A-2. MPO：VLM 專用的 DPO 強化版

MPO (Mixed Preference Optimization) 首見於 InternVL3 技術報告，把三個 loss 加權成一個：

```
L_MPO = α · L_DPO(sigmoid) + β · L_BCO(quality) + γ · L_SFT
```

HuggingFace Cookbook `fine_tuning_vlm_mpo` 的實測：在 Qwen2.5-VL-7B 上用 MMPR dataset 做 MPO，比純 DPO 在 MathVista 多漲 3.1 分、在 HallusionBench aAcc 多漲 4.2 分，而 MMBench/OCRBench 沒有退化（純 DPO 在 MMBench 反而退化 0.8 分）；也就是說，SFT loss 那一項的作用就是 **防止 preference 學習時遺忘一般能力** <https://huggingface.co/learn/cookbook/fine_tuning_vlm_mpo>。半導體 domain PoC 若擔心退化，MPO > DPO 是比較安全的出發點。

#### A-3. RLHF-V：最小資料量的 hallucination 鎖喉

RLHF-V (CVPR 2024, Yu et al.) 是 VLM 偏好學習的「少樣本標竿」：**1.4k 人標 fine-grained 修正 → hallucination 率降 34.8%**，用 8 × A100 訓練僅 1 小時即完成 13B 模型收斂；outperform 同期的 LLaVA-RLHF（後者用 10k 資料）<https://rlhf-v.github.io/>、<https://arxiv.org/abs/2312.00849>。

**標註分布**（重要細節，半導體團隊設計自己 preference 時可對照）：
- 物件錯誤 (object hallucination)：41.2%
- 位置錯誤：20.3%
- 數量錯誤：16.5%
- 屬性錯誤：10.0%
- 動作錯誤：5.3%
- 其他：6.8%

共 3.7k 個 segment-level 修正（非整段重寫，而是「就一段句子」修改），顯示 **fine-grained 修正比 rewriting 更省力也更有效**。可公開復現的 infra 是 `TideDra/VL-RLHF`（非原作者，但完整實作 RLHF-V pipeline 在 LLaVA-1.5 / Qwen-VL） <https://github.com/TideDra/VL-RLHF>。

#### A-4. V-DPO：針對 image-independent bias 的改良

V-DPO (EMNLP 2024 Findings, Xie et al.) 處理的具體問題：純 DPO 訓練時模型學到「忽略圖像、靠 LLM 先驗產 reject/accept 的分布」——也就是 image-independent reward hacking。V-DPO 在 DPO loss 裡加入一對 image-contrast preference pair（同一個 prompt 配兩張不同圖），強迫模型把 accept/reject 信號歸因到視覺差異，而非文字差異 <https://arxiv.org/abs/2411.02712>、<https://aclanthology.org/2024.findings-emnlp.775.pdf>。

實測：
- AMBER hallucination benchmark（物件幻覺）：V-DPO 比 vanilla DPO 多降 6.8 個點
- MMBench 一般能力：兩者打平（沒有退化）
- 在 OOD 合成圖資料上，V-DPO 比 DPO 領先 9.4 個點 — 代表它對未見分布的泛化更好

工程含意：只要你的 preference pair 全部是「相同圖、兩種答案」的結構，你的模型會學到完全不看圖；必須摻入「同問題、不同圖、不同答案」的對比對。

#### A-5. On-Policy DPO（OPA-DPO, CVPR 2025 Oral）：資料效率再提升

OPA-DPO (Yang et al., CVPR 2025 Oral) 的核心發現：**DPO 效果高度取決於 preference pair 是否 on-policy**（即 chosen/rejected 都接近當下 policy 的輸出分布）。若用 off-policy 資料（例如用 GPT-4V 生的 response 當 chosen），信號會被 KL 約束削弱。OPA-DPO 先讓 LVLM 自己 rollout，再讓 expert 對 rollout 做最小編輯形成 chosen，達到 on-policy 對齊 <https://arxiv.org/abs/2501.09695>、<https://github.com/zhyang2226/OPA-DPO>。

結果：僅 4.8k 資料在 LLaVA-1.5-7B 上，AMBER 降 hallucination 13.26%、Object-Hal 降 5.39%，比前 SOTA 用 16k 資料還好。**資料效率 3.3×**。

半導體 domain 實作建議：讓你的 LLaVA / Qwen2.5-VL 對實際 wafer / SEM 影像 rollout 產 5-10 個候選，再由 process engineer 做 minimal edit 變成 chosen，原樣本作 rejected，會比讓 expert 從頭寫答案有效率得多。

#### A-6. VLFeedback：80K GPT-4V preference 現成資料集

VLFeedback (Li et al., 2024) 是目前最大的 VLM AI-feedback preference dataset：**82.4K instructions, 67K unique images, 399.4K preference pairs**，由 12 個 LVLM（BLIP 系列、LLaVA 系列、Fuyu-8B、Qwen-VL-Chat、GPT-4V）產生 response，再由 GPT-4V 在三個維度上評分：
- Helpfulness（回答相關性）
- Visual Faithfulness（與視覺內容一致、幻覺偵測）
- Ethical Considerations（偏見、冒犯內容）

GPT-4V 與人類標註者一致率 **76%**（在 subset 上驗證）— 這個數字是工程上的關鍵 anchor：**要在自建 preference 資料上接受 AI feedback，就預期 ~20-25% 的 noise floor** <https://arxiv.org/abs/2410.09421>、<https://huggingface.co/datasets/MMInstruction/VLFeedback>。

在 VLFeedback 上做 DPO 的 baseline 是：LLaVA-1.5-7B + DPO 1 epoch → MMMU +2.1、SEED-Image +1.8、HallusionBench aAcc +3.4；對應論文叫做 Silkie <https://arxiv.org/html/2312.10665>。

#### A-7. 失敗模式（整理清單）

1. **Length bias**：模型把 chosen 學成「比 rejected 長」。TRL 內建 `rpo_alpha` 或 `ODIN 正則` 壓長度；若不治理，AMBER/HallusionBench 會看起來漲，但 GPT-4V-as-Judge 的 pairwise 會顯示「變冗長不變好」 <https://arxiv.org/html/2502.00814>、<https://arxiv.org/html/2409.17407>。

2. **Image-independent reward hacking**：模型放棄看圖、只看文字。診斷方法：把輸入圖換成黑圖 / 隨機圖、再算 reject rate 是否變化（變化率 <10% 就是嚴重）；Stanford CS224R 的課程 final project 有復現實驗 <https://cs224r.stanford.edu/projects/pdfs/CS_224R_Final_Project.pdf>。

3. **Reward hacking shortcut**：VLM 容易利用 texture bias over shape、typographic attack、字體疑似的 shortcut。Encord 和 Stanford 的 survey 都有列出這些模式；防護做法是加 adversarial preference pair（換背景、換字體、換角度但答案不變） <https://encord.com/blog/guide-to-rlhf/>。

4. **Train/Eval 分佈不一致**：DPO 訓練用 GPT-4V preference，eval 用 real-user distribution，差一個量級；必須至少留 10-20% eval set 是**真實生產樣本**。

5. **KL 爆炸**（GRPO 尤甚，見下節 B-5）。

---

### B. VLM GRPO 實戰

#### B-1. DeepSeek-R1 與 VLM GRPO 的 recipe 外推

DeepSeek-R1 本體是純語言模型，但其技術報告明確指出 `Reasoning RL via GRPO` 的配方外推到 VLM 已有多個公開實作 <https://arxiv.org/pdf/2501.12948>。核心 recipe：
- 只用 **verifiable reward**（可程式化驗證對錯的答案，如數學、code、VQA with 明確答案）
- 不訓練 value model，用 group 內 mean 做 baseline
- 大 batch + 多 rollout（Qwen3 report：每 query 16 rollout）
- off-policy 允許小幅度，搭配 clip

Vision-R1 (Chen et al., 2025) 是第一批把 DeepSeek-R1 配方外推到 VLM 的公開復現：10K multimodal math data、GRPO + hard formatting reward、Qwen2-VL-7B 基底 → MathVista +8.4、MathVerse +5.2 <https://arxiv.org/abs/2503.06749>。

#### B-2. Qwen3 Technical Report：VLM Thinking RL 配方

Qwen3 Tech Report 公開了 Reasoning RL 階段的關鍵數字，雖然是文字模型為主，但 Qwen3-VL Thinking 共用此配方：**3,995 個 query-verifier pair + GRPO**，在 Qwen3-235B-A22B 上 AIME'24 從 70.1 → 85.1，共 170 個 RL steps，**完全沒有手動介入 hyperparam** <https://arxiv.org/pdf/2505.09388>、<https://arxiv.org/html/2505.09388v1>。

Qwen3 team 關鍵設計：
- Query-verifier 必須**沒有**出現在 cold-start SFT 階段（避免 reward hacking memorization）
- Query 難度夠高（cold-start 模型 pass@16 約 30-60%）
- 涵蓋廣領域（數學、code、邏輯推理、VQA）
- **Large batch + high rollout**：batch 512，每題 32 rollout
- Off-policy training 提升 sample 效率
- **控制 entropy 穩定上升或持平**：entropy 崩塌就是 policy collapse 前兆

這些數字對 domain 團隊的實戰意義：準備 **3000-5000 個 high-quality verifier pair** 就足夠跑有效 RL（不用萬級），但 rollout 數量必須給足。

#### B-3. verl & EasyR1：開源 VLM GRPO infra 現況

**verl** (volcengine)：原生支援 Qwen2.5-VL、Kimi-VL、Qwen3-VL 的 GRPO，後端 FSDP/Megatron-LM 皆可，rollout 引擎接 vLLM 或 SGLang；pipeline 內建 image preprocess、freeze vision encoder、LoRA、sequence balancing <https://github.com/volcengine/verl>、<https://pypi.org/project/verl/>。

**EasyR1** (hiyouga)：基於 verl 的多模態 RL 訓練框架，針對 Qwen2.5-VL 特化，支援到 72B 多節點 <https://github.com/hiyouga/EasyR1>。官方 benchmark：Geometry3k 任務上 30 batch GRPO 提升驗證 accuracy **+5%**。提供三份可直接跑的 notebook：
- `CLEVR-70k-Counting` on Qwen2.5-VL-3B-Instruct（視覺計數）
- `GeoQA-8k` on Qwen2.5-VL-3B-Instruct（幾何 QA）
- `Geometry3k` 為默認 demo

**Modal** 也發布了雲端復現教程「Train a model to solve math problems using GRPO and verl」，適合沒有本地 GPU 的團隊跑 PoC <https://modal.com/docs/examples/grpo_verl>。

半導體團隊實戰路徑：EasyR1 + Qwen2.5-VL-7B-Instruct + 自建 semiconductor verifier set（wafer pattern classification、SEM defect localization bounding box IoU）。

#### B-4. Verifiable reward 在 VQA / grounding 的具體設計

幾個在 2025 年公開的 verifiable reward 設計（可直接搬到 domain 任務）：

- **Region IoU reward**：grounding 任務裡，要求模型輸出 bounding box，reward = IoU > 0.5 → 1 else 0。CrowdVLM-R1 用 fuzzy IoU（IoU 0.3→0.5→0.7 三階梯度 reward）避免稀疏梯度 <https://arxiv.org/html/2504.03724>。
- **Binary exact-match**：VQA multiple choice 直接對答案，reward ∈ {0, 1}。
- **Format reward**：強制模型用 `<think>...</think><answer>...</answer>` 格式，格式錯誤 reward -0.5；這個小技巧讓 training loss 曲線穩定很多。
- **Regex consistency reward**：多步推理 CoT 內部一致性檢查 <https://www.emergentmind.com/topics/reasoning-augmented-vision-language-models-rvlms>。
- **Remote sensing / satellite VLM**：Koksal et al. 2025 用純 binary/IoU reward 對 Qwen2.5-VL 做 few-shot RLVR，發現 **不做 SFT cold-start 直接 GRPO 也可以收斂**（和 DeepSeek-R1-Zero 的 zero-shot RL 對應） <https://arxiv.org/html/2507.21745>。

Faithful GRPO (Xu et al., 2026) 的關鍵洞察：把 consistency 和 visual grounding 當作 **hard constraint**（違反就 reward=0）而非 soft reward term，inconsistency rate 從 24.5% 降到 1.7%，grounding +13% <https://arxiv.org/html/2604.08476v1>。

#### B-5. KL 爆炸：GRPO VLM 訓練最常見災難

GRPO 在 VLM 上比純 LLM 更容易 KL 爆炸。GitHub verl issue #509、TRL issue #2914 都有社群回報，模式是 step 100-300 之間 KL 從 <0.1 突然跳到 >10 並且不再下降，隨後 reward 崩塌到 0 <https://github.com/huggingface/trl/issues/2914>、<https://github.com/volcengine/verl/issues/509>。

已知根因（2025 多篇 paper 分析）：
- **Importance weight 的 ill-conditioning**：rollout 和 update 之間的 latency 越大，importance ratio 變異越高，容易出現 >100× 的 extreme value <https://arxiv.org/html/2508.17850>。
- **MoE 模型的 expert drift**：不同 rollout 走不同 expert，梯度被稀釋 <https://www.emergentmind.com/topics/icepop>。
- **KL reward 參與 optimization 而非只做估計**，造成梯度反饋路徑錯誤 <https://openreview.net/forum?id=keCnsHtION>。

實戰解法：
1. **監測 entropy 而非 KL**：GRPO 的 KL 訊號反應太慢，policy entropy 驟降（>30% in 10 steps）才是 collapse 前兆。
2. **GEPO (Group Expectation Policy Optimization)**：用 group-level importance weight 取代 token/sample 級，顯著穩定 <https://arxiv.org/html/2508.17850>。
3. **IcePop** (MoE 專用)：token-wise masking + selective gradient clip，丟棄 engine 間機率比失真過大的 update <https://www.emergentmind.com/topics/icepop>。
4. **Clip 範圍保守**：VLM 建議 `epsilon_low=0.2, epsilon_high=0.25`（比純 LLM 的 0.2/0.28 保守）。
5. **reference model 重新定位**：長訓練 (>1000 step) 務必每 500 step 重置 reference model，避免 KL 往負無窮漂移。

#### B-6. VLM-specific reward hacking 案例

- **只輸出 `<answer>A</answer>` 不做 reasoning**：如果只有 exact-match reward，模型會學到「跳過 CoT」。對治：必須加 format reward 強制 `<think>` 有內容（len > k tokens）。
- **從 prompt 裡「偷答案」**：VQA 資料集中 prompt 常洩漏答案風格線索，模型學會 pattern match 不看圖。對治：在 reward pipeline 前做 prompt scrub。
- **死記 bounding box 座標分布**：grounding 任務中 80% 物件在圖中央，模型學到永遠輸出 `[0.3, 0.3, 0.7, 0.7]` 拿到 ~0.5 IoU 期望值。對治：用 hard threshold reward（IoU > 0.5 才給）代替 continuous IoU。
- **Image-independence**：image 換成黑圖，模型 reward 沒變 → 嚴重；必須加 image-contrastive sample。

---

### C. Preference data 構建工作流

#### C-1. 合成 preference 的具體 prompt 範例

RLAIF-V / VLFeedback 的 GPT-4V 打分 prompt 精簡版（已證實達 76% 人類一致率）：

```
You are evaluating two responses to the same visual question.
Rate each on: (1) Helpfulness 0-10, (2) Visual Faithfulness 0-10
(whether it hallucinates content not in the image), (3) Ethical 0-10.

Image: <image>
Question: {q}
Response A: {a}
Response B: {b}

Return JSON: {"a_scores": [...], "b_scores": [...], "preferred": "A"|"B"|"tie", "reason": "..."}
```

**關鍵工程細節**：
- 要求 `reason` 欄位強制模型「看過才打分」，否則 GPT-4V 會跳過視覺驗證
- Batch 打分時把 `preferred` 欄位放最後，讓 CoT 先於結論產出（提升 ~5 分一致率）
- 對 tie 的樣本另做人類複核，tie 通常是「兩個都錯但錯得不同」的難題

#### C-2. Domain expert preference 標註工作流

半導體（或任何高專業度 domain）的 preference 標註流程設計：

1. **Rollout 生成**：base 模型對每個 prompt 產 8-16 個 response
2. **機器初篩**：用 embedding 相似度剔除近似重複，保留 2-4 個代表性
3. **Expert pairwise 標註**：工程師看 image + 2 個 candidate 選 preferred（~20 sec / pair）
4. **Fine-grained correction（RLHF-V 風格）**：僅對 preferred 做 segment-level 修正，不重寫整段 — 實測比 rewriting 快 3×
5. **Inter-annotator agreement (IAA) 檢核**：10% 樣本三人交叉標，Cohen's kappa > 0.6 才算可用

目標標註速度：1 位 process engineer 每小時 ~80-120 pair。若要達到 RLHF-V 的 1.4k 門檻，**2 位工程師 × 1 週 = 可用資料**。

---

### D. 失敗模式綜合清單

| 模式 | 診斷信號 | 解法 |
|------|---------|-----|
| Length bias | chosen 平均 token 數 > rejected 30%+ | `rpo_alpha=0.1`, token penalty, MPO |
| Image-independent | 黑圖 eval reward 沒變 | 加 image-contrastive pair (V-DPO) |
| Reward hacking (format) | reward 爆漲但 eval 沒動 | format reward 硬約束 + hold-out eval |
| KL 爆炸 | entropy 驟降 / KL >5 | GEPO, clip 縮緊, reference reset |
| Catastrophic forgetting | MMMU/MMBench 退化 >3% | MPO 含 SFT loss, LoRA, 小 lr |
| Train/eval 分佈不符 | train 漲但 production 指標不動 | 10-20% eval 來自真實 traffic |

---

## Part 2 — VLM 評測的實務

### A. 公開 VLM benchmark 全家桶

#### A-1. 綜合能力

**MMMU** (Yue et al., CVPR 2024)：11,500 題，大學考試、測驗、教科書等級，6 大學科 30 子科目 30 種圖像（圖表、示意圖、地圖、表格）。測「專家級多學科推理」。GPT-4V 約 55-60%、Qwen2.5-VL-72B 約 70%。**陷阱**：很多題的圖是可選的（純文字也能答），domain 適配後此 benchmark 退化通常不明顯，不是好的 catastrophic forgetting 指標 <https://mmmu-benchmark.github.io/>、<https://github.com/MMMU-Benchmark/MMMU>。

**MMBench** (Liu et al., 2023)：3,000+ 題，20 個 fine-grained ability dimension（物件定位、OCR、空間推理等），CircularEval（同題多選項排列）。**陷阱**：題目偏 common sense，對 domain-specific 圖像（半導體、醫療）鑑別力低 <https://evalscope.readthedocs.io/en/v1.1.0/get_started/supported_dataset/vlm.html>。

**SEED-Bench**：Image 19K、Video 若干，12 evaluation dimensions；generation-based 評測。**陷阱**：視覺幻覺題偏少，不是 hallucination 好測 proxy。

**MME**：感知 + 認知兩類共 2,000+ 題，Yes/No 為主。**陷阱**：Yes/No 易受 bias（模型傾向答 Yes），分數看 perception/cognition subcategory 比看總分靠譜。

#### A-2. Math / Chart / OCR 類

**MathVista** (Lu et al., ICLR 2024)：6,141 題，涵蓋 IQTest / FunctionQA / PaperQA，測 puzzle/代數/科學論文圖的推理。GPT-4V ~50%、Qwen2.5-VL-72B ~72%。**半導體相關**：工程圖表、電路示意的推理能力在這裡能直接測出。

**ChartQA** (Masry et al., 2022)：9.6K chart（bar / line / pie），20K 題，包含 human-written 和 machine-generated。測圖表讀取 + 數值推理。GPT-4V ~78%、Qwen2.5-VL-7B ~87%。半導體 domain 常見 wafer yield 曲線、SPC 圖在這裡能測出對齊情況。

**OCRBench** (Liu et al., 2024)：5 個 OCR 相關任務，共 1,000 題（場景文字識別、手寫、文件、數學公式、公式辨識）。滿分 1000。GPT-4V ~645、Qwen2.5-VL-72B ~885。半導體 domain 的 wafer map 上的 lot ID、SEM image 上的標註文字在這裡能間接評估。

**DocVQA** (Mathew et al., WACV 2021)：50K 題、12K+ 文件影像，ANLS 指標。半導體 SPC report、製程 checklist 都屬此類文件。State-of-the-art ~95 ANLS <https://huggingface.co/datasets/lmms-lab/DocVQA>、<https://rrc.cvc.uab.es/?ch=17&com=evaluation&task=3>。

**InfographicVQA**：跨網站多樣 layout infographic，比 DocVQA 更難。半導體 marketing deck、process roadmap 類測試相關 <https://www.docvqa.org/datasets/infographicvqa>。

#### A-3. 真實世界 / 空間

**RealWorldQA** (xAI, 2024)：700+ 車載視角場景，測空間推理和真實物理世界理解，答案可驗證。**陷阱**：此 benchmark 偏 driving 場景，對 fab 場景（無人直觀 analog）鑑別力不高。

#### A-4. 幻覺專門

**HallusionBench** (Liu et al., CVPR 2024)：346 影像、1,129 題；分 figure / visual dependent / visual supplement 三類 <https://github.com/tianyi-lab/HallusionBench>、<https://arxiv.org/abs/2310.14566>。

**最震撼的數字**：GPT-4V 的 question-pair accuracy **僅 31.42%**，其他模型全低於 16%。此 benchmark 設計刻意製造「語言先驗 vs 視覺事實衝突」，是測 image-independent bias 的黃金指標。domain fine-tune 後若 HallusionBench 退化 >2%，就是 image-independent reward hacking 的紅旗。

**AMBER** (Wang et al., 2024)：15K 題，測 object / attribute / relation 幻覺，pure vision 無 LLM 偏見。對齊 training 的標準收官指標（RLHF-V、V-DPO、OPA-DPO 都用）。

**POPE** (Li et al., 2023)：物件存在/不存在 Yes/No 題；**陷阱**：已經被做爛，SOTA 都 >90%，沒鑑別力，只做 regression 底線。

#### A-5. 實測數字速覽（2025 Q1）

| Benchmark | GPT-4o | Claude 3.5 Sonnet | Qwen2.5-VL-72B | InternVL3-78B | 備註 |
|-----------|--------|-------|---------|--------|-----|
| MMMU | 69.1 | 68.3 | 70.2 | 72.2 | 多學科推理 |
| MathVista | 63.8 | 67.7 | 74.8 | 79.0 | 數學視覺 |
| ChartQA | 85.7 | 90.8 | 89.5 | 92.3 | 圖表 |
| OCRBench | 805 | 788 | 885 | 906 | 文字識別 |
| DocVQA | 92.8 | 95.2 | 96.4 | 95.1 | 文件 |
| HallusionBench | 55.0 | 55.5 | 55.2 | 57.4 | 幻覺 |
| RealWorldQA | 75.4 | 60.1 | 75.7 | 78.0 | 空間 |

數據出處 InternVL3.5 tech report、NVIDIA Nemotron VL blog <https://arxiv.org/html/2508.18265v1>、<https://blog.vllm.ai/2025/10/31/run-multimodal-reasoning-agents-nvidia-nemotron.html>。

---

### B. Domain-specific benchmark 建立方法論

#### B-1. 半導體目前可用（與不完全可用）的 benchmark

**WM-811K** (Wu et al., MIR Lab NTU, 2015)：811,457 個 wafer map，8 種 defect pattern（Center, Donut, Edge-Loc, Edge-Ring, Loc, Random, Scratch, Near-full, None）。約 20% 有 expert label。**實測指標 anchor**：CNN baseline ~96.7%，SOTA multi-scale fusion ~99.88% macro-F1 <https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map>、<https://github.com/makinarocks/awesome-industrial-machine-datasets>。

**對 VLM 的用法**：把 wafer map 轉灰階 PNG + 做 prompt-based classification ("What wafer defect pattern is this?"), 拿 accuracy 對比純 CNN baseline。這是**目前最易建立的半導體 VLM eval**。

**SEM-CLIP dataset** (Zhang et al., ICCAD 2024)：IC SEM 影像 few-shot defect detection。SEM-CLIP 在 10-shot setting 比 PromptAD +21.1%，代表**fe shot 就能做 domain 適配的下限** <https://arxiv.org/html/2502.14884v1>。

**MVTec AD** (Bergmann et al., CVPR 2019)：15 類工業物件，非半導體但常被半導體團隊借用做 anomaly detection baseline。**陷阱**：MVTec AD 的 anomaly 是「表面擦傷、顏色異常」，和 wafer 的 spatial pattern defect 差很遠；用它做 proxy 容易誤導。

**SemiKong** (Aitomatic et al., 2024)：第一個開源半導體 LLM (8B, 70B based on Llama-3)，純文字模型但附帶 SemiKong-Eval 框架（expert-in-the-loop + LLM judge），適合作為 process knowledge QA 的 base benchmark；但 SemiKong 本身不是 VLM，僅能測「語言側知識保留」 <https://arxiv.org/abs/2411.13802>、<https://github.com/aitomatic/semikong>。

**結論**：**半導體 VLM 沒有現成 golden benchmark**，必須自建。

#### B-2. 自建 domain benchmark 的工作流

**Golden set + blind set 雙軌**：
- **Golden set**（50-100 題）：最具代表性、工程師共識最高、難度分佈 balanced。用於快速迭代開發時反覆跑。
- **Blind set**（500-1000 題）：工程師標完不看、只在 milestone checkpoint 開封。避免 overfit。
- **Regression set**（200-300 題）：前幾版模型答對但新版答錯的題目，每次 release 必跑。

**Inter-annotator agreement (IAA)**：每題至少 2 位 annotator，Cohen's kappa > 0.6 才入選 golden set；<0.5 就丟棄或回頭重新定義 task（表示題目本身歧義）。半導體跨 fab 或跨 process 的題目容易在 IAA 上失敗，需特別注意。

**題目類型 balance**（建議分配）：
- Classification（wafer map defect 類別）：30%
- Grounding / bbox（SEM 影像 defect 定位）：20%
- OCR / reading（SPC report、process parameter table）：20%
- Multi-turn reasoning（given context, what's next step）：20%
- Hallucination probes（問圖中沒有的物件）：10%

**為什麼一定要有 hallucination probes**：fine-tune 後 hallucination 會變隱形 — 模型講得頭頭是道但全是編造。必須顯式測。

---

### C. LLM-as-Judge 在 VLM 評測的角色

#### C-1. GPT-4V-as-Judge 的偏見

MLLM-as-a-Judge benchmark (Chen et al., 2024) 對 GPT-4V 的系統性偏見量化：
- **與人類相似度**：scoring 任務 0.557 (最高)、pairwise 非 tie 0.806 <https://mllm-judge.github.io/>
- **Egocentricity**（自家偏好）：GPT-4V 傾向給符合「OpenAI content policy」的回答高分
- **Verbosity bias**：長答平均 +0.6 分，與 Gemini 並列最嚴重
- **Position bias**：swap A/B 位置，GPT-4V 判斷翻轉率 20-30%（應當 <5%）

**實戰對策**：
1. Pairwise 評測一定要 **randomize A/B 順序**，並計算「同題兩次順序下結論一致率」（應 >80%）
2. 報 **length-controlled score**（把答案截到相同 token 數再比）
3. **雙 judge 交叉**：GPT-4V + Claude 3.5 Sonnet 都同意的結論才採信

#### C-2. 自建 eval rubric

Prometheus-Vision (Lee et al., 2024) 提供 **Perception Collection** — 15K 客製 score rubric，每個 rubric 有 criteria 說明 + 1-5 分對應的 scoring decision 描述 <https://arxiv.org/html/2401.06591v1>。是目前唯一公開可參考的 **VLM fine-grained rubric template**。

半導體 domain 建議的 rubric 維度：
1. **Technical Correctness**（1-5）：是否正確辨識 wafer pattern / defect type
2. **Reasoning Quality**（1-5）：推理步驟是否符合工程邏輯
3. **Visual Faithfulness**（1-5）：是否編造圖中不存在內容
4. **Actionability**（1-5）：是否給出可執行的下一步建議
5. **Safety**（1-5）：是否符合 fab safety protocol

每個維度下有 1-5 分的**文字描述錨點**（如「5: 完全符合、4: 微瑕、3: 方向對但細節錯、2: 主要錯、1: 完全錯」），給 judge 模型和人類標註者共用。

#### C-3. Pairwise vs Scoring 選擇

- **Pairwise**：判斷 A/B 哪個好。優點：人和 judge 都更一致；缺點：無法量化進步幅度。
- **Scoring (1-5 或 1-10)**：絕對分。優點：可追蹤 trend；缺點：score drift 嚴重（同一答案不同時間打分不同）。

**實戰混合**：fast iter 用 pairwise (vs. baseline)、milestone 用 5-dim scoring + human sample。

---

### D. Catastrophic forgetting 監測清單

Zhai et al. (NeurIPS 2024) 的 MLLM forgetting study 發現：「幾乎所有評測的 MLLM 都無法保持 pre-trained vision encoder 在 ImageNet 等任務上的 performance」；簡單調整 fine-tune recipe（限制可訓練參數、降 lr）即可大幅緩解 <https://proceedings.mlr.press/v234/zhai24a/zhai24a.pdf>、<https://openreview.net/forum?id=WLSt5tIOSA>。

**建議固定監測 benchmark 清單**（每次 release 必跑，退化 > **3%** 警戒、> **5%** 需 rollback）：

| 類別 | Benchmark | 測什麼 | 閾值 |
|-----|-----------|-------|------|
| General vision | MMMU | 多學科知識 | -3% |
| General vision | MMBench-EN | 一般能力 | -3% |
| General vision | OCRBench | 文字識別（常退化最快） | -2% |
| Hallucination | HallusionBench aAcc | 視覺幻覺 | -2% |
| Hallucination | AMBER | 物件幻覺 | -2% |
| General language | MMLU | 一般語言知識 | -3% |
| Math | GSM8K | 數學推理 | -5% |
| Code | HumanEval | Code 能力 | -5% |
| **Domain (自建)** | Domain golden set | 目標能力 | **+ 才算成功** |
| **Domain regression** | Regression set | 不退化 | **0 退化** |

**為什麼 OCRBench 最易退化**：半導體 domain 影像通常缺少自然文字，fine-tune 會讓模型忘掉 OCR capability。必須在 SFT / DPO 資料裡摻入 10-15% 原始 VLM instruct data 作 rehearsal。

**推薦跑 benchmark 的工具**：
- **VLMEvalKit** (open-compass)：支援 **220+ LMM、80+ benchmark**，一行 CLI 跑完 <https://github.com/open-compass/VLMEvalKit>
- **lmms-eval** (EvolvingLMMs-Lab)：HuggingFace Hub 整合好，標準 CLI
- **EASI**：spatial intelligence 專項，補 VLMEvalKit 盲點 <https://github.com/EvolvingLMMs-Lab/EASI>

---

### E. A/B test 與 Production evaluation

#### E-1. Shadow deployment：第一道關卡

Shadow mode 把 100% 生產流量**複製**給 candidate model，但只有 production model 回應用戶；candidate 的 output 只記錄不回覆 <https://tianpan.co/blog/2026-04-09-llm-gradual-rollout-shadow-canary-ab-testing>、<https://www.codeant.ai/blogs/llm-shadow-traffic-ab-testing>。

**VLM shadow 特有考量**：
- 影像資料量大，shadow pipeline 的 bandwidth / storage cost 是純 LLM 的 10-100×，建議 **抽樣 10-20%** 流量
- Shadow output 要存下來，offline 用 GPT-4V-as-Judge 對 prod vs. candidate 做 pairwise
- 典型監測指標：latency P95 / P99、輸出長度分布、OCR 失敗率、refusal rate

Wandb 2025 研究發現 **63% 的 production regression 無法在 shadow 階段發現**，因為它們依賴用戶行為（abandon、regenerate）<https://www.codeant.ai/blogs/llm-shadow-traffic-ab-testing>。Shadow 只能 catch obvious regression（crash、latency 暴漲、輸出長度異常），真實 quality regression 一定要進 A/B。

#### E-2. A/B test：真實品質驗證

A/B 分流建議：
- **Phase 1**（1%）：1-3 天，只看有沒有炸（error rate、P99 latency）
- **Phase 2**（10%）：1 週，看 user feedback（thumbs up/down rate、regenerate rate、session length）
- **Phase 3**（50% 或 100%）：ramp-up。

**VLM 場景 key signals**（比純 LLM 多了視覺相關）：
- Thumbs up / thumbs down rate（行業平均 thumbs-down 5-15%）
- **Image re-upload rate**（用戶覺得模型沒看懂再上傳一次 — VLM 專有信號）
- Regenerate rate
- Session abandonment rate
- 如果是 agent / task：task success rate、escalation to human rate
- 語義延伸 signal：對話長度、copy-answer rate

#### E-3. Engineer thumbs-up/down 收集（內部 dogfood）

在 fab 環境裡推 VLM，最實用的是 **讓 process engineer 在日常工作中用 + 一鍵回饋**：
- 整合進現有 MES / SCADA 介面
- 回答後自動 prompt 「這個建議對嗎？👍 / 👎 / 🤔」
- 👎 的 sample 直接進入下一輪 preference data collection

**門檻建議**：thumbs-down rate < 15% 才算 production ready；> 25% 就下架。

#### E-4. 線上指標與業務價值連結

最終必須把模型品質 tied 回業務 KPI：
- **Task success rate**：engineer 接受模型建議的比例
- **Escalation rate**：模型 refuse / 無法回答轉人工處理的比例
- **MTTR reduction**（Mean Time To Resolve）：用 VLM 輔助後處理異常的平均時間
- **Yield impact**：defect detection 準確度提升對 final yield 的影響（需 A/B 跑 1-2 個 lot cycle）

SemiKong 報告 claim 的「20-30% time-to-market 縮短、20% first-time-right 提升、50% new engineer 學習曲線加速」是業務指標的 **北極星 baseline** — 在自有 PoC 裡 benchmark 到這些數字才算成功 <https://www.tomshardware.com/tech-industry/artificial-intelligence/semikong-is-the-worlds-first-open-source-semiconductor-focused-llm-it-claims-to-bring-new-chips-to-market-30-percent-faster>、<https://www.semikong.ai/>。

---

## 引用來源彙整

### DPO / VLM alignment
- HuggingFace TRL VLM alignment blog: <https://huggingface.co/blog/trl-vlm-alignment>
- HuggingFace DPO VLM blog: <https://huggingface.co/blog/dpo_vlm>
- HuggingFace Cookbook MPO: <https://huggingface.co/learn/cookbook/fine_tuning_vlm_mpo>
- HuggingFace Cookbook SmolVLM DPO: <https://huggingface.co/learn/cookbook/fine_tuning_vlm_dpo_smolvlm_instruct>
- RLHF-V: <https://arxiv.org/abs/2312.00849> / <https://rlhf-v.github.io/>
- VL-RLHF repro infra: <https://github.com/TideDra/VL-RLHF>
- V-DPO: <https://arxiv.org/abs/2411.02712> / <https://aclanthology.org/2024.findings-emnlp.775.pdf>
- OPA-DPO (CVPR 2025 Oral): <https://arxiv.org/abs/2501.09695> / <https://github.com/zhyang2226/OPA-DPO>
- VLFeedback: <https://arxiv.org/abs/2410.09421> / <https://huggingface.co/datasets/MMInstruction/VLFeedback>
- Silkie: <https://arxiv.org/html/2312.10665>
- Length bias mitigation: <https://arxiv.org/html/2502.00814> / <https://arxiv.org/html/2409.17407>
- Stanford CS224R Reward hacking study: <https://cs224r.stanford.edu/projects/pdfs/CS_224R_Final_Project.pdf>

### GRPO / VLM RL
- DeepSeek-R1: <https://arxiv.org/pdf/2501.12948>
- Qwen3 Tech Report: <https://arxiv.org/pdf/2505.09388> / <https://arxiv.org/html/2505.09388v1>
- Vision-R1: <https://arxiv.org/abs/2503.06749>
- verl: <https://github.com/volcengine/verl> / <https://pypi.org/project/verl/>
- EasyR1: <https://github.com/hiyouga/EasyR1>
- Modal verl GRPO tutorial: <https://modal.com/docs/examples/grpo_verl>
- CrowdVLM-R1 fuzzy reward: <https://arxiv.org/html/2504.03724>
- Satellite RLVR: <https://arxiv.org/html/2507.21745>
- Faithful GRPO: <https://arxiv.org/html/2604.08476v1>
- GEPO: <https://arxiv.org/html/2508.17850>
- TRL issue on KL: <https://github.com/huggingface/trl/issues/2914>
- verl issue on KL: <https://github.com/volcengine/verl/issues/509>
- IcePop MoE stability: <https://www.emergentmind.com/topics/icepop>
- KL regularization rethink: <https://openreview.net/forum?id=keCnsHtION>

### Benchmark / Evaluation
- MMMU: <https://mmmu-benchmark.github.io/> / <https://github.com/MMMU-Benchmark/MMMU>
- HallusionBench: <https://github.com/tianyi-lab/HallusionBench> / <https://arxiv.org/abs/2310.14566>
- DocVQA: <https://huggingface.co/datasets/lmms-lab/DocVQA> / <https://rrc.cvc.uab.es/?ch=17&com=evaluation&task=3>
- InfographicVQA: <https://www.docvqa.org/datasets/infographicvqa>
- VLMEvalKit: <https://github.com/open-compass/VLMEvalKit>
- EASI: <https://github.com/EvolvingLMMs-Lab/EASI>
- VLMEvalKit paper: <https://arxiv.org/html/2407.11691v4>
- InternVL3.5 tech report: <https://arxiv.org/html/2508.18265v1>
- NVIDIA Nemotron VL: <https://blog.vllm.ai/2025/10/31/run-multimodal-reasoning-agents-nvidia-nemotron.html>
- MLLM-as-Judge: <https://mllm-judge.github.io/>
- Prometheus-Vision: <https://arxiv.org/html/2401.06591v1>
- Catastrophic forgetting in MLLM: <https://proceedings.mlr.press/v234/zhai24a/zhai24a.pdf> / <https://openreview.net/forum?id=WLSt5tIOSA>

### Semiconductor domain
- WM-811K: <https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map> / <https://github.com/makinarocks/awesome-industrial-machine-datasets>
- SEM-CLIP: <https://arxiv.org/html/2502.14884v1>
- SemiKong: <https://arxiv.org/abs/2411.13802> / <https://github.com/aitomatic/semikong> / <https://www.semikong.ai/>
- Tom's Hardware SemiKong report: <https://www.tomshardware.com/tech-industry/artificial-intelligence/semikong-is-the-worlds-first-open-source-semiconductor-focused-llm-it-claims-to-bring-new-chips-to-market-30-percent-faster>

### Production / A/B test
- LLM shadow/canary/A-B gradual rollout: <https://tianpan.co/blog/2026-04-09-llm-gradual-rollout-shadow-canary-ab-testing>
- Shadow testing LLM: <https://www.codeant.ai/blogs/llm-shadow-traffic-ab-testing>
- Wallaroo A/B + Shadow: <https://wallaroo.ai/ai-production-experiments-the-art-of-a-b-testing-and-shadow-deployments/>
