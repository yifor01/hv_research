# 台灣半導體 AI 教授盡職調查 — TSMC 合作 PI 名單

> 對台灣大學體系（NTU / NTHU / NYCU / NCKU / NTUST + 中研院 + HHRI 等）做半導體 × AI 跨領域 PI 盤點，產出 TSMC 合作優先名單與備選池。

**最終交付**: v4.3（2026-04-27）— B47 李宏毅跨域題目雙 check + B53/B54/B55/C56-C61 合作方式 wording 精準化

---

## 資料夾結構

```
.
├── README.md               # 本檔（索引）
├── v4.3-final/             # 現役交付物（主管最新版）
├── archive/
│   ├── pdfs-old-versions/  # v1 / v2 / v3 / v3.4 / v4.0 / v4.1 / v4.2 PDF
│   └── md-superseded/      # 被 v4.x 取代的舊章節 md
├── process/                # 研究過程產物（phase 1-5）
└── planning/               # 研究計畫與評分表
```

---

## v4.3-final（最新交付）

| 檔案 | 用途 |
|---|---|
| `TSMC_PI_彙整大表_v4.3.pdf` | **主檔（直向）** — 主管摘要 + 大表 + Profile + 附錄 |
| `TSMC_PI_統一大表_橫式_v4.3.pdf` | A3 橫式速查表 |
| `TSMC_v4_00_封面與執行摘要.md` | 主管摘要章節（五軸 15 位 + 三波接觸 + 預算估算） |
| `TSMC_v4_01_統一大表.md` | 66 位完整大表（重編號 + 重排 + 附註） |
| `TSMC_v4_03_統一Profile.md` | 55 位 4 區塊 Profile（S15 + A15 + B25） |
| `TSMC_v4_07_合作狀況披露附錄.md` | 合作關係與利益揭露附錄 |

**v4.3 核心改動**（vs v4.2）— 「建議合作方式」wording double check：
1. **B47 李宏毅**（最大改動）：原「無半導體題目可接觸」過於否定 → 列出 5 條跨域題目（LLM-as-Evaluator 文件審查 / hands-free LALM / 交班轉寫 / 自監督聲學異常 / AI 素養課程），定位為工程師效率軸方法論候補；Profile 段補上完整題目表 + KPI
2. **B53 陳正剛**：「方法論顧問池」→ Tier 2 顧問（依 Jakey Blue 案需求橋接 SPC/APC 會診）
3. **B54 謝旻甫**：「轉給 Fab 設施部門」→ 補上題目細節（馬達/風機 ML 預測維護）+ 軸定位（fab 設施軸非製程軸）
4. **B55 洪英超**：「方法論顧問池」→ Granger 因果統計單次諮詢顧問（橋接 SPC 多變量根因分析）
5. **C56 林清安**：「不建議進階」→ 機械視覺/手臂與 AMHS 有間接接點，候補位待主軸 PI 飽和再重評
6. **C57/C58/C60/C61**：補上具體題目軸或競合說明（C57 與 B47 LALM 競合、C58 員工穿戴另案、C60 高維 DoE 統計支援、C61 員工關懷軸）
7. 大表附註 §C ranking 微調說明 + 執行摘要不啟動池說明同步更新

---

## archive/

### pdfs-old-versions/（10 份歷代 PDF）

| 檔案 | 版本說明 |
|---|---|
| `TSMC_Top10_長期投資分析.pdf` | v0 雛形（Top 10）|
| `TSMC_Top15_長期投資分析_v2.pdf` | v2（Top 15）|
| `TSMC_Top15_長期投資分析_v3.pdf` / `_v3.4.pdf` | v3 系列 — Top 15 完整版 |
| `TSMC_Backup_備選候選名單_v1.pdf` / `_v1.4.pdf` | 備選名單獨立檔 |
| `TSMC_PI_彙整大表_v4.0.pdf` / `_v4.1.pdf` / `_v4.2.pdf` | v4 系列彙整大表（直向）|
| `TSMC_PI_統一大表_橫式_v4.0.pdf` / `_v4.1.pdf` / `_v4.2.pdf` | v4 系列橫式速查 |

### md-superseded/（14 份舊章節 md）

- `TSMC_Backup_v1_*.md` — v1 備選名單章節
- `TSMC_Top15_v3_*.md` + `TSMC_Top15_長期投資分析_v3.md` — v3 章節原稿
- `TSMC_v4_05_A級profile.md` / `TSMC_v4_06_B級profile.md` — v4 早期分檔 profile（已合併進 `v4.2-final/TSMC_v4_03_統一Profile.md`）
- `TSMC_v4_06_方法論與版本差異.md` — 早期版本差異說明（已併入主檔）

---

## process/（61 份研究過程產物）

| 階段 | 內容 |
|---|---|
| `phase1-candidates.md` | 廣度候選池掃描（~80 位初篩） |
| `phase2-*` （30 份） | Tier 1 verification + 26 位完整 profile + ranking + 投資分析 |
| `phase3-*` （4 份） | 補強 batch（LLM/RAG + 封裝候選） + integrated ranking |
| `phase4-*` （16 份） | 主管反饋第二輪補強（11 位 profile + 5 位 mini） |
| `phase5-haiku-scan/` | Haiku 模型掃描補充候選（G4 summary + 8 位）|

---

## planning/

- `RESEARCH_PLAN.md` — 研究計畫總綱
- `unified-score-table-v4.md` — v4 統一評分表（5 維 × 66 位）
- `profile-2025-2026-delta.md` — 2025→2026 PI 動態變化
- `phase4-补强說明.md` — Phase 4 補強說明

---

## 累積教訓（→ `~/vault/projects/hv-research/lessons.md`）

主要 lesson 已記錄在 vault：
- WebSearch 無法驗證企業內部借調 / 顧問私約 / 未公開合作
- 主管摘要按題目軸而非分數分組（避免「誰最強」型誤導）
- 學生招募欄位 pass — 「教授是否公開 Lab 頁面」為個人習慣，會造成系統性偏誤
- 完整重編號 vs 保留編號的取捨（主管以姓名為主，犧牲跨版本 ID 追蹤性）

---

## 引用 PDF 主檔給主管

```
v4.3-final/TSMC_PI_彙整大表_v4.3.pdf      # 直向主檔
v4.3-final/TSMC_PI_統一大表_橫式_v4.3.pdf  # A3 橫式速查
```
