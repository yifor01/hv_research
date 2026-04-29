# Karpathy LLM Wiki — 原始 gist 摘要

**來源**：https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
**發布日期**：2026-04-04 16:25
**訪問日期**：2026-04-29

## 三層架構

1. **Raw sources（不可變）** — 策展文件：文章、論文、圖、資料檔
2. **The wiki（LLM 維護）** — markdown 檔：summaries / entity pages / concept pages / cross-references
3. **The schema（配置）** — 一個文件（如 `CLAUDE.md`）定義 wiki 結構、慣例、workflow

## 核心模式：incremental，非 retrieval-only

每個新 source 觸發：
- 閱讀 + 討論
- 寫 summary 頁
- 更新 index
- 修訂相關 entity / concept 頁面（每個 source 約 10-15 頁）
- append log entry

## 關鍵差異於 RAG

- **RAG**：每次 query 重新從原文 retrieve + re-synthesize
- **LLM Wiki**：knowledge **compiled once**，wiki 是 persistent artifact，cross-references 已就位

## LLM 角色：Research Librarian（人類策展，LLM 維護）

> "You're in charge of sourcing, exploration, and asking the right questions. The LLM does all the grunt work — the summarizing, cross-referencing, filing, and bookkeeping that makes a knowledge base actually useful over time."

> "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

## 架構規範細節

- **index.md**：content-oriented catalog（按 category 組織，每頁一行 summary）
- **log.md**：append-only chronological，可解析前綴 `## [YYYY-MM-DD] operation | Title`
- **可選 CLI**：qmd（本地 markdown 搜尋，BM25 / vector）

範例 log：
```
## [2026-04-02] ingest | Article Title
## [2026-04-03] query | Topic Analysis
```

## Karpathy 自述限制

- "This document is intentionally abstract. It describes the idea, not a specific implementation."
- index.md 在 ~100 sources / 數百頁規模 work surprisingly well，更大規模需 qmd 或自製搜尋
- **未明確處理 LLM hallucination / citation grounding** — 社群（如 badwally）已自製 citation validator 補

## 必引用的 Karpathy 原句

1. "the wiki is a persistent, compounding artifact. The cross-references are already there."
2. "You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it."
3. "the tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping."
4. "The LLM's job is everything else."
5. "The right way to use this is to share it with your LLM agent and work together to instantiate a version that fits your needs."

## 主要差異化主張

> "Most people's experience with LLMs and documents looks like RAG: you upload a collection of files, the LLM retrieves relevant chunks at query time, and generates an answer. This works, but **the LLM is rediscovering knowledge from scratch on every question**."

vs.

> "the LLM **incrementally builds and maintains a persistent wiki**"
