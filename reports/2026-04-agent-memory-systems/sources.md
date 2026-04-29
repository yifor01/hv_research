# Agent 長期記憶系統 — 引用清單

訪問日期：2026-04-29（v2 新增來源同日訪問）

## v2 新增：Model Provider 官方資源

| 來源 | URL | 用途 |
|---|---|---|
| Anthropic Memory tool | https://docs.claude.com/en/docs/build-with-claude/tool-use/memory-tool | §2.7 主要參考 |
| Anthropic Prompt Caching | https://docs.claude.com/en/docs/build-with-claude/prompt-caching | §2.6 cache 機制 |
| Anthropic Files API | https://docs.claude.com/en/docs/build-with-claude/files | §2.7 持久檔案系統 |
| Claude Skills（Agent Skills）| https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview | §2.7 capability primitive |
| Anthropic 1M Context Window | https://docs.claude.com/en/docs/build-with-claude/context-windows | §2.6 1M tokens |
| OpenAI Memory | https://openai.com/index/memory-and-new-controls-for-chatgpt/ | §2.8 ChatGPT Memory |
| OpenAI Responses API | https://platform.openai.com/docs/api-reference/responses | §2.8 stateful threads |
| Google Gemini Long Context | https://ai.google.dev/gemini-api/docs/long-context | §2.6 1M tokens |
| Google Context Caching | https://ai.google.dev/gemini-api/docs/caching | §2.6 cache |
| LangChain LangMem | https://github.com/langchain-ai/langmem | §2.9 三類記憶 modular |
| Qwen2.5-1M | https://qwenlm.github.io/blog/qwen2.5-1m/ | §2.6 開源 1M 雛形 |
| GLM-4-1M | https://github.com/THUDM/LongAlign | §2.6 開源 1M 雛形 |

## Karpathy 一手來源

| 來源 | URL | 用途 |
|---|---|---|
| LLM Wiki gist | https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f | §2.5 主要原文 |
| System Prompt Learning 推文 | https://x.com/karpathy/status/1921368644069765486 | §5.2 範式提案 |
| AGI is still a decade away（Simon Willison 整理）| https://simonwillison.net/2025/Oct/18/agi-is-still-a-decade-away/ | §1.2 Decade of Agents |
| Software 3.0（Latent.space S3）| https://www.latent.space/p/s3 | 背景框架 |
| autoresearch | https://github.com/karpathy/autoresearch | §9.8 應用雛形 |

## 框架官方資源

| 框架 | URL |
|---|---|
| Mem0 — State of AI Agent Memory 2026 | https://mem0.ai/blog/state-of-ai-agent-memory-2026 |
| Letta forum 對比 | https://forum.letta.com/t/agent-memory-letta-vs-mem0-vs-zep-vs-cognee/88 |
| Letta docs | https://docs.letta.com/concepts/letta |
| Letta GitHub | https://github.com/letta-ai/letta |
| Zep Knowledge Graph | https://www.getzep.com/product/knowledge-graph |
| Graphiti GitHub | https://github.com/getzep/graphiti |
| MemPalace 介紹 | https://recca0120.github.io/en/2026/04/08/mempalace-ai-memory-system/ |
| MemPalace GitHub | https://github.com/milla-jovovich/mempalace |

## 第三方對比

| 來源 | URL |
|---|---|
| Atlan — Best AI Agent Memory Frameworks 2026 | https://atlan.com/know/best-ai-agent-memory-frameworks-2026/ |
| Top 6 AI Agent Memory Frameworks（DEV.to）| https://dev.to/nebulagg/top-6-ai-agent-memory-frameworks-for-devs-2026-1fef |
| 5 AI Agent Memory Systems Compared（DEV.to）| https://dev.to/varun_pratapbhardwaj_b13/5-ai-agent-memory-systems-compared-mem0-zep-letta-supermemory-superlocalmemory-2026-benchmark-59p3 |
| Survey of AI Agent Memory Frameworks（Graphlit）| https://www.graphlit.com/blog/survey-of-ai-agent-memory-frameworks |
| Comparison of AI Agent Memory Systems 2026（n1n.ai）| https://explore.n1n.ai/blog/ai-agent-memory-comparison-2026-mem0-zep-letta-cognee-2026-04-23 |

## 學術論文 / 文獻

| 論文 / 資源 | URL |
|---|---|
| MemGPT 原 paper | https://arxiv.org/abs/2310.08560 |
| Mem0 LOCOMO（ECAI 2025）| https://arxiv.org/abs/2504.19413 |
| ICLR 2026 MemAgents Workshop Proposal | https://openreview.net/pdf?id=U51WxL382H |
| Spatial Metaphors for LLM Memory（MemPalace 批評）| https://arxiv.org/abs/2604.21284 |
| Memory Mechanisms in LLM Agents（emergentmind 整理）| https://www.emergentmind.com/topics/memory-mechanisms-in-llm-based-agents |
| Agent-Memory-Paper-List | https://github.com/Shichun-Liu/Agent-Memory-Paper-List |
| Awesome-Memory-for-Agents | https://github.com/TsinghuaC3I/Awesome-Memory-for-Agents |

## 批評 / 修訂 / 衍生

| 來源 | URL |
|---|---|
| MemPalace Review（Nicholas Rhodes）| https://nicholasrhodes.substack.com/p/mempalace-ai-memory-review-benchmarks |
| I Over-Engineered Karpathy's Agent Memory（DEV.to）| https://dev.to/awrshift/i-over-engineered-karpathys-agent-memory-heres-what-actually-works-4imk |
| LLM Wiki v2（rohitg00）| https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2 |
| Andrej Karpathy's LLM Wiki（Mehul Gupta）| https://medium.com/data-science-in-your-pocket/andrej-karpathys-llm-knowledge-bases-explained-2d9fd3435707 |

## Karpathy 概念解讀（Cognitive Core / Memory Wiki）

| 來源 | URL |
|---|---|
| Karpathy is Talking About Cognitive Core（Memco）| https://www.memco.ai/blog/karpathy-cognitive-core-memory |
| Why Karpathy is Right: RAG is Dead（Epsilla）| https://www.epsilla.com/blogs/karpathy-agentic-wiki-beyond-rag-enterprise-memory |
| Beyond RAG（Level Up Coding）| https://levelup.gitconnected.com/beyond-rag-how-andrej-karpathys-llm-wiki-pattern-builds-knowledge-that-actually-compounds-31a08528665e |
| The LLM Wiki: How Karpathy's AI Memory Idea Sparked a Movement（TecAdRise）| https://tecadrise.ai/blog/llm-wiki-karpathy-ai-knowledge-management-2026 |
| Compiler Analogy for AI Memory（MindStudio）| https://www.mindstudio.ai/blog/karpathy-llm-knowledge-base-compiler-analogy |
| MemPalace: 170 Tokens to Recall Everything（DEV.to）| https://dev.to/recca0120/mempalace-170-tokens-to-recall-everything-a-long-term-memory-system-for-ai-agents-2855 |

## 產業實踐

| 來源 | URL |
|---|---|
| LinkedIn Cognitive Memory Agent（ZenML）| https://www.zenml.io/llmops-database/cognitive-memory-agent-building-stateful-ai-agents-with-multi-layer-memory-architecture |
| Karpathy LLM Knowledge Base 報導（VentureBeat）| https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an |
| MemPalace 22K stars in 48 hours（Medium）| https://medium.com/@creativeaininja/mempalace-the-viral-ai-memory-system-that-got-22k-stars-in-48-hours-an-honest-look-and-setup-26c234b0a27b |

## 報告內部參考

- 同 repo `reports/2026-04-claude-code/` — 接續 §9.3 AI Coding Agent 跨 session 記憶
- 同 repo `reports/2026-04-agentic-ai-tech/` — 補充 agent 廣義架構
- 同 repo `templates/` — 後續若做框架評分可復用 PI 盡調 5 維度模板
