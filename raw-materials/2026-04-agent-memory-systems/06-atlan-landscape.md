# Atlan — 2026 Agent Memory Frameworks Landscape

**來源**：https://atlan.com/know/best-ai-agent-memory-frameworks-2026/
**訪問日期**：2026-04-29

## 整體框架

三類記憶 scope（episodic / semantic / procedural）已成標準。
兩種 delivery：managed cloud + self-hosted open source。
Independent benchmarks: 「15-point accuracy differences between architectures on temporal retrieval tasks」。

## 框架逐一（最重要的對照表）

### Mem0
- **定位**：Largest community standalone memory tool；managed drop-in API for personalization
- **強**：self-editing memory（自動去重）；~48K stars；SOC 2 Type II
- **弱**：Graph memory 鎖在 Pro tier；無 temporal fact modeling；**LongMemEval 49.0%（GPT-4o），比 Zep 低 15 點**
- **場景**：consumer chatbot、B2B copilot 的 user preference persistence

### Zep / Graphiti
- **定位**：Temporal knowledge graph 引擎；agents 推理 fact 隨時間變化
- **強**：「Stores facts as nodes with validity windows」；P95 retrieval ~300ms；query 時不需 LLM call
- **弱**：社群比 Mem0 小；enterprise 訂價不透明；無 constitutional governance
- **場景**：long-running agents 追 customer behavior / metrics / business relationship 演變
- **Benchmark**：LongMemEval 63.8%（GPT-4o）— 本對照中最高

### Letta（MemGPT）
- **定位**：OS-inspired tiered memory；agents 是主動記憶管理者，非被動接收
- **強**：「Agents decide what to keep close, what to archive」；free self-hosted tier 全功能；原生多 agent 協作
- **弱**：非 drop-in 元件，需採完整 agent runtime；社群比 Mem0 / LangChain 小；訂價不透明
- **場景**：複雜 long-running agents 需 fine-grained 控制 memory tier（core / archival / recall）
- **Benchmark**：無獨立 benchmark 公開

### LangChain / LangMem
- **定位**：LangChain 生態的 modular memory sub-package
- **強**：procedural memory（agent 自更新 system instruction）；pluggable storage；~100K stars 生態
- **弱**：與 LangChain/LangGraph 緊耦合；無 managed hosting；版本 API churn；無 temporal reasoning
- **場景**：已在 LangGraph 上的團隊
- **Benchmark**：無

### Cognee
- **定位**：Local-first poly-store graph memory；隱私關鍵 deployment
- **強**：「最簡 onboarding：`.add()`, `.cognify()`, `.search()` 6 行起步」；Ollama 全離線；graph DB 可換
- **弱**：~7K stars；Time Awareness 較新；無 managed hosting；無合規認證
- **場景**：Air-gapped、GDPR 嚴格、data residency
- **Benchmark**：無

### Supermemory
- **定位**：MCP-native memory API；直接整合 Claude Code / OpenCode
- **強**：「explicit forgetting mechanism」；自報跨 LongMemEval / LoCoMo / ConvoMem 領先
- **弱**：自報數字無第三方驗證；產品年輕；合規未確立
- **場景**：coding agent 工作流跨 session 持久化
- **Benchmark**：自報

## 共同盲點：企業治理缺口

8 大框架共同短板：
- 無 business glossary integration
- 無 data lineage tracking
- 無 governance policy enforcement
- 無 entity resolution across operational systems

Memory 以 string / embedding 儲存，斷開 authoritative data definition / 法規合規 / cross-platform identity。
企業需在這些框架之上再加一層 governance infra 才能滿足 audit / compliance。
