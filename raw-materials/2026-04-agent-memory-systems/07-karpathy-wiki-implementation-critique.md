# Over-Engineering Karpathy's Agent Memory — 實作批評

**來源**：https://dev.to/awrshift/i-over-engineered-karpathys-agent-memory-heres-what-actually-works-4imk
**日期**：2026-04-17
**訪問日期**：2026-04-29

## 失敗模式（在 Claude Code / 本地環境）

Karpathy 原架構假設 server-side 執行 + 可靠 background process。在 local 跑時三大失敗：

1. **Background Process Dropout**：session 結束後 subprocess 自動化會 timeout 或 silently exit，無 output
2. **Transcript Parser Choking**：長 session 讓 transcript parse 失敗，daily log 空
3. **Silent Pipeline Failures**：after-6pm auto-compile 從未觸發（hash check 是對的但 pipeline 沒跑）

> 7 個專案 3 週實測：「about half the time, the background process either timed out, failed to parse the transcript, or exited silently with no output」

## 簡化後 work 的版本

| Karpathy 原版 | Working 版 |
|---|---|
| Async background process | **Synchronous in active session**（agent 保有完整 context）|
| Transcript extraction & parsing | **File-based date filtering** + 簡單 grep |
| Recursive guards + hash compare | **Manual checkpoint command**（如 `/close-day`，~300 行自動化簡化為一個指令）|
| 所有檔放 `.claude/` | **搬到 project root**（`.claude/` 阻擋寫入造成 silent fail）|

## 結論

> "Simplicity First. Minimum code that solves the problem"（引 Karpathy 自己的 principle）

**過度自動化會掩蓋失敗；明確指令配 session context 反而可靠。**

## 對 §8 失敗模式章節的關鍵啟示

LLM Wiki 路線雖 elegant，但 **client-side 實作有真實工程坑**：
- 不要依賴 background process
- 不要 parse transcript
- daily log 不要放 `.claude/`
- 用 manual checkpoint 而非 silent automation
