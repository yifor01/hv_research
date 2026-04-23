# Handoff — Top 15 PDF v3.2 完成（三輪迭代後定版） — 2026-04-23

Generated: 2026-04-23 12:10 Asia/Taipei
Branch: master
Status: v3.2 PDF 定版並 push；等主管回覆第一波圈選

## v3.0 → v3.1 → v3.2 迭代歷程

| 版本 | 變動 | 原因 |
|---|---|---|
| v3.0 | 初版重排版（移除 Phase/Batch/Wave 字樣） | 主管看不懂內部流程 |
| v3.1 | 移除彭文志 | 業界內部消息：已借調 TSMC 當處長，非合作候選 |
| **v3.2** | **（1）移除關鍵字矩陣表（2）每位教授 section 加專長標籤列（3）取消王俊明法務顧慮（4）新增附錄 E 資料來源** | **PDF 矩陣表太寬被切；王俊明本就是 SAT-TSMC 體制內合作方；主管需可查證 refs** |

## v3.2 交付（38 頁 / 692 KB）

### 主檔
- **PDF**：`reports/2026-04-tw-univ-semi-ai-professors/TSMC_Top15_長期投資分析_v3.pdf`（38 頁 / 692 KB）
- **合併 MD**：`TSMC_Top15_長期投資分析_v3.md`（1222 行 / 54,424 字元）

### 分檔 MD（5 份，矩陣已刪）
- `TSMC_Top15_v3_00_封面與摘要.md`
- `TSMC_Top15_v3_01_大表.md`（15 位 × 11 欄）
- `TSMC_Top15_v3_02_教授檔案_1-8.md`（王俊明 → 江國寧）
- `TSMC_Top15_v3_03_教授檔案_9-16.md`（宋振銘 → 黃瀚萱，檔名保留）
- `TSMC_Top15_v3_05_附錄.md`（策略 / 預算 / 法務 / **資料來源**）
- 已刪除：`TSMC_Top15_v3_04_關鍵字矩陣.md`

### v3.2 關鍵改動

#### 1. 關鍵字矩陣 → 標籤列（修復 PDF 切斷）
- 刪除整個矩陣檔 `v3_04_關鍵字矩陣.md`
- 每位教授 section 頂部加一行 `**專長標籤**：`kw1` · `kw2` · `kw3` · `kw4` · `kw5``
- 15 位教授 × 2-5 個 backtick-quoted 關鍵字

#### 2. 王俊明 TSMC 綁定顧慮取消
- **釐清**：SAT 中心本身是 TSMC 支持設立的，王為體制內合作方，非離職自由身
- 大表：移除 `*` 與「法務 check 後定案」註記
- 個別檔案 #1：缺點段移除離職年數 / 商秘綁定 / 競爭關係敏感三條；建議合作方式改為「在既有 SAT-TSMC 合作框架下擴大」
- 附錄 C：完整刪除 C.1 王俊明 checklist；重編號保留 銀慶剛 IP / 鄭桂忠 TSMC-JDP / 胡璧合 美光 Chair 等其他 check
- 隱形綁定風險統計：🟢 10→11 / 🟡 4→3 / 🔴 1→0

#### 3. 附錄 E：Reference Sources（供主管查證）
新增於 `v3_05_附錄.md` 末尾：
- **E.1 每位教授公開資料**：15 位 × 3-6 個 URL（共 76 個公開連結）
  - 學校官方教授頁 / Google Scholar / DBLP / Lab 頁 / 獎項公告 / 機構 Hub
- **E.2 方法論與框架**：template + integrated-ranking 檔案引用
- **E.3 驗證紀錄**：phase3-verification-notes.md 引用
- **E.4 能力限制聲明**：列出 WebSearch 無法獨立驗證的類別（Lab 人數、私約、借調動態等）

### 資料正確性驗證
- `phase3-verification-notes.md`
- 16 位 WebSearch 平行驗證
- **完全確認無誤**：14 位
- **職位失效（已移除）**：1 位（彭文志）
- **合作狀態釐清（取消法務 check）**：王俊明 — 體制內合作方
- **疑似需更正（v3 已保守化）**：江國寧（職銜）、林嘉文（合聘）
- **未驗證（維持原文）**：詹寶珠 2026 院長任期、黃瀚萱 TAIDE 顧問、各 PI Lab 人數

## 4 個互補題目組（v3.2 下）

1. **前段 Device（2nm/A16）**：王俊明 / 馬誠佑 / 胡璧合（3 位）
2. **CoWoS 封裝**：陳冠能 / 陳智 / 江國寧 / 宋振銘（4 位）
3. **Fab AI 方法論**：銀慶剛 / 詹寶珠 / 李家岩 / 蔡佩璇 / 鄭桂忠（5 位）
4. **人員效率 RAG**：蔡銘峰 / 黃瀚萱（2 位；原彭文志 Agentic 路線缺）

## 預算估算

| 波次 | 位數 | 5 年總預算 |
|---|---|---|
| 第一波 | 6 位 | 2000-3500 萬 |
| 第二波 | 7 位 | 1500-2500 萬 |
| 第三波 | 1 位（林嘉文）| 300-500 萬 |
| **合計** | **15 位** | **3800-6500 萬 NTD** |

## Git 狀態

已 push 到 `origin/master`：
- `d1c8dfb feat: v3 初版`
- `0359fcc chore: handoff v3`
- `ad0f6c6 fix: v3.1 移除彭文志`
- `<new> fix: v3.2 移除關鍵字矩陣 + 王俊明 TSMC 綁定釐清 + 新增附錄 E`

## 關鍵 Lessons Learnt（本次 session）

### Lesson 1：WebSearch 能力邊界
- **彭文志案例**：WebSearch 2 次不同查詢都找不到他已借調 TSMC
- **結論**：企業內部借調 / 任命 / 私約等**非公開事件 WebSearch 不可見**
- **對後續工作的意義**：Top 15 接觸前**必須透過業界內部管道 double-check 現職狀態**

### Lesson 2：避免誤判 TSMC 體制內合作方
- **王俊明案例**：原以為是「TSMC 前員工轉任學界」需法務 check，實際是「體制內 SAT 中心合作方」
- **結論**：判斷 PI 的 TSMC 綁定時**必須區分**：
  - 離職後自由身（需 check 競業 / 商秘）
  - 體制內合作方（無離職綁定疑慮，反而是現成合作管道）
- **已寫入**：`templates/pi-due-diligence-framework.md` 可新增此判斷節點

### Lesson 3：報告排版要預留可查證路徑
- **原缺失**：v3 初版沒有 Reference sources 附錄，主管/HR/法務無法獨立驗證
- **已修復**：v3.2 新增附錄 E（76 個公開 URL）
- **template 建議**：`pi-due-diligence-framework.md` 增補「交付文件必附 Reference URL」規範

## 未完成

- [P1] 主管圈選第一波（6 位）接觸 owner — 等主管
- [P1] 預算核准：第一波 2000-3500 萬 / 5 年
- [P2] 法務 check（精簡版）：
  - (a) 銀慶剛 US12354122B2 與 NCKU 鄭芳田 IP 共有狀態
  - (b) 鄭桂忠 TSMC-JDP 既有題目盤點
  - (c) 胡璧合 美光 Chair 合作範圍
  - ~~(d) 王俊明 TSMC 綁定~~ ✅ 已釐清為體制內合作方
- [P2] Agentic IR 方向是否補人（彭文志移除後空缺）
- [P3] `templates/pi-due-diligence-framework.md` 新增三條 lesson

## 下一步

### Option A（主流）：主管圈選後啟動第一波接觸 briefing 包
每位 PI 產 3-5 KB briefing：合作題目 × 預算 × 期程 × KPI；Email 模板；會議議程；法務 pre-flight（簡化後的 B/C）。

### Option B：Agentic IR 替代人選補位
掃描 NYCU/NTU/AS 其他 Agentic AI / Decomposed IR PI。

### Option C：替代候選快速掃描
針對第一波每位 PI 的 plan B。

### Option D：方法論 template 迭代
把本次三個 Lessons 寫入 `pi-due-diligence-framework.md`。

### Option E：跨領域驗證 template
用 template 套用到第二主題（HBM 材料 / 國際比較）。

## Resume Prompt

「恢復 hv-research：v3.2 PDF 已定版（38 頁 / 15 位 / 附錄 E 76 個 URL / 王俊明 TSMC 綁定已釐清 / 彭文志已移除）。下一步：主管圈選第一波；或補方法論 template lessons；或啟動第二主題驗證。」
