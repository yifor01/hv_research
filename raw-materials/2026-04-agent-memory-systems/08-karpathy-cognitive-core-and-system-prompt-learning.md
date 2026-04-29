# Karpathy — Cognitive Core + System Prompt Learning

**Cognitive Core 來源**：https://www.memco.ai/blog/karpathy-cognitive-core-memory（2025-10-21，引 Karpathy Dwarkesh podcast）

## Cognitive Core 核心主張

把模型的 raw reasoning ability 與 knowledge storage 解耦。模型不該同時是「智能體」+「百科全書」，應只當前者。

### 必引用的 Karpathy 原句

> "I want to remove the memory... and only maintain the algorithms for thought"

### 對 agent 設計的意義

- 小模型 + 外掛專業 memory 也能達到大模型表現
- 模型專注 dynamic problem-solving，不當 static knowledge repository
- 隱含預測：~1B 參數模型 + 好的外掛記憶 = 取代當前大模型

## System Prompt Learning（X 推文 2025-05，原 status 1921368644069765486）

> "We're missing (at least one) major paradigm for LLM learning. Not sure what to call it, possibly it has a name - system prompt learning? Pretraining is for knowledge. Finetuning (SL/RL) is for habitual behavior. Both of these involve a change in parameters but a lot of human..."

### 三層學習範式

| 範式 | 機制 | 對應人類 |
|---|---|---|
| Pretraining | 改參數 | 從小到大累積知識 |
| Finetuning（SL/RL）| 改參數 | 養成習慣 / 個性 |
| **System Prompt Learning** | 不改參數，改顯式規則 / 筆記 / 反思 | **寫筆記、總結教訓、列規則** |

### 為何這層缺失

LLM 沒有「我學到一個新教訓 → 把它寫成下次要遵守的規則」這個機制。
所有現有路徑（fine-tune / 修 prompt）都需 human in the loop。
LLM Wiki 路線正是 System Prompt Learning 的具體落地。

## 三概念串連邏輯

```
Decade of Agents（記憶是缺口） 
   ↓
System Prompt Learning（缺失的學習範式）
   ↓
LLM Wiki（System Prompt Learning 的具體實作）
   ↓
Cognitive Core（最終形態：瘦核心 + 外掛記憶）
   ↓
Wiki → Fine-tune（explicit → implicit consolidation）
```

這條線是 §1 / §3.3 / §5.2 / §5.4 / §9.1 / §9.9 的全文骨架。
