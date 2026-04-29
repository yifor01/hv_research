# Letta forum — Letta vs Mem0 vs Zep vs Cognee

**來源**：https://forum.letta.com/t/agent-memory-letta-vs-mem0-vs-zep-vs-cognee/88
**訪問日期**：2026-04-29

## 各框架定位（forum 視角）

| 框架 | 定位 | 寫入方式 |
|---|---|---|
| **Mem0** | "drop-in memory layer"（外部 service 包 stateless agent）| LLM extraction |
| **Zep** | "context engineering platform built around temporal knowledge graphs"，bi-temporal model（event time vs transaction time）| 自動 KG 構建 |
| **Cognee** | "open-source library that builds semantic knowledge graphs from your data"，焦點在概念關係的 ontology | KG + ontology |
| **Letta** | "general-purpose memory programming system"，**fundamentally different approach**：把 agent 當 persistent entity with continuous state，不是 stateless function | OS-style paging |

## Cost / Latency

- **Mem0**：自己宣稱 vs full-context 「90% token cost reduction」「26% better accuracy」「91% lower latency」（hybrid: vector + graph + KV）
- **Letta AI Memory SDK（輕量版）**：`zero latency overhead during user interactions`，因為 memory processing async 在 interaction 之間（不在 query path 上）
- Zep / Cognee / Letta Platform：本 forum 未給數字

## 推薦使用場景

| 框架 | 場景 |
|---|---|
| Mem0 | 簡單 user/session memory，最少改動 |
| Zep | 「facts evolve」場景：要「current state + historical context」（地點變更、偏好變化）|
| Cognee | 「relationships between concepts matter」（技術文件、研究 paper、KB）|
| Letta Platform | agents 需 self-modify 知識/行為，或多 agent 共享 memory blocks |
| AI Memory SDK | drop-in 智能處理，不採 full stateful 架構 |

## 結論

只有 Mem0 給數字。其他四家無 cross-framework comparable benchmark。**這是 §4 Benchmark 章必須點出的口徑差異**。
