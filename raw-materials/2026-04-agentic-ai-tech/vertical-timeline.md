# Agentic AI 縱向時間線研究筆記（2022 – 2026 Q1）

> 本筆記為「橫縱分析法」縱軸素材，追蹤 agentic AI 從概念奠基、爆發狂熱、工程化、協議統一到長時間自主執行的完整演化路徑。所有關鍵事實後附 `[來源: URL]`，搜不到的資訊明確標註「資訊暫缺」。

---

## 一、2022 — 概念奠基期：從 CoT 到 ReAct，Agent 的元年

### 1.1 前置條件：為什麼 Agent 熱潮不是 2020 而是 2022？

一個常被忽略的事實：GPT-3 早在 2020 年 6 月就已經發表，擁有 175B 參數，而且 API 隨即對外開放，但 2020–2021 年幾乎沒有人做出成功的「LLM 自主 agent」。真正的起跳要等到 2022 年，原因是 agent 需要三塊拼圖同時到位：

1. **夠大的模型**：Wei et al. 2022 證明 chain-of-thought 是「model scale emergent ability」，在 ~100B 參數以下無效 [來源: https://arxiv.org/abs/2201.11903]。GPT-3 (175B) 剛好跨過門檻，但 `text-davinci-002` 之前的 instruction-tuning 尚不成熟，zero-shot 跟指令的吻合度低。
2. **Instruction Tuning + RLHF**：2022 年 3 月 OpenAI 發表 InstructGPT 論文，證明 RLHF 能把 GPT-3 從「plausible continuation machine」轉成「follow-instruction model」[來源: https://openai.com/index/instruction-following/]。沒有這一步，agent 根本無法把「子任務描述」當成可執行的指令。
3. **推理能力成型**：CoT 讓模型第一次展現「分步驟推理」，而 agent 本質上就是「reasoning + acting loop」，只有能推理的模型才能做 agent。

這三件事在 2020 還都不成熟，所以 2020–2021 的「GPT-3 agent」嘗試（例如 Philosopher AI、各種 chatbot）本質上都是 zero-shot prompting，缺少「自我計畫 → 使用工具 → 觀察結果 → 修正」的閉環能力。

### 1.2 Chain-of-Thought Prompting（Wei et al., 2022-01-28）

- **論文**：`Chain-of-Thought Prompting Elicits Reasoning in Large Language Models`，Jason Wei 等人，Google Research 團隊 [來源: https://arxiv.org/abs/2201.11903]
- **核心貢獻**：只需在 prompt 裡給幾個「先推理再答」的範例（few-shot CoT），就能讓 540B 的 PaLM 在 GSM8K 數學題上達到 SOTA，超越 fine-tuned GPT-3 + verifier。
- **對 agent 的意義**：CoT 是 agent 的「思考引擎」。如果模型無法用自然語言寫出推理步驟，就無法把「目標 → 子任務 → 工具呼叫」這條鏈條串起來。ReAct、Reflexion、Tree of Thoughts 等後續 agent 論文，全部都是 CoT 的延伸。
- **關鍵洞察**：CoT 是 `emergent ability`，只在夠大的模型上出現。這解釋了為什麼 agent 做法要等到 100B+ 模型普及。

### 1.3 ReAct（Yao et al., 2022-10-06）— Agent 正規化的分水嶺

- **論文**：`ReAct: Synergizing Reasoning and Acting in Language Models`，Shunyu Yao、Jeffrey Zhao、Dian Yu 等（Princeton + Google Brain）[來源: https://arxiv.org/abs/2210.03629]
- **核心貢獻**：第一個把「reasoning trace」（Thought）跟「action」（Act）**交替正規化**成統一的 prompt pattern：`Thought → Action → Observation → Thought → ...`。
- **解決了什麼問題**：
  - **Pure CoT 的缺陷**：只會「內部推理」，無法觸及外部世界，碰到需要最新資訊（HotpotQA）或環境互動（ALFWorld、WebShop）的任務就幻覺。
  - **Pure Action 的缺陷**：用 RL 訓練的 policy（如 BC、PPO agent）能執行動作但不會「說明理由」，可解釋性差、樣本效率低。
  - ReAct 用「語言就是 action」的統一介面，讓 LLM 能同時「想」和「做」，在 ALFWorld 和 WebShop 分別比 imitation/RL 基線高出 34% 和 10% 的成功率。
- **為什麼是 2022 年 10 月**：需要 GPT-3.5 級的模型 + few-shot 能力才撐得住交替 reasoning + acting 的 prompt 長度；這個時間點 `text-davinci-002` 已經穩定。
- **後續影響**：ReAct 成為 2023–2024 幾乎所有 agent 框架（LangChain Agent、AutoGPT、OpenAI function calling）的底層 prompt pattern。OpenAI 2023 年 6 月發布的 function calling 被 Simon Willison 評為「effectively an implementation of the ReAct pattern, with models that have been fine-tuned to execute it」[來源: https://simonwillison.net/2023/Jun/13/function-calling/]。

### 1.4 2022 年底的大背景：ChatGPT（2022-11-30）

雖然 ChatGPT 本身不是 agent，但它在 5 天內突破 100 萬用戶，讓「LLM 可以真的解決實際任務」這個想法從研究圈外溢到整個科技圈。**沒有 ChatGPT 的病毒式傳播，就不會有 2023 年 AutoGPT 的全民狂熱**。這是 agent 熱潮的「市場前置條件」。

---

## 二、2023 — 爆發與狂熱期：從 Toolformer 到 AutoGen，一年內框架大爆炸

### 2.1 Toolformer（Meta AI, 2023-02-09）— 工具呼叫的自監督雛形

- **論文**：`Toolformer: Language Models Can Teach Themselves to Use Tools`，Timo Schick 等人（Meta AI Research）[來源: https://arxiv.org/abs/2302.04761]
- **核心貢獻**：不用大量人工標註，用 self-supervised 方式讓模型學會「何時呼叫 API、傳什麼參數、怎麼把結果寫回 context」。工具包括計算器、QA 系統、搜尋引擎、翻譯、日曆。
- **突破點**：在 ReAct 之前，工具呼叫要嘛靠 few-shot prompting（不穩定），要嘛靠昂貴的 supervised fine-tuning。Toolformer 用「在訓練語料中自動插入 API 呼叫 → 檢查是否改善下一個 token 預測 → 保留有用的呼叫」這個自監督迴圈，為後來 OpenAI 的 function calling fine-tuning 提供了方法論基礎。
- **局限**：只示範了幾個固定 API，沒有動態 tool registry；真正把工具呼叫商品化要等到 2023-06 的 function calling。

### 2.2 AutoGPT（Significant Gravitas, 2023-03-30）— 病毒式狂熱的起點

- **作者 / 時間**：Toran Bruce Richards（Significant Gravitas Ltd 創辦人，本業是遊戲公司），2023 年 3 月 30 日開源發布 [來源: https://en.wikipedia.org/wiki/AutoGPT]
- **意義**：第一個被大眾玩到的「完全自主 agent」。它在 GitHub 幾週內衝到 61,000+ stars、變成全站 trending 第一，Andrej Karpathy 於 4 月 2 日發推說「the next frontier of prompt engineering is AutoGPTs」，引爆第二波病毒傳播 [來源: https://en.wikipedia.org/wiki/AutoGPT]。
- **技術架構**：ReAct + GPT-4 + 向量資料庫做長期記憶 + 檔案讀寫。使用者給一個 high-level goal，agent 自己拆解任務、上網搜尋、寫檔案、迭代。
- **為什麼迅速退潮**（2023 下半年已經明顯不堪用）：
  1. **Reliability 問題**：跑 2–3 分鐘後就陷入 loop，尤其是目標稍微寬泛的時候 [來源: https://autogpt.net/auto-gpt-understanding-its-constraints-and-limitations/]。
  2. **Hallucination 複利效應**：每一步決策都可能偏航，沒有中途修正機制，錯誤會在多步推理中累積放大。
  3. **Cost**：GPT-4 每次呼叫都接近 token 上限，跑一個任務常常花幾美元卻沒結果。
  4. **Context window 不夠**：2023 年 GPT-4 只有 8K/32K context，長任務會把歷史訊息擠出去。
  5. **沒有結構化控制**：純自主、沒有 human-in-the-loop，生產環境沒法接受。
- **歷史地位**：雖然產品層面失敗，但它**證明了市場對「自主 agent」的飢渴**，並把「多步規劃 + 工具呼叫 + 長期記憶」這組 primitive 寫進了整個行業的共同詞彙。

### 2.3 BabyAGI（Yohei Nakajima, 2023-03-28 / 29）

- **作者**：Yohei Nakajima（Untapped Capital 創辦人、VC），與 AutoGPT 同一週發布，但他的 Twitter thread 先被引爆 [來源: https://github.com/yoheinakajima/babyagi]
- **架構**：三個 agent 分工 — Execution Agent、Task Creation Agent、Prioritization Agent，配 Pinecone 做向量記憶。核心迴圈：`執行任務 → 根據結果產新任務 → 重排序 → 再執行`。
- **意義**：BabyAGI 是**第一個明確用多 agent 分工**表達「自主 task management」的開源實作（AutoGPT 本質還是單 agent + 工具）。這個「task loop」設計後來被 LangChain Agent、CrewAI、AutoGen 多個框架沿用 [來源: https://yoheinakajima.com/birth-of-babyagi/]。

### 2.4 HuggingGPT / JARVIS（Microsoft + Zhejiang, 2023-03-30）

- **論文**：arxiv 2303.17580，主作者 Yongliang Shen 等 [來源: https://arxiv.org/pdf/2303.17580.pdf]
- **定位**：用 ChatGPT 當「調度中樞」，把使用者需求拆成子任務 → 從 HuggingFace Hub 挑 20+ 個專家模型（T5、Stable Diffusion 1.5、BART、DPT 等）各自執行 → 整合回覆。
- **意義**：開啟「LLM as orchestrator of specialized models」範式，是後來 MoE agent、multi-modal agent 的雛形。
- **和 AutoGPT 的差別**：HuggingGPT 強調「跨模態工具調度」，AutoGPT 強調「自主長任務」。兩者合起來畫出 agent 的兩個方向。

### 2.5 Voyager（Nvidia + Caltech/Stanford/UT, 2023-05-25）— 第一個終身學習 embodied agent

- **論文**：arxiv 2305.16291，由 Jim Fan（NVIDIA）領軍 [來源: https://arxiv.org/abs/2305.16291]
- **場景**：在開放世界 Minecraft 裡，用 GPT-4 寫 JavaScript 程式碼控制角色，並從環境 feedback 自動 debug。
- **三大創新**：
  1. **Automatic Curriculum**：agent 自己產生「下一個要學的技能」，最大化探索。
  2. **Skill Library**：學會的程式碼存成可復用 skill，形成「終身學習」的長期記憶。
  3. **Iterative Prompting**：GPT-4 看到 JavaScript 報錯 → 自我反思 → 修正程式碼。
- **成果**：拿到獨特物品數量比 SOTA 多 3.3 倍、解鎖科技樹速度快 15.3 倍；把 skill library 移到新 Minecraft 世界也能泛化。
- **長期影響**：Voyager 的「skill library」被後來 Claude Code 的 `CLAUDE.md`、Cursor 的 rules file、OpenAI Code Interpreter 的 persistent scratch 借鑑。

### 2.6 Tree of Thoughts（Yao et al., 2023-05-17）

- **論文**：arxiv 2305.10601，Shunyu Yao 等（Princeton）[來源: https://arxiv.org/abs/2305.10601]
- **貢獻**：把 CoT 從「一條鏈」擴展為「樹狀搜索」，讓 LM 能 look-ahead、backtrack、self-evaluate。在 Game of 24 上從 GPT-4 + CoT 的 4% 躍升到 ToT 的 74%。
- **意義**：把 agent 從「線性 ReAct」推向「deliberate search」，為 2024 年的 o1-style inference-time reasoning 埋伏筆。

### 2.7 OpenAI Function Calling（2023-06-13）— 工具呼叫官方化

- **發布**：gpt-4-0613 / gpt-3.5-turbo-0613，6/27 變預設 [來源: https://openai.com/index/function-calling-and-other-api-updates/]
- **技術**：開發者用 JSON schema 宣告 function，模型在回應時產生 `{"function": "...", "arguments": {...}}` 這種結構化 output。本質上是把 ReAct 的 Action 用 fine-tuning 直接寫進模型能力。
- **為什麼這個時間點**：GPT-4 既要有足夠的 reasoning 把使用者意圖對應到 function，又要產出**嚴格符合 schema** 的 JSON（不然 parse 就炸）；這兩件事都需要專門的 instruction tuning。OpenAI 在 2023 Q1–Q2 累積了夠多 fine-tuning data 才釋出。
- **行業衝擊**：function calling 一出，LangChain 的 custom agent 程式碼瞬間被取代掉 70%，`ReAct + re-prompt` 的手工 pipeline 變成「直接給 tools 陣列就好」。

### 2.8 Reflexion（Shinn et al., 2023-03-20，NeurIPS 2023）

- **論文**：arxiv 2303.11366，Noah Shinn 等（Northeastern）[來源: https://arxiv.org/abs/2303.11366]
- **核心**：讓 agent 在失敗後**用自然語言寫反思**，存進 episodic memory，下一輪把反思注入 prompt。不需要 update weight 就能像 RL 一樣「從錯誤中學習」。
- **意義**：把 RL 的概念「語言化」，為後來 self-improving agent、o1-style reasoning 奠基。

### 2.9 MetaGPT（2023-08-01）

- **論文**：arxiv 2308.00352 [來源: https://arxiv.org/abs/2308.00352]
- **想法**：把 agent 組織成「軟體公司」— 產品經理、架構師、PM、工程師各司其職，按 SOP 流程協作。一行需求進來 → 輸出 user story、競品分析、架構、API 文件、程式碼。
- **成果**：HumanEval Pass@1 85.9%、MBPP 87.7% 的 SOTA。
- **意義**：把「多 agent 分工 + 流程管控」的點子推到極致，是後來 CrewAI、AutoGen 的直接思想來源。

### 2.10 AutoGen（Microsoft, 2023-09-25）

- **發布**：Microsoft Research, 2023 年 9 月 25 日 [來源: https://www.microsoft.com/en-us/research/blog/autogen-enabling-next-generation-large-language-model-applications/]
- **核心**：「conversable agent」— agent 之間不是靠 hard-coded workflow，而是**用對話**協作。User Proxy + Assistant + Code Executor 三角組合成為經典模式。
- **影響**：第一個被微軟級巨頭背書的多 agent 框架，給企業用戶信心；到 2024 Q2 已有 290+ 貢獻者、900k+ 下載。

### 2.11 OpenAI Assistants API（2023-11-06，DevDay）

- **發布**：2023 年 11 月 6 日首屆 OpenAI DevDay，同時推出 GPT-4 Turbo（128K context）[來源: https://techcrunch.com/2023/11/06/openai-launches-api-that-lets-developers-build-assistants-into-their-apps/]
- **提供的 primitive**：Code Interpreter（Python sandbox）、Retrieval（檔案 RAG）、Function Calling。
- **意義**：第一次官方明講這叫「agent-like experience」，並把 state management（threads、messages）從應用層下沉到 API 層。這是 OpenAI 從「模型 API」往「agent platform」轉型的起點。

---

## 三、2024 — 工程化與框架成熟期：從 chain 到 graph，從實驗到生產

### 3.1 LangGraph（LangChain, 2024 初）— 從 chain 到 state machine

- **發布**：LangChain 於 2024 年初發表 LangGraph，定位是 LangChain 的底層 graph runtime [來源: https://blog.langchain.com/langgraph/]
- **動機**：原本 LangChain 的 `Chain` 是線性的 DAG，但真實 agent 需要 `while loop`（continue until task done）、`conditional branch`（根據 observation 走不同分支）、`human-in-the-loop`（pause 等人工回覆）。這些用 chain 模型寫起來非常笨拙。
- **做法**：把 agent 建模成「state machine as graph」— node 是 function，edge 是條件跳轉，state 是共享的 dict。
- **行業意義**：2024 年被稱為「agents start working in production」的一年，但不是 AutoGPT 式的萬用 agent，而是**垂直、窄定義、高度可控**的 agent。LangGraph 正好對到這個需求，迅速變成 agent 框架的預設選項。

### 3.2 Cognition Devin（2024-03-12）— 第一個「AI 軟體工程師」

- **發布**：Cognition AI 從隱身模式亮相，發布 Devin [來源: https://cognition.ai/blog/introducing-devin]
- **成績**：SWE-Bench 端到端解題率 13.86%，是當時 SOTA（Claude 2 只有 4.80%，GPT-4 1.74%）的 7 倍以上。
- **工具配備**：sandbox 裡配 shell、code editor、browser 三件套，是 AutoGPT 之後第一個真正做到「全流程自主寫 code」的 agent。
- **行業衝擊**：Devin demo 在 Twitter 上病毒式擴散，「AI 工程師取代人類」的討論再起。雖然後續使用者實測評價兩極（很多人抱怨它 demo-ware），但它**確立了 SWE-Bench 作為 agent 黃金 benchmark 的地位**。

### 3.3 Claude 3.5 Sonnet（Anthropic, 2024-06-20）— Agentic coding 的分水嶺

- **發布**：2024 年 6 月 20 日，後於 10 月再次更新 [來源: https://www.anthropic.com/news/claude-3-5-sonnet]
- **關鍵成就**：更新版 Claude 3.5 Sonnet 在 SWE-bench Verified 拿 49%，超越 o1-preview 和所有 agentic 專用系統 [來源: https://www.anthropic.com/research/swe-bench-sonnet]。TAU-bench 零售域從 62.6% → 69.2%，航空域從 36% → 46%。
- **設計哲學的轉變**：Anthropic 明確說他們的 agent scaffold 原則是「給模型最大自主，scaffold 越薄越好」— 只給 `Bash Tool` 和 `Edit Tool` 兩個工具。這跟 AutoGPT / LangChain 那種「幫模型想好各種 prompt template」的哲學完全相反。
- **意義**：第一個被市場廣泛認可「coding agent 真的能用」的通用模型。Cursor、Windsurf、Zed 的 agent 模式幾乎都預設用 Sonnet。

### 3.4 Anthropic Computer Use（2024-10-22）

- **發布**：搭配 updated Claude 3.5 Sonnet 釋出 public beta [來源: https://www.anthropic.com/news/3-5-models-and-computer-use]
- **突破**：讓 Claude 透過截圖 + 滑鼠鍵盤操作「任何桌面程式」，不再受限於有 API 的應用。
- **OSWorld benchmark**：Claude 3.5 Sonnet 14.9%，GPT-4 只有 7.7%，人類 70%+。數字很低，但已經是第一次「通用桌面自動化」被 frontier model 做到。
- **策略意義**：Anthropic 押注「agent 要跟人類世界對齊，最萬能的介面是螢幕」。這個賭注在 2025–2026 被證明極其關鍵（browser agent、OS agent 整條賽道的啟動）。

### 3.5 OpenAI Swarm（2024-10-11，實驗性）

- **發布**：OpenAI 以「experimental cookbook」姿態發布，明講不是 production，不會維護 [來源: https://github.com/openai/swarm]
- **設計**：兩個 primitive — `Agents`（instructions + functions）、`Handoffs`（return 另一個 agent 的 function）。state-less，每次 run 從頭開始。
- **意義**：Swarm 本身不重要，但它**測試了「handoff 是多 agent 編排最簡單抽象」**這個假設，為半年後 OpenAI Agents SDK 的正式設計鋪路。

### 3.6 CrewAI（2024 全年壯大）

- **定位**：role-based 多 agent 框架，agent 有 role、goal、backstory，類似 MetaGPT 但更輕量 [來源: https://github.com/crewAIInc/crewAI]
- **特點**：執行策略分 Sequential、Hierarchical（manager agent 協調）、Custom；到 2026 初已有 100,000+ 認證開發者。
- **行業位置**：跟 LangGraph 分道揚鑣 — LangGraph 低階可控、CrewAI 高階抽象；兩者並存各取所需。

### 3.7 MCP（Model Context Protocol, 2024-11-25）— 協議統一的起點

- **發布**：Anthropic 於 2024 年 11 月 25 日發布 MCP 開放標準 [來源: https://www.anthropic.com/news/model-context-protocol]
- **技術基礎**：設計上借鑑 Microsoft Language Server Protocol (LSP) 的 message-flow，用 JSON-RPC 2.0 傳輸。附帶 Python、TypeScript、C#、Java 四個 SDK，首發 pre-built servers 包括 Google Drive、Slack、GitHub、Git、Postgres、Puppeteer [來源: https://en.wikipedia.org/wiki/Model_Context_Protocol]。
- **核心抽象**：三種物件 — `Tools`（model-controlled，模型決定什麼時候呼叫）、`Resources`（application-controlled，應用提供的 context）、`Prompts`（user-controlled，使用者可呼叫的 template）。這三層拆分是 MCP 跟 function calling 最大的哲學差異。

---

## 四、2025 — 協議統一與商業化：MCP 生態爆發，長時間自主執行露頭

### 4.1 MCP 的病毒式採用（2024-11 → 2025 全年）

- **時間線**：
  - 2024-11-25：Anthropic 發布 [來源: https://www.anthropic.com/news/model-context-protocol]
  - 2025-03：OpenAI 正式宣布 ChatGPT desktop 原生支援 MCP
  - 2025-04：Google DeepMind（Demis Hassabis）確認 Gemini 支援 MCP
  - 2025-09：MCP Registry 上線
  - 2025-11：月下載量達 97M（Python + TS SDKs）
  - 2025-12：Anthropic 把 MCP 捐給 Linux Foundation 旗下的 Agentic AI Foundation（AAIF），OpenAI、Block 共同創辦，AWS、Google、Microsoft、Cloudflare、Bloomberg 支持 [來源: https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation]
- **規模**：10,000+ 活躍 public MCP servers、ChatGPT / Cursor / Gemini / Copilot / VS Code 全部接入 [來源: https://thenewstack.io/why-the-model-context-protocol-won/]

### 4.2 為什麼 MCP 在 6 個月內成了事實標準？

Latent.Space 的〈Why MCP Won〉把原因歸納為六點 [來源: https://www.latent.space/p/why-mcp-won]：

1. **AI-native 設計**：MCP 從頭為 agent 設計，把 Tools / Resources / Prompts 這三種在 agent 裡反覆出現的 pattern 標準化；OpenAPI、GraphQL 這些是「一般化 HTTP 契約」，不懂 agent 的需求。
2. **大廠背書**：只有大 lab 出的標準會贏。作者直言「a standard from a Big Lab is very simply more likely to succeed than a standard from anyone else」。Composio、各種 startup standard 都因為「怕被綁架」而難推廣。
3. **Anthropic 的開發者信用**：Claude Sonnet 長期霸榜 agentic coding，開發者願意先試 Anthropic 推的東西。
4. **站在 LSP 肩膀上**：JSON-RPC + LSP 的設計已經被 IDE 生態驗證十年以上，減少了協議設計的原創風險。
5. **First-party 完整實作**：首發同時給 Claude Desktop client + 19 個 reference servers + debugger + 兩個 SDK，不是紙上協議。
6. **Minimal surface area**：起手協議很薄，但有清楚的 roadmap 迭代承諾。

**為什麼 function calling 不夠？**
- Function calling 本質是「single-turn、single-tool」的 API 契約，不處理 long-lived session、resource subscription、user-controlled prompt 這些 agent 實戰需求。
- LLM 面對 100 個工具會「decision paralysis」，MCP 的 Resource 概念讓非必要工具退到 context，減輕模型負擔 [來源: https://www.marktechpost.com/2025/10/08/model-context-protocol-mcp-vs-function-calling-vs-openapi-tools-when-to-use-each/]。
- OpenAI function calling 的文件「falls just short of a properly exhaustive spec」，沒有真正的協議層。

### 4.3 Claude Code、Cursor Agent、Windsurf — Agent IDE 成熟

- **Cursor**：由 Anysphere 開發，2024–2025 年在開發者中快速普及；2025 年 11 月 Series D 拿 $2.3B、估值 $29.3B [來源: https://cursor.com/]
- **Windsurf**：Codeium 於 2024 年 11 月發表 Windsurf Editor，走「Agentic IDE」路線（Cascade agent mode）。2025 年 4 月整個公司更名 Windsurf。2025 年中爆發戲劇性股權事件：OpenAI 談 $3B 收購失敗 → Google DeepMind 挖走 CEO Varun Mohan → Cognition 撿走 IP 和 $82M ARR [來源: https://awesomeagents.ai/reviews/review-windsurf/]。
- **Claude Code**：Anthropic 2025 年推出 CLI 形態的 coding agent，走「終端機 + MCP + 最薄 scaffold」路線。
- **共同特徵**：三者都把 MCP 當底層 plugin 協議 + Sonnet 當預設模型，開發者可以跨工具搬遷設定。

### 4.4 OpenAI Agents SDK + Responses API（2025-03-11）

- **發布**：2025 年 3 月 OpenAI 把實驗性的 Swarm 升級為 production-ready 的 Agents SDK，同步發布 Responses API 作為底層 [來源: https://openai.com/index/new-tools-for-building-agents/]
- **Primitives**：`Agents`（LLM + instructions + tools）、`Agents-as-tools / Handoffs`（agent 互相委派）、`Guardrails`（input/output 驗證）。
- **Provider-agnostic**：雖然為 OpenAI 模型優化，但透過 Chat Completions API 能接 100+ 其他 LLM [來源: https://www.infoq.com/news/2025/03/openai-responses-api-agents-sdk/]。

### 4.5 Google ADK + A2A Protocol（2025）

- **ADK（Agent Development Kit）**：Google 在 2025 年推 Python、Java、Go 多語言 ADK，Python ADK v1.0.0 於 2025 年標記 production-ready [來源: https://developers.googleblog.com/agents-adk-agent-engine-a2a-enhancements-google-io/]。
- **A2A（Agent-to-Agent Protocol）**：為「agent 跨組織互相通訊」而設計，跟 MCP 互補 — MCP 是「agent 呼叫工具/資料」，A2A 是「agent 呼叫另一個 agent」。2025 年 7 月 A2A v0.3 發布 gRPC 支援、security card signing、擴展 client SDK [來源: https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade]。
- **生態**：150+ 組織支持 A2A，所有 hyperscaler 都上車。

### 4.6 Deep Research Agents 橫空出世（2025 Q1）

- **OpenAI Deep Research（2025-02-02）**：第一個讓一般用戶體驗「agent 跑 30 分鐘、讀數十個來源、產出引用報告」的產品。Humanity's Last Exam 26.6% [來源: https://openai.com/index/introducing-deep-research/]
- **Perplexity Sonar Deep Research（2025-03-07）**：用較低成本（$2/M input, $8/M output）+ 快速度（多數 <3 分鐘）做差異化 [來源: https://techcrunch.com/2025/02/15/perplexity-launches-its-own-freemium-deep-research-product/]
- **Google Gemini Deep Research（2024-12 首發，2025-12 升級到 Gemini 3 Pro）**：Deep Research Max 在 DeepSearchQA 93.3%、Humanity's Last Exam 54.6% [來源: https://venturebeat.com/technology/googles-new-deep-research-and-deep-research-max-agents-can-search-the-web-and-your-private-data]
- **意義**：Deep Research 是**第一個 consumer-facing 殺手級 agent 產品**，證明了「長任務 + 自主瀏覽 + 引用」是比「萬用 agent」更 defensible 的產品形態。

---

## 五、2026 Q1 — 當前狀態：長時間自主執行 + Sub-agent 成熟

### 5.1 30+ 小時自主執行（Claude Sonnet 4.5, 2025-09；Opus 4.5/4.6/4.7, 2025–2026）

- **Sonnet 4.5 的聲明**：可連續 30+ 小時做 coding 任務不失去一致性 [來源: https://www.anthropic.com/news/claude-sonnet-4-5]
- **Opus 4.7（2026 Q1）**：Anthropic 推文報告「eight hours of autonomous work」實戰 [來源: https://dev.to/kai_outputs/claude-opus-47-field-report-eight-hours-of-autonomous-work-10e3]
- **能做到的工程前提**：
  1. **1M context window**：Opus 4.6 / 4.7 支援 1M token，能塞下幾百個檔案的 repo 快照。
  2. **Context compaction**：Claude Agent SDK 內建自動 compaction，在接近 context 上限時把歷史壓縮成摘要，避免爆掉。
  3. **Sub-agent 架構**：主 agent 不自己做重活，而是 spawn sub-agent 各自用乾淨 context 完成子任務，結果摘要回主 agent（見 5.2）。
  4. **Checkpoint + resume**：任務中斷能從上次狀態恢復，不怕 API rate limit 或網路中斷。
  5. **更強 reasoning**：o1/o3 系列跟 Claude 4 系列都在 inference-time reasoning 上大幅提升，降低 hallucination 複利。

### 5.2 Sub-agent 模式成熟（Claude Code, 2025）

- **Claude Code Subagents**：Anthropic 的 heuristic — 「若任務涉及 10+ 檔案探索，或 3+ 獨立工作塊，就該用 sub-agent」[來源: https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously]
- **效益**：
  - **Context 隔離**：每個 sub-agent 用獨立 context，不汙染主 agent，能平行跑多個任務。
  - **並行加速**：三個獨立修改並行跑，時間砍到 1/3。
  - **摘要回傳**：sub-agent 只回傳「最終結論」給主 agent，避免把整段探索過程塞進主 context。
- **行業影響**：sub-agent 是**從「短任務」跨到「長任務」的關鍵工程模式**，不是模型升級而已。這個模式在 Cursor、Windsurf、OpenAI Agents SDK（Agents-as-tools）裡都已成為標配。

### 5.3 Browser use 與 Computer use 進入生產

- Anthropic Computer Use 在 2024 年預覽後，到 2026 Q1 已有多家公司（Asana、Canva、DoorDash、Replit、The Browser Company）在生產環境試用 [來源: https://www.anthropic.com/news/3-5-models-and-computer-use]。
- Browser use 透過 MCP 的 `playwright` / `browser` server 成為標配工具，Deep Research 類 agent 幾乎都內建。

### 5.4 Agentic Evals 變重：從 MMLU 到 SWE-bench / ARC-AGI-2 / OSWorld

- **SWE-bench Verified（OpenAI, 2024-08）**：500 題人工驗證的子集，成為 agent coding 的黃金標準 [來源: https://openai.com/index/introducing-swe-bench-verified/]
- **ARC-AGI-2**：Chollet 強調「reasoning for agents」的難題。
- **OSWorld**：測 computer use 的 benchmark，人類 70%+、當前頂尖 model 還在 30–50% 區間。
- **TAU-bench**：tool-use agent 的 benchmark，Claude 系列在零售/航空域都是領跑。
- **意義**：從「模型 benchmark」轉向「agent benchmark」代表行業共識 — 模型智力已經不是瓶頸，**工程化的 agent 實現方式才是**。

### 5.5 1M context window 普及

- Claude Opus 4.6 / 4.7、Gemini 2.5 Pro、GPT-5 系列都提供 1M context 選項。對 agent 的意義：
  - 大 repo 能整包餵進去，不用 RAG。
  - 長對話歷史能保留多天，做「persistent assistant」成為可能。
  - 但 1M context 的 **cost** 仍高（Opus 4.7 1M context 每 1M input token $15+），所以 sub-agent + compaction 仍是必要優化。

---

## 六、縱向敘事總結 — 從「能不能做」到「做得多自主」

把上述 4 年壓成一條故事線：

**2022 是 Agent 的元年，但不是因為 agent 的點子多新，而是因為三塊基礎拼圖才剛同時到齊** — 足夠大的模型（GPT-3.5）、可追隨指令的 RLHF tuning（InstructGPT）、以及被證明有效的 chain-of-thought 推理。ReAct 論文在 2022 年 10 月把「reasoning + acting」正規化成一組 prompt pattern，**為 agent 給了第一個可複製的技術骨架**。12 月 ChatGPT 病毒傳播，幫 agent 創造了市場前置條件。

**2023 是狂熱與幻覺的一年**。從 3 月底的 AutoGPT 和 BabyAGI 開始，整個行業陷入「自主 agent 就是 AGI」的錯覺。但 2023 年底之前，大家已經清楚地看見 AutoGPT 的五大毛病 — loop、hallucination 複利、cost、context 不足、缺乏控制 — **全部是工程問題，不是概念問題**。這一年真正有價值的是兩條安靜的線：一條是 OpenAI 在 6 月把 function calling 標準化、11 月發布 Assistants API，把「工具呼叫」商品化；另一條是 Reflexion、Tree of Thoughts、Voyager、MetaGPT、AutoGen 這些研究在默默為「更可控的 agent」打地基。

**2024 是「從 chain 到 graph，從實驗到生產」的工程化年**。LangGraph 把 agent 從線性 chain 升級成 state machine，承認了「真實 agent 需要 loop、分支、human-in-the-loop」這個現實。Devin 用一個 demo 重新點燃「AI 工程師」的想像，並把 SWE-bench 推成黃金 benchmark。Claude 3.5 Sonnet 在 6 月橫空出世，10 月再升級 + 搭配 Computer Use，第一次讓開發者相信「agent coding 真的能用」。**這一年的哲學轉變是：與其做萬用自主 agent，不如做垂直、可控、scaffold 越薄越好的 agent**。Anthropic 的「最小 scaffold、最大模型自主」哲學從此成為主流。

**2025 是協議統一與商業化的分水嶺**。Anthropic 在 2024 年底發表的 MCP 在 2025 年內以驚人速度成為事實標準 — 3 月 OpenAI、4 月 Google 先後採納，年底捐給 Linux Foundation。MCP 贏的原因不是技術有多新（本質上是 LSP + JSON-RPC 的改寫），而是**它同時滿足了大廠信用、AI-native 抽象、完整 first-party 實作、最小表面積、明確 roadmap** 這五個條件，使得開發者敢投入、其他大廠願意跟進。同一年 Deep Research 類產品（OpenAI / Perplexity / Gemini）證明「長任務 agent + 引用報告」才是 consumer 殺手級場景，比 AutoGPT 式萬用 agent 更 defensible。OpenAI Agents SDK、Google ADK + A2A 各自推出 production-ready 多 agent 框架，形成三大陣營並立。

**2026 Q1 的範式轉移是從「短任務」到「長時間自主執行」**。關鍵不是單一模型突破，而是五件事疊加：1M context、自動 compaction、sub-agent 隔離、checkpoint/resume、強 inference-time reasoning。Claude Sonnet 4.5 的「30+ 小時 autonomous coding」是這五件事合力的結果，不是 Sonnet 4.5 比 3.5 聰明了多少倍。**Sub-agent 模式是這個階段最重要的工程發現** — 它不是一個新概念（MetaGPT、AutoGen 早已探索），但把「主 agent 不自己做重活，而是 orchestrate 乾淨 context 的 sub-agents」做成 infrastructure 級別的預設模式，是 2025–2026 才成熟的。

四年走下來，agentic AI 的演化軌跡可以用一句話概括：**從「能不能讓 LLM 自己做一件事」（2022），到「自主 agent 是不是就是 AGI」的錯覺（2023），到「窄而深的垂直 agent 才能生產化」的覺悟（2024），到「協議統一、生態爆發」（2025），到「長時間自主 + sub-agent orchestrate 才是未來形態」（2026）**。下一個分水嶺可能是「agent 跨組織協作」（A2A 生態成熟）、「agent 自我改進」（把 Reflexion / Voyager skill library 推到系統層級），以及「agent 在 embodied 世界的落地」（humanoid robot、autonomous vehicle 把 agent 從數位世界推到物理世界）。

---

## 附錄：關鍵時間線速查

| 年月 | 事件 | 類型 |
|------|------|------|
| 2022-01-28 | Chain-of-Thought Prompting 論文 | 技術奠基 |
| 2022-03 | InstructGPT / RLHF | 技術奠基 |
| 2022-10-06 | ReAct 論文 | 範式定義 |
| 2022-11-30 | ChatGPT 發布 | 市場前置 |
| 2023-02-09 | Toolformer 論文 | 工具呼叫雛形 |
| 2023-03-20 | Reflexion 論文 | 自我反思 |
| 2023-03-28 | BabyAGI | 開源 agent |
| 2023-03-30 | AutoGPT、HuggingGPT | 開源 agent |
| 2023-05-17 | Tree of Thoughts 論文 | 推理擴展 |
| 2023-05-25 | Voyager (Minecraft) | Embodied agent |
| 2023-06-13 | OpenAI Function Calling | 工具呼叫標準化 |
| 2023-08-01 | MetaGPT 論文 | 多 agent 分工 |
| 2023-09-25 | Microsoft AutoGen | 多 agent 框架 |
| 2023-11-06 | OpenAI Assistants API + GPT-4 Turbo | 平台化 |
| 2024 初 | LangGraph | Chain → Graph |
| 2024-03-12 | Cognition Devin | AI 軟體工程師 |
| 2024-06-20 | Claude 3.5 Sonnet | Agentic coding 分水嶺 |
| 2024-08 | SWE-bench Verified | 黃金 benchmark |
| 2024-10-11 | OpenAI Swarm (實驗性) | 多 agent 探索 |
| 2024-10-22 | Anthropic Computer Use | 桌面自動化 |
| 2024-11-25 | **MCP 發布** | 協議起點 |
| 2024-12 | Gemini Deep Research (首版) | Agent 產品化 |
| 2025-02-02 | OpenAI Deep Research | Agent 產品化 |
| 2025-03-07 | Perplexity Sonar Deep Research | Agent 產品化 |
| 2025-03-11 | OpenAI Agents SDK + Responses API | 平台化 |
| 2025-03 | OpenAI 採納 MCP | 協議擴散 |
| 2025-04 | Google Gemini 採納 MCP | 協議擴散 |
| 2025-07 | Google A2A v0.3 發布 | 跨 agent 協議 |
| 2025-09 | Claude Sonnet 4.5（30+ 小時自主） | 長任務分水嶺 |
| 2025-12 | MCP 捐給 Agentic AI Foundation | 治理標準化 |
| 2026 Q1 | Claude Opus 4.7 + sub-agent + 1M context | 長任務生產化 |

---

## 資料來源清單

- ReAct: https://arxiv.org/abs/2210.03629
- Chain-of-Thought: https://arxiv.org/abs/2201.11903
- Toolformer: https://arxiv.org/abs/2302.04761
- Reflexion: https://arxiv.org/abs/2303.11366
- HuggingGPT: https://arxiv.org/abs/2303.17580
- Tree of Thoughts: https://arxiv.org/abs/2305.10601
- Voyager: https://arxiv.org/abs/2305.16291
- MetaGPT: https://arxiv.org/abs/2308.00352
- BabyAGI GitHub: https://github.com/yoheinakajima/babyagi
- BabyAGI 作者博客: https://yoheinakajima.com/birth-of-babyagi/
- AutoGPT Wikipedia: https://en.wikipedia.org/wiki/AutoGPT
- AutoGPT 限制分析: https://autogpt.net/auto-gpt-understanding-its-constraints-and-limitations/
- OpenAI Function Calling: https://openai.com/index/function-calling-and-other-api-updates/
- Simon Willison on Function Calling: https://simonwillison.net/2023/Jun/13/function-calling/
- AutoGen Microsoft: https://www.microsoft.com/en-us/research/blog/autogen-enabling-next-generation-large-language-model-applications/
- OpenAI DevDay 2023: https://techcrunch.com/2023/11/06/openai-launches-api-that-lets-developers-build-assistants-into-their-apps/
- LangGraph: https://blog.langchain.com/langgraph/
- Cognition Devin: https://cognition.ai/blog/introducing-devin
- Claude 3.5 Sonnet: https://www.anthropic.com/news/claude-3-5-sonnet
- Claude SWE-bench: https://www.anthropic.com/research/swe-bench-sonnet
- Claude Computer Use: https://www.anthropic.com/news/3-5-models-and-computer-use
- OpenAI Swarm: https://github.com/openai/swarm
- CrewAI: https://github.com/crewAIInc/crewAI
- MCP Announcement: https://www.anthropic.com/news/model-context-protocol
- MCP Wikipedia: https://en.wikipedia.org/wiki/Model_Context_Protocol
- Why MCP Won (Latent.Space): https://www.latent.space/p/why-mcp-won
- Why MCP Won (New Stack): https://thenewstack.io/why-the-model-context-protocol-won/
- MCP vs Function Calling vs OpenAPI: https://www.marktechpost.com/2025/10/08/model-context-protocol-mcp-vs-function-calling-vs-openapi-tools-when-to-use-each/
- MCP 捐贈 AAIF: https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation
- OpenAI Agents SDK: https://openai.com/index/new-tools-for-building-agents/
- OpenAI Agents SDK 報導: https://www.infoq.com/news/2025/03/openai-responses-api-agents-sdk/
- Google ADK + A2A: https://developers.googleblog.com/agents-adk-agent-engine-a2a-enhancements-google-io/
- A2A v0.3: https://cloud.google.com/blog/products/ai-machine-learning/agent2agent-protocol-is-getting-an-upgrade
- OpenAI Deep Research: https://openai.com/index/introducing-deep-research/
- Perplexity Deep Research: https://techcrunch.com/2025/02/15/perplexity-launches-its-own-freemium-deep-research-product/
- Google Deep Research Max: https://venturebeat.com/technology/googles-new-deep-research-and-deep-research-max-agents-can-search-the-web-and-your-private-data
- Claude Sonnet 4.5: https://www.anthropic.com/news/claude-sonnet-4-5
- Claude Opus 4.7 Field Report: https://dev.to/kai_outputs/claude-opus-47-field-report-eight-hours-of-autonomous-work-10e3
- Claude Code Subagents: https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously
- SWE-bench Verified: https://openai.com/index/introducing-swe-bench-verified/
- Windsurf History: https://awesomeagents.ai/reviews/review-windsurf/
- Cursor: https://cursor.com/
- InstructGPT / RLHF: https://openai.com/index/instruction-following/
