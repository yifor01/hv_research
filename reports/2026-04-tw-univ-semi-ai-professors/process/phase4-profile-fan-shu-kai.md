# Phase 4 Profile — 范書愷 Shu-Kai S. Fan（NTUT 工業工程與管理系 特聘教授兼管理學院院長）

> 訪查日期：2026-04-24　|　phase 1 評級「⭐⭐⭐⭐⭐ 待核實」 → phase 4 確認

---

## 結論先行

**Tier：A（Backup PDF 強烈建議入榜，置於 36-50 段最前列）**

- **姓名核實 OK**：范書愷確為 NTUT 工管系教授，英文 Morris Fan = Shu-Kai S. Fan，無同名混淆。
- **職等高於預期**：不僅是教授，目前任 **NTUT 管理學院院長 + 特聘教授**，並為 Engineering Optimization (Taylor & Francis) **首位亞洲主編**。
- **半導體 VM/APC 命中度極高**：研究主軸明確為「半導體先進製程控制 (APC) + Virtual Metrology + 良率機器學習」，且論文中明文寫到「a leading semiconductor manufacturing company in Taiwan」實證合作 — 實質指向 TSMC/UMC 等級客戶。
- **唯一弱點**：技職體系 + 工管系出身，學生規模可能不及 NTU/NTHU/NYCU 電機所，但對 TSMC IE/MFG/良率工程職位反而 **是強匹配**。

**對 TSMC 的價值**：可作為 **VM/APC 演算法外部第二意見 + 工管系大量 IE 工程師輸送源**，非 IC design / device 主流派但補強「製造資料科學」缺口。

---

## §1 隱形綁定檢查

| 檢查項 | 結果 |
|---|---|
| 是否已是 TSMC 顧問 / 借調 | **無公開資訊** — 但其 2022 CIE 論文明確致謝 a leading TSMC-class fab 提供資料,推測有 NDA-level 合作 |
| 是否陽明交大/清大聯合中心 PI | 否（NTUT 體系獨立） |
| 是否聯電 / 力積電董事 / 顧問 | 無公開資訊 |
| 是否有美國 fab 同步合作 (Intel/GF) | 無公開資訊；學經歷在 UTArlington,網路偏 US 工管圈 |
| 是否兼任新創 CTO/共同創辦人 | 未見公開記錄 |

**判斷**：無強隱形綁定,**TSMC 可主動接觸**,但需注意他可能已私下與某 fab 有 VM 案合作（論文實證資料來源指向）— 建議首談時直接問清。

---

## §2 技術契合度（對 TSMC AI Top 痛點）

### 命中項目
- **Virtual Metrology (VM)** —— 直接命中 fab APC 痛點;2022 CIE 論文 "Decision-based virtual metrology for advanced process control" 整合 Isolation Forest 分群 + Random Forest 迴歸,且在台灣半導體大廠落地驗證。
- **Wafer Map Defect Classification** —— 2024 兩篇:"A new ViT-based augmentation framework for wafer map defect classification" + "Auto-Labeling for Pattern Recognition of Wafer Defect Maps"。直接對應 fab 良率工程師日常工作。
- **Photomask AI** —— 2024 "AI transformation model — pod redesign of photomasks in semiconductor manufacturing"（J. Industrial and Production Engineering）— 罕見的工管學者跨入光罩議題。
- **Rolling-Window VM (2025 IEEE)** —— "A Novel Rolling-Window and Production-Maintenance-Based Machine Learning Approach to Virtual Metrology" — 結合維護排程,fab planning 角度有實用性。

### 弱項
- 不做 device-level AI、不做 EUV/OPC 物理建模、不做 IC layout — **純資料科學派**。
- 對 GPU 大模型 / LLM 涉獵屬「探索」階段(個人頁列大語言模型,但無代表作）。

**契合度評分**：**1.5/2** — VM/wafer map/photomask 三項都打到痛點,但廣度受限於工管系定位。

---

## §3 學生 Lab 規模與流向（技職體系觀察）

- 實驗室名稱：**大數據分析與智慧計算實驗室** + Engineering Data Analysis and Optimization Laboratory
- 招生規模：NTUT 工管系碩班每年規模約 30-40 人,范老師組推測 8-12 位碩生 + 2-3 位博生（典型工管教授 lab）
- **流向預測**:
  - 主流向 → TSMC IE 處 / MFG / 良率工程師（碩班學生最大宗,非設計類職缺）
  - 次流向 → 聯電、力積電、日月光 IE / quality
  - 少數 → 鴻海、和碩 manufacturing 資料分析職位
- **技職特色**：學生實作技能強、SQL/Python/Minitab 上手快,**進 fab 即戰力高於 NTU IE 同班**;但 fundamental theory 厚度通常較低。

**5 年招募潛力評分**：**2/2** — TSMC 工程職一年 100+ 名額對 NTUT 工管系是穩定來源,加上院長加持可開「定向班」。

---

## §4 5 維度評分明細

| 維度 | 分數 | 理由 |
|---|---|---|
| 1. 技術命中度 | **1.5/2** | VM/wafer map/photomask 三項都實證落地,但純資料科學派、無 device 整合 |
| 2. 5 年學生招募潛力 | **2.0/2** | 工管系穩定流向 IE 工程職,院長身分可促成定向合作 |
| 3. 企業共建長期 Lab 開放度 | **1.5/2** | 已有 fab 實證合作經驗(NDA)、行政權力大、技職院校產學文化活躍 |
| 4. 資源未被搶佔程度 | **1.5/2** | 無強隱形綁定,但可能已有 fab NDA 案;非顯赫名教授,競爭壓力低 |
| 5. 個人黃金期剩餘 | **1.0/2** | 1996 PhD,推估 1968 年生左右,黃金期約 5-7 年;院長行政負擔可能稀釋研究時間 |
| **合計** | **7.5/10** | **Tier A**(進 backup 36-50 名單,可放前段) |

---

## §5 合作優缺點 + 3 個合作題目建議

### 優點
- **工管系 + APC 跨界稀缺**：台灣多數 VM 研究來自 NYCU 電機/工工(王琮裕、陳麗芬等),NTUT 工管系角度是新觀點;
- **行政權力大、執行力強**：院長身分可短期內動員系內資源開定向班;
- **論文 → fab 落地路徑成熟**：CIE 2022 論文已有實證模板,新案可快速啟動;
- **Engineering Optimization 主編**：學術網絡廣,可作為 TSMC 對外發表 / 期刊布局合作對象。

### 缺點
- **lab 不大、無 GPU 集群**：跑不動大模型訓練,適合中小型 ML/data analytics 案而非 LLM/CV foundation model;
- **行政負擔重**：院長 + EMBA 執行長 + 學會召集人,實際投入單一 industry 專案的時間有限;
- **可能已有 fab NDA**：若 TSMC 接觸前不確認,可能撞題或踩到競爭對手案。

### 3 個合作題目建議

1. **「跨機台 / 跨配方 VM 模型泛化框架」**（小型 PoC,6-9 個月）
   - 以 CIE 2022 論文的 Isolation Forest + Random Forest 為基礎,延伸到 N-1 / N-2 製程節點 fleet-wide deployment;
   - TSMC 提供匿名 FDC 資料,范老師團隊建模,目標降低 VM 重訓練頻率 50%。

2. **「Wafer Map Defect Pattern Auto-Labeling Pipeline」**（中型,1-2 年）
   - 接續 2024 ViT augmentation + auto-labeling 兩篇,延伸到 N5/N3 高密度 wafer map;
   - 整合 active learning 降低工程師標註成本,目標單顆 wafer 標註時間 < 5 分鐘。

3. **「定向班 + JDP 雙軌:NTUT 工管系 VM 工程師培育計畫」**（戰略級,3-5 年）
   - 院長身分可促成系上 30-40 人/年的碩班學生,部分課程由 TSMC 工程師授課;
   - 對 TSMC 是穩定 IE/yield engineer 人才源,對 NTUT 是品牌升級;雙贏。

---

## §6 Reference URL 清單

1. [范書愷 個人頁(中) — NTUT 工管系](https://iem.ntut.edu.tw/p/405-1081-121127,c3754.php?Lang=zh-tw)（訪 2026-04-24)
2. [Professor Shu-Kai Fan — NTUT IEM (EN)](https://iem.ntut.edu.tw/p/405-1081-65517,c11955.php?Lang=en)（訪 2026-04-24）
3. [Shu-Kai Fan — Elsevier Pure NTUT Profile（98 publications, h=29）](https://ntut.elsevierpure.com/en/persons/shu-kai-fan)（訪 2026-04-24）
4. [Shu-Kai Fan — ResearchGate(2,753 citations,107 publications)](https://www.researchgate.net/profile/Shu-Kai-Fan)（訪 2026-04-24)
5. [范書愷--北科大管理學院院長 — Technice](https://www.technice.com.tw/experts/173619/)（訪 2026-04-24)
6. [北科大教授范書愷榮任工程國際期刊首位亞洲主編 — 經濟日報](https://money.udn.com/money/story/5723/4787811)（訪 2026-04-24)
7. [Decision-based virtual metrology for APC empirical study(CIE 2022,Taiwan semi fab 落地)](https://www.sciencedirect.com/science/article/abs/pii/S0360835222003151)（訪 2026-04-24)
8. [Rolling-Window VM 2025 IEEE](https://ieeexplore.ieee.org/document/11006089/)（訪 2026-04-24)

---

**Phase 4 結論**：范書愷是 phase 1「待核實」名單中,Phase 4 最值得提拔者。建議 Backup PDF 36-50 段 **置於最前**,加註「VM/APC 工管派代表 + NTUT 管院院長」標籤。
