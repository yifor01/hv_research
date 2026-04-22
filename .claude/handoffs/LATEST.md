# Handoff — TSMC 視角 5 位 P2 重評 + 3 commit 完成 — 2026-04-22
Generated: 2026-04-22（續夜）
Branch: master（已推進 3 commit，尚未 push）
Status: Ready for PDF 產出 + 法務 check

## 目標
為 TSMC AI 部門產出「可長期投資（5-10 年人才共建 + 技術合作）的學界 PI」完整決策文件；從 21 位候選人中依 5 維度量化評分得出 Top 7，並附全 37 位（21 主選 + 16 未入選名人）總表供主管查閱。

## 本次 session 新增

### A. Phase 2 排序 v2（三維度量化）
- `phase2-final-ranking-v2.md`（~30 KB）
- 5 組 Haiku agent 讀 21 份 profile 做三維度評估
- 綜合分數公式：技術 × 0.5 + 學生 × 0.3 - 綁定折扣

### B. 未入選 16 位 AI 名人說明
- `phase2-non-selected-rationale-batch1.md`（U1-U8）
- `phase2-tier2-why-not-selected.md`（U9-U16）
- 分佈：9 位 0/3、7 位 1/3、無人達 2/3

### C. TSMC 視角 Top 7 深度投資分析
- `phase2-top7-investment-analysis.md`（~40 KB）
- **Top 7**：馬誠佑 8.9 > 胡璧合 8.7 > 銀慶剛 8.5 > 詹寶珠 8.3 > 李家岩/鄭桂忠 8.0 > 林嘉文 7.5
- 關鍵視角翻轉：SAT 合聘 = TSMC 同陣營（不扣分）
- 全 37 位總表 + 5 年 Top 7 學生流向 TSMC ~105 人估算

### D. ⚠️ 5 位 TSMC 視角重評（本次 session 新增）
- `phase2-tsmc-reeval-5pis.md`（~17 KB）
- **王俊明 4.8→9.0** 🚀🚀（SAT 同陣營 + AI 光刻完全命中 2nm，擠進 Top 3 候選；公開論文量少是唯一風險）
- **宋振銘 6.1→8.0** 🚀（CoWoS Hybrid Bonding 無競爭）
- **蔡佩璇 5.9→7.7** 🚀（每年 2-3 名直進 TSMC + 零綁定）
- **蔡銘峰 4.8→7.2** 🚀（補 Top 7 缺的「人員效率 RAG」題目首選）
- **李祈均 2.6→2.3** ⬇️（NVIDIA Deputy 綁定，王鈺強反例翻版，**建議排除**）
- 更新後 Top 12：王俊明插隊 Top 7；宋振銘/蔡佩璇/蔡銘峰進 Top 8-11

### E. Git Commits（本次 session 完成 3 個）
1. `af6761b` docs: Phase 2 補完 profile + v2 三維度量化排序（9 files）
2. `737c58b` docs: 16 位未入選 AI 名人分析（U1-U16）（2 files）
3. `907f233` docs: TSMC 視角 Top 7 投資分析 + ⚠️ 5 位重評（2 files）

## 關鍵決策（累積）

- **用戶明確公司 = TSMC**（非競爭對手），觸發全盤重評維度 #4
- **「不特意加強原先 TSMC 合作的教授」**原則：既有 JDP 不加權重
- **SAT 合聘 = TSMC 同陣營**，非外部綁定
- **王俊明加入 Wave 1 候選**（若公開論文量確認無虞，可與馬誠佑並列 #1）

## 未完成

- [ ] [P0] `git push origin master`（13 files 已 commit 但未 push）
- [ ] [P1] 主管圈選 Wave 1 候選接觸 owner（**新建議**：馬誠佑 / 胡璧合 / 銀慶剛 / 王俊明 4 位）
- [ ] [P1] Wave 1 預算核准（合計 1500-2500 萬台幣 / 5 年，王俊明加入後需追加 300-500 萬）
- [ ] [P1] 用 `hv-analysis` skill 整合 `phase2-top7-investment-analysis.md` + `phase2-tsmc-reeval-5pis.md` + `phase2-final-ranking-v2.md` 產 PDF 給主管簡報
- [ ] [P2] 法務先行確認：
  - (a) 銀慶剛 US12354122B2 與 NCKU 鄭芳田 IP 共有狀態
  - (b) 王俊明 TSMC 離職年數 + 商秘獎/專利綁定
- [ ] [P3] 檢查 agent 產出 ref URL 可達性（部分可能是合成或 placeholder）

## 下一步（可直接執行）

### Option A：`git push` + 產 PDF（推薦）
```bash
git push origin master
# 然後用 hv-analysis skill 整合 3 個主文件產 PDF
```

### Option B：直接產 PDF
```
用 hv-analysis skill 把以下 3 份整合產 PDF 給主管：
- phase2-top7-investment-analysis.md（~40 KB，主決策文件）
- phase2-tsmc-reeval-5pis.md（~17 KB，5 位重評附錄）
- phase2-final-ranking-v2.md（~30 KB，21 位 v2 排序補充）
輸出：reports/2026-04-tw-univ-semi-ai-professors/TSMC_Top10_長期投資分析.pdf
```

### Option C：法務 check 王俊明後定案
- Email NSYSU SAT 詢問王俊明 TSMC 離職年數
- 若確認無商秘獎綁定 → 升 Wave 1 並與馬誠佑並列 #1
- 若有綁定 → 維持 Wave 2，且合作題目須先過 IP 審查

## 需要載入的檔案（下一 session）

**優先載入**：
- `reports/2026-04-tw-univ-semi-ai-professors/phase2-top7-investment-analysis.md`（主決策文件）
- `reports/2026-04-tw-univ-semi-ai-professors/phase2-tsmc-reeval-5pis.md`（最新重評）
- `reports/2026-04-tw-univ-semi-ai-professors/phase2-final-ranking-v2.md`（v2 排序）

**次優先**：
- `reports/2026-04-tw-univ-semi-ai-professors/phase2-non-selected-rationale-batch1.md`（U1-U8）
- `reports/2026-04-tw-univ-semi-ai-professors/phase2-tier2-why-not-selected.md`（U9-U16）

## Resume Prompt

「繼續 hv-research TSMC 視角半導體 AI 教授投資分析；Top 7 + 5 位重評完成（王俊明躍升 Top 3 候選；李祈均排除），3 個 commit 已推進。下一步：git push + 用 hv-analysis skill 產 PDF 給主管，或先法務 check 王俊明 TSMC 離職年數後升 Wave 1。」
