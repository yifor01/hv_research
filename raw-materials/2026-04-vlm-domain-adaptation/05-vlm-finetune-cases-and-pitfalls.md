# 05 · VLM Fine-tuning 真實世界案例與踩坑錄

> 素材定位：為半導體 VLM domain adaptation 研究報告蒐集「工程師踩過的坑 + 可量化成果 + 工單式教訓」。
> 不做方法論論述（那在 01/02 縱橫章節）；這裡只負責「誰做過、數字多少、踩什麼坑、解法是什麼、URL 在哪裡」。
> 素材蒐集時間：2026-04，資訊 snapshot。

---

## 目次
- A. 跨領域公開案例盤點（Medical / Document AI / Industrial / Robotics / Chart / Retail / Legal）
- B. 典型踩坑清單（資料層 / 架構層 / 訓練層 / 推理層）
- C. 具體 GitHub Issue / Reddit / Blog 索引（20+ 條）
- D. 可量化實戰數字（LoRA rank、VRAM、throughput、image tokens）
- E. 失敗案例 / Lessons Learned（公開承認走錯、RAG 比 FT 划算）
- F. 半導體相鄰 Industrial AI 經驗輸入（PCB / MVTec / Solar / Wafer SEM）

---

## A. 跨領域公開案例盤點

### A.1 Medical VLM

**案例 A1.1 — LLaVA-Med（Microsoft, NeurIPS 2023）**
- 領域：Biomedical VQA（radiology / pathology / histology mix）
- 基座：LLaVA v1（Vicuna 7B + CLIP-ViT-L/14）
- 資料：兩階段 curriculum — (1) PMC-15M 圖文對齊 (2) 60K GPT-4 生成的 instruction-following 對話
- 訓練成本：8× A100, < 15 小時
- 效果數字：在 VQA-RAD 上 **74.2% accuracy**，在 PathVQA / SLAKE 上 fine-tune 後超過當時 supervised SOTA
- 出處：<https://arxiv.org/pdf/2306.00890>, <https://github.com/microsoft/LLaVA-Med>
- 作者：Chunyuan Li et al., Microsoft Research

**案例 A1.2 — RadVLM（Arxiv 2025-02）**
- 領域：胸部 X-ray conversational CXR
- 基座：LLaVA-OneVision-7B
- 資料：自建 1M+ image-instruction pairs（single-turn + multi-turn + grounding）
- 效果：在 grounding / conversational 雙指標上 SOTA（用 GPT-4o 打 0-10 分，中位數領先同規模模型 1-2 分）
- 出處：<https://arxiv.org/abs/2502.03333>
- 作者：Nicolas Deperrois 等，ETH Zurich / Chuv

**案例 A1.3 — Med-PaLM M（Google, 2023）**
- 領域：Generalist biomedical AI（含 radiology report generation）
- 基座：PaLM-E 84B（ViT + PaLM）
- 關鍵 finding：**LoRA fine-tune 僅用 10% 資料即回收 >90% full FT 效能** — 是「大資料不必要」最早的公開 evidence 之一
- 臨床偏好度：**40.50%** 的胸片 report 生成結果被 radiologist 偏好於人類撰寫原版
- 出處：<https://arxiv.org/pdf/2307.14334>, <https://sites.research.google/gr/med-palm/>

**案例 A1.4 — PathChat（Nature 2024）**
- 領域：Pathology（組織病理）
- 基座：UNI（自監督病理 encoder，100M 組織學影像預訓練）+ 13B LLM
- 資料：250K+ 病理 instruction pairs（自建 450K 精選後）
- 效果：多選診斷題 **87% accuracy**（有臨床 context）、**86%** 開放式問答，勝過 GPT-4V
- 同領域 benchmark：PathMMU 上 Qwen2-VL-72B-Instruct 平均 63.97%，pathology-VLM 專用模型明顯領先通用模型
- 出處：<https://pmc.ncbi.nlm.nih.gov/articles/PMC12236927/>, <https://pmc.ncbi.nlm.nih.gov/articles/PMC12276438/>

---

### A.2 Document AI（最成熟、踩坑最多）

**案例 A2.1 — Ubicloud 製造業發票 OCR（2025-11）**
這是目前最接近「中小企業實戰」的一份公開 case study，數字極完整。
- 領域：製造業 invoice / form（含手寫與印刷混雜）
- 基座：**Qwen3-VL-8B**
- 資料：**20 張人工標註 + 2,000 張合成（synthetic）表單**
- 硬體 / 時間 / 成本：**1× B200 GPU、約 1 天、~USD 100**
- 效果：
  - Overall error rate: **9.1% → 4.3%（-53%）**
  - 印刷文字錯誤率：**4.6% → 0.0%**
  - 手寫文字錯誤率：**10.5% → 5.6%**
- 關鍵做法：用 **Levenshtein edit distance 做 reinforcement fine-tune**（而非純 SFT），強化 regularization（dropout + weight decay），避免手寫筆跡有限風格 memorization
- 額外亮點：8B 模型匹敵 Qwen3-VL-235B-A22B（4.3% error）與 Gemini 2.5 Pro（4.8% error）的 error rate — **小模型 + 精準 FT 可打平 30 倍大的模型**
- 出處：<https://www.ubicloud.com/blog/end-to-end-ocr-with-vision-language-models>
- 作者：Junhao Li, Senior Software Engineer, Ubicloud

**案例 A2.2 — Hyperscience 多文檔類型 FT（2025-07）**
- 領域：invoices / government IDs / 駕照 / bills of lading / receipts / forms
- 基座：未揭露單一，但提到 Qwen / InternVL / DeepSeek 系列
- 效果：
  - Out-of-the-box vs fine-tuned：**+10% ~ +30% 單類型準確率提升**
  - 搭配 HITL（human-in-the-loop）後：**99% 最終準確率**
- 作者名言："prioritizes fine-tuning over few-shot prompting to maximize accuracy, reduce latency, lower memory consumption, and avoid storing PII in prompts"
- 出處：<https://www.hyperscience.ai/blog/out-of-the-box-to-state-of-the-art-how-vision-language-models-are-transforming-document-processing/>
- 作者：Chuyao Shen, Antonin Vidon (Senior ML Engineers)

**案例 A2.3 — TRM Labs 區塊鏈交易截圖萃取（2025-09，反例）**
- 領域：從交易所截圖萃取區塊鏈地址 / 金額
- 基座：**Gemini 2.5 Pro — 完全沒 fine-tune，純 prompt engineering**
- 資料：500+ 真實圖（多版型 / 字型 / 畫質）
- 效果階梯：
  - 傳統 OCR baseline: **~40% usable accuracy**
  - VLM + basic prompt: **80%**
  - VLM + 三輪 iterative prompt refinement: **98% accuracy, 100% structural consistency**
- Lesson：**工程師原本打算 fine-tune，發現 prompt 三輪迭代就夠了**，省下一整套訓練 infra
- 踩坑點：
  - OCR 字元錯誤致命（O vs 0、I vs 1 → 區塊鏈地址失效）
  - VLM 首輪輸出格式不一致 → 需顯式 JSON template + constraint filter
- 出處：<https://www.trmlabs.com/resources/blog/from-brittle-to-brilliant-why-we-replaced-ocr-with-vlms-for-image-extraction>
- 作者：Mohan Kumar, Rahul Raina

**案例 A2.4 — Qwen2.5-VL CORD 發票（Medium）**
- 基座：Qwen2.5-VL-7B
- 資料：CORD dataset（公開的餐廳收據 800+ 張）
- 框架：Unsloth + LoRA
- Loss 曲線：**1.72 → 0.98（3 epoch），val loss 穩在 1.05**
- LoRA 配置：r=8, alpha=16, target q_proj + v_proj
- 出處：<https://medium.com/@shrinath.suresh/finetuning-qwen-2-5-vl-7b-invoice-extraction-part-7-e8997d3f667a>
- 作者：Shrinath Suresh (2025-04)

**案例 A2.5 — Donut vs LayoutLMv3 vs Qwen2.5-VL 對比（社群共識）**
- Donut（OCR-free Transformer）：CORD 上曾超越 LayoutLM，低計算成本、少 OCR pipeline 錯誤
- LayoutLMv3：強在 word-level 精度，但要 OCR 前處理（錯誤傳遞）
- Qwen2.5-VL：DocVQA **94% @ $0.0004/page** vs Gemini 1.5 Flash **96% @ $0.0012/page**（Qwen 1/3 成本換 2% accuracy）
- 結論（從各家部落格推論）：**< 5K 樣本用 Qwen2.5-VL LoRA；> 50K 樣本用 Donut full FT；非結構化混合用 Qwen FT**

**案例 A2.6 — Manchu（滿文）木刻 OCR**
- 基座：LLaMA-3.2-11B-Vision
- 資料：21,245 木刻字 + 6,721 手寫字 + 合成資料增強
- 效果：字符準確率 **98.24%**、詞準確率 **93.84%**（合成 benchmark 上 98.3% word-level）
- 出處：<https://arxiv.org/html/2507.06761v1>

---

### A.3 Industrial / Manufacturing VQA（半導體最近鄰）

**案例 A3.1 — AnomalyGPT（AAAI 2024）**
- 領域：MVTec-AD / VisA 工業異常檢測（有文字對話介面）
- 基座：ImageBind + Vicuna（LVLM）
- 做法：模擬異常 + 文字描述生成 + 圖像 decoder + prompt learner
- 效果：**1-shot MVTec-AD 準確率 86.1%**，免除人工 threshold
- 功能：multi-turn 對話、few-shot in-context、直接定位缺陷座標
- 出處：<https://dl.acm.org/doi/10.1609/aaai.v38i3.27963>, <https://github.com/M-3LAB/awesome-industrial-anomaly-detection>

**案例 A3.2 — NV-DINOv2 for PCB defect（NVIDIA 2024）**
- 領域：PCB defect classification
- 做法：拿 1M 未標 PCB / 工業影像做自監督 domain adaptation，再用 600 張訓練 + 400 張測試下游 FT
- 效果：**通用 DINOv2 93.84% → NV-DINOv2 98.51%（+4.67 pp）**
- 啟發半導體：這是最接近半導體的 two-stage（domain pretrain → task FT）量化 evidence
- 出處：<https://developer.nvidia.com/blog/optimizing-semiconductor-defect-classification-with-generative-ai-and-vision-foundation-models/>

**案例 A3.3 — DeepPCB CLIP FT（Central South University, 2025）**
- 領域：PCB defect detection few-shot
- 做法：CLIP 雙約束對齊（contrastive + triplet），用 structure-and-physics-prior 生成 synthetic anomaly
- Key message：**在少樣本下優於通用 CLIP**
- 出處：<https://pmc.ncbi.nlm.nih.gov/articles/PMC12653441/>

**案例 A3.4 — Solar panel defect（PV cell）**
- 傳統 CNN/YOLO 為主，VLM 應用仍在實驗階段
- 代表數字：
  - Binary 缺陷分類：**96.17%**
  - 多分類：**92.13%**
  - Mask R-CNN 變體：**98.7% precision, 0.913 recall**
  - YOLOv11：mAP@0.5 **85%**
- 出處：<https://www.nature.com/articles/s41598-024-66234-3>, <https://pmc.ncbi.nlm.nih.gov/articles/PMC12470506/>
- 啟發半導體：VLM 還沒在太陽能全面打贏 CNN，說明「VLM 不是萬靈丹」

**案例 A3.5 — Wafer SEM defect classification（最直接同領域）**
- ViT + DinoV2 transfer learning：**< 15 張/類即 >90% 準確率**（長尾分類情境）
- PEFT ViT 進一步改善，DDPM 生成合成 SEM 圖增補資料
- 關鍵：業界實務上 foundation model + PEFT + 合成資料的 **三件套已是新常態**
- 出處：<https://arxiv.org/abs/2506.03345>, <https://arxiv.org/html/2407.10348v1>

**案例 A3.6 — Agriculture plant disease FT**
- CLIP FT + Qwen-VL 生成 prompt text → classifier weights
- benchmark：AgroBench（203 種作物、682 種病害）、AgMMU、PlantVillage
- 出處：<https://www.mdpi.com/1424-8220/24/18/6109>, <https://arxiv.org/pdf/2507.20519>

---

### A.4 E-commerce / Retail

**案例 A4.1 — Amazon SageMaker + Bedrock 時尚商品描述生成**
- 流程：VLM FT 提取 product attribute → Bedrock LLM 生成描述
- 場景：時尚品類描述自動化
- 啟示：Amazon 官方在 retail 側推的 pattern 仍是「**VLM FT 做 perception → LLM prompt 做 generation**」分工
- 出處：<https://aws.amazon.com/blogs/machine-learning/generating-fashion-product-descriptions-by-fine-tuning-a-vision-language-model-with-sagemaker-and-amazon-bedrock/>

**案例 A4.2 — 貨架 shelf monitoring**
- 產業玩家：Walgreens、Trax Retail、ShelfWise
- 主流仍是 YOLOv5/v7 + EfficientDet，VLM 用於「異常解釋」second-stage
- 手動巡店成本降 **60%+**
- 出處：<https://labelbox.com/guides/how-to-boost-retail-profitability-with-ai-powered-shelf-object-detection/>

---

### A.5 Autonomous / Robotics VLA

**案例 A5.1 — π0 (Physical Intelligence, 2024-12)**
- 基座：PaliGemma（VLM）+ flow matching action head
- 核心洞察：**VLM 原生的 discrete token 輸出頻率不夠做 50Hz 控制** → 必須加 flow matching / diffusion head
- 資料需求：最簡單任務 **5 小時 demo**；最複雜任務 **100+ 小時**
- 已報問題：collision avoidance 弱、fine-grained manipulation 失敗率高、diffusion 推理慢於實時
- 出處：<https://www.pi.website/blog/pi0>, <https://arxiv.org/html/2410.24164v1>

**案例 A5.2 — VLM2VLA（避免災難性遺忘，2025-09）**
- 核心承諾：**在 VQA benchmark 上保留 base model **85%+** 效能**，同時學會 action
- 驗證：800+ 真實機器人實驗、新物件新指令 generalization
- 方法：actions as language（而非獨立 head）
- 出處：<https://vlm2vla.github.io/>, <https://arxiv.org/html/2509.22195v1>
- 啟發半導體：**catastrophic forgetting 是 domain adaptation 核心風險**，VLM2VLA 做法（action as language）可借鑑到 defect-as-language

**案例 A5.3 — InstructVLA**
- 與 SpatialVLA 比較：in-domain SimplerEnv 任務 **+33.3%**
- 關鍵：MoE adaptation 抑制 forgetting
- 出處：<https://openreview.net/forum?id=tsxwloasw5>

---

### A.6 Chart / Table / OCR

**案例 A6.1 — Predibase Llama-3.2-11B-Vision ChartQA（2024-12 Wrapped）**
- 資料量：**僅 300 rows** ChartQA
- 效果：**accuracy 2x lift**
- 基礎設施：LoRA Exchange（LoRAX）動態載入，>100x 部署成本下降
- 出處：<https://predibase.com/blog/predibase-wrapped-our-greatest-hits-of-2024>, <https://x.com/predibase/status/1877782900176986447>

**案例 A6.2 — InternVL 系列 ChartQA 演進**
- InternVL-Chat-V1-5: 83.8（avg, human 73.6 + augmented 94.08）
- InternVL2-Llama3-76B: 88.4（human 81.6 + augmented 95.2）
- InternVL3.5-4B: 86.0（小模型靠新 recipe 超越大模型）
- 出處：<https://internvl.readthedocs.io/en/latest/internvl1.5/evaluation.html>

**案例 A6.3 — ChartQA-X**
- InternVL-2.5 FT 後 overall acc **79.78%**
- 出處：<https://arxiv.org/html/2504.13275v1>

**案例 A6.4 — Chart Robustness 反思**
- 論文 "Do VLMs really Understand Charts?" 顯示：同資料不同視覺呈現會讓 VLM 表現崩盤
- 啟發：**benchmark 刷分 ≠ 真懂圖表**，工程師要額外設計 robustness eval
- 出處：<https://aclanthology.org/2024.findings-emnlp.973/>

---

### A.7 Legal / Finance

**案例 A7.1 — ContractEval benchmark（2025-08）**
- 基座：GPT-4.1 / GPT-4.1 mini（未 FT，僅 prompt）
- 效果：Governing Law / Parties 條款 F1 ≈ 0.9；複雜條款 F1 ~ 0.641
- 啟發：**簡單條款 prompt 就夠，複雜條款才需要 FT**
- 出處：<https://arxiv.org/html/2508.03080v1>

**案例 A7.2 — Legal-BERT + GPT-4o 合約風險 chatbot**
- 兩階段：Legal-BERT 做 clause classification（快速）→ GPT-4o 做風險解釋（深）
- 啟示：**專用小模型 + 通用大模型 orchestration 比單一 VLM FT 更經濟**
- 出處：<https://medium.com/@prakarsha/automated-contract-clause-understanding-and-risk-assessment-with-fine-tuned-legal-bert-and-gpt-4o-3a6f0423ace3>

---

## B. 典型踩坑清單（工單式）

### B.1 資料層

**B1.1 — Chat template 用錯，模型學會講「用戶說話風格」**
- 症狀：fine-tune 完模型會自己生出 `<|im_start|>user` 之類標籤，或模仿 user query 語氣
- Root cause：labels 沒正確 mask system/user/image tokens，loss 全序列計算
- 正解：TRL 0.18+ 提供 `assistant_only_loss=True`（需要 chat template 支援 `{% generation %}` keyword，如 SmolLM3）；否則手動在 collator 裡把 system + user + image token 位置的 label 設 `-100`
- Philipp Schmid 的 phil-schmid.de tutorial 與 HF cookbook 都強調這點：「the model should learn to generate responses given instructions, NOT predict the next token in the instruction」
- 出處：<https://github.com/huggingface/trl/issues/3751>, <https://www.philschmid.de/fine-tune-multimodal-llms-with-trl>

**B1.2 — Image-text alignment 不匹配，模型 "trains fine but learns nothing"**
- 症狀：loss 下降正常、eval 完全沒提升
- Root cause：Qwen2.5-VL 對檔名 / annotation / image 路徑對齊極嚴，小差異就矽默失敗
- 正解：嚴格驗證 data pipeline，每個 step 打印 5 筆樣本 sanity check
- 社群警語（多篇 blog 一致）："Qwen2.5 VL expects image-text alignment to be exact"

**B1.3 — Multi-image 輸入 attention mask 亂掉**
- 症狀：single image OK，multi image 訓練 loss 無法收斂或 NaN
- 社群回報：LLaMA-Factory issue #5648「Full Fine-Tuning of Qwen2-VL with Mixed Image and Text-Only Datasets Fails to Proceed」—前向在 VisionSdpaAttention 某幾層後 hang 住、不報錯
- 目前解法：只混單一模態、或用最新 lazy loading（LlamaFactory 已 deprecate `visual_inputs` 參數）
- 出處：<https://github.com/hiyouga/LlamaFactory/issues/5648>

**B1.4 — Dynamic resolution 爆 image token → OOM**
- 症狀：單張大圖訓練即 OOM，降 batch size 也救不回
- Root cause：Qwen2-VL/2.5-VL/3-VL native dynamic resolution → 一張 3000×4000 圖可能展成 16K+ image tokens
- 正解（來自官方 + 2U1 Qwen-VL-Finetune repo）：
  ```
  --image_min_pixels $((256 * 28 * 28))   # 下限
  --image_max_pixels $((1280 * 28 * 28))  # 上限
  # 或直接固定
  --image_resized_width 448 --image_resized_height 448
  ```
- 社群 rule of thumb：**< 18GB VRAM 幾乎一定 OOM**（開 LoRA + 動態解析度時）
- 出處：<https://github.com/2U1/Qwen2-VL-Finetune>, <https://www.restack.io/p/vision-fine-tuning-answer-qwen2-vl-finetuning-cat-ai>

**B1.5 — 訓練 / 推理 preprocessing 不一致**
- 症狀：模型在自家 eval 上好，換 vLLM / SGLang 部署就降級
- Root cause：
  - HF AutoProcessor 的 resize / normalize 參數與 vLLM 內建 processor 不完全一致
  - tokenizer_config.json 被改動過（例如 custom chat template）
- 正解：deploy 時用 `--tokenizer-revision <commit-hash>` 鎖版本；比對 train/infer end-to-end tokenized output
- 出處：<https://huggingface.co/Qwen/Qwen2.5-VL-32B-Instruct-AWQ/discussions/10>

---

### B.2 架構層

**B2.1 — Vision encoder 要不要解凍？**
- LLaVA 系列官方立場：**凍結 CLIP vision tower** 保住 generalization、省參數
- LLaVA-NeXT ablation 結論：**LLM size scaling 比 vision encoder size scaling 更有效**；vision 側的提升多來自輸入配置（解析度、token 數）而非模型大小
- 實務社群：
  - **通用任務 FT → 凍結 vision encoder**
  - **Domain gap 極大（SEM / radiology / pathology）→ 需解凍 vision，或先做 domain pretrain（如 UNI、NV-DINOv2）**
- 出處：<https://github.com/haotian-liu/LLaVA/issues/1398>, <https://llava-vl.github.io/blog/2024-05-25-llava-next-ablations/>

**B2.2 — LoRA target_modules 選錯 → 沒效果**
- 最小可用：`["q_proj", "v_proj"]`（attention 的 Q / V）
- 中檔：`["q_proj", "k_proj", "v_proj", "o_proj"]`
- 重度 domain gap：加 `["gate_proj", "up_proj", "down_proj"]`（MLP），甚至 `embed_tokens`（但必須同時 tune `lm_head`，否則輸出端不對齊，這是 Qwen 系列的官方警告）
- 常見配置：r=8, alpha=16（LoRA 輕量）；r=128, alpha=256（深度 domain shift）
- 出處：<https://gautam75.medium.com/fine-tuning-vision-language-models-using-lora-b640c9af8b3c>, <https://github.com/QwenLM/Qwen-VL/issues/517>

**B2.3 — Projector 單訓 vs 全訓**
- LLaVA 兩階段訓練：Stage 1 只訓 projector（feature alignment），Stage 2 才開 LLM + projector
- 社群教訓：**跳過 Stage 1 直接 joint FT 會讓 projector 學不好**，domain gap 大時尤甚
- 出處：<https://arxiv.org/pdf/2304.08485>

**B2.4 — Gradient checkpointing + Flash Attention 衝突**
- 症狀：LLaMA-Factory issue #7708「Unable to use flash-attention2 for qwen2-vl training」—設 `flash_attn: fa2` 卻沒加速
- 目前常見 workaround：確認 `torch>=2.1`、`flash-attn>=2.5`、關掉 `gradient_checkpointing_reentrant=True`
- 出處：<https://github.com/hiyouga/LLaMA-Factory/issues/7708>

---

### B.3 訓練層

**B3.1 — OOM 排查 SOP（社群歸納）**
1. 先看 image token 數（印一個 batch 的 `input_ids.shape`）
2. `min_pixels`/`max_pixels` 砍半
3. 降 per_device_batch_size 到 1，用 grad_accum 補
4. 開 gradient checkpointing（換 20-30% throughput）
5. 4bit QLoRA（peak mem 再降 ~4x）
6. 仍 OOM → DeepSpeed ZeRO-3 或 FSDP
- 實測 reference：Unsloth Qwen2.5-VL **4-bit 加載只要 7.11 GB**，7B 完整 LoRA 訓練全程 peak 仍 ~7.1GB
- 出處：<https://learnopencv.com/unsloth-guide-efficient-llm-fine-tuning/>, <https://github.com/huggingface/transformers/issues/33379>

**B3.2 — FSDP 配 VLM 的坑**
- FSDP auto_wrap_policy 不認 vision encoder 的子模組類型，需要手動指定
- DeepSpeed Stage 3 在 Qwen3-VL-30B-A3B 上曾報 slow training（issue #9374）
- 社群推：**VLM 訓練優先用 DeepSpeed Stage 2，Stage 3 慎用**
- 出處：<https://github.com/hiyouga/LLaMA-Factory/issues/9374>

**B3.3 — Learning rate 常見錯誤值**
- Qwen 官方 README：`5e-6`（full FT）
- LLaMA-Factory qwen2vl_lora_sft.yaml：`1e-4`（LoRA）
- 踩過的工程師：LoRA 用 `5e-6` 收斂太慢；Full FT 用 `1e-4` 直接 diverge
- 安全區間：
  - LoRA: `1e-4 ~ 2e-4`（cosine schedule + 0.1 warmup）
  - Full FT: `1e-5 ~ 5e-6`
- 出處：<https://github.com/QwenLM/Qwen2.5-VL/issues/127>

**B3.4 — Batch size / grad accum 配置**
- Gemma 3 4B VLM FT（Anshuman Mishra）：per_device=4, grad_accum=8, effective=32 @ QLoRA
- 實務社群：**effective batch 32-64 最穩**，低於 8 容易 loss 震盪

**B3.5 — Training loss 收斂但 eval 爛的案例**
- 常見原因排序：
  1. 資料 label 錯（最常見）— "the model blindly trusts labels"
  2. train / eval preprocessing 不一致（第二常見）
  3. chat template 不一致（第三常見）
  4. 過擬合少樣本（如手寫風格）
- Ubicloud 解法：用 **edit distance reward 做 RL FT** 而非純 SFT，強制模型學「相似即可」而非背答案

**B3.6 — Catastrophic forgetting 真實數字**
- VLM2VLA: 保留 **85%+** base VQA 能力
- GaB (CLOVE-function)：**38.34 AP vs real rehearsal 差 3 pp**（data-free 最好）
- InstructVLA MoE 抑制 forgetting：SimplerEnv **+33.3% vs SpatialVLA**
- 業界 rule：**全量 FT 對 base VQA 能力損失 20-40% 極常見**，不做 replay buffer 或 MoE 就是 default 壞掉
- 出處：<https://openreview.net/pdf/278c682d3fdae858e47cc6e1111e5d282dd787fa.pdf>, <https://openaccess.thecvf.com/content/WACV2025/papers/Das_One_VLM_to_Keep_it_Learning_Generation_and_Balancing_for_WACV_2025_paper.pdf>

---

### B.4 推理層

**B4.1 — vLLM 載入 LlamaFactory 匯出的 Qwen2.5-VL 報錯**
- Error: `assert hasattr(config.text_config, "num_attention_heads")` AssertionError
- Root cause：匯出的 config.json 缺 `text_config.num_attention_heads`（VLM 結構 attribute 沒寫對）
- Fix：PR #8245 已修，升到最新 LlamaFactory
- 出處：<https://github.com/hiyouga/LlamaFactory/issues/8241>

**B4.2 — vLLM LoRA adapter 推理比 merge 後差**
- 症狀：同一組權重，vLLM AsyncLLMEngine 用 adapter 動態載入的結果 << 預先 merge 後載入
- 社群暫時解法：**部署前 `peft.merge_and_unload()` 再 export**
- SGLang 目前強制 `merge=True`（2026-04 snapshot），native adapter 載入還在開發
- 出處：<https://github.com/vllm-project/vllm/issues/11255>, <https://docs.vllm.ai/en/latest/features/lora/>

**B4.3 — vLLM chat template 與訓練時不一致**
- 症狀：同 prompt，HF transformers 產 A，vLLM 產 B
- Root cause：Qwen2.5-VL default chat template 不含 tool-use；fine-tune 時如果改過 tokenizer_config.json，vLLM 可能 hang（無錯誤訊息，記憶體和功耗飆高）
- Fix：部署時顯式 `--chat-template custom_template.jinja`；並確保 trainer 與 vLLM 用同一份
- 出處：<https://github.com/QwenLM/Qwen3-VL/issues/1093>, <https://github.com/vllm-project/vllm/issues/4490>

**B4.4 — Parallel request 時掛掉**
- Ray Serve + vLLM + Qwen2-VL，`max_ongoing_requests >= 2` 就 shape mismatch
- 出處：<https://discuss.ray.io/t/shape-mismatch-error-on-ray-serve-vllm-qwen2-vl-with-chatcompletionrequest/21575>

---

## C. 具體踩坑帖 / Issue / Blog 索引（22 條）

| # | 類型 | 一句話描述 | URL |
|---|---|---|---|
| 1 | GitHub | Qwen2.5-VL LR 5e-6 vs 1e-4 矛盾 | <https://github.com/QwenLM/Qwen2.5-VL/issues/127> |
| 2 | GitHub | llava-next-110B QLoRA 8×A100 仍 OOM | <https://github.com/huggingface/transformers/issues/33379> |
| 3 | GitHub | Unsloth Qwen2.5-VL raw text+image+video collator 壞 | <https://github.com/unslothai/unsloth/issues/2026> |
| 4 | GitHub | Qwen2-VL mixed image+text dataset hang | <https://github.com/hiyouga/LlamaFactory/issues/5648> |
| 5 | GitHub | Qwen2.5-VL 匯出 vLLM 載不起來 | <https://github.com/hiyouga/LlamaFactory/issues/8241> |
| 6 | GitHub | flash-attn2 + Qwen2-VL 無加速 | <https://github.com/hiyouga/LLaMA-Factory/issues/7708> |
| 7 | GitHub | Qwen3-VL-30B-A3B DeepSpeed Stage3 訓練慢 | <https://github.com/hiyouga/LLaMA-Factory/issues/9374> |
| 8 | GitHub | vLLM Qwen2.5-VL tool call 斷掉 | <https://github.com/QwenLM/Qwen3-VL/issues/1093> |
| 9 | HF Discuss | Qwen2.5-VL-32B-AWQ tokenizer 更新後 tool call 壞 | <https://huggingface.co/Qwen/Qwen2.5-VL-32B-Instruct-AWQ/discussions/10> |
| 10 | Ray Discuss | Qwen2-VL parallel request shape mismatch | <https://discuss.ray.io/t/shape-mismatch-error-on-ray-serve-vllm-qwen2-vl-with-chatcompletionrequest/21575> |
| 11 | TRL Issue | VLM assistant-only loss feature request | <https://github.com/huggingface/trl/issues/3751> |
| 12 | GitHub | LlamaFactory Qwen2-VL video processor call bug | <https://github.com/hiyouga/LLaMA-Factory/issues/6850> |
| 13 | GitHub | vLLM Qwen2-VL LoRA feature request / degradation | <https://github.com/vllm-project/vllm/issues/11255> |
| 14 | GitHub | unsloth Qwen2.5-VL 沒看到 2x 加速 | <https://github.com/unslothai/unsloth/issues/2404> |
| 15 | Blog | Ubicloud 8B 打平 235B 完整 case study | <https://www.ubicloud.com/blog/end-to-end-ocr-with-vision-language-models> |
| 16 | Blog | TRM Labs 放棄 FT 改 prompt 拿到 98% | <https://www.trmlabs.com/resources/blog/from-brittle-to-brilliant-why-we-replaced-ocr-with-vlms-for-image-extraction> |
| 17 | Blog | Hyperscience 多文檔類型 FT 10-30% + HITL 99% | <https://www.hyperscience.ai/blog/out-of-the-box-to-state-of-the-art-how-vision-language-models-are-transforming-document-processing/> |
| 18 | Blog | Anshuman Mishra 2025 VLM FT 教學（含 pitfall 清單） | <https://heyyanshuman.com/posts/fine-tuning-vlm> |
| 19 | Blog | Predibase Llama-3.2-11B-Vision 300 rows 2x lift | <https://predibase.com/blog/predibase-wrapped-our-greatest-hits-of-2024> |
| 20 | Blog | Phil Schmid HF TRL VLM FT 權威教學 | <https://www.philschmid.de/fine-tune-multimodal-llms-with-trl> |
| 21 | Paper | VLMs 真懂圖表嗎？robustness 崩盤 | <https://aclanthology.org/2024.findings-emnlp.973/> |
| 22 | Paper | VLM2VLA 保留 85% base capability | <https://arxiv.org/html/2509.22195v1> |

---

## D. 可量化實戰數字彙編

### D.1 LoRA rank 對 accuracy 影響
- 小 rank（r=4-8）：invoice extraction loss 1.72→0.98（3 epoch），adequate for narrow task
- 中 rank（r=16-32）：推薦 chart / multi-domain
- 大 rank（r=128, alpha=256）：domain gap 大（如醫療、SEM）才值得
- **沒有公開「同任務 r=4/8/16/32/128 系統性 A/B」的 paper** — 這是一個 research gap

### D.2 Full FT vs LoRA wall-time / VRAM
| 設定 | 7B VLM peak VRAM | 相對 throughput |
|---|---|---|
| Full FT fp16 | **~140 GB** (ZeRO-3 across 4-8 GPU) | 1.0x |
| LoRA 16-bit | **~24 GB** 可 consumer GPU | 1.5-2x |
| QLoRA 4-bit | **~6.5-7 GB** (Unsloth) | 2-5x (Unsloth 聲稱) |

參考：Unsloth benchmark 7B Qwen2.5-VL LoRA，T4 GPU 2921 秒（~48.7 分）完成一個小 dataset；Lyceum 指出 H100 vs A100 有 **+67% memory bandwidth**、**+50% NVLink**，H100 實測 FT throughput 提升 40-90%。

### D.3 Batch size VRAM scaling（7B VLM，LoRA）
- bs=1, dyn-res max 1280 tokens：~18 GB
- bs=2, dyn-res max 1280 tokens：~26-28 GB
- bs=4, dyn-res max 512 tokens（固定）：~24 GB
- **rule of thumb**：image token 每翻倍 VRAM ≈ +30-40%（不成線性是 attention memory O(N²)）

### D.4 Context length × training throughput
- 1024 token attention：FA2 相對 vanilla 省 3-4x memory、整體 +20-40% 速度（7B baseline）
- 2048 tokens：gradient checkpointing 掉 20-30% throughput，但 peak activation 減半

### D.5 Dynamic resolution 對速度
- Qwen2-VL naive dynamic res：memory 尖刺可達 5-10x 平均值
- 固定 448×448：throughput 提升 2x，但小字辨識準確率會掉（社群共識，無統一數字）

---

## E. 失敗案例 / Lessons Learned（最珍貴）

**E1 — TRM Labs：fine-tune 沒做成、prompt 三輪就解決**
- 他們本來計劃 FT，但算完訓練 infra、data labeling 成本後，發現 Gemini 2.5 Pro 純 prompt iteration 就能到 98%；最終決定**不 FT，省下一整個 MLOps pipeline**
- 啟示：**< 500 樣本 + closed-source 強模型可用時，優先 prompt**
- URL：見 C.16

**E2 — Unsloth Qwen2.5-VL 用戶抱怨沒看到 2x 加速**
- issue #2404：有人測出來跟 vanilla HF 差不多
- 社群回應：**2-5x 是 QLoRA 4bit + 特定優化下才成立，16bit LoRA 通常 1.5x**
- 啟示：行銷數字要自己再 benchmark
- URL：見 C.14

**E3 — LlamaFactory Qwen2-VL mixed dataset 沉默 hang**
- issue #5648：混圖 + 純文字資料，forward pass 某幾層 SdpaAttention 後停住、不報錯、不 OOM
- 啟示：**沉默失敗比 crash 更可怕**，必須自己加 timeout + sanity check
- URL：見 C.4

**E4 — vLLM + Qwen2-VL LoRA 推理質量下降**
- 眾多工程師發現 vLLM 動態 LoRA adapter 載入後效果 << merge 後 export
- 暫時解法：部署前 merge（繞開 LoRAX 的動態切換優勢）
- 啟示：**production 先用 merge 後版本驗收，再評估 dynamic adapter 是否需要**
- URL：見 C.13

**E5 — Chart robustness 崩盤論文**
- 同資料不同視覺呈現讓 VLM 表現大跌（ACL 2024 Findings）
- 啟示：**benchmark 刷分 ≠ 真 robust**，FT 前必須設計 stress-test eval（不同解析度、重排、裁切、去色）
- URL：見 C.21

**E6 — Medical VLM 改走 RAG + KG 的證據**
- LLaVA Needs More Knowledge（2024-10，arXiv 2410.04749）：純 FT 的 LLaVA 在胸腔病理解釋上 AUC 普通，加 KG retrieval 後 **AUC +16 pp**
- 啟示：**domain 知識極深時（病理 / 法律 / 半導體 process window），FT + RAG 組合勝純 FT**

---

## F. 半導體相鄰 Industrial AI 經驗（直接可借鑑）

### F.1 two-stage 策略（最硬的 evidence）
- NV-DINOv2：1M 無標籤工業影像 SSL pretrain → 600 張 task FT → **93.84% → 98.51%**
- PathChat：100M 組織學影像 SSL → 250K instruction pairs SFT → **87% multi-choice**
- 半導體推論：**先拿廠內 SEM/OM/AOI 海量 unlabeled 圖做 SSL domain pretrain，再少樣本 FT**

### F.2 合成資料幾乎必備
- DDPM 生成 SEM 缺陷圖緩解 class imbalance（arxiv 2407.10348）
- Central South University：CLIP + structure-and-physics-prior synthetic anomaly（arXiv 2025）
- Ubicloud：20 真 + 2000 合成 → 1 天 USD 100 訓練到 4.3% error
- **合成資料比真標註便宜 1-2 個數量級**，是 domain adaptation 的 default 手段

### F.3 PEFT + ViT + 少樣本的成熟 recipe
- Wafer SEM：DinoV2 + PEFT + **每類 < 15 張** = >90%
- 半導體製程廠已可用此 recipe 快速冷啟

### F.4 VLM 不總是贏 CNN
- Solar panel defect：YOLOv11、Mask R-CNN 變體仍拿 98.7% 高精度
- PCB defect：YOLOv10 改進版拿 mAP@0.5 **85%**
- **啟示：不是所有 defect 都該用 VLM**。VLM 的價值在需要「可對話解釋 + zero/few-shot 泛化 + 多模態 OCR+ 結構化輸出」時才明顯

### F.5 VLA 給半導體的啟示（catastrophic forgetting）
- 半導體製程 VLM 通常希望保留 "generic vision + OCR" 能力（讀 lot ID、batch number）
- VLM2VLA / InstructVLA 的 MoE 或 action-as-language 做法，可直接類比到 **defect-class-as-language**：把 defect token 當新語言 token 學，避免破壞 base VLM

---

## 附錄：資料空缺與風險聲明

**公開資訊缺口（半導體 VLM domain adaptation 直接 evidence）**
1. 沒有主流半導體大廠（TSMC/Intel/Samsung）公開的 VLM FT benchmark 報告（NDA 常態）
2. 沒有「同任務 LoRA rank 系統 sweep」公開資料（r=4/8/16/32/64/128）
3. 沒有 Qwen3-VL / InternVL3 在 MVTec / VisA 上對比 AnomalyGPT 的 head-to-head
4. 沒有「半導體 SEM Qwen2.5-VL FT 前後 defect classification F1」公開

**此素材的 reliability 分級**
- S 級（官方數字、paper、company blog）：A1-A7 所有數字、E 段全部案例
- A 級（社群普遍共識 + 多源交叉確認）：B1-B4 多數踩坑
- B 級（單一 issue / 單一部落格）：C 表中 issue、部分 D 段估計數字

**給下游撰寫者的建議**
- 優先引用 S 級（Ubicloud、Predibase、TRM Labs、PathChat、Med-PaLM、NVIDIA NV-DINOv2）
- B / C 級當「趨勢參考」，不作 "definitive benchmark"
- 缺口清單可以當成報告的「半導體落地機會」章節 — 公開資料還沒覆蓋的地方正是未來工作空間
