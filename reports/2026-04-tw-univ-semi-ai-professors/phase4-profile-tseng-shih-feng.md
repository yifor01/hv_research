# Phase 4 Profile — 曾釋鋒 Shih-Feng Tseng（NTUT 機械工程系 教授兼系主任）

> 訪查日期：2026-04-24

---

## 結論先行

**Tier：B（Backup PDF 建議入榜,置於 36-50 段中段；以「設備/封裝雷射加工」標籤獨特定位）**

- **職等核實 OK**：曾釋鋒為 NTUT 機械系**教授兼系主任**,交大機械所博士,亦為製造科技研究所合聘師資。
- **半導體相關 deliverable 確實存在**：核心代表作為 **silicon wafer dicing 雷射切割**(Optics & Laser Technology 2018,multilayer stack on Si wafer UV laser direct dicing & milling)— 與 TSMC 後段 / 半導體設備商高度相關。
- **AI 命中度低**：研究核心是雷射光機物理 + CAD/CAM,非 AI/ML 派;但實驗室「光製造與檢測實驗室」名稱含「檢測」,可能有智慧感測器 ML 應用。
- **141 篇論文、1,686 citations**(ResearchGate)— 學術產出穩定,但屬「應用物理 / 雷射工程」社群,不在 TSMC AI Top 15 主流戰場。

**對 TSMC 的價值**：**設備派代表** — 對 wafer dicing / stealth dicing / 微孔加工 / TGV (Through-Glass Via) 等先進封裝工序有直接技術切入點;但與 TSMC「AI 教授」主題契合度較低,**建議定位為設備合作而非 AI 合作**。

---

## §1 隱形綁定檢查

| 檢查項 | 結果 |
|---|---|
| 是否已是 TSMC 顧問 | 無公開資訊;但研究主題與 TSMC 後段(dicing)有高重疊,可能有 NDA 案 |
| 是否與 ASM Pacific / Disco / 漢民 等設備商合作 | **可能性高** — 雷射 wafer dicing 是設備商核心技術,但無公開合作公告 |
| 是否聯電 / 力積電 顧問 | 無公開資訊 |
| 是否陽明交大/清大聯合中心 PI | 否（NTUT 機械系獨立） |
| 是否兼任新創 CTO/共同創辦人 | 未見公開記錄 |

**判斷**：無公開強綁定,但雷射加工領域業界合作頻繁,實際隱形綁定可能性中等。建議接觸前先 query ITRI 雷射中心、漢民、雷虎等業者是否已有合作。

---

## §2 技術契合度（對 TSMC AI Top 痛點）

### 命中項目
- **Silicon Wafer 雷射切割 (2018 Optics & Laser Tech)** —— Multilayer stack on silicon wafer 直接 UV 雷射 dicing/milling,對應 TSMC backend dicing process 痛點。
- **Stealth Dicing / Laser Ablation Dicing 技術族群** —— 業界 trend(取代傳統 blade dicing,適用於 ultra-thin wafer < 50μm)— 曾老師方向 fits。
- **光機系統 + 智慧感測器** —— 對應 fab 內部量測設備 retrofit / 感測器升級。
- **Graphene / Thin Film / Glass Substrate 雷射加工** —— 跨入 advanced packaging glass interposer (TGV) 議題。

### 弱項
- **完全不做 AI/ML 主軸** —— 雖有「智慧感測器」字眼,但無 deep learning 代表論文;
- **無 wafer map / VM / 良率 ML 任何切入點** —— 與 phase 1-2 Tier S 候選完全不同戰場;
- **學術社群與 TSMC AI Top 名單脫鉤** —— 屬光學/物理會議圈,不在 IEDM/ISSCC/MLSys 雷達上。

**契合度評分**：**0.5/2** —— 設備技術命中,但 AI 角度幾乎無;依「TSMC 學界 AI PI」定義屬邊緣。

---

## §3 學生 Lab 規模與流向

- 實驗室名稱：**光製造與檢測實驗室**（綜合科館 707-1、B13-5）
- 招生規模：機械系系主任,推測 lab 規模 10-15 人(碩+博);141 篇論文意味多年累積大量學生
- **流向預測**:
  - 主流向 → **半導體設備商**：漢民科技、亞智科技(ASYS)、東捷、雷虎科技;**外商**：Disco、ASMPT、Applied Materials Taiwan
  - 次流向 → TSMC / 聯電 後段 dicing / packaging 設備工程師
  - 少數 → ITRI 雷射中心、工研院機械所
- **技職特色**：學生實作雷射光機系統能力強,**設備廠搶手**;但 fab 內部直接招募數量小於工管系。

**5 年招募潛力評分**：**1.0/2** — 設備工程師補強牌,fab 直接招募人數有限。

---

## §4 5 維度評分明細

| 維度 | 分數 | 理由 |
|---|---|---|
| 1. 技術命中度 | **0.5/2** | 雷射 dicing 設備派命中,AI 角度幾乎無 |
| 2. 5 年學生招募潛力 | **1.0/2** | 設備廠搶手,fab 直接招募有限 |
| 3. 企業共建長期 Lab 開放度 | **1.5/2** | 系主任行政力強,雷射業界合作文化活躍 |
| 4. 資源未被搶佔程度 | **1.0/2** | 雷射加工業界合作密集,可能已被設備廠占用 |
| 5. 個人黃金期剩餘 | **1.5/2** | 推估 1970-72 出生,黃金期 7-10 年 |
| **合計** | **5.5/10** | **Tier B**(進 backup 36-50 段,定位「設備合作」非「AI 合作」) |

---

## §5 合作優缺點 + 3 個合作題目建議

### 優點
- **設備技術稀缺**：fab 內部 dicing 製程改善需要外部光機專家,曾老師是 NTUT 體系最強候選;
- **跨足 advanced packaging glass interposer (TGV) 議題**：對 TSMC CoWoS 玻璃載板路徑(2027+)有前瞻價值;
- **141 篇論文穩定產出**：學術紀律強,合作後可確保 deliverable;
- **系主任行政權**：可整合機械系資源開定向課程。

### 缺點
- **AI 主題契合度低**：若 TSMC 內部 KPI 是「AI 教授」,曾老師打分數會被低估;
- **設備合作可能已被 Disco/ASMPT 包走**：雷射 dicing 是業界 hot topic,接觸前需 due diligence;
- **與 phase 1-2 Top 15 主流社群脫鉤**：不在同一研討會 / 期刊圈,跨界協作成本高;
- **個人頁產學案資訊極少**：透明度低,需直接 Email 確認。

### 3 個合作題目建議

**注意**:這 3 個題目以「設備合作」為主軸,不適合作為「AI 合作」題目。

1. **「Ultra-Thin Wafer Stealth Dicing 良率優化(Sub-40μm)」**（中型,1 年）
   - 對應 TSMC 3D IC / SoIC 超薄晶圓堆疊需求;
   - 結合曾老師 UV laser direct dicing 經驗 + TSMC 現場實證,目標 chipping 缺陷 < 5μm。

2. **「TGV (Through-Glass Via) 雷射鑽孔 PoC」**（前瞻,1.5 年）
   - 為 TSMC 2027+ glass interposer 路徑準備;
   - 玻璃基板雷射微孔加工,孔徑 50μm、AR 5:1。

3. **「智慧感測器 + ML 雷射加工製程監控」**（橋接 AI,2 年）
   - 將曾老師原本的「智慧感測器」與 TSMC fab AI infrastructure 串接;
   - 目標：dicing 製程線上 ML monitoring,異常即時 alert。**唯一一題能勉強掛上 AI 標籤**。

---

## §6 Reference URL 清單

1. [曾釋鋒教授 — NTUT 機械系(中)](https://me1.ntut.edu.tw/p/405-1062-84682,c13043.php?Lang=zh-tw)(訪 2026-04-24)
2. [Professor Shih-Feng Tseng — NTUT 製造科技研究所](https://imt.ntut.edu.tw/p/405-1065-87844,c382.php?Lang=en)（訪 2026-04-24)
3. [Shih-Feng Tseng — ResearchGate(141 publications,1,686 citations)](https://www.researchgate.net/profile/Shih-Feng-Tseng)(訪 2026-04-24)
4. [Multilayer stack materials on silicon wafer dicing using UV laser — Optics & Laser Technology 2018](https://www.sciencedirect.com/science/article/abs/pii/S0030399218301889)（訪 2026-04-24)
5. [SHIH-FENG TSENG — NTUT Pure 個人頁](https://ntut.elsevierpure.com/en/persons/shih-feng-tseng/)（訪 2026-04-24)
6. [光製造與檢測實驗室 — NTUT 學術資源網](https://academic.ntut.edu.tw/5157/)（訪 2026-04-24)

---

**Phase 4 結論**：曾釋鋒以「半導體後段雷射 dicing 設備合作」獨特定位,對「TSMC 學界 AI Top 名單」契合度偏低。**建議 Backup PDF 收錄,但放在「設備合作」分類欄位,不與 AI 教授混排**;若 backup PDF 沒有「設備派」分類,可改放置技術備援名單,不主推。
