# Sources — 最新 Agentic AI 技術細節與實現方式

研究時間：2026-04-24
研究方法：橫縱分析法（hv-analysis skill），三路並行子 agent 收集（縱向時間線 / 橫向框架對比 / 技術實現深潛）

---

## 學術論文（arXiv）

| 論文 | URL | 用於 |
|------|-----|------|
| ReAct (Yao et al., 2022) | https://arxiv.org/abs/2210.03629 | 縱向 2022、技術 §3.7.1 |
| Chain-of-Thought (Wei et al., 2022) | https://arxiv.org/abs/2201.11903 | 縱向 2022 前置條件 |
| Toolformer (Schick et al., 2023) | https://arxiv.org/abs/2302.04761 | 縱向 2023 |
| Reflexion (Shinn et al., 2023) | https://arxiv.org/abs/2303.11366 | 縱向 2023、技術 §3.7.1 |
| HuggingGPT (Shen et al., 2023) | https://arxiv.org/abs/2303.17580 | 縱向 2023 |
| Tree of Thoughts (Yao et al., 2023) | https://arxiv.org/abs/2305.10601 | 縱向 2023、技術 §3.7.1 |
| Voyager (Wang et al., 2023) | https://arxiv.org/abs/2305.16291 | 縱向 2023 |
| MetaGPT (Hong et al., 2023) | https://arxiv.org/abs/2308.00352 | 縱向 2023、交匯 §4.2 |
| AutoGen (Wu et al., 2023) | https://arxiv.org/abs/2308.08155 | 縱向 2023、橫向 |
| MemGPT (Packer et al., 2023) | https://arxiv.org/abs/2310.08560 | 技術 §3.7.3 |
| SWE-bench (Jimenez et al., 2023) | https://arxiv.org/abs/2310.06770 | 縱向 2024、技術 §3.7.6 |
| LATS (Zhou et al., 2023) | https://arxiv.org/abs/2310.04406 | 技術 §3.7.1 |
| Agentic Misalignment (Anthropic, 2025) | https://arxiv.org/abs/2510.05179 | 技術 §3.7.7、交匯 §4.5 |
| Agentic Reasoning Survey (2026) | https://arxiv.org/abs/2601.12538 | 技術 §3.7.1 |

## Anthropic 官方

- MCP Announcement: https://www.anthropic.com/news/model-context-protocol
- MCP 捐給 AAIF: https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
- Claude 3.5 Sonnet: https://www.anthropic.com/news/claude-3-5-sonnet
- Claude SWE-bench: https://www.anthropic.com/research/swe-bench-sonnet
- Computer Use: https://www.anthropic.com/news/3-5-models-and-computer-use
- Claude Sonnet 4.5: https://www.anthropic.com/news/claude-sonnet-4-5
- Claude Code Subagents: https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously
- Claude Agent SDK blog: https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk
- Context Management: https://www.anthropic.com/news/context-management
- Context Engineering: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Agentic Misalignment Research: https://www.anthropic.com/research/agentic-misalignment
- Extended Thinking Docs: https://platform.claude.com/docs/en/build-with-claude/extended-thinking
- Compaction Docs: https://platform.claude.com/docs/en/build-with-claude/compaction
- Tool Use Overview: https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview

## OpenAI 官方

- Function Calling: https://openai.com/index/function-calling-and-other-api-updates/
- Agents SDK 文件: https://openai.github.io/openai-agents-python/
- Agents SDK GitHub: https://github.com/openai/openai-agents-python
- Agents SDK Launch: https://openai.com/index/new-tools-for-building-agents/
- Swarm: https://github.com/openai/swarm
- SWE-bench Verified: https://openai.com/index/introducing-swe-bench-verified/
- Deep Research: https://openai.com/index/introducing-deep-research/
- Computer Use API: https://developers.openai.com/api/docs/guides/tools-computer-use
- InstructGPT: https://openai.com/index/instruction-following/

## Google / DeepMind

- ADK + A2A: https://developers.googleblog.com/agents-adk-agent-engine-a2a-enhancements-google-io/
- ADK TypeScript: https://developers.googleblog.com/introducing-agent-development-kit-for-typescript-build-ai-agents-with-the-power-of-a-code-first-approach/
- A2A 發佈: https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/
- A2A v0.3: https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade
- ADK 文件: https://google.github.io/adk-docs
- Gemini Deep Research Max: https://venturebeat.com/technology/googles-new-deep-research-and-deep-research-max-agents-can-search-the-web-and-your-private-data

## Microsoft

- AutoGen Research Blog: https://www.microsoft.com/en-us/research/blog/autogen-enabling-next-generation-large-language-model-applications/
- AutoGen 0.4 Launch: https://devblogs.microsoft.com/autogen/autogen-reimagined-launching-autogen-0-4/
- Microsoft Agent Framework 1.0: https://visualstudiomagazine.com/articles/2026/04/06/microsoft-ships-production-ready-agent-framework-1-0-for-net-and-python.aspx
- Agent Framework 文件: https://learn.microsoft.com/en-us/agent-framework/overview/

## MCP 與 A2A 協議

- MCP Wikipedia: https://en.wikipedia.org/wiki/Model_Context_Protocol
- MCP Python SDK: https://github.com/modelcontextprotocol/python-sdk
- MCP Transport Spec: https://modelcontextprotocol.io/specification/2025-06-18/basic/transports
- MCP 一週年: https://blog.modelcontextprotocol.io/posts/2025-11-25-first-mcp-anniversary/
- Resources 概念: https://modelcontextprotocol.info/docs/concepts/resources/
- A2A GitHub: https://github.com/a2aproject/A2A

## 框架 / SDK

- LangGraph: https://github.com/langchain-ai/langgraph, https://www.langchain.com/langgraph
- LangChain Plan-and-Execute: https://blog.langchain.com/planning-agents/
- CrewAI: https://github.com/crewAIInc/crewAI
- CrewAI Stars Analysis: https://theagenttimes.com/articles/44335-stars-and-counting-crewais-github-surge-maps-the-rise-of-the-multi-agent-e
- AutoGen GitHub: https://github.com/microsoft/autogen
- LlamaIndex Multi-Agent: https://developers.llamaindex.ai/python/framework/understanding/agent/multi_agent/
- Dify: https://github.com/langgenius/dify
- n8n: https://github.com/n8n-io/n8n
- n8n AI Agent: https://docs.n8n.io/advanced-ai/
- Flowise Review: https://aiagentslist.com/agents/flowise

## 第三方分析

- Why MCP Won (Latent.Space): https://www.latent.space/p/why-mcp-won
- Why MCP Won (The New Stack): https://thenewstack.io/why-the-model-context-protocol-won/
- MCP vs Function Calling: https://www.descope.com/blog/post/mcp-vs-function-calling
- MCP vs Function Calling vs OpenAPI: https://www.marktechpost.com/2025/10/08/model-context-protocol-mcp-vs-function-calling-vs-openapi-tools-when-to-use-each/
- AutoGen 分裂史: https://www.gettingstarted.ai/autogen-vs-ag2/
- 2026 AI Agent Showdown: https://topuzas.medium.com/the-great-ai-agent-showdown-of-2026-openai-autogen-crewai-or-langgraph-7b27a176b2a1
- LangGraph vs CrewAI vs AutoGen: https://medium.com/data-science-collective/langgraph-vs-crewai-vs-autogen-which-agent-framework-should-you-actually-use-in-2026-b8b2c84f1229
- Claude Code Prompt Caching: https://www.claudecodecamp.com/p/how-prompt-caching-actually-works-in-claude-code
- Sandbox 技術對比: https://manveerc.substack.com/p/ai-agent-sandboxing-guide
- Benchmark Exploit 分析: https://moogician.github.io/blog/2026/trustworthy-benchmarks-cont/
- Langfuse Framework Comparison: https://langfuse.com/blog/2025-03-19-ai-agent-comparison
- Context Management 痛點: https://www.mindstudio.ai/blog/context-management-ai-agents
- Simon Willison on Function Calling: https://simonwillison.net/2023/Jun/13/function-calling/

## 新聞與背景

- AutoGPT Wikipedia: https://en.wikipedia.org/wiki/AutoGPT
- AutoGPT Limitations: https://autogpt.net/auto-gpt-understanding-its-constraints-and-limitations/
- BabyAGI GitHub: https://github.com/yoheinakajima/babyagi
- BabyAGI 作者 blog: https://yoheinakajima.com/birth-of-babyagi/
- Cognition Devin: https://cognition.ai/blog/introducing-devin
- Windsurf History: https://awesomeagents.ai/reviews/review-windsurf/
- Cursor: https://cursor.com/
- OpenAI DevDay 2023: https://techcrunch.com/2023/11/06/openai-launches-api-that-lets-developers-build-assistants-into-their-apps/
- Perplexity Deep Research: https://techcrunch.com/2025/02/15/perplexity-launches-its-own-freemium-deep-research-product/
- Claude Opus 4.7 Field Report: https://dev.to/kai_outputs/claude-opus-47-field-report-eight-hours-of-autonomous-work-10e3
- A2A 採用度質疑: https://blog.fka.dev/blog/2025-09-11-what-happened-to-googles-a2a/
- Agents SDK Sandboxing 更新: https://devops.com/openai-upgrades-its-agents-sdk-with-sandboxing-and-a-new-model-harness/

---

訪問日期：2026-04-24
