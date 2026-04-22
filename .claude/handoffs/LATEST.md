# Handoff — Phase 3 完成（Top 15 + 方法論 template） — 2026-04-23
Generated: 2026-04-23
Branch: master
Status: Phase 3 主體完成；等主管回覆 Wave 1 圈選後進 Phase 4（Option A briefing 包）

## 本次 session 總結

### Phase 3 交付
- **Top 15 最終版 PDF**：`reports/2026-04-tw-univ-semi-ai-professors/TSMC_Top15_長期投資分析_v2.pdf`（76 頁，1.3 MB）
- **Batch A 補 3 位 LLM/RAG PI**：黃瀚萱（AS）7.2 / 彭文志（NYCU）7.0 / 高宏宇（NTHU）6.4
- **Batch B 補 3 位封裝 PI**：陳冠能（NYCU Dean）8.7 / 陳智（NYCU 材料主任）8.3 / 江國寧（NTHU 講座）8.1
- **整合文件**：`phase3-integrated-ranking.md` — Top 15 總表 + Wave 1-3 調整 + 對主管 3 問防禦

### 方法論 template（B 完成）
- `templates/pi-due-diligence-framework.md` — v1.0 首發
- 5 維度錨點定義、綁定折扣判斷樹、Phase 1-4 標準流程、換公司視角調整、6 大判斷陷阱
- 未來其他題目（MediaTek / HBM 材料 / 國際比較）可直接套用

## Top 15 最終排序（TSMC 視角）

| 排名 | PI | 分數 | Wave |
|---|---|---|---|
| 1* | 王俊明（NSYSU SAT）| 9.0 | Wave 1（法務 check 後定案）|
| 2 | 馬誠佑（NSYSU 電機 + SAT）| 8.9 | Wave 1 |
| 3 | 胡璧合（NTU 電機）| 8.7 | Wave 1 |
| 3 | 陳冠能（NYCU ICST Dean）| 8.7 🆕 | Wave 1 |
| 5 | 銀慶剛（NTHU 統計）| 8.5 | Wave 1 |
| 6 | 陳智（NYCU 材料主任）| 8.3 🆕 | Wave 2 |
| 6 | 詹寶珠（NCKU 電資院長）| 8.3 | Wave 2 |
| 8 | 江國寧（NTHU PME）| 8.1 🆕 | Wave 1 |
| 9 | 宋振銘（NCHU 研發長）| 8.0 | Wave 2 |
| 9 | 李家岩（NTU 資管副院長）| 8.0 | Wave 2 |
| 9 | 鄭桂忠（NTHU 電機）| 8.0 | Wave 2 |
| 12 | 蔡佩璇（NCKU IMIS）| 7.7 | Wave 2 |
| 13 | 林嘉文（NTHU 電機）| 7.5 | Wave 3 |
| 14 | 蔡銘峰（NCCU 資科）| 7.2 | Wave 2 |
| 14 | 黃瀚萱（AS 資訊所）| 7.2 🆕 | Wave 2 |
| 16 | 彭文志（NYCU 資工）| 7.0 🆕 | Wave 3 |

**Wave 1 已擴到 6 位**：馬誠佑 / 胡璧合 / 銀慶剛 / 王俊明 / 陳冠能 / 江國寧

## 對主管 3 問的防禦（已建立）

- Q1「CoWoS/封裝為何只推一位？」→ 現有 4 位互補（材料 陳智/宋振銘 → 系統 陳冠能 → AI 方法論 江國寧）
- Q2「人員效率為何只推一位？」→ 現有 4 位互補（傳統 RAG 蔡銘峰 / CAG 黃瀚萱 / Agentic IR 彭文志 / Domain Adaptation 高宏宇）
- Q3「都不合作怎麼辦？」→ Phase 4 替代候選快速 scan（150-200 位台灣 AI/半導體 PI 中還有 100+ 未深度盤點）

## Git 狀態

- 本地領先 origin/master 2 commits（未 push）：
  - `8076228` docs: 新增 PI 盡職調查方法論 template（v1.0）
  - `1d5b368` docs: Phase 3 擴充候選池 — Top 10 → Top 15
- 上一次 push：`98cbe32`（handoff Phase 3 啟動）

## 未完成

- [P0] `git push origin master`（2 commits 未 push）
- [P1] 主管圈選 Wave 1（6 位）接觸 owner — **等主管**
- [P1] 預算核准：Wave 1 合計 2000-3500 萬台幣 / 5 年（原 Phase 2 估 1500-2500 萬，+陳冠能/江國寧/王俊明 需追加 500-1000 萬）
- [P2] 法務 check：
  - (a) 王俊明 TSMC 離職年數 + 商秘獎/專利綁定（影響 #1 最終定位）
  - (b) 銀慶剛 US12354122B2 與 NCKU 鄭芳田 IP 共有狀態
- [P3] URL 可達性 check（phase2/3 agent 產出 ref 部分 placeholder）

## 下一步（下次 session）

### Option A：主管圈選後啟動 Wave 1 接觸 briefing 包
待主管回覆；每位 PI 產 3-5 KB briefing：
- 3 個具體合作題目（預算 × 期程 × KPI × deliverable）
- Email 初次邀約模板（含對教授研究的具體提問）
- 第一次會議議程 + 3 個關鍵問題
- 法務/IP pre-flight checklist

### Option B：若主管延遲，補 Phase 4 替代候選掃描
針對 Wave 1 每位 PI 的「plan B」，各列 2-3 位替代（例如王俊明被拒 → 林勇志 / 廖建能 / 劉致為等）

### Option C：跨領域驗證 template
用 `templates/pi-due-diligence-framework.md` 套用到第二個主題（例如 HBM 材料 PI 或國際比較 Stanford/MIT AI × 2nm），驗證框架通用性 + 累積第二個案例豐富 template

## Resume Prompt

「恢復 hv-research Phase 3 結束狀態。Top 15 PDF v2 已交付主管。方法論 template v1.0 已沉澱。等主管回覆 Wave 1 圈選（6 位）；若等待期可做 Phase 4 替代候選掃描或用 template 啟動第二主題驗證。」
