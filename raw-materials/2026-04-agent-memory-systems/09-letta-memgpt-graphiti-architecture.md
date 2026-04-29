# Letta (MemGPT) + Graphiti (Zep) 架構細節

## MemGPT 原 paper（arXiv:2310.08560，2023-10）

### OS 隱喻
> "inspiration from hierarchical memory systems in traditional operating systems that provide the appearance of large memory resources through data movement between fast and slow memory"

| OS 概念 | MemGPT 對應 |
|---|---|
| RAM（fast、small）| **Main context**（context window 內可見）|
| Disk（slow、unlimited）| **External context**（archival storage）|
| Page in/out | LLM 自己決定何時 retrieve / archive |
| Interrupt | 控制 user / agent 之間的流程 |

### Virtual Context Management
讓 LLM 處理超出 native context window 的資料：information 在不同 tier 間智能搬移。

### 核心應用
- **Document analysis**：處理遠超 context window 的文件
- **Multi-session chat**：agents「remember, reflect, and evolve dynamically through long-term interactions」

## Letta（MemGPT 商業化後）

### Memory Block 概念
- Labeled memory blocks（如 "human", "persona"）
- Agent 可在互動中 reference 並 update 各 block
- 支援多 agent 共享 memory blocks

### 商業化版本差異
- **Letta Code SDK**：本地 tool execution（Bash / Grep），對標 Claude Code / Codex
- **Letta API**：純 chatbot 場景，對標 OpenAI Responses API
- **MemFS**：git-tracked memory system（最新加）

### 核心差異化
- **Statefulness**：跨互動持久
- **Self-improvement**：agent 主動 update 自己的 memory + system instruction
- **Native multi-agent coordination**：透過共享 memory blocks

## Graphiti / Zep 架構

### Bi-Temporal Model
> "facts have validity windows. When information changes, old facts are invalidated — not deleted."

Entity / relationship 都帶時間戳：
- 何時 valid
- 何時被 supersede（如有）

### 儲存模式
- 三元組：Entity → Relationship → Entity
- 自動從非結構化 / 結構化資料抽取
- 「Everything traces back to episodes — the raw data that produced it」（保 provenance lineage）

### Graphiti vs Zep Platform
| 層 | 角色 |
|---|---|
| **Graphiti** | 開源 temporal context graph engine，flexible core |
| **Zep platform** | managed infra：governance + users + threads + message storage + 預配 retrieval + dashboards + SDK + enterprise support |

推薦：自建用 Graphiti，turnkey 用 Zep。

### 性能聲明
- Sub-second latency
- 「optimized for large datasets」「parallel processing」

## 學術系統補充（emergentmind 整理）

| 系統 | 特色 |
|---|---|
| **A-MEM** | Zettelkasten-inspired note-based，dynamic linking |
| **HiAgent** | 階層 chunking via subgoals |
| **MIRIX** | 六模組（Core / Episodic / Semantic / Procedural / Resource / Knowledge Vault）|
| **Collaborative Memory** | Dual-tiered private / shared fragments |
| **Coarse-to-Fine** | 多層 memory 支援 exploration + 錯誤修正 |

### Recall 數學模型（emergentmind）
$$ p(t) = 1 - \exp(-r \cdot e^{-a t}) $$

組合 relevance r、time decay a、頻率，給 recall probability。
