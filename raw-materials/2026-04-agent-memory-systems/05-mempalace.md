# MemPalace — 架構與爭議

**官方介紹**：https://recca0120.github.io/en/2026/04/08/mempalace-ai-memory-system/
**GitHub**：https://github.com/milla-jovovich/mempalace
**發布日期**：2026-04-08
**訪問日期**：2026-04-29

## 四層記憶堆疊

| Layer | Tokens | 載入時機 | 內容 |
|---|---|---|---|
| **L0 Identity** | ~50 | 啟動時必載 | AI persona 基礎資料 |
| **L1 Critical Facts** | ~120（AAAK 格式）| 啟動時必載 | team rosters / projects / preferences |
| **L2 Room Recall** | 按需 | 對話觸發 session context | 近期 session 重點 |
| **L3 Deep Search** | 按需 | semantic search | 全部 compressed memory vaults |

**170 token 喚醒成本** = L0 + L1，vs 19.5M tokens 原始歷史 / ~650K LLM-summarized

## 空間隱喻（method of loci）

- **Wing**：major categories
- **Room**：sub-topics
- **Hall**：shared memory corridors（facts / events / discoveries / preferences / advice）
- **Closet**：compressed summaries
- **Drawer**：verbatim originals（不丟原文）
- **Tunnel**：cross-wing connections

## Verbatim-First 哲學

雙層保存：drawers 存原檔（lossless）+ closets 存 AAAK 壓縮 summary。
原文可恢復，不像 extraction-based 系統 compress 後就丟。

## 96.6% 爭議（Nicholas Rhodes 批評文）

**來源**：https://nicholasrhodes.substack.com/p/mempalace-ai-memory-review-benchmarks（2026-04-08，2026-04-11 更新）

四點方法論問題：

1. **Hand-tuning**：找出 failing questions 後針對性修補再重測（違反 benchmark integrity）
2. **Retrieval window gaming**：top_k=50 但 dataset 只有 19-32 items → 「memory system contributes nothing」
3. **Metric confusion**：分數量的是 retrieval presence 而非 answer correctness
4. **API dependency**：100% 配置需要付費 Claude API，但 marketing 強調 local-only

**獨立重現**：88.9% R@10（hybrid retrieval，無 LLM）；無 reranking 時掉到 60.3%

## 真正的創新點（按批評者）

- Verbatim 儲存（vs LLM filtered summary）
- 階層架構（wings / halls / rooms / closets / drawers）
- MIT 授權、open source、local only
- MCP 整合 19 個工具

## 不是真的創新

- 空間隱喻本身貢獻有限
- "ChromaDB is doing the heavy lifting, not MemPalace"
- 架構 elegant 但偏組織性（organizational）而非性能性（performance）

## 技術瑕疵

- SQLite 在長期使用後問題多
- 無法跨設備 / 跨應用同步
- 依賴漂移（dependency drift）造成隱性維護成本
