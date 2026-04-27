# Handoff — TSMC PI v4.5 PDF 巢狀清單渲染修復 — 2026-04-28

## 狀態摘要

- **原定目標**：進行 v4.6 Profile 的大幅度 Markdown 表格化改版（為了解決 3 層巢狀 bullet 在 PDF 上呈現為密集文字牆的易讀性問題）。
- **轉折與發現**：發現核心痛點並非 Markdown 格式本身，而是 `md_to_pdf.py` 中的 Python `markdown` 庫預設需要 4 格縮排，而原稿使用 2 格縮排，導致在開啟 `nl2br` 擴充套件時，第二和第三層清單被壓平成同一層。
- **最終解法**：直接修改 `scripts/md_to_pdf.py`，加入 `tab_length=2` 參數並補充 CSS 樣式（為三層配置 `●`, `○`, `■` 與漸進縮排）。
- **結果**：成功產出具有清晰 3 層結構的 PDF，大幅改善閱讀體驗，**免除了改寫 3000 多行 Markdown 的巨大工程**。

## 已完成項目

- [x] 修復 `scripts/md_to_pdf.py` 的巢狀清單渲染 bug (`tab_length=2` + CSS)
- [x] 重新產生測試用的 PDF (`TSMC_PI_統一Profile_v4.5_fixed_bullets.pdf`)
- [x] 重新產生完整大表 PDF (`TSMC_PI_彙整大表_v4.5_fixed.pdf`)
- [x] 更新 `CHANGELOG.md` 紀錄此修復

## 待辦事項 (Next Steps)

- v4.6 易讀性改版（全數改為 Markdown 表格）**暫緩**，待主管檢視 fixed 版本的 PDF 後，若仍覺排版過度密集，再考慮重啟計畫。
- 專案維持穩定狀態，隨時可進行新一輪的 PI 盡調或新增報告。
