# Changelog

All notable changes to the hv-research project.

Format: `## [YYYY-MM-DD]` with Added / Changed / Fixed / Removed subsections.

## [2026-04-23]

### Added
- **TSMC Top 15 教授投資分析 v3.2 PDF**（38 頁 / 692 KB）— 兩層結構：主管摘要 → 統一大表 → 個別教授三段細節（技術契合度 / 學生素養 / 合作分析）→ 附錄（策略/預算/法務/76 個 Reference URL）
- **TSMC 備選候選名單 v1.2 PDF**（23 頁 / 931 KB）— 38 位備選（A 差一點 4 / B 待觀察 6 / C 方向偏 3 / D 名氣大但未入選 20 / E 已失效 5）
- `phase3-verification-notes.md` — 16 位 WebSearch 平行驗證紀錄
- `templates/pi-due-diligence-framework.md` — PI 盡職調查 template（5 維度評分框架 v1.0）
- 附錄 E：每位教授 Reference URL（76 個公開連結）+ 能力限制聲明

### Changed
- 移除所有內部流程字樣（Phase 1/2/3、Batch A/B、Wave）— 主管版只有兩層結構
- 關鍵字矩陣表（20 欄）→ 改為每位教授 section 頂部「專長標籤列」（解決 PDF 寬表格切斷）
- Backup PDF 結構統一為 Top 15 式兩層（原四章四格式 confuse → 三章兩層式）
- CLAUDE.md 新增 PI 盡職調查工作流程 + 慣例（PDF 寬表格上限 / 必附 Reference URL / Companion 結構對齊）

### Fixed
- 彭文志從 Top 15 移除（已借調 TSMC 當處長，非合作候選；WebSearch 未能抓到）
- 王俊明 TSMC 綁定顧慮取消（SAT 中心為 TSMC 支持設立，體制內合作方 ≠ 離職自由身）

### Removed
- `TSMC_Top15_v3_04_關鍵字矩陣.md`（PDF 寬表格切斷問題）

## [2026-04-22]

### Added
- Phase 1-3 台灣 11 校半導體 AI 教授盤點完成
- Top 15 PDF v1 / v2
- `phase3-integrated-ranking.md`、`phase3-batch-a-llm-rag-candidates.md`、`phase3-batch-b-packaging-candidates.md`

### Changed
- Top 10 → Top 15 擴充（Batch A/B 各補 3 位）

## [2026-04-20]

### Added
- 專案初始化（CLAUDE.md / README.md / 目錄結構）
- 第一份研究：Claude Code 橫縱分析報告（13,860 中文字 / 1.1 MB PDF）
- `scripts/md_to_pdf.py`（weasyprint + markdown 工具）
