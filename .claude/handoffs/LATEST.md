# Handoff — 台灣 11 校半導體 AI 教授盤點（Phase 2 完成）— 2026-04-22

## Goal

為 AI 部門主管建立「長期投資」教授人才資料庫：(1) 合作提升 2nm+ 良率、生產速度、工程師生產力；(2) 找高潛力學生為未來 RD 儲備。

11 校範圍：NTU、NTHU、NYCU、NCKU、NCU、NTUST、NSYSU、NCCU、NCHU、NTNU、NTUT。

## Current State

### Phase 1（廣度盤點） ✅ 完成
- 11 校共 ~210 位候選教授
- 5 所統計所補強 pass、核實 pass 10 位

### Phase 2（深度 profile） ✅ 20/20 完成
- 6 批並行 sonnet agents + WebFetch + Google Scholar + 隱形綁定檢查
- **重大新發現 🔴 Deep Bound 3 位**（Phase 1 未抓到）：張孟凡（TSMC CR Director）、張耀文（MediaTek 獨立董事）、林勇志（前 TSMC 13 年 + 商秘獎）
- Phase 1 標籤過期 3 位：陳正剛、洪英超、柏林
- 姓名勘誤 2 位、隱形兼職 2 位
- **Batch 3 補完（2026-04-22 本 session）**：蔡銘峰（NCCU T7b RAG）🟢🟡、鄭少為（NTHU T1 DoE）🟢🟡
  - 均 Free Agent 零綁定；蔡銘峰 T7b 核心但無半導體 domain 先例；鄭少為 TSMC-JDP 未列名但近 5 年頂期刊論文不可追溯

### 累計 🔴 Deep Bound 9 位
吳安宇、王鈺強、林本堅、李耀仁、林君雄、YuanFu Yang、張孟凡、張耀文、林勇志

## Key Decisions Made

1. **兩階段方法論**（Phase 1 廣→Phase 2 深）
2. **7 大主題群**（T1-T7b）+ T7a overlay + T7b 獨立 LLM 軌
3. **🟢🟡🔴 綁定分級**（Phase 1 對 🔴 識別率僅 67%，必須 deep profile）
4. **統計所補強獨立 pass**
5. **Agent 平行上限 2 位**（用戶指示避免結果遺失，改為一次最多 2 個 sonnet）
6. **sonnet 而非 opus**
7. **.gitignore 取消 reports/raw-materials 排除**
8. **Feature branch workflow**（master push 被 permission rule 擋，改 PR 流程）

## Files Modified（關鍵檔案）

### reports/2026-04-tw-univ-semi-ai-professors/
- `RESEARCH_PLAN.md` — 方法論
- `phase1-candidates.md` — 11 校頓號名單 + 總表
- `phase2-recommendations.md` — Top 20 建議
- `phase2-batch1-tier-s-summary.md`、`phase2-batch2a-summary.md`、`phase2-batch2b-summary.md`、`phase2-batch2c-summary.md`
- `phase2-final-summary.md` — **主總結**（**推薦讀此份**；已更新至 20/20）
- 20 份 `phase2-profile-<name>.md`

### raw-materials/2026-04-tw-univ-semi-ai-professors/
- 11 校 professors.md + 5 校 statistics-supplement.md + `verification-results.md`

## Blockers / Issues

1. **王俊明（NSYSU）TSMC 年數不明**
   - 行動：email albert.wang@g-mail.nsysu.edu.tw 確認
   - 若 <8 年 = 🟡 OK；≥10 年 + 商秘 = 🔴 轉替代

2. **T4 主力僅宋振銘 1 位**（林勇志排除後）
   - 可選：補 NYCU 陳冠能（ICST 院長）做 profile

3. **蔡銘峰 domain gap**：無半導體先例，合作啟動需廠方提供匿名製程資料集做 onboarding

4. **鄭少為近年空窗**：2020+ 無可追溯頂期刊論文、副教授 17 年未升等 — 建議「方法論顧問」而非「深度合作」

5. **Git 狀態**：7 個 feature branches 全合併或待合。本 session 新增 2 份 profile + final-summary 更新 + LATEST.md 更新，需另開 feature branch + PR。

## Next Steps（依優先度）

### 🥇 最迫切
1. **主管圈選**：從 `phase2-final-summary.md §5` 圈選實際要接觸的 PI（16 位）
2. **email 確認王俊明 TSMC 年數**

### 🥈 短期（本週）
3. **（選配）T4 補強**：NYCU 陳冠能 profile
4. **Git cleanup**：刪除 7 個已 merged feature branches（本地 + remote）

### 🥉 中期（下週起）
5. **用 hv-analysis skill 產出最終 PDF**（給主管內部簡報用）
6. **逐位聯絡**：依 Top 20 Tier-S 5 位 → Tier-1 5 位 → 條件式 6 位 順序

## 關鍵方法論教訓（供下次研究參考）

1. **Training-data agent 盤點幻覺率 ~30%**
2. **Phase 1 對 🔴 Deep Bound 識別率 67%**
3. **Phase 1 標籤過期 ~15%**
4. **姓名勘誤 ~10%**
5. **冠名講座 ≠ 排他綁定**（Micron/TSMC/Delta 皆有現役 PI 接受）
6. **論文 Acknowledgments 段是隱形綁定的快速核實工具**
7. **個人網頁「最後更新時間」與「論文/期刊空窗」是偵測 PI 動量下降的 proxy**（鄭少為案例）

## 結論

本次 Phase 1 + Phase 2 **共產出 20 位現役 PI 深度 profile + 210 位候選總表**，建立了台灣學界半導體 AI 方向的完整情報資料庫。**🔴 黑名單 9 位**、**最終推薦 16 位可接觸 PI**（Tier-S 5 + Tier-1 5 + 條件式 6）。主管可直接依 `phase2-final-summary.md §5` 順序啟動實際接觸流程。
