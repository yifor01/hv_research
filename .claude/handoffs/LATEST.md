# Handoff — Agentic AI 報告 v2 評審修訂 + SVG 視覺修正 — 2026-04-26

## Goal
針對 2026-04-24 產出的 Agentic AI 橫縱分析報告 v1（7.4/10）做評審 → v2 全面修訂，並補 6 張 SVG 示意圖視覺化關鍵概念。

## Current State
✅ **已交付**：v2 完整版本 + PDF 已生成（1.29 MB / 35 頁），三輪 SVG 修正完成

## Key Decisions Made

### 評審視角
以「Anthropic AI 技術總監」身分自審 v1，發現 3 處事實錯誤 + 7 處重大內容缺漏。打分 7.4/10。

### v2 修訂優先序（按 ROI）
**必修三件（出 v2 必須做）**：
1. Opus 4.7 定價修正：v1 寫 `$15+/M input` → 實際 `$5/M input、$25/M output`、no long-context premium
2. Agentic Misalignment 研究時間修正：v1 標 2024 → 實際 2025-06（arXiv 2510.05179）
3. 補 Agent Skills 章節（agentskills.io 2025-12 開放標準，當前完全缺席）

**強烈建議**：
- 補 Claude Managed Agents（2026-04-08 發布）
- 補 Agentic RL 訓練範式（§3.7.1.5 全新章節）
- 擴展 Computer Use API 2026 Q1 變更
- 補新世代 evals（SWE-Lancer / AgentBench-2 / LiveSWEBench）
- 安全章節從 3 威脅擴為 4 威脅（補 tool poisoning、memory poisoning、multi-agent collusion）

**錦上添花**：
- 加附錄 A：起手套件三層
- §4.6 三個未定賭注
- Memory 框架對比表
- Sub-agent 實作層細節

### 視覺化策略
6 張 SVG 示意圖（依章節順序編號）：
1. 圖 1（§2.6）：五條演化線匯流到 2026 Q2
2. 圖 2（§3.1）：三陣營 + 三協議 bus 格局
3. 圖 3（§3.7）：七層工程棧 + 成熟度漸變
4. 圖 4（§3.7.3）：Context Lifecycle 四階段
5. 圖 5（§3.7.4）：Multi-agent 四種編排模式拓撲
6. 圖 6（§4.6）：三個未定賭注

## Files Modified

### Agentic AI v2 報告
- `reports/2026-04-agentic-ai-tech/最新_agentic_ai_技術細節與實現方式_橫縱分析報告_v2.md`（108 KB，~1100 行）
- `reports/2026-04-agentic-ai-tech/最新_agentic_ai_技術細節與實現方式_橫縱分析報告_v2.pdf`（1.29 MB，35 頁）
- `reports/2026-04-agentic-ai-tech/sources.md`（補 11 條 v2 新增來源）

### 跨專案文件
- `CHANGELOG.md`（新增 `[2026-04-26] Agentic AI v2` 條目，含 lessons learnt）
- `~/vault/projects/hv-research/lessons.md`（追加 3 條 [PDF 排版] [研究方法] lessons）
- `~/vault/projects/hv-research/status.md`（Last updated + Completed + Next Steps）
- `~/vault/daily-notes/2026-04-26.md`（hv-research section 從 5 項擴為 11 項）

## Blockers / Issues
無。但有一個工作流改進建議：把本次學到的 SVG 規則寫進 `~/.claude/skills/hv-analysis/` skill 內的 SVG 慣例（目前只在 lessons.md，下次別的專案可能還會再撞）。

## Next Steps (priority order)
1. **`git add . && git commit && git push`**（v2 + sources + CHANGELOG + 跨 vault 同步）
2. **舊 v1 PDF 是否保留**：reports/ 內目前 v1 + v2 並存，保留 v1 以利版本對比 vs 刪除避免主管混淆——待用戶決定
3. **更新 hv-analysis skill 的 SVG 慣例**：把 `font:` shorthand 禁令、polygon apex 規則、event bus pill 設計寫進 skill（避免下次別的專案再撞）
4. **TSMC PI 主管圈選**（既有 next step）

## Lessons Learnt（已寫入 vault lessons.md）

### [PDF 排版] WeasyPrint SVG `font:` shorthand 不渲染
- 問題：`font: bold 11px sans-serif` cairosvg 解析 OK，WeasyPrint 把整條規則丟掉
- 修法：拆成 `font-weight: bold; font-size: 11px; font-family: sans-serif`
- 教訓：SVG → PDF pipeline **一律用顯式 font-* 屬性**，不用 shorthand

### [PDF 排版] SVG 箭頭 / event bus / 對抗徽章三條視覺規則
- 箭頭 polygon：apex 點偏離另兩點最遠的方向 = 指向；base 兩點 y 對稱於 line
- Event bus：用 `<rect rx>` pill 形 channel，所有 publisher/subscriber 實線連到上下緣，不用 dashed line
- VS 對抗徽章：直徑 24-26px 圓 badge + 11px 粗體文字，不用 28px 大字（會溢界）

### [研究方法] 評審 → v2 ROI 排序
- 在快速演進領域（AI / 加密貨幣 / 政治），hv-analysis 需要多一道「事實校驗 pass」
- 訂閱式服務的定價、近 30 天內發布的產品必須再 WebSearch 核實
- 橫向時間切面要明確標出「截止日」而非空泛寫「2026 Q1」

### AI 繪 SVG 三步驗證 SOP
1. 寫完先用 cairosvg 抽 PNG 看排版（無中文 OK，但抓得出重疊 / 溢界）
2. 灌進 PDF 後用 pdftoppm 200dpi 抽頁看實際渲染（中文 + WeasyPrint quirks）
3. Read tool 視覺核驗（人眼抓 high-level 視覺隱喻是否直觀，例如箭頭方向、bus 是否懸空）
