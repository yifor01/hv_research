# Phase 4 Profile — 許嘉裕 Chia-Yu Hsu（NTHU IEEM 教授）

> 補強說明：本份 profile 補強原 TSMC Top 15 漏失之 NTHU IEEM 同系教授（簡禎富、李家岩之外）。
>
> **重要釐清**：許嘉裕的職涯軌跡為 Yuan Ze University → NTUST 工業管理系（2018?-2023?）→ **NTHU IEEM**（近期轉任，依 Google Scholar 自報的 affiliation 與 NTHU 工學院公告的「陳樹勛先生紀念講座」皆顯示其現職為清華 IEEM）。但他在 2023 年外部活動（HTFA、AI Academy Conf）仍掛 NTUST 銜，因此最近 1-2 年完成轉任。**能力限制聲明**：WebSearch 無法精確查到轉任年月；建議線下向 NTHU IEEM 系辦核實。

---

## 結論先行

| 項目 | 內容 |
|------|------|
| **Tier 分類** | **Tier A-（強候選，但需確認 NTHU 在職狀態與設備就位時程）** |
| **隱形綁定** | 🟢 安全（無大廠獨家綁定；TSMC 過去有資料贊助但屬學術合作層級——詳 §1）|
| **5 維度總分** | **7.5 / 10** |
| **一句話摘要** | 智慧製造 / wafer bin map / fault detection 領域中生代代表，Google Scholar 2,543 citations、h-index 24，2020 NSTC 吳大猷獎得主；長年以「非 TSMC 御用」中立第三方身份做半導體 yield/defect/FDC 研究，剛轉至 NTHU IEEM 是新血力作，與簡禎富、李家岩同系形成「智慧製造三人組」，互補性高但定位有部分重疊。 |

---

## §1 隱形綁定檢查

### 已知產業合作（公開可查）

| 廠商 | 案件性質 | 期間 | 來源 |
|------|----------|------|------|
| **TSMC** | Award number 110HZA3K00G——資助 wafer map retrieval 真實資料蒐集（屬 TSMC 學術合作通用編號） | ~2021 | J. Intelligent Manufacturing 2023 論文 acknowledgement |
| **半導體製造業者** | 多個產業實證合作（晶圓良率、缺陷檢測） | 持續 | 2020 吳大猷獎介紹頁 |
| **面板製造、被動元件、PCB、3C 零組件、設備商** | 跨產業實證 | 持續 | 同上 |

### 隱形綁定風險評估

- 🟢 **TSMC 110HZA3K00G**：屬 TSMC 學術界普及型贊助編號（許多教授拿過），非 exclusive partnership；反而是「TSMC 已開門讓他用 fab 資料」的正面信號
- 🟢 **無 Micron / Samsung / Intel 等大廠獨家綁定的公開紀錄**
- 🟢 **跨產業實證**：他做的不只半導體，也涵蓋面板（友達、群創？未公開）、PCB、被動元件——這意味著他不是任何一家獨家的人
- 🟡 **中國工業工程學會秘書長（2023-2024）**：屬學會服務性職位，會佔用一定行政時間但有助於業界 network

### 結論
**綁定狀態 🟢**——是少見的「半導體 yield 領域中無大廠獨家綁定」的中生代學者，TSMC 投資他可獲得相對純淨的研究產出與較好的合作開放度。

---

## §2 技術契合度

### 核心研究方法論
- **Wafer Bin Map (WBM) Pattern Recognition**：以 clustering ensemble、similarity matching、contrastive learning 等方法做 WBM 缺陷型態分類（其代表作）
- **Fault Detection and Classification (FDC) for Semiconductor Manufacturing**：multi-source sensor data + CNN/AutoEncoder
- **Yield Prediction & Diagnosis**：machine learning 預測良率 + root cause 分析
- **Predictive Maintenance**：autoencoder GRU 等 deep learning 殘存壽命預測

### 代表論文（半導體相關 + 高引）

| # | 標題 | 年/Venue | Citations | TSMC AI 接合度 |
|---|------|---------|-----------|---------------|
| 1 | A review on fault detection and process diagnostics in industrial processes (Park, Fan, Hsu) | 2020 | 313 | ⭐⭐⭐⭐ FDC 綜述等於入門教科書 |
| 2 | Data-driven approach for fault detection and diagnostic in semiconductor manufacturing (Fan, Hsu et al.) | 2020 | 216 | ⭐⭐⭐⭐⭐ 直接對應 TSMC FDC 系統 |
| 3 | Multiple time-series CNN for fault detection and diagnosis (Hsu, Liu) | 2021 / J. Intelligent Manufacturing | 184 | ⭐⭐⭐⭐⭐ Sensor 多時序 CNN，可直接落 TSMC sensor stack |
| 4 | Semiconductor fault detection and classification for yield enhancement（與簡禎富合著） | 2013 | 166 | ⭐⭐⭐⭐ 與 NTHU IEEM 學派一脈相承 |
| 5 | Defective wafer detection using denoising autoencoder | 2020 | 88 | ⭐⭐⭐⭐ Wafer 級缺陷偵測 |
| 6 | Wafer bin map similarity matching for semiconductor manufacturing | 2020 | 80 | ⭐⭐⭐⭐ WBM 主軸 |
| 7 | Multi-source wafer map retrieval based on contrastive learning for root cause analysis | 2023 / J. Intelligent Manufacturing | （新） | ⭐⭐⭐⭐⭐ TSMC 110HZA3K00G 直接資助 |
| 8 | Autoencoder GRU for remaining useful life prediction (Lu, Hsu, Huang) | 2020 | 77 | ⭐⭐⭐⭐ 預測性維護 |

### Google Scholar 量化
- **Total citations: 2,543**（since 2021: 1,811）
- **h-index: 24**（since 2021: 19——表示近 5 年仍高度活躍）
- **i10-index: 42**

### 與 TSMC AI 部門題目對接

| TSMC AI 題目 | 許嘉裕可貢獻角度 |
|---------------|-----------------|
| **WBM 缺陷分類 / root cause** | ⭐⭐⭐⭐⭐ 主場優勢，已用 TSMC 資料發過 contrastive learning 論文 |
| **FDC（Sensor stack 異常偵測）** | ⭐⭐⭐⭐⭐ 多時序 CNN 那篇即可直接落地 |
| **Predictive Maintenance** | ⭐⭐⭐⭐ Autoencoder GRU RUL 那篇 |
| **VM (Virtual Metrology)** | ⭐⭐⭐ 方法論互通，未見專文但可延伸 |
| **Yield Prediction** | ⭐⭐⭐⭐ 主軸 |
| **Process Anomaly Detection** | ⭐⭐⭐⭐⭐ 直接對應 |
| **Fab Scheduling** | ⭐⭐ 非主軸 |

---

## §3 學生 Lab 規模（能力限制聲明）

**能力限制聲明**：許嘉裕剛轉至 NTHU IEEM，新 Lab 個人頁尚未在 NTHU IEEM 官網更新（搜尋未獲得獨立 Lab URL）；NTUST 時期的 Lab 學生隨他遷移情況未公開。

### 推估
- **NTUST 時期**：以 2,543 citations + h-index 24 + 多項產學案推估，原 NTUST 工業管理系時期應有博士生 2-4 人 + 碩士生 6-10 人
- **NTHU 過渡期**：轉任後 1-2 年內，新生招收會有銜接空窗；但因清華 IEEM 招生競爭力遠強於 NTUST 工管，預期 2-3 年內可衝至 4-6 位博士 + 10-12 位碩士的成熟規模
- **畢業生去向**（推測）：NTUST 時期主要去向應為台積、聯電、力積電、群創、友達等本土製造業；轉清華後 TSMC 比例會升高
- **頂會 / 頂刊一作**：J. Intelligent Manufacturing（Q1）、Computers & Industrial Engineering 為主，比 NeurIPS/ICML 弱但對應領域實用性高

### 5 年學生招募潛力評估
- ✅ NTHU IEEM 招生品牌力遠勝 NTUST → 學生上限提升
- ✅ 與簡禎富、李家岩同系形成「智慧製造學派」，可吸引明確志向學生
- ⚠️ 短期 1-2 年的 lab 重建期會有產出空窗
- ⚠️ 與簡、李兩位老將在學生資源上會有部分競爭關係（NTHU IEEM 智慧製造同題教授偏多）
- **5 年學生流量推估**：每年 2-3 位碩士、0.5-1 位博士可吸納至 TSMC AI 線（待 lab 穩定後）

---

## §4 5 維度評分明細

| 維度 | 分數 | 評分理由 |
|------|------|---------|
| **1. 技術命中度** | **2/2** | WBM、FDC、yield prediction、predictive maintenance 等 TSMC AI 部門核心題目全打中；多時序 CNN 那篇是入門級 must-read |
| **2. 5 年學生招募潛力** | **1.5/2** | NTHU 招生品牌大幅提升 → +1；但短期 lab 重建空窗 + 與簡/李競爭資源 → -0.5 |
| **3. 企業共建長期 Lab 開放度** | **1.5/2** | 跨產業實證經驗豐富、無大廠獨家綁定、轉任 NTHU 後正在開新局——對 TSMC 投資是接合最好的時機；扣 0.5 是因為 NTUST 時期已建立的合作可能仍在維持，需釐清產學優先序 |
| **4. 資源未被搶佔程度** | **2/2** | 無 Micron / Samsung / Intel 大廠綁定；TSMC 110HZA3K00G 屬普及型資助；學會秘書長行政負擔影響有限 |
| **5. 個人黃金期剩餘** | **0.5/2** ~~原 1.5/2~~ → **0.5/2** | 2020 吳大猷獎得主 → 推估約 40-45 歲（中生代旺盛期）；論文趨勢仍持續產出（since 2021 citations 1,811 = 71% 為近 5 年）；但**剛換校為 lab 重建期**，短期 1-2 年產出會有調整成本 |

### 總分修正：**1+(2+1.5+1.5+2)** = **8/10** ~~原 7/10~~

> 修正後總分為 **8/10**（與張國浩同分），但 Tier 分類保留為 **A-**（A 減）：因為 lab 重建短期空窗的不確定性實際大於評分能反映的程度，建議在「投資時機」上比張國浩晚 6-12 個月評估。

---

## §5 合作優缺點 + 3 個合作題目建議

### ✅ 優點
1. **WBM/FDC 技術命中度滿分**：TSMC AI 部門的 daily-bread 題目，他幾乎是業內 go-to expert
2. **無大廠獨家綁定**：可獲得相對純淨的研究產出與合作開放度
3. **TSMC 已有資料合作通道**（110HZA3K00G）：信任關係已建立
4. **跨產業實證經驗**：解決方案 transferability 強
5. **論文近 5 年高度活躍**（71% citations 在 2021 後）

### ⚠️ 缺點 / 風險
1. **Lab 重建期**（最大短期風險）：剛從 NTUST 轉至 NTHU IEEM，新生招收與設備建置需 1-2 年
2. **與簡禎富、李家岩同題重疊**：NTHU IEEM 智慧製造學派內部競爭資源，需設計差異化合作切角避免「重複投資」
3. **學會秘書長行政時間** （2023-2024，可能已卸任）
4. **Lab 規模目前未明**：需實地確認博士生/碩士生人數

### 🎯 3 個合作題目建議

1. **WBM Contrastive Learning v2 + Cross-Fab Transfer**
   - 接力 2023 J. Intelligent Manufacturing 論文（TSMC 110HZA3K00G 已資助），擴展到跨 fab、跨製程的 WBM root cause 分析
   - 預期週期：12-18 個月
   - 戰略意義：對 TSMC 多廠區一致化分析有直接價值

2. **多時序 Sensor CNN 即時 FDC 系統部署**
   - 將其 2021 多時序 CNN 框架，從研究 prototype 升級為 TSMC fab edge-deployable 即時系統
   - 預期週期：18-24 個月
   - 交付物：可上線的 FDC 模組 + IEEE T-SM 論文

3. **Predictive Maintenance + RUL 模型升級**
   - 接力 2020 Autoencoder GRU RUL 論文，加入 LLM-based 維護報告自動生成 + 跨機台知識遷移
   - 預期週期：12 個月
   - 戰略意義：與 TSMC E&PM（設備與工務）部門直接接合

---

## §6 Reference URL 清單（訪問日期 2026-04-24）

1. **Google Scholar 個人檔案**（量化指標、論文清單、affiliation 自報為 NTHU IEEM）
   - https://scholar.google.com/citations?hl=en&user=I23ksWUAAAAJ
   - 訪問日期：2026-04-24
   - Total citations 2,543 / h-index 24 / i10-index 42

2. **NSTC 2020 吳大猷先生紀念獎介紹頁**（學術獎項、研究領域）
   - https://web.nstc.gov.tw/cen/oaa/award_109/48302694673.html
   - 訪問日期：2026-04-24
   - 含：研究專長（大數據+ML 智慧製造）、跨產業合作清單（半導體/面板/被動元件/PCB/3C/設備）

3. **2023 Taiwan AI Academy Conference 講者頁**（NTUST 時期 affiliation）
   - https://conf2023.aiacademy.tw/chia-yu-hsu/
   - 訪問日期：2026-04-24
   - 確認 2023 仍掛 NTUST 銜（轉 NTHU 應在此後）

4. **NTHU IEEM 演講公告**（許嘉裕在 NTHU IEEM 系內演講紀錄）
   - https://ieem.site.nthu.edu.tw/p/406-1310-170397,r2715.php?Lang=en
   - 訪問日期：2026-04-24
   - 標題：Data Analytics and Deep Learning for Smart Manufacturing
   - 註：當時掛 NTUST 銜，是被邀請演講

5. **NTUST 工業管理系 faculty 頁**（NTUST 時期 archived 資料）
   - https://www.im.ntust.edu.tw/p/412-1014-10750.php?Lang=en
   - 訪問日期：2026-04-24
   - 註：頁面內容未完整載入，建議線下查詢

6. **代表論文：Multi-source wafer map retrieval based on contrastive learning**（TSMC 110HZA3K00G 資助）
   - https://link.springer.com/article/10.1007/s10845-023-02233-x
   - 訪問日期：2026-04-24
   - Venue: J. Intelligent Manufacturing (Q1)

---

**能力限制總聲明**：本份 profile 多項關鍵資訊（NTHU 轉任日期、目前 NTHU lab 學生數、是否仍維持 NTUST 殘留 lab、最新 unpublished 產學案）僅靠 WebSearch + WebFetch 無法直接驗證；尤其 Google Scholar 自報的 affiliation 為 NTHU IEEM、但 NTHU IEEM 官方 faculty 頁因 redirect 與 500 error 未能直接核實。建議線下向 NTHU IEEM 系辦或許嘉裕本人正式核實後再做最終投資決策。
