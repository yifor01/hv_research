# Qwen3 / Qwen3-VL 與半導體製程 VLM/LLM 應用全景調研

**調研日期**：2026-04-23
**目標讀者**：半導體業技術負責人 + VLM/LLM 訓練工程師
**用途**：為「把 Qwen3-VL 改造成半導體製程 domain model」提供基底模型 + 目標領域的現況盤點

---

## Part 1 — Qwen3 / Qwen3-VL 家族全景

### 1.1 Qwen3 LLM 系列（純文本基座）

Qwen3 是阿里巴巴（Alibaba Cloud）通義千問團隊於 **2025 年 4–5 月** 正式釋出的第三代大模型系列，技術報告 arxiv 2505.09388（2025 年 5 月 14 日公開，v1）。整個家族以 **Apache 2.0** 開源，涵蓋從邊緣到旗艦的完整尺寸矩陣。來源：<https://arxiv.org/abs/2505.09388>、<https://qwenlm.github.io/blog/qwen3/>。

#### 版本清單（Dense + MoE）

| 變體 | 型號 | 架構 | 備註 |
|------|------|------|------|
| Dense | Qwen3-0.6B / 1.7B / 4B / 8B / 14B / 32B | 標準 Transformer | 邊緣 → 單卡 → 多卡 |
| MoE | Qwen3-30B-A3B | 30B 總參 / 3B 活化 | 消費級 GPU 可跑 |
| MoE | Qwen3-235B-A22B | 235B 總參 / 22B 活化；94 層；128 experts（top-k=8）；Q heads=64, KV heads=4（GQA） | 旗艦 |

MoE 結構重點：**Qwen3-MoE 移除了 shared expert**（Qwen2.5-MoE 仍保留），改用 global-batch load balancing，刻意鼓勵 experts 之間的專業化分工。來源：<https://www.emergentmind.com/topics/qwen3-235b-a22b>、<https://huggingface.co/Qwen/Qwen3-235B-A22B>。

#### 技術特色（Qwen3 最關鍵的三項創新）

1. **Thinking / Non-thinking 模式統一** — 同一個模型可在「快速對話」與「長鏈思考」之間切換，使用者可透過 `enable_thinking` 參數控制。
2. **Thinking Budget 機制** — 允許使用者分配最多可花多少 thinking tokens，平衡延遲與品質；benchmark 顯示增加 budget 幾乎單調提升各項表現。
3. **119 種語言** — 從 Qwen2.5 的 29 種大幅擴展到 119 種（含方言）。

#### 訓練資料量

- **預訓練**：~36 T tokens（Qwen3-235B-A22B 採三階段預訓練，General → Reasoning → Long-context），涵蓋 web、STEM、books、code、PDF 萃取；相較 Qwen2.5 的 18 T tokens 幾乎翻倍。來源：<https://huggingface.co/Qwen/Qwen3-235B-A22B>。
- **後訓練**：Qwen2.5 公開數字為 SFT + DPO 共 1 M examples；Qwen3 技術報告提到 RL 階段採 **GRPO**（Group Relative Policy Optimization）作為主力演算法，並在 long-form reasoning 數據上做多階段強化。來源：Qwen3 Technical Report <https://arxiv.org/abs/2505.09388>。
- ms-swift 已對 Qwen3 / Qwen3-MoE 支援 CPT / SFT / DPO / GRPO 的完整 pipeline。來源：<https://swift.readthedocs.io/en/latest/BestPractices/Qwen3-Best-Practice.html>。

#### 上下文窗口

- 原生 32,768 tokens
- 透過 YaRN 外推 → 131,072 tokens（128K）

---

### 1.2 Qwen3-VL — 2026-04-23 發布狀態盤點（最關鍵資訊）

**結論：Qwen3-VL 已完整釋出，且是目前半導體 domain adaptation 最值得下手的基底。**

#### 精確發布時間軸

| 日期 | 釋出內容 |
|------|---------|
| 2025-09-23 | **Qwen3-VL-235B-A22B**（旗艦 MoE，Instruct + Thinking 雙版本） |
| 2025-10-04 | **Qwen3-VL-30B-A3B**（Instruct + Thinking + FP8） |
| 2025-10-15 | **Qwen3-VL-4B / 8B**（Instruct + Thinking） |
| 2025-10-21 | **Qwen3-VL-2B**（Instruct + Thinking） |
| 2025-11-26 | Qwen3-VL-32B 與 235B 系列更新（含 FP8 / GGUF 全量化） |
| 2025-11-27 | **Qwen3-VL 技術報告發布**（arxiv 2511.21631） |

來源：GitHub README <https://github.com/QwenLM/Qwen3-VL>、HuggingFace Collection <https://huggingface.co/collections/Qwen/qwen3-vl>、Technical Report <https://arxiv.org/abs/2511.21631>。

#### 完整模型矩陣（截至 2026-04-23 可下載）

| 尺寸 | Instruct | Thinking | FP8 | GGUF | 累積下載 |
|------|----------|----------|-----|------|---------|
| 2B | ✅ | ✅ | ✅ | ✅ | 2B-Instruct 86.3 M（最熱門） |
| 4B | ✅ | ✅ | ✅ | ✅ | 2.13 M |
| 8B | ✅ | ✅ | ✅ | ✅ | 3.86 M |
| 30B-A3B | ✅ | ✅ | ✅ | ✅ | 1.47 M |
| 32B | ✅ | ✅ | ✅ | ✅ | 1.56 M |
| 235B-A22B | ✅ | ✅ | ✅ | ✅ | 1.04 M |

**Instruct vs Thinking 分工**：Instruct 版本負責直接指令回應、生產部署（下載量通常高一個量級）；Thinking 版本內嵌長鏈推理、適合 visual reasoning / 數理 / complex grounding。下載比例約 10:1，暗示 production 端偏好 Instruct。

#### 三項架構升級（Qwen3-VL vs Qwen2.5-VL）

1. **Interleaved-MRoPE** — 進一步演化的多模旋轉位置編碼。從 Qwen2-VL 的 M-RoPE（把 rotary 分解為 temporal / height / width 三軸）升級到 interleaved 版本，對 time / width / height 做 full-frequency allocation；目的是強化 long-horizon video reasoning。
2. **DeepStack 整合** — 融合 ViT 多層特徵（而非只用最後一層），改善 vision-language alignment 與細節捕捉。對 fine-grained 辨識（例如電路裡的 μm 級缺陷）特別重要。
3. **Text-Timestamp Alignment** — 影片時序從 T-RoPE 改為顯式「文字時間戳」對齊，提供精確的事件定位。對 fab 流程影片 / SEM 動態影像特別有用。

來源：<https://arxiv.org/abs/2511.21631>、<https://thesalt.substack.com/p/qwen3-vl-deepstack-fusion-interleaved>、<https://deepwiki.com/QwenLM/Qwen3-VL/4.2-model-architecture>。

#### Vision Encoder 與動態解析度

- Vision encoder 採 **native dynamic resolution ViT**（由 Qwen2-VL 延續下來的設計），移除 absolute position embedding、改用 2D-RoPE，並引入 Window Attention 降低計算成本。任意解析度影像皆被動態切成可變 token 數。
- 原生 **256 K interleaved context**（文字 + 多張圖 + 影片片段混排），可外推到 1 M tokens。
- OCR 支援語言從 10 種擴到 32 種。

來源：<https://huggingface.co/docs/transformers/en/model_doc/qwen3_vl>、<https://arxiv.org/html/2409.12191v1>（Qwen2-VL 原始 M-RoPE 論文）。

#### 性能定位（vs GPT-4o / Gemini / Claude）

根據官方 paper 與第三方 benchmark：

- **Qwen3-VL-235B-A22B-Thinking** 在 **MMMU** 上 ~74.8（GPT-5 Vision ~72.1），**MathVista mini / MATH-Vision** 優於 GPT-4o 與 Gemini-2.0-Flash。
- **Qwen3-VL-235B-A22B-Instruct** 在純感知（perception）任務上與 **Gemini 2.5 Pro** 相當。
- 文件理解（DocVQA、InfographicVQA）、OCR、grounding、GUI agent 操作都達到 SOTA。

來源：<https://www.ywian.com/blog/qwen3-vl-vs-gemini-2-5-pro-multimodal-benchmark>、<https://crazyrouter.com/en/blog/qwen3-vl-235b-vs-gpt-5-vision-multimodal-comparison-2026>。

#### Qwen3-VL 在半導體情境下的能力映射

- **文件理解** → SPEC、SOP、workcard、FAR（Failure Analysis Report）、SEMI standards 的 RAG
- **OCR（32 語言）** → wafer map 標註、tool GUI 截圖的文字萃取
- **Grounding** → SEM 影像指向性缺陷定位（給出 bbox）
- **Video / Temporal** → etch endpoint 等工藝影像時序
- **GUI agent** → 自動操作 SEM review 軟體（KLA 29xx / Applied Materials SEMVision）
- **Visual coding** → 從工藝流程圖產 Draw.io / 從量測圖表產 Python 分析腳本

---

### 1.3 Qwen2.5-VL 的現狀（備胎 / 穩定選擇）

若團隊希望等 Qwen3-VL 社群工具鏈更成熟，Qwen2.5-VL 仍是很實用的備胎：

- 尺寸：3B / 7B / 32B / 72B，釋出於 2025 年 1–3 月
- 旗艦 72B 在 document + diagram 上與 GPT-4o / Claude 3.5 Sonnet 同水平
- 後訓練：SFT + DPO 共 1 M examples
- Native dynamic-resolution ViT + 動態 FPS 影片取樣 + 絕對時間對齊的 mRoPE
- 技術報告：arxiv 2502.13923 <https://arxiv.org/abs/2502.13923>

社群已有大量 fine-tune 案例：
- **Document AI**：ubiai 的發票 / 表單資訊萃取教學 <https://ubiai.tools/fine-tuning-qwen-for-reliable-information-extraction-from-documents/>
- **Medical**：眼科雙語 VQA benchmark 顯示 closed-ended 表現強、open-ended 臨床推理仍輸 Gemini 2.0
- **7B 微調 CFD**：僅 7B 微調後在 CFD 自動化任務達 88.7% 準確率，勝過 72B 的 31.4% —— 這個對比對半導體團隊非常有啟發，**small + domain FT ≫ large + zero-shot**

來源：<https://www.emergentmind.com/topics/qwen2-5-72b-instruct>、<https://www.f22labs.com/blogs/complete-guide-to-fine-tuning-qwen2-5-vl-model/>。

---

### 1.4 官方推薦微調生態

#### 官方偏好度

- **MS-SWIFT**（ModelScope Swift）— 阿里自家，對 Qwen3 / Qwen3-VL 的 CPT / SFT / DPO / GRPO 支援最即時；官方文件首推。<https://swift.readthedocs.io/en/latest/BestPractices/Qwen3-VL-Best-Practice.html>
- **LLaMA-Factory** — 社群主流，Qwen 官方也在 readthedocs 提供整合指南。支援 full-parameter / LoRA / QLoRA / DoRA。<https://qwen.readthedocs.io/en/latest/training/llama_factory.html>
- **qwen-vl-finetune**（官方 repo 內建）— 針對 Qwen2-VL / Qwen2.5-VL 的參考實作，Qwen3-VL 專屬 recipe 尚待補齊
- **Unsloth** — 快速 LoRA/QLoRA，記憶體最省；已有 Qwen3-VL 專屬教學 <https://docs.unsloth.ai/models/qwen3-vl-how-to-run-and-fine-tune>
- **2U1/Qwen-VL-Series-Finetune** — 社群熱門第三方實作 <https://github.com/2U1/Qwen-VL-Series-Finetune>

#### LoRA / Full FT 成本參考（實測數字）

| 模型 | LoRA VRAM | Full FT VRAM | 備註 |
|------|-----------|--------------|------|
| Qwen3-VL-2B | ~12 GiB | ~40 GiB | 單張 3090 / 4090 可跑 LoRA |
| Qwen3-VL-4B | ~16 GiB | 2×21 GiB（SWIFT 實測）| A10/L4 夠 |
| Qwen3-VL-8B | ~24 GiB | ~80 GiB | 單張 A100 40G 邊緣 |
| Qwen3-VL-30B-A3B | QLoRA ~48 GiB | 8×80 GiB（SWIFT 實測） | DGX Spark 可 QLoRA |
| Qwen3-VL-32B | LoRA ~80 GiB | 多機 | H100 起跳 |
| Qwen3-VL-235B-A22B | 多機 QLoRA | 不現實 | 推薦直接用 API |

來源：Kaitchup Substack <https://kaitchup.substack.com/p/qwen3-vl-fine-tuning-on-your-computer>、NVIDIA 開發者論壇 DGX Spark QLoRA 帖 <https://forums.developer.nvidia.com/t/fine-tuning-qwen-qwen3-vl-30b-a3b-instruct-fp8-with-qlora-on-dgx-spark/351329>、Medium 30B-A3B MoE LoRA 教學 <https://medium.com/@ishaafsalman/fine-tuning-qwen-qwen3-vl-30b-a3b-moe-architecture-with-lora-2365359e870f>。

**實務建議**：半導體團隊若要做缺陷辨識 + 文件理解，建議從 **Qwen3-VL-8B 或 32B Instruct** 起步，先用 LoRA 在專屬資料集（SEM + SOP 混編）做 SFT，再視需求加一輪 DPO 或 GRPO 做人類偏好對齊。成本落在單機 A100/H100 可負擔的範圍。

---

## Part 2 — 半導體製程領域的 VLM / LLM 應用現況

### 2.1 各製程模組縮寫與 AI 可介入點

半導體前段（FEOL）與後段（BEOL）製程由多個模組串接，各 fab 的縮寫略有差異（台積電內部慣用的 YED / TF / MET 在 Samsung / Intel 會叫 YE / FILM / METRO），但功能對應相同。

| 縮寫 | 全名 | 主要產出資料 | VLM/LLM 典型介入場景 |
|------|------|-------------|---------------------|
| **LITHO** | Lithography（微影） | 光罩 layout、曝光後 SEM（ADI）、疊對（overlay）量測 | OPC 模型修正、mask defect classification、ADI vs AEI 比對 |
| **ETC** | Etch（蝕刻） | 蝕刻後 SEM（AEI）、sidewall profile、endpoint 時序 | Sidewall defect 分類、endpoint 偵測、profile segmentation |
| **DIF** | Diffusion（擴散 / 氧化 / 退火） | 爐管溫度曲線、particle map | 爐管均勻性異常、粒子 pattern 分析 |
| **CMP** | Chemical Mechanical Planarization | AFM / optical topography、scratch 影像 | Scratch / dishing / erosion 分類 |
| **IMP** | Implant（離子植入） | Dose uniformity map、SIMS profile | 劑量均勻性異常、profile 回歸 |
| **PVD / CVD** | Physical / Chemical Vapor Deposition | Thickness map、pinhole 影像、GIXRD | Thickness 回歸、pinhole 偵測、deposition recipe 優化 |
| **TF** | Thin Film（薄膜）— 涵蓋 PVD+CVD+ALD | 同上 | 同上 |
| **MET** | Metrology（量測） | CD-SEM、OCD、ellipsometry、overlay | CD-SEM 分割、contour 萃取、denoising |
| **YED / YE** | Yield Enhancement | 跨模組資料整合、commonality chart、bin map | 跨製程 root-cause analysis |
| **FA** | Failure Analysis | SEM / TEM / FIB 影像、EDX spectrum | 失效影像判讀、FAR 報告自動生成 |

**讀者提醒**：台積電系統內「YED」專指 Yield Enhancement Department，與製程模組並列但實為跨模組；Samsung/Intel 對應單位名稱不同。跨 fab 溝通時務必先對齊術語。

---

### 2.2 SEM Defect Classification — 學術 + 產業現況

這是目前公開論文最多、也是 VLM 最成熟的半導體應用場景。

#### 關鍵論文

- **Deep Learning based Defect Classification and Detection in SEM Images** (arxiv 2206.13505) — 早期基線 <https://arxiv.org/pdf/2206.13505>
- **SEM-CLIP: Precise Few-Shot Learning for Nanoscale Defect Detection** (arxiv 2502.14884, ICCAD 2024) — 把 CLIP 客製化，用 domain-prompt（"linear scratch" / "blurry photo of the..."）導引注意力到 defect 區域。這是目前最接近「VLM 直接應用於 SEM」的代表作。<https://arxiv.org/abs/2502.14884>
- **Semiconductor SEM Image Defect Classification Using Supervised and Semi-Supervised Learning with Vision Transformers** (arxiv 2506.03345, ASMC 2025，IBM Research) — 11 種缺陷、>7,400 張、DINOv2 transfer learning，< 15 張/類別也能達 90%+ 準確率 <https://arxiv.org/abs/2506.03345>
- **Foundation deep learning model for accurate SEM image segmentation for CD-SEM measurements** (SPIE 2025) — CD-SEM 量測專用的 foundation model <https://www.spiedigitallibrary.org/conference-proceedings-of-spie/13426/134260M/>
- **Progressive Alignment with VLM-LLM Feature to Augment Defect Classification (ASE Dataset)** (arxiv 2404.05183) — 後段封裝 ASE defect 分類，用 VLM-LLM 特徵對齊 <https://arxiv.org/html/2404.05183v1>

#### 產業/商用

- **NVIDIA Cosmos Reason VLM** — fine-tune 後在 wafer map 缺陷分類達 96%+，可做 interactive Q&A、few-shot、自動標註。NV-DINOv2 在 die-level 達 98.51%。Cookbook 公開完整 post-training recipe：<https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/post_training/reason1/wafermap_classification/post_training.html>。對半導體團隊而言，Cosmos Reason 可以做為 Qwen3-VL 的主要對比基準。NVIDIA Blog：<https://developer.nvidia.com/blog/optimizing-semiconductor-defect-classification-with-generative-ai-and-vision-foundation-models/>
- **KLA** — 281x 系列（bright-field / dark-field optical）、eSL10（e-beam），已內建 AI-driven classification 與 design-aware review
- **Applied Materials SEMVision H20**（2025 年 2 月發表）— e-beam + AI image recognition，專攻 advanced-node buried defect
- **ASML HMI multi-beam e-beam** — 與 lithography / computational control 深度整合，做 inline monitoring
- **Lasertec** — EUV mask inspection 市場霸主，用 AI 處理 actinic pattern inspection

來源：<https://averroes.ai/blog/kla-defect-inspection>、<https://www.kla.com/advance/innovation/klas-process-control-solutions-are-shaping-the-future-of-ai>。

---

### 2.3 Wafer Map Pattern Classification — 資料集 + 模型

這是**公開資料最豐富**的半導體 AI 任務。

#### WM-811K（旗艦資料集）

- **釋出方**：台積電前研發、台大 MIR Lab（Ming-Ju Wu et al.），由 Samsung 實務數據來源；也可從 Kaggle 取得 <https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map>
- **規模**：811,457 張 wafer map，來自 46,293 個批次
- **標註**：僅 ~20%（172,950）有人工標註，分為 9 類（Center / Donut / Edge-Loc / Edge-Ring / Loc / Near-full / Random / Scratch / None）
- **挑戰**：嚴重類別不平衡（None 占 78.7%，defective 僅 3.1%）

#### 最新 benchmark

| 方法 | 準確率 |
|------|--------|
| CBAM 注意力輕量 CNN | 99.88%（balanced 子集）|
| Autoencoder 資料擴增 + CNN | 98.56% |
| Tiny Vision Transformer | > 95% <https://arxiv.org/pdf/2504.02494> |
| NVIDIA Cosmos Reason（VLM）| 96%+ with few-shot fine-tune |
| 加權軟投票 ensemble | 95.09% / F1=0.95 |

來源：<https://arxiv.org/html/2411.11029v1>、<https://jivp-eurasipjournals.springeropen.com/counter/pdf/10.1186/s13640-025-00666-3.pdf>、<https://www.frontiersin.org/journals/electronics/articles/10.3389/felec.2026.1750707/abstract>。

---

### 2.4 OPC / Litho Simulation AI — 最成熟的商用案例

- **Synopsys × NVIDIA cuLitho** — 跑 OPC 從 weeks → days，40× 加速；500 張 DGX H100 = 40,000 CPU 系統的工作量。<https://www.synopsys.com/blogs/chip-design/computational-lithography-chip-design-with-nvidia.html>、<https://developer.nvidia.com/culitho>
- **ASML Deep Learning OPC Agent** — 2017 年起 DCNN 協助 SRAF placement；2020 年 Synopsys Liu 用 TensorFlow + RL + GPU 做 3D mask synthesis。近年轉為「data-driven agent + physical model」的 hybrid 路線，避免黑盒。
- **NVIDIA + ASML + TSMC + Synopsys 聯盟**（2023 年開始）— GPU 加速 computational lithography 的產業級合作。
- **Inverse Lithography Technology (ILT)** — Nature Light: Science & Applications 2025 回顧「AI-based ILT」進展 <https://www.nature.com/articles/s41377-025-01923-w>

這塊高度 proprietary，VLM 少見，多為 CNN / diffusion / RL 為主。

---

### 2.5 Yield Root Cause Analysis

- **Intel 公開案例**：AI 自動偵測 EOL wafer 的 GFA（Gross Failure Area），新 pattern 加進全 fab 知識庫。<https://www.intel.com/content/dam/www/central-libraries/us/en/documents/intel-it-manufacturing-yield-analysis-with-ai-paper.pdf>
- **PDF Solutions** — 早期 discovery + root cause + 預測性品控，compound semi 端到端 yield management。<https://www.pdf.com/>
- **Optimal+ / NI**（2020 已併購）、**yieldWerx**、**Camtek** — 商用 yield management 系統，大量導入 ML
- **Samsung LLMOps（ZenML case study）** — 多模 LLM + RL 做自動化 fab，engineering assistant 能回答「我遇到 error ABC 怎辦」並給歷史案例：<https://www.zenml.io/llmops-database/autonomous-semiconductor-manufacturing-with-multi-modal-llms-and-reinforcement-learning>

---

### 2.6 Semiconductor Domain LLM — SemiKong 是唯一公開的旗艦

- **SemiKong**（Aitomatic + AI Alliance，2024 年 SEMICON West 首發）— 世界第一個開源半導體 LLM
- 基座：**Meta Llama 3.1 70B**
- 資料：129 本教科書 / 章節 + 708 篇 etching 專論 + 20,000 篇一般研究 + 50,000 筆專門指令 + **總計 525.6 M tokens**
- 專長：**蝕刻（Etch）是主 focus**
- 效果宣稱：chip 上市時間 -20~30%、first-time-right +15~25%、新工程師 onboarding +40~50%
- 商業模式：Aitomatic 提供 Domain-Expert Agent（DXA）作為客製包覆層；SemiKong 是免費基座
- arxiv：2411.13802 <https://arxiv.org/abs/2411.13802>
- 官網：<https://www.semikong.ai/>
- Tom's Hardware：<https://www.tomshardware.com/tech-industry/artificial-intelligence/semikong-is-the-worlds-first-open-source-semiconductor-focused-llm-it-claims-to-bring-new-chips-to-market-30-percent-faster>

**關鍵啟示給 Qwen3-VL 半導體項目**：SemiKong 已驗證「純文本 domain LLM」是可行的，但**SemiKong 沒有 VLM 能力** — 這正是 Qwen3-VL 的切入點，可以在 vision 端補上 SemiKong 缺的那半。

#### 其他 LLM / Agent 案例

- **Infineon 內部 FA Agent**（arxiv 2506.15567，ISTFA 2025）— ReAct + Mixtral 8x7B + intent classification + RAG，做失效分析工作流自動化。已部署於 Infineon IT 基礎設施。<https://arxiv.org/abs/2506.15567>
- **SemiFA**（arxiv 2604.13236，2026 年）— Agentic 多模框架，自動生成半導體失效分析報告
- **ChipBench**（arxiv 2601.21448）— 評估 LLM 在 AI-aided chip design 的 benchmark
- **Synopsys.ai Copilot** — 2025 年 9 月擴充，RTL 生成 + 形式化斷言生成，早期客戶報告工程師 onboarding 時間 -30%。<https://news.synopsys.com/2025-09-03-Synopsys-Announces-Expanding-AI-Capabilities-for-its-Leading-EDA-Solutions>
- **Synopsys AgentEngineer**（DAC 2025 原型，基於 Microsoft Discovery）— 多 agent 系統、漸進式自主執行
- **Cadence** — JedAI Platform、Cerebrus Intelligent Chip Explorer（未在本輪搜尋中獲得 2025 最新動態，但已知長期投入）

---

### 2.7 製程 SOP / 工單理解 / Visual Agent

這是目前**公開案例較少**的領域，但正快速成長：

- **SOPRAG**（arxiv 2602.01858）— 專為工業 SOP 設計的 RAG 框架，用 Entity / Causal / Flow graph 三種 expert 取代 flat chunking，解決 SOP 的結構性與條件依賴。對 fab SOP 特別貼切。<https://arxiv.org/html/2602.01858>
- **PARAM**（arxiv 2508.04714）— RAG 驅動的 prescriptive agent，做自動化維護
- **LLM-R**（arxiv 2411.04476）— 階層 agent + RAG 的維護方案生成
- **AHHA Labs** 工業專屬 RAG 白皮書 <https://ahha.ai/2025/07/07/industry-specific-rag/>

**Visual agent for fab tool**：
- Qwen3-VL / Qwen2.5-VL 本身就有 GUI agent 能力（PC/mobile 操作）。理論上可以操作 SEM review software、MES 介面，但**公開案例極少**（fab 內部資訊大多 NDA）。
- NVIDIA Metropolis 是一個可行的框架 <https://developer.nvidia.com/metropolis>
- **推測**：TSMC / Samsung / Intel 內部應該已有 PoC，但未公開。

---

### 2.8 公開可用資料集盤點

| 資料集 | 規模 | 領域 | 取得 |
|--------|------|------|------|
| **WM-811K** | 811K wafer maps / 9 類 | Wafer map pattern | Kaggle / MIR Lab <https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map> |
| **MVTec AD** | 5,354 張 / 15 類 / 70+ 缺陷 | 工業異常（非半導體但常作 transfer baseline） | <https://www.mvtec.com/company/research/datasets/mvtec-ad> |
| **MVTec AD 2** | 8,000+ 張 / 8 新場景 | 進階工業異常 | <https://www.mvtec.com/company/research/datasets/mvtec-ad-2> |
| **ASE Dataset** | 後段封裝缺陷 | 封裝 | 見 arxiv 2404.05183 |
| **SEMI PCB / SEMI ADC** | 小規模 | PCB / ADC | 散落於 IEEE 論文 |
| **SEMI standards** 文件 | 數千頁規範 | Domain corpus | SEMI 官網付費訂閱 |
| **半導體教科書**（Sze, Plummer, Ghandhi, May & Spanos）| 散裝 | 理論 corpus | 買書 / 學術用途 |

**真正的 bottleneck**：fab 內部每天產生 **TB 級** SEM / OCD / 量測 / WAT / CP / FT 資料，**全部 NDA 不外流**。公開資料僅占實際產業資料量的極小比例。任何外部 VLM 想進 fab 做 domain adaptation，**資料取得協議** 是比技術更大的關卡。

---

### 2.9 代表性研究團隊 / 會議

- **IEEE TSM** (Transactions on Semiconductor Manufacturing) — 製程 AI 主力期刊
- **SPIE Advanced Lithography + Photomask Technology** — Litho AI 主場，cuLitho / ASML-DL 論文多在此
- **SPIE Metrology, Inspection, and Process Control** — Vol 13426 (2025) 收錄多篇 SEM / CD-SEM / OCD 深度學習 <https://spie.org/Publications/Proceedings/Volume/13426>
- **ISSM** (International Symposium on Semiconductor Manufacturing)
- **ASMC** (Advanced Semiconductor Manufacturing Conference) — IBM SEM ViT 論文 (2025) 發表處
- **SEMICON West / Europe / Taiwan** — SemiKong 2024 首發於 SEMICON West
- **ICCAD / DAC** — SEM-CLIP (2024)、ChipBench (2026)
- **ISTFA** (Int'l Symposium for Testing and Failure Analysis) — Infineon FA Agent 論文（2025）
- **ITC** (International Test Conference) — 測試階段 AI

**研究團隊**（公開可查）：
- IBM Research（Albany / Zurich）— ASMC 2025 SEM ViT
- Infineon Dresden — FA planning agent
- Aitomatic（矽谷）+ AI Alliance — SemiKong
- 台大 MIR Lab — WM-811K 來源
- NVIDIA Applied Research — Cosmos Reason 半導體應用、cuLitho
- ASML Veldhoven R&D — DL-OPC
- Synopsys AI Lab — Synopsys.ai Copilot / AgentEngineer

---

### 2.10 資訊缺口與誠實聲明

**公開資訊稀少的領域**（請勿過度推論）：
1. **TSMC / Samsung / Intel 內部 domain LLM** — 沒有任何一家公開釋出；Samsung 有 ZenML case study 但細節有限。**推測**：三家都有 internal PoC，規模等級可能在 7B–70B，以 RAG + SFT 為主，但無公開證據。
2. **Fab 內 VLM on SEM software GUI agent** — 理論可行、未見公開案例
3. **YE (Yield Enhancement) 跨模組 root-cause 的 LLM 整合** — 商用系統都在做，但演算法細節黑盒
4. **Process recipe 自動化 tuning** — SemiKong 宣稱做 etching recipe，實際部署案例未公開
5. **SEMI standards / SOP 的 domain embedding**（如 SEMI S2、S8、E30、E40、E87、E90、E94 等規範的 RAG）— 多為內部專案

**信任等級**：
- ✅ 高信度：SemiKong / Cosmos Reason / cuLitho / KLA AI / SEM-CLIP / WM-811K — 都有論文或官方文章
- ⚠️ 中信度：Samsung / Infineon 內部 agent — 有 case study 但細節不全
- ❌ 多為推測：TSMC 內部 Qwen / Llama-based LLM、Intel Gaudi-driven 內部模型 — 僅產業傳聞，**請勿在報告中陳述為事實**

---

## 綜合建議：把 Qwen3-VL 改造成半導體 Domain Model 的技術路線

### 推薦 stack

1. **基座選擇**：Qwen3-VL-32B-Instruct（性能 / 成本平衡）或 Qwen3-VL-8B-Instruct（快速迭代）
2. **訓練框架**：MS-SWIFT（阿里原生） + DeepSpeed ZeRO-3；LLaMA-Factory 當次選
3. **訓練階段設計**：
   - **CPT**：SEMI standards + 教科書 + 內部工藝文件（500 M–2 B tokens）
   - **VLM SFT**：SEM / wafer map / OCD 影像 + 人工標註指令（目標 100 K–500 K 樣本）
   - **DPO 或 GRPO**：資深工程師的偏好標註（報告品質、root-cause 合理性）
4. **對比基準**：Qwen3-VL base / SemiKong / Cosmos Reason / GPT-4o / Gemini 2.5 Pro
5. **評測設計**：
   - 公開：WM-811K 9 類、MVTec AD、SEM-CLIP dataset
   - 內部：自家 FAR 重現率、SOP QA 準確率、SEM defect 4-class 確診率

### 關鍵風險

- **資料權限** > 技術：內部 SEM 必須留在 air-gap 環境，訓練 infra 要能在 on-prem H100 cluster 上跑
- **MoE 部署複雜度**：235B-A22B 除非已有多機 infra，否則先用 32B dense
- **MRoPE / DeepStack 細節**：custom data collator 需對齊原生 dynamic resolution，不能 naïve resize
- **幻覺**：製程 Q&A 若無 RAG 背書，幻覺率在專業問題可達 20–40%；必用 RAG + citation
- **Golden reference**：像 Cosmos Reason 一樣支援「test image vs golden image」比對模式，是工程師實際工作流所需

---

## 主要參考 URL 速查

**Qwen3 / Qwen3-VL**
- Qwen3 Tech Report: <https://arxiv.org/abs/2505.09388>
- Qwen3-VL Tech Report: <https://arxiv.org/abs/2511.21631>
- Qwen3-VL GitHub: <https://github.com/QwenLM/Qwen3-VL>
- Qwen3-VL Collection: <https://huggingface.co/collections/Qwen/qwen3-vl>
- Qwen Blog: <https://qwenlm.github.io/>
- SWIFT Best Practice: <https://swift.readthedocs.io/en/latest/BestPractices/Qwen3-VL-Best-Practice.html>
- LLaMA-Factory + Qwen: <https://qwen.readthedocs.io/en/latest/training/llama_factory.html>
- Unsloth Qwen3-VL: <https://docs.unsloth.ai/models/qwen3-vl-how-to-run-and-fine-tune>

**半導體 VLM/LLM 案例**
- SemiKong arxiv: <https://arxiv.org/abs/2411.13802>
- SemiKong 官網: <https://www.semikong.ai/>
- SEM-CLIP: <https://arxiv.org/abs/2502.14884>
- IBM SEM ViT (ASMC 2025): <https://arxiv.org/abs/2506.03345>
- NVIDIA Cosmos Reason Wafer Map Cookbook: <https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/post_training/reason1/wafermap_classification/post_training.html>
- NVIDIA Defect Classification Blog: <https://developer.nvidia.com/blog/optimizing-semiconductor-defect-classification-with-generative-ai-and-vision-foundation-models/>
- Infineon FA Agent: <https://arxiv.org/abs/2506.15567>
- Synopsys.ai Copilot: <https://news.synopsys.com/2025-09-03-Synopsys-Announces-Expanding-AI-Capabilities-for-its-Leading-EDA-Solutions>
- Synopsys + NVIDIA cuLitho: <https://www.synopsys.com/blogs/chip-design/computational-lithography-chip-design-with-nvidia.html>
- WM-811K Kaggle: <https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map>
- MVTec AD: <https://www.mvtec.com/company/research/datasets/mvtec-ad>
- Applied Materials SEMVision H20: 透過 Averroes / semi news 報導
- Samsung LLMOps Case: <https://www.zenml.io/llmops-database/autonomous-semiconductor-manufacturing-with-multi-modal-llms-and-reinforcement-learning>
- ILT AI Review (Nature 2025): <https://www.nature.com/articles/s41377-025-01923-w>
- SPIE Metrology Vol 13426: <https://spie.org/Publications/Proceedings/Volume/13426>

---

*調研完成時間：2026-04-23；建議半年後更新（Qwen4 / Qwen3-VL 2 可能釋出、fab AI 商用化新一輪動態）。*
