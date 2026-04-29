# Mem0 — State of AI Agent Memory 2026

**來源**：https://mem0.ai/blog/state-of-ai-agent-memory-2026
**訪問日期**：2026-04-29

## 自述定位

> 「memory is a first-class architectural component」取代 ad hoc conversation history

從 ~3 年前「barely existed」演進為成熟工程領域，有 standardized benchmarks + dedicated infra + 獨立研究文獻。

## 架構

### Multi-scope memory model
- 關聯：`user_id`, `agent_id`, `run_id`/`session_id`, `app_id`/`org_id`
- scopes 在 retrieval 時 compose
- v1.0.0 加 metadata filtering

### Hybrid storage
- Vector stores（19 個 backend，self-hosted + cloud）
- Graph memory variant **Mem0g**（Kuzu / Neo4j）
- 三種 hosting：managed cloud / open-source self-hosted / local MCP（隱私優先）

### 三類記憶
- Episodic（what happened）
- Semantic（what is known）
- Procedural（how to do things）

## Benchmark — LOCOMO（自己的 paper，arXiv:2504.19413，ECAI 2025）

| Approach | LLM Score | P95 Latency | Tokens/conv |
|---|---|---|---|
| Full-context | 72.9% | 17.12s | ~26,000 |
| **Mem0g (graph)** | 68.4% | 2.59s | ~1,800 |
| **Mem0 (vector)** | 66.9% | 1.44s | ~1,800 |
| RAG | 61.0% | 0.70s | — |
| OpenAI Memory | 52.9% | — | — |

> 注意：這是 Mem0 自家的 benchmark；LongMemEval 的數字（49% vs Zep 63.8%）來自第三方，是不同口徑。

## 競爭定位（自說自話的部分）

- 明寫 Zep 是 "third-party memory infrastructure"，但無 published comparison
- MemGPT、MemoryBank 列為 literature baselines 不深比
- **完全沒提 Letta、MemPalace** — 觀察重點

## 版本里程碑

- mid-2024 ~ 2026 早期：18 個月 release 期
- v1.0.0（2025-06）：async default, reranking, metadata filtering, procedural memory
- v1.0.1（2025-11）：Cassandra
- v1.0.3（2026-01）：inclusion/exclusion prompts, memory depth config
- v1.0.4（2026-02）：timestamp on updates
- 2025-09：Graph memory + Kuzu backend

## 整合廣度

- 13 個 agent framework integration
- Voice agents：ElevenLabs、LiveKit、Pipecat
- 強調平台廣度而非單一框架對戰
