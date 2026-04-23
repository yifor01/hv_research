# Handoff — Top 15 PDF v3.1 完成（移除彭文志後定版） — 2026-04-23

Generated: 2026-04-23 11:40 Asia/Taipei
Branch: master
Status: v3.1 PDF 定版並 push；等主管回覆第一波圈選

## 本次 session 交付

### v3.1 PDF（39 頁 / 682 KB）

主檔：`reports/2026-04-tw-univ-semi-ai-professors/TSMC_Top15_長期投資分析_v3.pdf`

**v3 → v3.1 關鍵變動**：移除彭文志。他已借調 TSMC 擔任處長（業界內部消息），非合作候選。Top 15 由並列 16 人回到 15 人。

### 分檔 MD（6 份 + 合併檔）
- `TSMC_Top15_v3_00_封面與摘要.md`
- `TSMC_Top15_v3_01_大表.md`（15 位 × 11 欄）
- `TSMC_Top15_v3_02_教授檔案_1-8.md`（王俊明 → 江國寧）
- `TSMC_Top15_v3_03_教授檔案_9-15.md`（宋振銘 → 黃瀚萱，原檔名保留）
- `TSMC_Top15_v3_04_關鍵字矩陣.md`（15 位 × 20 關鍵字）
- `TSMC_Top15_v3_05_附錄.md`
- 合併：`TSMC_Top15_長期投資分析_v3.md`（1,163 行 / 49,448 字元）

### 資料正確性驗證
- `reports/2026-04-tw-univ-semi-ai-professors/phase3-verification-notes.md`
- 16 位 WebSearch 平行驗證
- **完全確認無誤**：14 位
- **職位失效（從名單移除）**：1 位 — 彭文志（已借調 TSMC 當處長）
- **疑似需更正（v3 已保守化）**：江國寧、林嘉文
- **未驗證維持原文**：王俊明 TSMC 任職年數、詹寶珠 2026 院長任期、黃瀚萱 TAIDE 顧問、各 PI Lab 精確人數

### 重要 Lesson — WebSearch 驗證能力限制
彭文志借調 TSMC 一事 **WebSearch 查不到**（2 次不同查詢皆無結果）。企業內部借調/任命通常不公開，即使有新聞稿也常延遲或模糊。

**結論**：
- WebSearch 可驗證「學校職位、公開論文、獎項、公開專利」
- WebSearch **無法驗證**「產業內部借調、顧問私約、商業合作未公開者」
- 後續產業洞察類驗證 **必須倚靠業界電話 / 內部管道**，不能全依 web search
- 已在 `phase3-verification-notes.md` 留下能力限制備註，供未來 session 借鏡

## 結構革新（vs v2）
- 禁忌詞全清：0 個 Phase / Batch / Wave
- 兩層結構：Top 15 長期投資名單 → 個別教授分析
- 11 欄大表：排名 / 姓名 / 校系 / 專長領域 / 代表實績 / 合作企業 / 落地 / 製程封裝應用 / 學生素養 / 長期投資 Tier / NVIDIA-Google / 補充
- 三段細節：每位教授 (1) 技術契合度 (2) 學生素養 (3) 合作分析
- 頁數 76 → 39 頁（更聚焦）

## 4 個互補題目組（v3.1 下）

1. **前段 Device（2nm/A16）**：王俊明 / 馬誠佑 / 胡璧合（3 位）
2. **CoWoS 封裝**：陳冠能 / 陳智 / 江國寧 / 宋振銘（4 位，材料/系統/AI/量測互補）
3. **Fab AI 方法論**：銀慶剛 / 詹寶珠 / 李家岩 / 蔡佩璇 / 鄭桂忠（5 位）
4. **人員效率 RAG**：蔡銘峰 / 黃瀚萱（2 位，傳統 vs CAG 對照；原彭文志的 Agentic 路線暫缺）

## 預算估算（v3.1 更新）

| 波次 | 位數 | 5 年總預算 |
|---|---|---|
| 第一波 | 6 位 | 2000-3500 萬 |
| 第二波 | 7 位 | 1500-2500 萬 |
| 第三波 | 1 位（林嘉文）| 300-500 萬 |
| **合計** | **15 位** | **3800-6500 萬 NTD** |

## Git 狀態

已 push 到 `origin/master`：
- `d1c8dfb feat: Top 15 教授投資分析 PDF v3` （v3 初版，含彭文志）
- `0359fcc chore: handoff v3`
- `<new> fix: 移除彭文志（已借調 TSMC）— v3.1 定版` （本次）

## 未完成

- [P1] 主管圈選第一波（6 位）接觸 owner — 等主管
- [P1] 預算核准：第一波 2000-3500 萬 / 5 年
- [P2] 法務 check：
  - (a) 王俊明 TSMC 離職年數 + 商秘獎/專利綁定
  - (b) 銀慶剛 US12354122B2 與 NCKU 鄭芳田 IP 共有狀態
  - (c) 鄭桂忠 TSMC-JDP 既有題目盤點
- [P2] **新增：Agentic IR 方向是否補人**（彭文志移除後空缺）— 可考慮延攬國際 PI 或提升蔡銘峰 / 黃瀚萱合作規模
- [P3] URL 可達性 check

## 下一步

### Option A（主流）：主管圈選後啟動第一波接觸 briefing 包
每位 PI 產 3-5 KB briefing：合作題目 × 預算 × 期程 × KPI；Email 模板；會議議程；法務 pre-flight。

### Option B：Agentic IR 方向補人（彭文志空缺）
掃描替代候選：NYCU/NTU/AS 其他 Agentic AI / Decomposed IR PI，或降級用蔡銘峰 + 黃瀚萱擴大合作。

### Option C：替代候選快速掃描
針對第一波每位 PI 的 plan B，各列 2-3 位。

### Option D：跨領域驗證 template
用 `templates/pi-due-diligence-framework.md` 套用到第二主題（HBM 材料 / 國際比較）。

## Resume Prompt

「恢復 hv-research：v3.1 PDF 已定版（39 頁 / 15 位 / 禁忌詞全清 / 已移除彭文志）。等主管回覆第一波 6 位圈選；若等待期可補 Agentic IR 替代人選或啟動第二主題驗證 template。」
