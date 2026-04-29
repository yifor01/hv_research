# Karpathy Decade of Agents 框架

**來源**：Simon Willison — https://simonwillison.net/2025/Oct/18/agi-is-still-a-decade-away/
**訪問日期**：2026-04-29

## 命名訊息「Decade of Agents」非「Year of Agents」

Karpathy 框架反駁 2025-2026 樂觀派：當前 agent 缺基礎建設，要 ~10 年才能「達到員工 / 實習生水準的可靠性」。

## 三大缺口（明確列出）

1. **Multimodality** — 多模態能力不足
2. **Computer use** — 無法可靠操作系統（瀏覽器、檔案、IDE）
3. **Continual learning** — "You can't just tell them something and they'll remember it"

第四項（cognitive capacity / strong memory）在 simonwillison 整理裡是 implied 而非單獨列出。

## 必引用的 Karpathy 原句

1. > "It will take about a decade to work through all of those issues."
2. > "They don't have continual learning. You can't just tell them something and they'll remember it."
3. > "They're cognitively lacking and it's just not working."

## 區分 narrow vs general

- **Narrow coding agents**：現在已能用（指 Claude Code 等）
- **General-purpose employee-replacement agents**：still a decade away

## 對應到記憶系統的意涵

「continual learning 不存在」 = 訓練後 LLM 無法 consolidate 新知識 → 必須靠外部記憶層補

這正是 §5.2 System Prompt Learning + §5.4 三階段 consolidation 的論述基礎。
