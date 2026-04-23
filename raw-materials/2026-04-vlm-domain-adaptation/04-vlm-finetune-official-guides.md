# 04 — VLM Fine-Tuning：現成官方指南與實戰教學清單

> 目的：彙整 2025–2026 年可直接照抄的 VLM fine-tune 官方文件、blog、repo。每條都有 URL / 作者 / 時間 / 可抄的 config。讀者是半導體 VLM domain adaptation 的技術負責人 + 訓練工程師。

---

## 0. 執行摘要（給趕時間的人）

如果只能挑一條路線，依硬體優先順序：

| 場景 | 首選工具 | 次選 | 關鍵原因 |
|------|---------|------|---------|
| 單卡 24 GB（4090 / A10G / L4） | **Unsloth** + QLoRA | TRL SFTTrainer + bnb-4bit | Unsloth 官方數據 1.7× 快、60% 省 VRAM；Qwen3-VL 8B 可在 T4 Colab 跑 |
| 多卡 80 GB（A100/H100 ×2–8） | **MS-SWIFT**（LoRA）或 **LLaMA-Factory** | TRL + DeepSpeed ZeRO3 | MS-SWIFT 原生 Qwen3-VL / InternVL3.5 / GLM4.5-V best practice |
| 企業級 多節點（32×8 H100） | **NeMo-AutoModel** / **Megatron-Bridge** | MS-SWIFT Megatron 模式 | 支援 TP/PP/CP/EP，Qwen3.5-MoE-397B 有官方 recipe |
| 想要一鍵 WebUI | **LLaMA-Factory** | Unsloth Studio | `llamafactory-cli webui` 零程式碼 |
| 研究型 RLHF / DPO / GRPO | **TRL**（v0.22+） | MS-SWIFT | TRL 原生支援 VLM 的 SFT/DPO/MPO/GRPO/GSPO/RLOO/Online-DPO |

**最重要的 3 個 config 片段**（後面章節會有完整版）：

```python
# TRL 官方推薦的「VLM 全線性 LoRA」
LoraConfig(r=16, lora_alpha=16, lora_dropout=0.05,
           target_modules="all-linear", task_type="CAUSAL_LM",
           modules_to_save=["lm_head", "embed_tokens"])

# SFTConfig 關鍵：max_length=None 避免切掉 image token
SFTConfig(max_length=None, remove_unused_columns=False,
          dataset_kwargs={"skip_prepare_dataset": True})

# Axolotl VLM 必備四件套
processor_type: AutoProcessor
skip_prepare_dataset: true
remove_unused_columns: false
sample_packing: false
```

---

## A. HuggingFace TRL — VLM 對齊官方 Blog & Cookbook

### A.1 TRL VLM Alignment Blog（2025）—— 2025-08-07

- **URL**：<https://huggingface.co/blog/trl-vlm-alignment>
- **作者**：Sergio Paniego、merve、Quentin Gallouédec、Kashif Rasul、Aritra Roy Gosthipaty、taesiri 等 100+ 共同署名
- **定位**：TRL 對 VLM 的「完整 trainer 支援矩陣」官方宣告

**Trainer 支援矩陣（2025-08 起）**：

| Trainer | VLM 原生支援 | 備註 |
|---------|:---:|------|
| SFTTrainer | ✅ | 只要資料有 `images` / `image` 欄位即可 |
| DPOTrainer | ✅ | 支援 MPO loss 組合（sigmoid+bco_pair+sft） |
| GRPOTrainer | ✅ | 支援 reward functions |
| GSPOTrainer | ✅ | GRPO 的 sequence-level importance sampling 變體，MoE 更穩 |
| RLOOTrainer | ✅ | 搭配 `examples/scripts/rloo_vlm.py` |
| OnlineDPOTrainer | ✅ | 支援 vLLM online generation |

**MPO Config（論文推薦）**：
```python
mpo_config = DPOConfig(
    loss_type=["sigmoid", "bco_pair", "sft"],
    loss_weights=[0.8, 0.2, 1.0],
)
```
官方宣稱 MathVista **+6.2 pts**。

**GSPO 關鍵差異**（讓 MoE 訓練穩定）：
```python
GRPOConfig(
    importance_sampling_level="sequence",  # vs "token"
    epsilon=3e-4, epsilon_high=4e-4, beta=0.0,
    loss_type="grpo", steps_per_generation=4,
)
```

**vLLM integration 兩種 mode**：
- colocate：`--use_vllm --vllm_mode colocate`
- server：先 `trl vllm-serve --model Qwen/Qwen2.5-VL-3B-Instruct --tensor-parallel-size 1 --vllm_model_impl transformers`，再訓練

**踩坑提醒**：Blog 本身**沒有**列具體 LoRA target_modules / 學習率 / VRAM，那些都在 TRL docs 另一頁（training_vlm_sft.md）。

### A.2 TRL 官方 VLM SFT 訓練文件

- **URL**：<https://huggingface.co/docs/trl/main/en/training_vlm_sft>
- **GitHub 原始檔**：<https://github.com/huggingface/trl/blob/main/docs/source/training_vlm_sft.md>
- **最新例示模型**：`google/gemma-3-4b-it`（TRL 0.22+）

**完整可跑程式碼**（可以直接複製當 baseline）：

```python
import torch, io
from datasets import load_dataset
from transformers import AutoModelForImageTextToText, AutoProcessor, BitsAndBytesConfig
from peft import LoraConfig
from trl import SFTConfig, SFTTrainer
from PIL import Image

model_id = "google/gemma-3-4b-it"
dataset = load_dataset("HuggingFaceH4/llava-instruct-mix-vsft")

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_quant_storage=torch.bfloat16,
)

model = AutoModelForImageTextToText.from_pretrained(
    model_id, device_map="auto", torch_dtype=torch.bfloat16,
    attn_implementation="eager", quantization_config=bnb_config,
)
processor = AutoProcessor.from_pretrained(model_id)
processor.tokenizer.padding_side = "right"

peft_config = LoraConfig(
    lora_alpha=16, lora_dropout=0.05, r=16, bias="none",
    target_modules="all-linear", task_type="CAUSAL_LM",
    modules_to_save=["lm_head", "embed_tokens"],
)

training_args = SFTConfig(
    output_dir="gemma-3-4b-vsft",
    num_train_epochs=1,
    per_device_train_batch_size=8,        # 多圖時改 1
    gradient_accumulation_steps=4,        # 多圖時改 1
    gradient_checkpointing=True,
    gradient_checkpointing_kwargs={"use_reentrant": False},
    optim="adamw_torch_fused",
    learning_rate=2e-05,
    bf16=True,
    remove_unused_columns=False,           # 🚨 關鍵
    dataset_kwargs={"skip_prepare_dataset": True},  # 🚨 關鍵
)
```

**Collator 的靈魂**（多圖 vs 單圖分流 + 遮 image token）：
```python
def collate_fn(examples):
    texts = [processor.apply_chat_template(
        e["messages"], tokenize=False, add_generation_prompt=False).strip()
        for e in examples]

    if "images" in examples[0]:
        images = [[img.convert("RGB") for img in e["images"]] for e in examples]
    else:
        images = [process_vision_info(e["messages"]) for e in examples]

    batch = processor(images=images, text=texts,
                      return_tensors="pt", padding=True)
    labels = batch["input_ids"].clone()
    labels[labels == processor.tokenizer.pad_token_id] = -100
    labels[labels == 262144] = -100        # soft image token
    batch["labels"] = labels
    return batch
```

**Max length 陷阱**：VLM 不能用 LLM 習慣的 `max_length=2048`，會切掉 image placeholder token 導致 train error。官方寫死 `max_length=None`。

### A.3 Phil Schmid VLM + TRL 教學 Blog（2024-09，已更新 2025）

- **URL**：<https://www.philschmid.de/fine-tune-multimodal-llms-with-trl>
- **Notebook**：<https://github.com/philschmid/deep-learning-pytorch-huggingface/blob/main/training/fine-tune-multimodal-llms-with-trl.ipynb>
- **作者**：Philipp Schmid（HF 技術總監）
- **模型**：Qwen2-VL-7B-Instruct（可替換 Llama-3.2-11B-Vision、Pixtral-12B）

**實測數字（AWS g6.2xlarge = L4 24 GB）**：
- VRAM 佔用：~24 GB
- 訓練時間：3 epochs 約 **1h31m**（~1k Amazon 商品描述樣本）
- 成本：**US$1.40**（@ $0.98/hr）

**Config（較保守版）**：
```python
LoraConfig(r=8, lora_alpha=16, lora_dropout=0.05, bias="none",
           target_modules=["q_proj", "v_proj"], task_type="CAUSAL_LM")

# bnb-4bit nf4 + compute_dtype=bfloat16
learning_rate = 2e-4
per_device_batch_size = 4
gradient_accumulation_steps = 8   # effective batch = 32
epochs = 3
warmup_ratio = 0.03
lr_scheduler_type = "constant"
max_grad_norm = 0.3
optim = "adamw_torch_fused"
```

**Qwen2-VL image token id 黑名單**（loss mask）：`[151652, 151653, 151655]`。

### A.4 HF Smol Course — VLM Fine-Tune 章節

- **URL**：<https://huggingface.co/learn/smol-course/en/unit3/3>
- **GitHub**：<https://github.com/huggingface/smol-course/blob/main/5_vision_language_models/vlm_finetuning.md>
- 官方內建：SFT + DPO；強調 bfloat16 / 4-bit / LoRA 三段省記憶體策略
- 搭配 **HF Jobs** 可完全雲端化執行

### A.5 SmolVLM Cookbook（L4 GPU 實測）

- **URL**：<https://huggingface.co/learn/cookbook/fine_tuning_smol_vlm_sft_trl>
- **GPU**：Tesla L4（24 GB）
- **模型**：`HuggingFaceTB/SmolVLM-Instruct`（2B params）
- **Dataset**：`HuggingFaceM4/ChartQA`（取 10% train/val/test）

依賴版本（固定版）：
```bash
pip install -U -q git+https://github.com/huggingface/trl.git bitsandbytes peft qwen-vl-utils trackio
pip install -q flash-attn --no-build-isolation
# trl==0.22.0.dev0 / bitsandbytes==0.47.0 / peft==0.17.1 / qwen-vl-utils==0.0.11
```

標準多模態 message schema（抄這個即可跨模型通用）：
```json
{
  "images": ["<PIL.Image>"],
  "messages": [
    {"role": "system", "content": [{"type": "text", "text": "You are..."}]},
    {"role": "user", "content": [
      {"type": "image", "image": "<PIL.Image>"},
      {"type": "text", "text": "What is shown?"}
    ]},
    {"role": "assistant", "content": [{"type": "text", "text": "A bar chart..."}]}
  ]
}
```

### A.6 HF Cookbook — Qwen2.5-VL MPO

- **URL**：<https://huggingface.co/learn/cookbook/en/fine_tuning_vlm_mpo>
- **Model**：`Qwen/Qwen2.5-VL-3B-Instruct`
- **Dataset**：`HuggingFaceH4/rlaif-v_formatted`（prompt+image / chosen / rejected）
- **Config**：LoRA r=16–32、α=32–64、dropout=0.05；bnb-4bit；lr 1e-4 ~ 5e-4；eval on MathVista
- **目的**：降低幻覺 → DPO + BCO + SFT 三 loss 組合

### A.7 Zero-to-Hero TRL Learning Stack

- **URL**：<https://huggingface.co/blog/burtenshaw/trl-learning-stack>
- 作者把 TRL 所有 VLM-related cookbook / blog / script 串成學習路徑圖，推薦當 onboarding checklist。

---

## B. Unsloth VLM 系列教學

### B.1 Qwen3-VL Run & Fine-tune 官方 Docs

- **URL**：<https://docs.unsloth.ai/models/qwen3-vl-how-to-run-and-fine-tune>
- **Colab Notebooks**（免費 T4 就能跑）：
  - SFT：`https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_VL_(8B)-Vision.ipynb`
  - Vision GRPO：`https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Qwen3_VL_(8B)-Vision-GRPO.ipynb`

**官方數據（vs HF transformers 原生）**：
- **1.7× 訓練速度**
- **60% 省 VRAM**
- **8× 長 context**（同 VRAM）

**新增功能（2025 Q4）**：GGUF export、多圖訓練、影片 + object detection fine-tune、Vision GRPO。

**踩坑提醒**（Unsloth 文件 + 社群）：
- 多圖訓練**不要**用 `.map()`，用 list comprehension，否則 dataset 標準化會 break
- Chat template 用 `--jinja` flag
- 某些 Qwen3-VL MoE 變體需要 `trust_remote_code=True`

### B.2 Vision RL（GRPO / GSPO for VLM）

- **URL**：<https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/vision-reinforcement-learning-vlm-rl>
- **Blog**：<https://www.unsloth.ai/blog/vision-rl>

**支援模型**：Qwen3-VL、Qwen2.5-VL-7B、Gemma-3-4B。

**宣稱**：vs FA2 setup「**1.5–2× 快 / 90% 省 VRAM / 15× 長 context / 精度不降**」。

**vLLM 整合**：`fast_inference=True`（但要搭配 `finetune_vision_layers=False`，因為 vLLM 不支援 vision LoRA）。

**GSPO 開關**：
```python
GRPOConfig(importance_sampling_level="sequence")
```

**Reward function 範例（防 addCriterion 垃圾 token）**：
```python
if (len(completion) - len(removal)) / len(completion) >= 0.5:
    score -= 2.0
```

### B.3 Unsloth Notebooks 目錄

- **URL**：<https://unsloth.ai/docs/get-started/unsloth-notebooks>
- 維護了 Qwen3-VL / Qwen2.5-VL / Gemma 3 / SmolVLM / LLaVA 的 Colab & Kaggle notebook 清單

**記憶體公式（Unsloth 官方建議）**：
- OOM 時：先 `per_device_train_batch_size=1`，再降 `max_seq_length`
- 保持 `use_gradient_checkpointing="unsloth"`（Unsloth 客製版，比 HF 原生更省）

### B.4 DataCamp — Qwen3-VL 8B 完整步驟（2026-01-07）

- **URL**：<https://www.datacamp.com/tutorial/fine-tuning-qwen3-vl-8b>
- **場景**：電子電路圖（schematics）domain adaptation —— 對半導體 VLM 很相關
- **Pipeline**：載入 Unsloth → 掛 QLoRA adapter → ChartQA 轉 SFT 格式 → train → push HF Hub
- **可直接 fork 的部分**：資料集準備 + training args

---

## C. Kaitchup（Benjamin Marie）VLM Fine-Tune 系列

Kaitchup 是少數會列**精確 VRAM 實測**的獨立 blogger（付費 Substack，但預覽足以拿到關鍵數字）。

### C.1 Qwen3-VL Fine-Tuning on Your Computer

- **URL**：<https://kaitchup.substack.com/p/qwen3-vl-fine-tuning-on-your-computer>
- **作者**：Benjamin Marie
- **發表日**：2025-10-20
- **Notebook**：#185（付費）

**VRAM 實測（Unsloth + QLoRA）**：
| 模型 | VRAM |
|------|------|
| Qwen3-VL-4B | ~16 GB |
| Qwen3-VL-8B | ~24 GB |

**文章重點**：
- Qwen3-VL vs Qwen2.5-VL 架構 & 訓練差異
- **Patch size** 差異 → Qwen3-VL 用 `token * 32 * 32`（Qwen2.5-VL 是 `28 * 28`）
- **必須**加 `trust_remote_code=True`（早期 transformers 版本）
- 範例資料集：ChartQA 轉 SFT

### C.2 Kaitchup Tutorials 全集

- **URL**：<https://kaitchup.substack.com/t/tutorials>
- 系列題目：QLoRA / DoRA / 2-bit 量化 / LoRA 對比實測

---

## D. MS-SWIFT / ModelScope 官方 Best Practice

MS-SWIFT = ModelScope 陣營的全家桶訓練框架，支援 600+ LLMs + **300+ MLLMs**。AAAI 2025 paper。

- **GitHub**：<https://github.com/modelscope/ms-swift>
- **Docs root**：<https://swift.readthedocs.io/en/latest/>
- **支援 VLMs**（節選）：Qwen3-VL、Qwen3-Omni、InternVL3.5、Ovis2.5、GLM4.5v、Gemma4、Llava、Phi4、MiniCPM-V-4、DeepSeek-VL2、Kimi-VL

### D.1 Qwen3-VL Best Practice

- **URL**：<https://swift.readthedocs.io/en/latest/BestPractices/Qwen3-VL-Best-Practice.html>
- **支援訓練類型**：CPT / SFT / GRPO / DPO / KTO / RM

**Qwen3-VL-4B-Instruct LoRA（2 GPU × 21 GiB）**（抽要）：
```
torch_dtype: bfloat16
learning_rate: 1e-4
lora_rank: 8
lora_alpha: 32
target_modules: all-linear
freeze_vit: true
freeze_aligner: true
padding_free: true
attn_implementation: flash_attention_2
```

**Qwen3-VL-30B-A3B-Instruct 全參數 Megatron（8 GPU × 80 GiB）**：
- `tensor_model_parallel_size: 2`
- `expert_model_parallel_size: ...`（MoE）

### D.2 Megatron-SWIFT 多模態文件

- **URL**：<https://github.com/modelscope/ms-swift/blob/main/docs/source_en/Megatron-SWIFT/Multimodal-Model.md>

**Dense 模型（Qwen2.5-VL-7B-Instruct）**：
- TP=2 / sequence_parallel=true / freeze_llm=false / freeze_vit=true / freeze_aligner=true
- 全參數：2 × **72 GiB** VRAM、**4.1 s / iter**
- LoRA：2 × **23 GiB** VRAM、**2.3 s / iter**
- 樣例 dataset：`AI-ModelScope/LaTeX_OCR:human_handwrite#5000`

**MoE 模型（InternVL3.5-30B-A3B）**：
- `expert_model_parallel_size: 2` / `moe_permute_fusion: true` / `moe_grouped_gemm: true` / `moe_aux_loss_coeff: 1e-3` / `moe_shared_expert_overlap: true`
- 2 × **43 GiB** VRAM、**8 s / iter**

### D.3 Multimodal FAQ

- **URL**：<https://github.com/modelscope/ms-swift/blob/main/docs/source_en/Instruction/Frequently-asked-questions.md>
- 踩坑：Packing 啟用時多模態 data 會跑兩次 map（dataset + template），慢 → `OMP_NUM_THREADS=14` 或關 packing

---

## E. LLaMA-Factory VLM Case

- **GitHub**：<https://github.com/hiyouga/LLaMA-Factory>
- **Qwen 官方對接文件**：<https://qwen.readthedocs.io/en/latest/training/llama_factory.html>
- **ACL 2024 paper**

**支援 VLM 列表（2026-04 當前）**：
- Qwen3-VL：2B/4B/8B/30B/32B/235B（template `qwen3_vl`）
- Qwen2.5-VL：2B/3B/7B/32B/72B（template `qwen2_vl`）
- InternVL 2.5/3/3.5：1B–241B（template `intern_vl`）
- LLaVA-1.5 7B/13B（template `llava`）
- LLaVA-NeXT 7B–110B（template `llava_next`）

**安裝要點**（Qwen2.5-VL 需要 `transformers>4.49.0`）：
```bash
conda create -n llamafactory python=3.10 -y
conda activate llamafactory
pip install torch==2.4.0 --index-url https://download.pytorch.org/whl/cu121
git clone https://github.com/hiyouga/LLaMA-Factory && cd LLaMA-Factory
pip install -e ".[torch,metrics,deepspeed,bitsandbytes,liger-kernel]"
```

**訓練 CLI**：
```bash
llamafactory-cli train examples/train_lora/qwen2vl_lora_sft.yaml
llamafactory-cli webui      # zero-code WebUI
```

**Qwen3-VL image token 切法特例**：用 `token * 32 * 32`（其他 Qwen 是 `28 * 28`）。

### E.1 AWS SageMaker HyperPod + LLaMA-Factory Sample

- **Repo**：<https://github.com/aws-samples/fine-tune-qwen2-vl-with-llama-factory>
- **亮點**：用 **PiSSA**（Principal Singular Values Adaptation）取代 LoRA — 只訓練 principal components，凍結 residual，**收斂更快**
- Slurm config 多節點 + SageMaker real-time endpoint 部署

---

## F. 各官方 VLM Fine-Tune Repo

### F.1 Qwen-VL-Series-Finetune（2U1）

- **Repo**：<https://github.com/2U1/Qwen-VL-Series-Finetune>
- **支援**：Qwen-VL / Qwen2-VL / Qwen2.5-VL / Qwen3-VL（含 MoE） / Qwen3.5
- **作者**：2U1（社群高質量 fork，Qwen 官方 repo 指向它）

**關鍵 CLI 參數整理**（抄這份就不用翻原始碼）：

```
# 三段式不同 LR（VLM 關鍵！）
--learning_rate        # LLM 本體
--vision_lr            # vision encoder（建議比 LLM 小 5–10×）
--merger_lr            # projector / aligner

# 凍結控制
--freeze_vision_tower True/False
--freeze_llm
--freeze_merger
--unfreeze_topk_llm N  # 只解凍最後 N 層 LLM
--unfreeze_topk_vision N

# LoRA
--lora_enable True
--lora_rank 128        # 🚨 預設 128，比社群常見 16 大很多
--lora_alpha 256
--lora_dropout 0.05
--num_lora_modules -1  # -1 = all
--vision_lora          # 也對 vision tower 掛 LoRA
--use_dora             # LoRA → DoRA

# 圖像 / 影片 token 控制
--image_min_pixels / --image_max_pixels
--image_resized_width / --image_resized_height
--video_min_pixels / --video_max_pixels
--fps / --nframes      # 互斥，只能擇一
```

**Dataset JSON**（官方格式，多圖 / 影片 / DPO / reasoning 四合一）：
```json
[{
  "id": "sample_id",
  "image": "file.jpg",          // 或 ["a.jpg","b.jpg"]
  "conversations": [
    {"from": "human", "value": "<image>\nQuestion?"},
    {"from": "gpt",   "value": "Answer"}
  ]
}]
```

DPO 格式：
```json
{"prompt": "<image>\nQ", "chosen": "A1", "rejected": "A2"}
```

Reasoning 格式（啟用 `--enable_reasoning True`；for Qwen3-VL-Thinking / Qwen3.5）：
```json
{"conversations":[{"from":"gpt","reasoning":"steps...","value":"final"}]}
```

**訓練 script 總覽**：`finetune.sh` / `finetune_lora.sh` / `finetune_lora_vision.sh` / `finetune_video.sh` / `finetune_dpo.sh` / `finetune_grpo.sh` / `finetune_cls.sh`

**DeepSpeed 建議**：`scripts/zero2.json`（速度優先，推薦）/ `scripts/zero3.json`（記憶體優先） / `zero3_offload.json`（OOM 再開）。LoRA 多 GPU 推薦 ZeRO2（ZeRO3 某些架構會壞 LoRA 梯度）。

**注意事項**：
- Qwen3.5：`--disable_flash_attn2 True`（穩定性）
- QLoRA **不要**跟 vision LoRA 同時開
- 影片 `fps` 跟 `nframes` 二擇一

### F.2 Qwen-VL 官方 finetune.py（Qwen1 代）

- **Repo**：<https://github.com/QwenLM/Qwen-VL/blob/master/finetune.py>
- **DeepWiki LoRA 頁**：<https://deepwiki.com/QwenLM/Qwen-VL/5.3-lora-fine-tuning>
- 典型超參：`per_device_train_batch_size=1`、`gradient_accumulation_steps=16`、`learning_rate=1e-5`、`weight_decay=0.1`、`adam_beta2=0.95`、`warmup_ratio=0.01`、`lr_scheduler_type=cosine`、`model_max_length=512`、`gradient_checkpointing=True`
- QLoRA 推薦 ZeRO2

### F.3 LLaVA / LLaVA-NeXT 官方 fine-tune 腳本

- **LLaVA finetune.sh**：<https://github.com/haotian-liu/LLaVA/blob/main/scripts/finetune.sh>
- **Open-LLaVA-NeXT**：<https://github.com/xiaoachen98/Open-LLaVA-NeXT>
- **LR**：2e-5（官方預設）
- **Vision tower**：CLIP ViT-L/14 336px；connector = mlp2x_gelu
- **訓練時間**：Open-LLaVA-NeXT-7B 約 20 小時（16×A100 80G）
- **DeepSpeed**：ZeRO-2（pretrain + finetune 都是）
- **LoRA 排除**：官方 script 手動排除 multi-modal-projector / vision-model / lm-head

### F.4 MiniCPM-V 2.6 / MiniCPM-o 官方 fine-tune

- **README**：<https://github.com/OpenBMB/MiniCPM-V/blob/main/finetune/readme.md>
- **Docs**：<https://minicpm-o.readthedocs.io/en/latest/finetune/fintune.html>

**命令**：`sh finetune_lora.sh` 或 `sh finetune_ds.sh`

**超參**：
- `model_max_length=2048`（記憶體換算基準）
- `batch_size=1`
- `LLM_TYPE="qwen"`（for MiniCPM-V 2.6）
- `--tune_vision false`（可選；關閉 vision 模塊訓練）

**VRAM 實測（A100）**：
- LoRA：**13.1–14.4 GiB**（2–8 GPUs）
- 全參數：**15.63–16.0 GiB**（2–8 GPUs）
- DeepSpeed stage 2 / 3 皆可，stage 3 支援 offload

**Dataset JSON**：單圖 `"<image>"` placeholder；多圖 `"<image_00>"`, `"<image_01>"` dict mapping。

### F.5 InternVL 3 官方 fine-tune 指南

- **URL**：<https://internvl.readthedocs.io/en/latest/internvl3.0/finetune.html>
- **COCO Caption LoRA 教學**：<https://internvl.readthedocs.io/en/latest/tutorials/coco_caption_finetune.html>

**LoRA rank**：128（約 6.24% 參數 → InternLM2-Chat-1.8B 約 125.8M trainable）。

**Target modules（Qwen3ForCausalLM 類 backbone）**：
```
self_attn.q_proj, k_proj, v_proj, o_proj
mlp.gate_proj, down_proj, up_proj
```

**資源**：LoRA 要 2×32/40G GPU；全參數要 8× GPU。預設凍結 vision encoder，但解凍通常表現更好。

**典型命令**：
```bash
GPUS=8 PER_DEVICE_BATCH_SIZE=1 \
  sh shell/internvl3.0/2nd_finetune/internvl3_2b_dynamic_res_2nd_finetune_full.sh
```

**Meta file**：指向 JSON dataset，需要 `--meta_path`。

**Merge LoRA**：`python tools/merge_lora.py <input_path> <output_path>`

### F.6 Idefics3

- **URL**：<https://huggingface.co/HuggingFaceM4/Idefics3-8B-Llama3>
- HF blog 原始 alignment recipe 用 Idefics2 示範（見 A.1）；Idefics3 model card 說明了對任意 image+text 交錯的輸入支援。

---

## G. 雲端 / Colab 教學

### G.1 NVIDIA NeMo / NeMo-AutoModel / Megatron-Bridge

**NeMo Framework User Guide**：
- **Qwen2-VL**：<https://docs.nvidia.com/nemo-framework/user-guide/25.04/vlms/qwen2vl.html>
- **LLaVA-NeXT**：<https://docs.nvidia.com/nemo-framework/user-guide/25.02/vlms/llavanext.html>
- **NeVA (LLaVA)**：<https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/neva.html>

**Qwen2-VL 啟動**：
```bash
torchrun --nproc_per_node=2 scripts/vlm/qwen2vl_finetune.py --devices=2 --tp=2
```

Target modules 自訂範例：
```
finetune.peft.target_modules=["*.language_model.*.linear_qkv"]
```
只對 self-attention qkv 掛 LoRA。

**NeMo-AutoModel**：
- **Repo**：<https://github.com/NVIDIA-NeMo/Automodel>
- **Qwen3-VL**：<https://docs.nvidia.com/nemo/automodel/latest/model-coverage/vlm/qwen/qwen3-vl.html>
- **Qwen3.5-VL MoE recipe**：<https://docs.nvidia.com/nemo/automodel/nightly/guides/vlm/qwen3-5.html>
  - YAML: `examples/vlm_finetune/qwen3_5_moe/qwen3_5_moe_medpix.yaml`
  - 配 32 × 8 H100 nodes
  - 資料集範例：MedPix-VQA（20,500 samples）
  - 啟動：
    ```bash
    CUDA_DEVICE_MAX_CONNECTIONS=1 automodel \
      examples/vlm_finetune/qwen3_5_moe/qwen3_5_moe_medpix.yaml \
      --nproc-per-node=8 \
      --model.pretrained_model_name_or_path=/path \
      --processor.pretrained_model_name_or_path=/path
    ```
- **Qwen2.5-VL 3B**：`automodel examples/vlm_finetune/qwen2_5/qwen2_5_vl_3b_rdr.yaml --nproc-per-node 8`

**Megatron-Bridge**：
- **URL**：<https://docs.nvidia.com/nemo/megatron-bridge/0.2.0/models/vlm/qwen2.5-vl.html>
- 提供 3B / 7B / 32B / 72B 四 recipes（`qwen25_vl_{3b,7b,32b,72b}_finetune_config`）
- Dataset 格式：JSONL conversation
- 啟動：
  ```bash
  torchrun --nproc-per-node=8 examples/recipes/qwen_vl/finetune_qwen25_vl.py \
    --pretrained-checkpoint $MEGATRON_MODEL_PATH \
    --recipe qwen25_vl_3b_finetune_config \
    --dataset-type hf
  ```

### G.2 Modal

- **Blog**：<https://modal.com/blog/fine-tuning-llms>
- **Modal SGLang VLM 範例**：<https://modal.com/docs/examples/sglang_vlm>
- Modal 適合當 training 平台，Serverless GPU，VLM fine-tune 用他們的 Volume + Container image，文件比較通用沒有專精 VLM
- Modal 自己的教學主要在 LLM，VLM 靠引用 Phil Schmid 與 Unsloth

### G.3 Lightning Studio

- 免費 $15 / mo credit，常見配置：NVIDIA L4（24 GB）
- 搭 QLoRA + Unsloth 是最便宜的 VLM fine-tune 路徑之一
- Lightning Studio 本身沒有 first-party VLM tutorial，第三方教學：<https://pavankunchalapk.medium.com/the-definitive-guide-to-fine-tuning-a-vision-language-model-on-a-single-gpu-with-code-79f7aa914fc6>

### G.4 AMD ROCm Dev Hub — Qwen2-VL LoRA

- **URL**：<https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/fine_tune/fine_tuning_lora_qwen2vl.html>
- **GPU**：MI300X
- Config 抄 Phil Schmid：r=8, α=16, dropout=0.05, target=[q_proj,v_proj], lr=2e-4, batch=4, grad_accum=8, epochs=3

### G.5 Google Gemma Vision QLoRA 官方教學

- **URL**：<https://ai.google.dev/gemma/docs/core/huggingface_vision_finetune_qlora>
- LoRA：r=16 / α=16 / dropout=0.05 / `target_modules="all-linear"` / `modules_to_save=["lm_head","embed_tokens"]`
- 4-bit nf4 double quant + bfloat16
- lr=2e-4、batch=1、epochs=3、max_grad_norm=0.3、optim=adamw_torch_fused
- Dataset：`philschmid/amazon-product-descriptions-vlm`
- Merge 階段需要 **>30 GB CPU RAM**（LoRA merge back 對 CPU 很吃）

---

## H. Axolotl VLM Support

- **Docs**：<https://docs.axolotl.ai/docs/multimodal.html>
- **狀態**：BETA；2025-10 加入 Qwen2.5-VL

**多模態強制四件套**（不加會 train 不起來）：
```yaml
processor_type: AutoProcessor
skip_prepare_dataset: true
remove_unused_columns: false
sample_packing: false   # multimodal 不支援 packing
```

**逐模型 YAML**：
```yaml
# Qwen2.5-VL
base_model: Qwen/Qwen2.5-VL-7B-Instruct
chat_template: qwen2_vl

# LLaVA-1.5
base_model: llava-hf/llava-1.5-7b-hf
chat_template: llava

# Llama 3.2 Vision
base_model: meta-llama/Llama-3.2-11B-Vision-Instruct
chat_template: llama3_2_vision

# Pixtral
base_model: mistralai/Pixtral-12B-2409
chat_template: pixtral

# Gemma-3
base_model: google/gemma-3-4b-it
chat_template: gemma3

# Mistral-Small-3.1 （需要 'pip install mistral-common[opencv]==1.8.5'）
base_model: mistralai/Mistral-Small-3.1-24B-Instruct-2503
```

**LoRA target（regex，Axolotl 推薦）**：
```yaml
adapter: lora
lora_target_modules: 'model.language_model.layers.[\d]+.(mlp|cross_attn|self_attn).(up|down|gate|q|k|v|o)_proj'
```

**圖像尺寸控制**：
```yaml
image_size: 512
image_resize_algorithm: bilinear
```

---

## I. TRL VLM-Specific Trainer 總表

- 官方 example scripts（GitHub `huggingface/trl/examples/scripts/`）：
  - `sft_vlm.py` / `sft_vlm_smol_vlm.py`
  - `dpo_vlm.py`
  - `grpo_vlm.py`
  - `rloo_vlm.py`
  - `online_dpo_vlm.py`

**跑法範例**（GRPO + vLLM colocate 模式）：
```bash
CUDA_VISIBLE_DEVICES=1,2 python3 examples/scripts/grpo_vlm.py \
  --model_name_or_path Qwen/Qwen2.5-VL-3B-Instruct \
  --use_vllm --vllm_mode colocate
```

**GRPOTrainer reward function 骨架**：
```python
def format_reward(completions, **kwargs):
    pattern = r"^<think>.*?</think>\s*<answer>.*?</answer>$"
    return [1.0 if re.match(pattern, c) else 0.0 for c in completions]

def accuracy_reward(completions, solution, **kwargs):
    # math_verify.parse + verify 比對 latex
    ...
```

**學習率基準**：`learning_rate=1e-5`（GRPO / GSPO / RLOO 共通預設）。

---

## J. 工程重點提取（跨教學的 Cross-Reference Checklist）

### J.1 Chat template & dataset format

統一「訊息 schema」範本（跨 TRL / Unsloth / LLaMA-Factory 可用）：
```json
"messages": [
  {"role": "system|user|assistant", "content": [
     {"type": "text", "text": "..."},
     {"type": "image", "image": "<PIL or path>"}
  ]}
]
```

Qwen 風 ShareGPT（MS-SWIFT / 2U1 repo 用）：
```json
"conversations": [
  {"from": "human", "value": "<image>\nQ"},
  {"from": "gpt",   "value": "A"}
]
```

### J.2 Vision encoder 凍結策略

| 教學 | 預設 |
|------|------|
| HF TRL cookbook | vision frozen，LoRA 只到 LLM |
| MS-SWIFT Qwen3-VL | `freeze_vit=true, freeze_aligner=true` |
| NeMo Qwen2-VL | vision 不 frozen（預設） |
| InternVL3 | vision frozen，文件明說解凍通常更好 |
| 2U1 repo | 三段 LR（LLM / vision / merger）獨立設定 |

**共通建議**：第一步先只訓 LLM + projector；觀察 val loss 平穩後，再解凍 vision 小 LR（比 LLM 小 5–10×）。

### J.3 LoRA target_modules 三種流派

| 流派 | 語法 | 覆蓋範圍 | 最適合 |
|------|------|---------|--------|
| 最小集 | `["q_proj","v_proj"]` | QV 投影 | VRAM 緊（r=8） |
| 全線性 | `"all-linear"` | 所有 Linear | 一般 domain adaptation |
| 全線性 + head | `all-linear` + `modules_to_save=[lm_head, embed_tokens]` | +輸出嵌入 | 新增 token / OCR |
| 高 rank 全模組 | r=128 α=256 all | 接近全參數 | 2U1 repo 預設 |
| regex | `model.language_model.layers.\d+.*.(q|k|v|o|up|down|gate)_proj` | 精準 | Axolotl |

### J.4 Data collator 關鍵要素

- 必須 **mask image token**（不同模型 id 不同，不能硬 copy）
  - Qwen2-VL：`151652, 151653, 151655`
  - Gemma 3：`262144`（soft image token）
- 必須 **mask pad token**（label = -100）
- 必須 `remove_unused_columns=False`、`dataset_kwargs={"skip_prepare_dataset": True}`（否則 TRL / Axolotl 會拆掉 image 欄位）

### J.5 OOM 防線（套路化）

依序加上，每步加完重測 VRAM：
1. `per_device_train_batch_size=1`
2. `gradient_checkpointing=True`（Unsloth 用 `"unsloth"` 模式）
3. `gradient_checkpointing_kwargs={"use_reentrant": False}`
4. bnb-4bit nf4（`load_in_4bit=True, bnb_4bit_compute_dtype=bfloat16`）
5. `torch_dtype=torch.bfloat16` + `attn_implementation="flash_attention_2"`
6. 減 `image_max_pixels` / `max_seq_length`
7. DeepSpeed ZeRO2 → ZeRO3 → ZeRO3 + CPU offload

### J.6 Flash Attention 2 相容性

- Qwen2-VL / Qwen2.5-VL / Qwen3-VL：支援（MS-SWIFT、TRL 預設建議開）
- Gemma 3：官方 TRL cookbook 用 `attn_implementation="eager"`（FA2 與 4-bit 量化時在某些版本不穩）
- Qwen3.5：要 `--disable_flash_attn2 True`（2U1 repo 警告）

### J.7 多 GPU scaling 指引

| 規模 | 推薦 |
|------|------|
| 2–4 GPU 同機 | DeepSpeed ZeRO2 + LoRA |
| 8 GPU 同機 | ZeRO3（全參）或 ZeRO2（LoRA） |
| 多節點（16 GPU+） | MS-SWIFT Megatron（TP=2, SP=true）或 NeMo Bridge |
| MoE（30B A3B, 235B, 397B） | 必須 EP（expert_model_parallel_size）+ moe_grouped_gemm |

### J.8 Evaluation benchmark（VLM 常用）

- **ChartQA**：圖表問答，domain 很 tight，每個教學都拿它 demo
- **MMIU-Benchmark**：多圖理解
- **MathVista**：數學圖像推理（MPO / GRPO 評測）
- **MedPix-VQA**：醫療影像（NeMo Qwen3.5-VL MoE demo 用這個）
- **RefCOCO / POPE**：grounding / hallucination

### J.9 互相矛盾處與可信度

1. **LoRA rank 預設差很大**：HF TRL / Phil Schmid / Gemma 官方都是 r=8–16；2U1 repo 預設 r=128、α=256；InternVL3 預設 r=128。**更可靠的做法**：小 domain（< 10k 樣本）用 r=16；大 domain / 有能力訓全參數時用 r=64–128。HF 官方 r=16 是「最小可用」，適合 consumer GPU；2U1 / InternVL 的 r=128 是「接近全參數」心態。
2. **Vision encoder 預設凍結 vs 解凍**：MS-SWIFT 凍、NeMo 解凍、InternVL 凍但推薦解凍。**保守做法**：先凍（穩定）→ 驗證 pipeline 通 → 再用很小 LR（LLM 的 1/10）解凍看是否有 marginal gain。
3. **DeepSpeed ZeRO2 vs ZeRO3 for LoRA**：2U1 / Qwen-VL 官方都警告 ZeRO3 + LoRA 在某些架構會壞梯度；ZeRO2 更穩。全參數用 ZeRO3。
4. **Gemma 3 attention**：TRL cookbook `attn_implementation="eager"` vs 其他全家用 FA2 → Gemma 3 的 bnb-4bit + FA2 組合在 transformers 某些版本有已知問題，eager 是安全路徑。

---

## K. 可直接複製的 Baseline 組合（半導體 domain 起手式推薦）

**場景**：4×A100 80 GB，半導體 wafer defect / schematic / SEM 圖片 + 中英文描述，~50k samples。

**推薦組合 1：MS-SWIFT + Qwen3-VL-8B-Instruct LoRA**
```
swift sft \
  --model Qwen/Qwen3-VL-8B-Instruct \
  --train_type lora \
  --dataset your_dataset.jsonl \
  --torch_dtype bfloat16 \
  --learning_rate 1e-4 \
  --lora_rank 16 --lora_alpha 32 \
  --target_modules all-linear \
  --freeze_vit true --freeze_aligner true \
  --padding_free true \
  --attn_impl flash_attention_2 \
  --num_train_epochs 3 \
  --per_device_train_batch_size 1 \
  --gradient_accumulation_steps 8
```

**推薦組合 2：TRL SFTTrainer + Qwen2.5-VL-7B-Instruct QLoRA（單卡 A100）**
```python
peft_config = LoraConfig(r=16, lora_alpha=32, lora_dropout=0.05,
    target_modules="all-linear", modules_to_save=["lm_head","embed_tokens"])
SFTConfig(
    max_length=None,
    per_device_train_batch_size=2, gradient_accumulation_steps=8,
    learning_rate=2e-4, bf16=True,
    gradient_checkpointing=True, optim="adamw_torch_fused",
    remove_unused_columns=False,
    dataset_kwargs={"skip_prepare_dataset": True},
)
```

**推薦組合 3：LLaMA-Factory WebUI（零程式碼，工程師交接給 PM/研究員用）**
```bash
llamafactory-cli webui
# 瀏覽器選 Qwen3-VL-8B-Instruct / qwen3_vl template / LoRA / your_dataset
```

---

## L. 資訊缺口（需要進一步驗證的點）

- **Qwen3-VL-4B vs 8B 在半導體圖像 domain 上的 accuracy gap**：所有教學都拿 ChartQA / MMIU / MedPix 當 benchmark，半導體專用還沒有公開對比數據 → 建議自己跑
- **Kaitchup 文章付費內容**：notebook #185 的完整 hyperparameter 表未公開
- **NeMo Megatron-Bridge 的精確 per-GPU VRAM / throughput**：官方文件跳過，需要自己 profile
- **Gemma 3 VLM 與 Qwen3-VL 在中文半導體文字（晶圓標籤、中文報告）上的表現差異**：目前所有教學都是英文資料集；中文需要 custom eval
- **Unsloth Vision RL 對 Qwen3-VL 30B MoE 的支援狀態**：文件只列 8B，30B 未明確

---

## M. 來源總表（URL + 作者 + 時間）

| # | 類別 | 來源 | URL | 作者 / 維護方 | 時間 |
|--|--|--|--|--|--|
| 1 | TRL Blog | Vision Language Model Alignment in TRL | https://huggingface.co/blog/trl-vlm-alignment | Sergio Paniego et al. | 2025-08-07 |
| 2 | TRL Docs | Training VLM with SFT | https://huggingface.co/docs/trl/main/en/training_vlm_sft | HuggingFace | 持續更新 |
| 3 | TRL Docs | SFT Trainer | https://huggingface.co/docs/trl/en/sft_trainer | HuggingFace | 持續更新 |
| 4 | Blog | Phil Schmid TRL Multimodal | https://www.philschmid.de/fine-tune-multimodal-llms-with-trl | Philipp Schmid | 2024-09（2025 更新） |
| 5 | Cookbook | Qwen2-VL TRL | https://huggingface.co/learn/cookbook/en/fine_tuning_vlm_trl | HF Cookbook | 2024 |
| 6 | Cookbook | Qwen2.5-VL MPO | https://huggingface.co/learn/cookbook/en/fine_tuning_vlm_mpo | HF Cookbook | 2025 |
| 7 | Cookbook | SmolVLM SFT | https://huggingface.co/learn/cookbook/fine_tuning_smol_vlm_sft_trl | HF Cookbook | 2025 |
| 8 | Cookbook | SmolVLM DPO | https://huggingface.co/learn/cookbook/fine_tuning_vlm_dpo_smolvlm_instruct | HF Cookbook | 2025 |
| 9 | Smol Course | VLM Fine-Tuning Unit | https://huggingface.co/learn/smol-course/en/unit3/3 | HF | 2024-25 |
| 10 | Unsloth Docs | Qwen3-VL Run & Fine-tune | https://docs.unsloth.ai/models/qwen3-vl-how-to-run-and-fine-tune | Unsloth | 2025 Q4 |
| 11 | Unsloth Docs | Vision RL Guide | https://unsloth.ai/docs/get-started/reinforcement-learning-rl-guide/vision-reinforcement-learning-vlm-rl | Unsloth | 2025 Q4 |
| 12 | Unsloth Blog | Vision RL | https://www.unsloth.ai/blog/vision-rl | Unsloth | 2025 |
| 13 | Unsloth Docs | All Notebooks | https://unsloth.ai/docs/get-started/unsloth-notebooks | Unsloth | 持續更新 |
| 14 | Substack | Qwen3-VL Fine-Tuning on Your Computer | https://kaitchup.substack.com/p/qwen3-vl-fine-tuning-on-your-computer | Benjamin Marie (Kaitchup) | 2025-10-20 |
| 15 | Tutorial | DataCamp Qwen3-VL 8B | https://www.datacamp.com/tutorial/fine-tuning-qwen3-vl-8b | Abid Ali Awan (DataCamp) | 2026-01-07 |
| 16 | MS-SWIFT | Qwen3-VL Best Practice | https://swift.readthedocs.io/en/latest/BestPractices/Qwen3-VL-Best-Practice.html | ModelScope | 2025 |
| 17 | MS-SWIFT | Megatron Multimodal | https://github.com/modelscope/ms-swift/blob/main/docs/source_en/Megatron-SWIFT/Multimodal-Model.md | ModelScope | 2025 |
| 18 | MS-SWIFT | Qwen3 Best Practice | https://swift.readthedocs.io/en/latest/BestPractices/Qwen3-Best-Practice.html | ModelScope | 2025 |
| 19 | MS-SWIFT | FAQ | https://github.com/modelscope/ms-swift/blob/main/docs/source_en/Instruction/Frequently-asked-questions.md | ModelScope | 持續更新 |
| 20 | LLaMA-Factory | GitHub | https://github.com/hiyouga/LLaMA-Factory | hiyouga | 持續更新 (ACL 2024) |
| 21 | LLaMA-Factory | Qwen Docs | https://qwen.readthedocs.io/en/latest/training/llama_factory.html | QwenLM | 2025 |
| 22 | AWS Sample | SageMaker + LLaMA-Factory + Qwen2-VL | https://github.com/aws-samples/fine-tune-qwen2-vl-with-llama-factory | AWS Samples | 2024-25 |
| 23 | Qwen Repo | Qwen-VL finetune.py | https://github.com/QwenLM/Qwen-VL/blob/master/finetune.py | QwenLM | 2023-24 |
| 24 | Community | Qwen-VL-Series-Finetune (2U1) | https://github.com/2U1/Qwen-VL-Series-Finetune | 2U1 | 持續更新 |
| 25 | LLaVA | LLaVA finetune script | https://github.com/haotian-liu/LLaVA/blob/main/scripts/finetune.sh | Haotian Liu | 2024 |
| 26 | LLaVA-NeXT | Open-LLaVA-NeXT | https://github.com/xiaoachen98/Open-LLaVA-NeXT | xiaoachen98 | 2024-25 |
| 27 | MiniCPM | MiniCPM-V finetune README | https://github.com/OpenBMB/MiniCPM-V/blob/main/finetune/readme.md | OpenBMB | 2024-25 |
| 28 | MiniCPM | MiniCPM-o docs | https://minicpm-o.readthedocs.io/en/latest/finetune/fintune.html | OpenBMB | 2025 |
| 29 | InternVL | InternVL3 Finetune | https://internvl.readthedocs.io/en/latest/internvl3.0/finetune.html | OpenGVLab | 2025 |
| 30 | InternVL | COCO Caption LoRA | https://internvl.readthedocs.io/en/latest/tutorials/coco_caption_finetune.html | OpenGVLab | 2024 |
| 31 | NVIDIA | NeMo Qwen2-VL | https://docs.nvidia.com/nemo-framework/user-guide/25.04/vlms/qwen2vl.html | NVIDIA | 2025 |
| 32 | NVIDIA | NeMo LLaVA-NeXT | https://docs.nvidia.com/nemo-framework/user-guide/25.02/vlms/llavanext.html | NVIDIA | 2025 |
| 33 | NVIDIA | NeMo NeVA | https://docs.nvidia.com/nemo-framework/user-guide/latest/vlms/neva.html | NVIDIA | 持續更新 |
| 34 | NVIDIA | NeMo-AutoModel Qwen3-VL | https://docs.nvidia.com/nemo/automodel/latest/model-coverage/vlm/qwen/qwen3-vl.html | NVIDIA | 2026 Q1 |
| 35 | NVIDIA | NeMo-AutoModel Qwen3.5-VL MoE | https://docs.nvidia.com/nemo/automodel/nightly/guides/vlm/qwen3-5.html | NVIDIA | 2026 Q1 |
| 36 | NVIDIA | Megatron-Bridge Qwen2.5-VL | https://docs.nvidia.com/nemo/megatron-bridge/0.2.0/models/vlm/qwen2.5-vl.html | NVIDIA | 2025-26 |
| 37 | NVIDIA | NeMo-AutoModel LLaVA | https://docs.nvidia.com/nemo/automodel/nightly/model-coverage/vlm/llava-hf/llava.html | NVIDIA | 2026 Q1 |
| 38 | NVIDIA | NeMo-AutoModel GitHub | https://github.com/NVIDIA-NeMo/Automodel | NVIDIA-NeMo | 持續更新 |
| 39 | Axolotl | Multimodal Docs | https://docs.axolotl.ai/docs/multimodal.html | axolotl-ai-cloud | 2025 |
| 40 | Axolotl | GitHub | https://github.com/axolotl-ai-cloud/axolotl | axolotl-ai-cloud | 持續更新 |
| 41 | Modal | Fine-tuning LLMs blog | https://modal.com/blog/fine-tuning-llms | Modal | 2025 |
| 42 | Modal | SGLang VLM example | https://modal.com/docs/examples/sglang_vlm | Modal | 2025-26 |
| 43 | AMD | ROCm Qwen2-VL LoRA | https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/fine_tune/fine_tuning_lora_qwen2vl.html | AMD | 2025 |
| 44 | Google | Gemma Vision QLoRA | https://ai.google.dev/gemma/docs/core/huggingface_vision_finetune_qlora | Google | 2025 |
| 45 | HF Blog | SmolVLM | https://huggingface.co/blog/smolvlm | HuggingFace | 2024 |
| 46 | HF Blog | VLMs Explained | https://huggingface.co/blog/vlms | HuggingFace | 2024-25 |
| 47 | TRL Blog | Burtenshaw learning stack | https://huggingface.co/blog/burtenshaw/trl-learning-stack | Ben Burtenshaw | 2025 |
| 48 | DeepWiki | Qwen-VL LoRA | https://deepwiki.com/QwenLM/Qwen-VL/5.3-lora-fine-tuning | DeepWiki | 自動化 |
| 49 | Qwen Repo | Qwen3-VL GitHub | https://github.com/QwenLM/Qwen3-VL | QwenLM | 2025 Q4 |

---

_文件完成日：2026-04-23；維護者：hv-research VLM domain adaptation 專案_
