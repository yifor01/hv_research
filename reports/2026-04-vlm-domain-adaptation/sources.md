# Sources — Qwen3-VL 半導體 Domain Adaptation 橫縱分析

> 訪問日期：2026-04-23
> 研究範圍：四階段訓練 pipeline（CPT + SFT + Preference Alignment + Agent SFT）+ Qwen3-VL 生態 + 半導體製程 VLM 應用

---

## 一手來源（按類別分組）

### A. 核心方法論（arxiv 論文，按時間順序）

| 時間 | 論文 | URL |
|------|------|-----|
| 2018-01 | ULMFiT | https://arxiv.org/abs/1801.06146 |
| 2019-01 | BioBERT | https://arxiv.org/abs/1901.08746 |
| 2019-03 | SciBERT | https://arxiv.org/abs/1903.10676 |
| 2020-02 | T5 | https://arxiv.org/abs/1910.10683 |
| 2020-05 | GPT-3 | https://arxiv.org/abs/2005.14165 |
| 2020-04 | DAPT/TAPT (Don't Stop Pretraining) | https://arxiv.org/abs/2004.10964 |
| 2020-06 | FinBERT | https://arxiv.org/abs/2006.08097 |
| 2021-06 | LoRA | https://arxiv.org/abs/2106.09685 |
| 2022-03 | InstructGPT | https://arxiv.org/abs/2203.02155 |
| 2022-12 | Constitutional AI / RLAIF | https://arxiv.org/abs/2212.08073 |
| 2023-01 | BLIP-2 | https://arxiv.org/abs/2301.12597 |
| 2023-02 | LLaMA | https://arxiv.org/abs/2302.13971 |
| 2023-04 | LLaVA v1 | https://arxiv.org/abs/2304.08485 |
| 2023-04 | MiniGPT-4 | https://arxiv.org/abs/2304.10592 |
| 2023-05 | LIMA | https://arxiv.org/abs/2305.11206 |
| 2023-05 | QLoRA | https://arxiv.org/abs/2305.14314 |
| 2023-05 | Gorilla | https://arxiv.org/abs/2305.15334 |
| 2023-05 | DPO | https://arxiv.org/abs/2305.18290 |
| 2023-07 | ToolLLM | https://arxiv.org/abs/2307.16789 |
| 2023-08 | Qwen-VL | https://arxiv.org/abs/2308.12966 |
| 2023-10 | LLaVA-1.5 | https://arxiv.org/abs/2310.03744 |
| 2023-10 | NEFTune | https://arxiv.org/abs/2310.05914 |
| 2023-10 | IPO | https://arxiv.org/abs/2310.12036 |
| 2023-11 | CogVLM | https://arxiv.org/abs/2311.03079 |
| 2024-01 | Self-Rewarding LM | https://arxiv.org/abs/2401.10020 |
| 2024-01 | LLaMA-Pro | https://arxiv.org/abs/2401.02415 |
| 2024-01 | Examining Forgetting in CPT | https://arxiv.org/abs/2401.03129 |
| 2024-02 | KTO | https://arxiv.org/abs/2402.01306 |
| 2024-02 | DeepSeekMath / GRPO | https://arxiv.org/abs/2402.03300 |
| 2024-02 | DoRA | https://arxiv.org/abs/2402.09353 |
| 2024-03 | ORPO | https://arxiv.org/abs/2403.07691 |
| 2024-04 | PiSSA | https://arxiv.org/abs/2404.02948 |
| 2024-05 | LoRA Learns Less, Forgets Less | https://arxiv.org/abs/2405.09673 |
| 2024-05 | SimPO | https://arxiv.org/abs/2405.14734 |
| 2024-08 | LLaVA-OneVision | https://arxiv.org/abs/2408.03326 |
| 2024-09 | Qwen2-VL | https://arxiv.org/abs/2409.12191 |
| 2024-09 | Molmo / PixMo | https://arxiv.org/abs/2409.17146 |
| 2024-10 | OS-Atlas | https://arxiv.org/abs/2410.23218 |
| 2024-11 | V-DPO | https://arxiv.org/abs/2411.02712 |
| 2024-11 | SemiKong | https://arxiv.org/abs/2411.13802 |
| 2025-01 | Learning Beyond the Surface | https://arxiv.org/abs/2501.17840 |
| 2025-01 | UI-TARS | https://arxiv.org/abs/2501.12326 |
| 2025-02 | Qwen2.5-VL | https://arxiv.org/abs/2502.13923 |
| 2025-02 | SEM-CLIP | https://arxiv.org/abs/2502.14884 |
| 2025-05 | Qwen3 Tech Report | https://arxiv.org/abs/2505.09388 |
| 2025-06 | IBM SEM ViT (ASMC 2025) | https://arxiv.org/abs/2506.03345 |
| 2025-06 | Infineon FA Agent (ISTFA 2025) | https://arxiv.org/abs/2506.15567 |
| 2025-11 | Qwen3-VL Tech Report | https://arxiv.org/abs/2511.21631 |

### B. 官方 blog / release / 文件

| 來源 | URL |
|------|-----|
| **Qwen3.6 GitHub（2026-04）** | https://github.com/QwenLM/Qwen3.6 |
| **Qwen3.6-27B HuggingFace** | https://huggingface.co/Qwen/Qwen3.6-27B |
| **Qwen3.6-27B-FP8** | https://huggingface.co/Qwen/Qwen3.6-27B-FP8 |
| **Qwen3.6 Blog** | https://qwen.ai/blog?id=qwen3.6-27b |
| **Qwen3.6 Simon Willison 分析** | https://simonwillison.net/2026/Apr/22/qwen36-27b/ |
| **Qwen3.6 MarkTechPost 解讀** | https://www.marktechpost.com/2026/04/22/alibaba-qwen-team-releases-qwen3-6-27b-a-dense-open-weight-model-outperforming-397b-moe-on-agentic-coding-benchmarks/ |
| Qwen Blog | https://qwenlm.github.io/ |
| Qwen3-VL GitHub | https://github.com/QwenLM/Qwen3-VL |
| Qwen3-VL HuggingFace Collection | https://huggingface.co/collections/Qwen/qwen3-vl |
| **SemiKong Training Dataset（社群版）** | https://huggingface.co/datasets/sitloboi2012/SemiKong-Training-Dataset |
| SWIFT Qwen3-VL Best Practice | https://swift.readthedocs.io/en/latest/BestPractices/Qwen3-VL-Best-Practice.html |
| Qwen Function Calling Docs | https://qwen.readthedocs.io/en/latest/framework/function_call.html |
| Unsloth Qwen3-VL Guide | https://docs.unsloth.ai/models/qwen3-vl-how-to-run-and-fine-tune |
| TRL VLM Alignment Blog | https://huggingface.co/blog/trl-vlm-alignment |
| Stanford Alpaca Release | https://crfm.stanford.edu/2023/03/13/alpaca.html |
| Dolly v2 Release (Databricks) | https://www.databricks.com/blog/2023/04/12/dolly-first-open-commercially-viable-instruction-tuned-llm |
| SemiKong 官網 | https://www.semikong.ai/ |
| NVIDIA Cosmos Reason Wafer Cookbook | https://nvidia-cosmos.github.io/cosmos-cookbook/recipes/post_training/reason1/wafermap_classification/post_training.html |
| NVIDIA Semi Defect Blog | https://developer.nvidia.com/blog/optimizing-semiconductor-defect-classification-with-generative-ai-and-vision-foundation-models/ |
| Synopsys × NVIDIA cuLitho | https://www.synopsys.com/blogs/chip-design/computational-lithography-chip-design-with-nvidia.html |
| Synopsys.ai Copilot 2025 | https://news.synopsys.com/2025-09-03-Synopsys-Announces-Expanding-AI-Capabilities-for-its-Leading-EDA-Solutions |
| Intel Manufacturing Yield AI | https://www.intel.com/content/dam/www/central-libraries/us/en/documents/intel-it-manufacturing-yield-analysis-with-ai-paper.pdf |
| Samsung LLMOps (ZenML case) | https://www.zenml.io/llmops-database/autonomous-semiconductor-manufacturing-with-multi-modal-llms-and-reinforcement-learning |

### C. 工具鏈 GitHub

| 工具 | URL |
|------|-----|
| LLaMA-Factory | https://github.com/hiyouga/LLaMA-Factory |
| MS-SWIFT | https://github.com/modelscope/ms-swift |
| Axolotl | https://github.com/axolotl-ai-cloud/axolotl |
| unsloth | https://github.com/unslothai/unsloth |
| TRL | https://github.com/huggingface/trl |
| OpenRLHF | https://github.com/OpenRLHF/OpenRLHF |
| verl | https://github.com/volcengine/verl |
| Megatron-LM | https://github.com/NVIDIA/Megatron-LM |
| Megatron-Bridge | https://github.com/NVIDIA-NeMo/Megatron-Bridge |
| Qwen-Agent | https://github.com/QwenLM/Qwen-Agent |
| 2U1/Qwen-VL-Series-Finetune | https://github.com/2U1/Qwen-VL-Series-Finetune |
| InternVL | https://github.com/OpenGVLab/InternVL |

### D. 資料集與 benchmark

| 資料集 | URL |
|--------|-----|
| WM-811K Wafer Map | https://www.kaggle.com/datasets/qingyi/wm811k-wafer-map |
| MVTec AD | https://www.mvtec.com/company/research/datasets/mvtec-ad |
| MVTec AD 2 | https://www.mvtec.com/company/research/datasets/mvtec-ad-2 |
| SPIE Metrology Vol 13426 | https://spie.org/Publications/Proceedings/Volume/13426 |

### E. 分析與補充

| 來源 | URL |
|------|-----|
| Post-Training in 2026 (LLM-stats) | https://llm-stats.com/blog/research/post-training-techniques-2026 |
| Advanced LoRA Fine-Tuning Guide (Kaitchup) | https://kaitchup.substack.com/p/advanced-lora-fine-tuning-how-to |
| GRPO Primer (Wolfe) | https://cameronrwolfe.substack.com/p/grpo |
| EVAL #003 Fine-Tuning in 2026 | https://dev.to/ultraduneai/eval-003-fine-tuning-in-2026-axolotl-vs-unsloth-vs-trl-vs-llama-factory-2ohg |
| Qwen3-VL DeepStack 分析 | https://thesalt.substack.com/p/qwen3-vl-deepstack-fusion-interleaved |
| Qwen3-VL DeepWiki | https://deepwiki.com/QwenLM/Qwen3-VL/4.2-model-architecture |
| Nature ILT AI Review (2025) | https://www.nature.com/articles/s41377-025-01923-w |
| Tom's Hardware SemiKong 報導 | https://www.tomshardware.com/tech-industry/artificial-intelligence/semikong-is-the-worlds-first-open-source-semiconductor-focused-llm |

---

## 原始素材檔

研究過程由三個平行子 agent 聯網收集，產出三份原始素材（位於 `raw-materials/2026-04-vlm-domain-adaptation/`）：

| 檔案 | 內容 | 字數 |
|------|------|------|
| `01-diachronic.md` | 縱向：四階段 pipeline 2018–2026 歷史演化 | ~28K 字元 |
| `02-synchronic.md` | 橫向：各階段方法 + 工具鏈橫向對比 | ~22K 字元 |
| `03-qwen3-vl-semiconductor.md` | Qwen3-VL 生態 + 半導體 VLM 應用盤點 | ~22K 字元 |

最終報告（`Qwen3-VL半導體領域適應_橫縱分析報告.md`）從以上三份素材整合而來，並補上橫縱交匯洞察章節。

---

## 資料覆蓋度與限制

**高信度**（有官方 blog / arxiv / GitHub / 論文支撐）：
- Qwen3-VL 家族發布時程、架構細節、訓練配比
- 四階段 pipeline 各方法的論文與基準
- 工具鏈功能矩陣（LLaMA-Factory / MS-SWIFT / verl / TRL 等）
- SemiKong / SEM-CLIP / IBM SEM ViT / Cosmos Reason / Infineon FA Agent

**中信度**（Case study 或部分披露）：
- Samsung LLMOps（ZenML case study）
- Qwen3-VL VLM 側 RL 配比（僅籠統描述「GRPO + GSPO」）
- GRPO hyperparameter 最佳實務（社群仍在收斂中）

**未能驗證 / 無公開證據**：
- TSMC / Intel / Micron / SK Hynix 內部 domain LLM（皆為推測）
- Fab 內部 VLM + SEM GUI agent 實際部署狀態
- 各家 fab 內部 process recipe auto-tuning 的 AI 介入程度

這些限制在報告中已明確標註，避免將推測陳述為事實。

---

**訪問日期統一**：2026-04-23（所有 URL 於該日期前最後一次驗證可訪問）。
**半年後重訪建議**：Qwen4 / Qwen3-VL-2 / DeepSeek-V4 等可能釋出，GRPO 最佳實務應有更穩定預設，SEMICON West 2026 / ASMC 2026 可能有新的 fab AI 案例公開。
