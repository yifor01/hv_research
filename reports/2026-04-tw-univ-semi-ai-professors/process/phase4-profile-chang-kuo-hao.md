# Phase 4 Profile — 張國浩 Kuo-Hao Chang（NTHU IEEM 特聘教授）

> 補強說明：本份 profile 補強原 TSMC Top 15 漏失之 NTHU IEEM 同系教授（簡禎富、李家岩之外）。Phase 1 候選池僅抓取簡、李兩位，未納入張國浩，屬覆蓋遺漏。

---

## 結論先行

| 項目 | 內容 |
|------|------|
| **Tier 分類** | **Tier A**（強候選，建議擠入 Top 15 替換邊緣人選） |
| **隱形綁定** | 🟡 中度綁定（Powerchip 2 個連續案 2023-2025 + 過去與 Micron 有 Chair Professor 名稱關聯之傳聞——詳 §1）|
| **5 維度總分** | **8 / 10** |
| **一句話摘要** | 模擬最佳化 (Simulation Optimization) 國際頂尖學者，INFORMS Bonder Scholar 唯一台灣得主 + IEEE T-SM Best Paper（半導體領域官方認證），近 2 年明確切入半導體 CVD 機台先進製程控制 (APC)，具 TSMC/UMC/VisEra/ITRI 顧問實績；唯一短板是 Lab 主軸偏 OR/方法論而非 deep-learning-first，與 TSMC AI 部門需要的「VM/缺陷 CV」題目接合需要轉譯。 |

---

## §1 隱形綁定檢查

### 已知產業合作（公開可查）

| 廠商 | 案件性質 | 期間 | 來源 |
|------|----------|------|------|
| **力積電 Powerchip** | CVD 機台先進製程控制系統（大數據+AI） | 2024.07–2025.06 | NTHU IEEM 官方 Research Projects 頁 |
| **力積電 Powerchip** | 薄膜厚度預測（big data + AI） | 2023.07–2024.06 | 同上 |
| **TSMC** | 「最適化決策模型於產品抽樣」、「生產管理決策模型與資訊價值最佳化」（顧問案，年代較早） | 過往 | chang.ie.nthu.edu.tw 自述 |
| **UMC、VisEra（采鈺）、ITRI、YOMURA（鈺豐）** | 多項顧問案 | 過往 | chang.ie.nthu.edu.tw |
| **敦泰電子 FocalTech** | 血壓裝置校正模型（AI） | 2023.07–2024.04 | NTHU IEEM Research Projects |

### 隱形綁定風險評估

- 🟡 **Powerchip 連續 2 年案件**：明顯為主力產業夥伴，但 Powerchip 屬二線晶圓代工/記憶體（非 TSMC、Samsung、Micron 級的「綁定致命」對手）；不影響 TSMC 接合。
- 🟡 **「Micron Chair Professor」傳聞**：搜尋結果中有單一來源（一份 search snippet）提到此頭銜，但 NTHU IEEM 官方 faculty 頁僅標示「Distinguished Professor + Associate Director of NCDR」，未掛 Micron 冠名。**能力限制聲明**：WebSearch 無法確認 Micron 是否曾贊助講座；建議線下向 NTHU IEEM 系辦或 Chang 本人核實。若屬實，則為 🔴 高度綁定（與 TSMC AI 直接競爭的記憶體大廠）；若不實，則為 🟢 安全。
- 🟢 **TSMC 過往顧問案**：屬正面信號（已有合作通道），非排除性綁定。
- 🟢 **政府職務**：兼任 NCDR 副主任（國家災害防救科技中心，2020 起）——屬公部門服務，與半導體無利益衝突，但會佔用其行政時間（影響「個人黃金期剩餘」評分）。

### 結論
**綁定狀態 🟡**——主因是 Micron 冠名的不確定性 + Powerchip 連續產學案。建議 TSMC 投資前先就 Micron 議題正式確認；其餘都是正面或可接受的訊號。

---

## §2 技術契合度

### 核心研究方法論
- **Simulation Optimization（模擬最佳化）**：方法論大師級——STRONG (Stochastic Trust-Region) 與 Stochastic Nelder-Mead Simplex 兩大演算法（兩篇合計 ~280 citations）即出自其手。
- **Stochastic Models / Monte Carlo Simulation**：擅長隨機系統下的決策最佳化。
- **Big Data Analytics + AI for Manufacturing**：近 5 年明確轉向智慧製造應用層。

### 代表論文（半導體相關 + 近期高引）

| # | 標題 | 年/Venue | Citations | TSMC AI 接合度 |
|---|------|---------|-----------|---------------|
| 1 | Risk-Controlled Product Mix Planning in Semiconductor Manufacturing Using Simulation Optimization | IEEE T-SM | （**2017 Best Paper Award**） | ⭐⭐⭐ 直接對應產品組合/排程 |
| 2 | An empirical study of design-of-experiment data mining for yield-loss diagnosis for semiconductor manufacturing | 2014 / J. Intelligent Manufacturing | 92 | ⭐⭐⭐⭐ 良率 root cause |
| 3 | Big data analytics energy-saving strategies for air compressors in the semiconductor industry | 2022 / Int. J. Production Research | 80 | ⭐⭐⭐ Fab 能耗最佳化 |
| 4 | Overall wafer effectiveness (OWE): A novel industry standard for semiconductor ecosystem | 2013 / Computers & Industrial Engineering | 60 | ⭐⭐⭐ Wafer 級 KPI 設計 |
| 5 | STRONG — A new response-surface framework for simulation optimization | 2013 / INFORMS J. Computing | 142 | ⭐⭐ 方法論基底（可賦能 RL/排程） |

### Google Scholar 量化
- **Total citations: 1,908**
- **h-index: 26**（recent: 19）
- **i10-index: 45**

### 與 TSMC AI 部門題目對接

| TSMC AI 題目 | 張國浩可貢獻角度 |
|---------------|-----------------|
| **Fab 排程 / Dispatching** | ⭐⭐⭐⭐ 模擬最佳化是 fab scheduling 的金標準工具，他的 STRONG 演算法可作為 RL 演算法 baseline 比較 |
| **CVD/Thin-Film APC** | ⭐⭐⭐⭐⭐ Powerchip 案就是現在進行式 |
| **良率診斷 (Yield-loss diagnosis)** | ⭐⭐⭐⭐ 2014 那篇即是此題目 |
| **Tool / Equipment 預測性維護** | ⭐⭐⭐ 隨機建模強項 |
| **VM (Virtual Metrology)** | ⭐⭐ 非主軸但有方法論互通性 |
| **缺陷 CV / Defect detection** | ⭐ 不是他的強項（這塊看陳煥宗、徐繼聖等 CV 教授） |

---

## §3 學生 Lab 規模（能力限制聲明）

**能力限制聲明**：Lab 官網 `sites.google.com/site/ssoptimizationlab/` 需 Google 登入無法公開存取；NTHU IEEM 官方頁未列學生數。以下為間接推估：

- **Lab 名稱**：Statistics, Simulation & Optimization Lab（推測，依 URL 命名）
- **預估規模**：以 NTHU IEEM 特聘教授常態 + Powerchip 連續產學案 + 多項 NSTC/業界 funding 推估，**博士生 3-5 人 + 碩士生 8-12 人**（中型偏大實驗室）
- **畢業生去向**（推測）：依 NTHU IEEM 一般軌跡，主流為 TSMC、聯電、Powerchip、Micron、ITRI、本土科技業
- **頂會一作**：以 IEEE T-SM Best Paper 與 EJOR、INFORMS J. Computing 等 OR 頂刊為主——屬 OR 領域頂級期刊，但**非 NeurIPS/ICML 等 AI 頂會**（這是與 TSMC「AI 學界 Top 15」題目方向最大的張力）

### 5 年學生招募潛力評估
- ✅ 中型 Lab + 連續產學案 → 學生 funding 穩定
- ✅ NTHU 工工招生競爭力強
- ⚠️ Lab 主軸 OR/方法論非 deep-learning-first，會與「想做 LLM/CV」的學生有方向落差，可能影響近年招募聲量
- **5 年學生流量推估**：每年 2-3 位碩士、0.5-1 位博士可吸納至 TSMC AI 線

---

## §4 5 維度評分明細

| 維度 | 分數 | 評分理由 |
|------|------|---------|
| **1. 技術命中度** | **2/2** | 半導體 simulation/yield/APC 全打中，IEEE T-SM Best Paper 是業內官方認證；唯有 deep-CV/VM 不是主軸 |
| **2. 5 年學生招募潛力** | **1.5/2** | 中型 Lab 穩定，但 deep learning 學生會偏向其他 PI（如李家岩），扣 0.5 |
| **3. 企業共建長期 Lab 開放度** | **1.5/2** | 過去與 TSMC/UMC/VisEra/ITRI 均有顧問案——開放度高；但目前主力 funding 在 Powerchip + NCDR 公部門服務，重組產學優先序需要 TSMC 主動強誘因 |
| **4. 資源未被搶佔程度** | **1/2** | 🟡 Powerchip 兩年連案明顯排擠工作量；🟡 Micron Chair 待核實——若屬實則扣至 0.5 |
| **5. 個人黃金期剩餘** | **2/2** | 2009 入清華、Purdue PhD 2008，現約 45-50 歲，學術產出黃金期；論文趨勢從 OR 方法論平穩轉向 manufacturing application 的「應用爆發期」；但 NCDR 副主任會佔行政時間，不再扣分（已含於維度 3 的考量） |

### 總分：**8 / 10** — Tier A

> 與 Top 15 中的「邊緣 Tier B」候選（如 Berlin Chen、Yao-Wen Chang、Pau-Choo Chung 等）比較，張國浩的「半導體 application 命中度 + 業界顧問實績」更強，建議**取代 Top 15 中半導體應用接合度較弱的人選**。

---

## §5 合作優缺點 + 3 個合作題目建議

### ✅ 優點
1. **方法論國際頂尖 + 半導體應用深耕**：少數兼具 OR theory（Bonder Scholar）與 fab-floor 經驗（IEEE T-SM Best Paper、Powerchip 兩案）的學者
2. **與 TSMC 已有合作通道**：過往兩個 TSMC 顧問案（產品抽樣、生產管理決策）顯示信任關係已建立
3. **NCDR 副主任職務帶來決策層人脈**：跨部會、跨領域協調經驗加分
4. **論文穩定產出 + i10-index 45**：生涯仍處上升期

### ⚠️ 缺點 / 風險
1. **Micron 綁定不確定性**（最大風險，須先確認）
2. **Lab 非 deep-learning-first**：若 TSMC AI 想要 NeurIPS/ICML 級研究，需找其他人搭配（如李家岩、簡禎富）
3. **Powerchip 連續 2 年案排擠工時**：投資需要設計足以蓋過 Powerchip 的承諾誘因
4. **NCDR 行政負擔**：每週需固定投入公部門事務

### 🎯 3 個合作題目建議

1. **TSMC CVD/PVD 機台先進製程控制 v2**
   - 直接複製 Powerchip 案模型，但用 TSMC fab-scale 資料訓練
   - 預期週期：12-18 個月
   - 交付物：APC 系統 + 期刊論文（IEEE T-SM 命中度高）

2. **Fab 排程模擬最佳化 + RL 混合框架**
   - 結合 STRONG/Nelder-Mead simulation optimization 與 deep RL，做為傳統 dispatching rule 的升級
   - 預期週期：18-24 個月，可接力 SAS-RL（self-supervised + RL）論文線
   - 交付物：可部署於 TSMC fab 的混合排程引擎 + 頂刊論文

3. **產品 mix planning under demand uncertainty（risk-controlled v2）**
   - 接力 2017 IEEE T-SM Best Paper，加入近期 LLM-based demand forecasting 信號
   - 預期週期：12 個月
   - 戰略意義：CFO/COO 級決策支援，能進入 TSMC 高層視野

---

## §6 Reference URL 清單（訪問日期 2026-04-24）

1. **NTHU IEEM 官方 faculty 頁**（職稱、聯絡資訊）
   - https://ieem.site.nthu.edu.tw/p/406-1310-111510,r5910.php?Lang=en
   - 訪問日期：2026-04-24

2. **個人實驗室網頁**（chang.ie.nthu.edu.tw）
   - https://chang.ie.nthu.edu.tw/about.php
   - 訪問日期：2026-04-24
   - 含：研究領域、產業合作清單（TSMC/UMC/VisEra/YOMURA/ITRI）、獎項

3. **Google Scholar 個人檔案**（量化指標、論文清單）
   - https://scholar.google.com/citations?user=ZfWgbacAAAAJ&hl=en
   - 訪問日期：2026-04-24
   - Total citations 1,908 / h-index 26 / i10-index 45

4. **NTHU IEEM Research Projects 頁**（半導體產學案明細）
   - https://ieem.site.nthu.edu.tw/p/404-1310-39354.php?Lang=en
   - 訪問日期：2026-04-24
   - 含：Powerchip 2 個連續案 (2023-2025)、FocalTech、ITRI、MOST 計畫

5. **科技大觀園專訪**（個人背景與研究故事）
   - https://scitechvista.nat.gov.tw/Article/c000003/detail?ID=9e3093cb-69e8-4684-b64d-b70cfebb636d
   - 訪問日期：2026-04-24
   - 含：5 年內 4 項技轉、2 項專利、13 項產學合作的自述

6. **Asia-Pacific J. Operational Research 2024 review article**（近期方法論回顧）
   - https://www.worldscientific.com/doi/10.1142/S0217595924400086
   - 訪問日期：2026-04-24
   - 篇名：Simulation Learning and Optimization: Methodology and Applications

---

**能力限制總聲明**：本份 profile 多項數據（Lab 學生數、Micron Chair 確認、最新 unpublished 產學案、TSMC 內部評價）僅靠 WebSearch + WebFetch 無法直接驗證；建議線下向 NTHU IEEM 系辦或張國浩本人正式核實後再做最終投資決策。
