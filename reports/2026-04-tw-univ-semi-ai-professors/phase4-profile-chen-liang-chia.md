# 深度 Profile：陳亮嘉 Liang-Chia Chen
**Phase 4 補強 PI — NTU 機械系光學量測軌道**
*產出日期：2026-04-24 | 資料截止：2026-04-24*

---

## 結論先行

| 項目 | 內容 |
|------|------|
| **Tier 評等** | 🟢 **Tier-1 強烈推薦（建議直接拉入 Top 15 候選）** |
| **核心定位** | 台灣**光學量測 + 半導體先進封裝 AOI** 的代表性學者；國際 SPIE 活躍會員（13.9 年）+ 國科會 2022 未來科技獎得主 |
| **與題目契合度** | 直接命中「3D 光學量測 / Optical Metrology / 白光干涉 / 共焦顯微 / AOI」全套核心關鍵字 |
| **TSMC 隱形綁定** | 🟢 **無明確獨家綁定**；產學合作對象以**設備商與 OSAT** 為主（致茂、均豪、致伸、揚明光等），對 TSMC 而言為**中性可接觸**的學界資源 |
| **學界頭銜** | NTU 機械系**特聘教授（Distinguished Professor）**；NTU AOIEC 聯盟主持人（聯盟會員 43 家） |
| **獨家價值** | 唯一同時涵蓋「OCD scatterometry + AI metrology + TSV/HAR 先進封裝量測 + 整合設備聯盟」的台灣學者；**直接補完 Top 15 在 T4 先進封裝量測軸與 T0 製程設備軸的雙缺口** |

---

## §1 隱形綁定檢查

### 1.1 已知學術／企業／聯盟關聯

| 機構／企業 | 關係 | 期間 | 強度 |
|-----------|------|------|------|
| **NTU AOIEC**（先進自動化光學檢測設備研發聯盟）| **聯盟主持人**；43 家會員企業 + 4 校（NTU/NYCU/NTUST/NTUT）| 2017–至今 | 🟢 主導者 |
| **致茂電子（Chroma ATE）** | 已驗證合作夥伴（先進封裝量測技術）| 多年 | 🟢 直接合作 |
| **均豪精密（Gallant Precision Machining）** | 已驗證合作夥伴 | 多年 | 🟢 直接合作 |
| **致伸科技（Tri Technology）** | 已驗證合作夥伴 | 多年 | 🟢 直接合作 |
| **揚明光學（Young Optics）** | 已驗證合作夥伴 | 多年 | 🟢 直接合作 |
| **国研院台灣儀器科技研究中心（TIRI/NSTC）** | 跨校聯盟成員 | 持續 | 🟢 |
| **Technische Universität Ilmenau**（德國）| 國際合作夥伴；人員與設備互換 | 2019–至今 | 🟡 |
| **NSTC（國科會）** | 主要研究經費來源；2022 未來科技獎 | 持續 | 🟢 |
| **TSMC** | ⚠️ **無公開直接合作紀錄**（屬「first tier semiconductor companies in Taiwan 驗證」中之一可能） | — | 不可驗證 |
| **KLA / AMAT / ASML / 三星 / Intel** | ⚠️ **無公開顧問或合作紀錄** | — | 中性 |

### 1.2 隱形綁定風險評估

| 競爭情境 | 風險程度 | 說明 |
|---------|---------|------|
| **與設備商（致茂/均豪等）競合** | 🟢 低 | 合作夥伴均為**台灣量測設備商**，非晶圓代工本身；對 TSMC 為上下游中性 |
| **與 KLA/AMAT/ASML 競合** | 🟢 低（依任務指引：設備商屬上下游中性，不扣分） | 公開資料無這些國際大廠綁定；其研究反而是台灣 metrology 本土化的學術支柱 |
| **與 TSMC 直接競爭** | 🟢 低 | 無已知 TSMC 競爭者（Samsung/Intel）合作；與 OSAT（日月光等）合作度也未公開為強綁定 |
| **顧問私約／企業借調** | ⚠️ 不可驗證 | WebSearch 範圍內僅見聯盟主持與技轉案；需面談確認個人顧問 |

### 1.3 3 個必問防禦題

> 1. 「AOIEC 聯盟 43 家會員中，是否有 TSMC 直接會員身份？」（探最關鍵的綁定狀態）
> 2. 「致茂、均豪等技轉案是否含獨家授權條款，是否會影響後續同類技術授權給其他客戶？」
> 3. 「您個人是否擔任任何上市半導體量測公司的獨立董事、技術顧問或股權持有？」

---

## §2 技術契合度

### 2.1 真實研究主軸（依 Lab Spotlight + NSTC 公告 + SPIE 論文）

| 軸 | 關鍵字 | 對應 TSMC 痛點 |
|----|--------|---------------|
| **M1 OCD（光學關鍵尺寸）量測** | OCD scatterometry, AI-guided scatterometry, ANN-assisted DUV scatterometry | 直接對應 TSMC 2nm/A14 in-line CD 量測；**取代/補完 KLA OCD 機台**之學術替代路線 |
| **M2 高深寬比結構量測（HAR）** | High Aspect Ratio sub-micron via, TSV measurement (15:1 D/W ratio) | **直接對應先進封裝（CoWoS、SoIC、3D IC）TSV 量測**；TSMC 2024+ 主戰場 |
| **M3 共焦／白光干涉／3D 掃描** | Confocal microscopy, Interferometry, 3D scanning, High-speed color confocal probe | 線上製程動態 3D 量測；CMP/Deposition 製程監控 |
| **M4 AI 驅動 AOI 演算法** | Deep learning OCD model, Transformer-based data augmentation, Diffraction imaging neural network | 解決 metrology 反問題的 AI 化；對 TSMC 良率工程價值極高 |
| **M5 X-ray Scatterometry** | X-ray scatterometry | 次世代 EUV-era metrology 候選 |
| **M6 光機電整合系統** | Optomechatronics, Abbe principle nano-precision platform | 機台級量測系統設計能力 |

### 2.2 代表論文（2023–2026）

| 標題 | 期刊／會議 | 年份 |
|------|----------|------|
| **Advancements in metrology for advanced semiconductor packaging** | Proc. SPIE 12997（Optical Measurement Systems for Industrial Inspection）| 2024-06 |
| **Non-integral model-based scatterometry for single-structure OCD metrology** | Proc. SPIE 12619 | 2023 |
| **AI-guided OCD metrology for single HAR sub-micron via measurement** | Proc. SPIE 12496（**Metrology, Inspection, and Process Control XXXVII**）| 2023 |
| **Artificial-neural-network-assisted DUV scatterometry for OCD on HAR sub-micron structures** | Proc. SPIE 12496 | 2023 |
| **AI-guided numerical-aperture-controlled scatterometry for measurement of deep HAR and thin-film structures with a large depth variation** | （ResearchGate 2023） | 2023 |
| **Development of an OCD measurement model enhanced by transformer-based data augmentation** | *Optics 期刊*（ScienceDirect S0030399226002082）| 2026 |

> 📈 **產量觀察**：SPIE Metrology, Inspection, and Process Control（**MIPC，半導體量測領域最頂級會議**）連年發表，與 KLA / AMAT / ASML 內部研究員同台；2026 已有 ScienceDirect 期刊新作。**研究活力強。**

### 2.3 重要獎項與聯盟主導

| 年份 | 獎項／頭銜 |
|------|-----------|
| 2022 | **NSTC 未來科技獎**（AI-powered Optical Measurement System for Advanced Package Critical Dimensions）|
| 2021 | **科技部傑出研究獎** |
| — | **NTU 特聘教授**（Distinguished Professor）|
| 2017–至今 | **NTU AOIEC 聯盟主持人**（43 家會員，跨 4 校）|
| — | SPIE 多次 Conference Session Chair（Optical Measurement Systems for Industrial Inspection 系列）|
| — | SPIE 個人會員 13.9 年（**SPIE Fellow 狀態：未確認，建議面談時直接詢問**）|

### 2.4 與 Phase 1/2 候選池的軸交叉

| 軸 | 既有 Top 15 涵蓋 | 陳亮嘉補位價值 |
|----|-----------------|----------------|
| **T0 製程設備／量測** | Top 15 無人專責 | ⭐⭐⭐⭐⭐ **完全補完空缺** |
| **T3 良率／缺陷檢測** | 連震杰（3D AOI 但方向漂移）、詹寶珠（DL-AOI 跨域遷移）| ⭐⭐⭐⭐ **連震杰已淡出 AOI；詹寶珠偏 DL 演算法；陳亮嘉是唯一仍以 metrology 為主軸 + AI 加值的學者** |
| **T4 先進封裝** | 宋振銘 | ⭐⭐⭐⭐⭐ **宋偏材料/封裝結構，陳亮嘉補完封裝 inspection／量測；雙軌互補** |
| **與蔡坤諭（本批另一位）形成設計-量測雙人組合** | — | ⭐⭐⭐⭐ DFM 模型輸出 ↔ OCD 量測驗證；可組大型 NSTC 計畫 |

---

## §3 學生 Lab 規模

### 3.1 Precision Metrology Lab（PMLab）規模

依 NTU Lab Spotlight 官方資料：

| 項目 | 數據 |
|------|------|
| **Lab 總成員** | **21 人**（一個科研團隊規模上限的水準）|
| **Lab 所在地** | NTU 機械工程館 423 室 + 601 室（雙實驗空間）|
| **NTU AOIEC 聯盟下游影響** | 4 校跨校學生網絡（NTU/NYCU/NTUST/NTUT）|
| **博士生估計** | 5–8 人（21 人成員中常見比例）|
| **碩士生估計** | 10–13 人 |
| **博士後／RA** | 2–3 人 |

> 對比 Phase 2 觀察的 NTU 多數 PI 規模（10–15 人），陳亮嘉 Lab 屬於 **NTU 機械系前 1/4 大型 Lab**。

### 3.2 在進行中之計畫

| 計畫 | 來源 | 期程 |
|------|------|------|
| **創新全域高速彩色共焦量測探頭關鍵技術開發** | NSTC（3 年期） | 進行中 |
| **教育部 113 深度學習為基礎的先進封裝 OCD 量測系統** | 教育部 | 進行中 |
| **NTU AOIEC 聯盟運作** | NSTC + 43 家企業 | 持續 |
| 已結案：4 年期半導體先進封裝 AOI 技術 + DL-CD 量測系統 | NSTC | 已結 |

### 3.3 學生競賽／輸出

- **無公開 GitHub 組織**（量測演算法多含產業 IP）
- **AOIEC 聯盟年會**為學生與設備商接觸主管道
- **技轉成果**：多項已透過 AOIEC 聯盟廠商實現產業化（致茂、均豪、致伸、揚明光等）
- **畢業生去向推估**：致茂、均豪、致伸、KLA Taiwan、TSMC metrology 部門、應材台灣

### 3.4 國際合作

- **TU Ilmenau（德國）**：2019 起的長期合作，含人員交換 + 設備共用 + 潛在共同專利
- **SPIE 國際舞台**：MIPC 系列年年發表，與 KLA、ASML、imec 內部研究員同場

---

## §4 5 維度評分明細

| 維度 | 分數 | 理由 |
|------|------|------|
| **1. 技術命中度（3D AOI/量測精度提升）** | **2** | 完全命中——OCD scatterometry、HAR via、AI metrology 全部涵蓋；先進封裝量測為 TSMC 2024+ 核心戰場 |
| **2. 5 年學生招募潛力** | **2** | Lab 21 人為大型團隊；AOIEC 聯盟提供跨校學生網絡（NTU/NYCU/NTUST/NTUT）；領域人才稀缺 → 招募議價力高 |
| **3. 企業共建長期 Lab 開放度** | **2** | 已主持 43 家企業聯盟，**證明可組大型多企業合作**；機制與合約框架成熟 |
| **4. 資源未被搶佔程度** | **2** | 設備商合作（致茂、均豪等）對 TSMC 為**中性**（任務指引明確：設備商不扣分）；無公開 KLA/AMAT/ASML 直接綁定；無 TSMC 排他性合約 |
| **5. 個人黃金期剩餘** | **2** | NTU 特聘教授 + 2022 未來科技獎 + 2026 仍有期刊新作 + SPIE MIPC 年年發表 → **正處於黃金產出期**；估計可活躍 8–12 年 |

**加權總分**：**10 / 10** ⭐⭐⭐⭐⭐

> **關鍵判讀**：陳亮嘉是 Phase 4 兩位 PI 中**少見的滿分候選**；技術命中度、Lab 規模、聯盟整合、產學成熟度、個人黃金期五項全綠；建議**從備選池直接拉進 Top 15**（替換 Top 15 中既不命中又綁定重的候選）。

---

## §5 合作優缺點 ＋ 3 個合作題目建議

### 5.1 優點

1. **唯一性**：台灣學界唯一同時涵蓋 OCD/scatterometry/AI-metrology/TSV/共焦／白光干涉**全套**的學者
2. **聯盟主持經驗**：43 家企業聯盟主持人 → **已驗證大型多企業合作能力**
3. **設備商中立性高**：合作對象為台灣本土設備商（致茂、均豪等），對 TSMC、Samsung、Intel 等任何客戶皆中性
4. **國際舞台**：SPIE MIPC 年年發表 → 國際同行可背書、學術重量足夠
5. **黃金期**：2022 未來科技獎、2026 期刊新作、Lab 21 人規模 → **產出活力為 Top 15 候選中前 25%**
6. **與宋振銘形成 T4 封裝雙軸**：宋偏材料/結構，陳偏 inspection；可組封裝整合大計畫

### 5.2 缺點

1. **Lab 已大**：21 人規模意味產能已部分占用；**新合作需排隊**
2. **AOIEC 聯盟競合風險**：43 家會員中若有 sponsor 的競爭者，需排他條款設計
3. **技轉案優先級**：致茂、均豪等技轉夥伴為現金流來源，sponsor 進入需釐清優先順序
4. **個人顧問狀態未公開**：建議首次面談直接詢問是否有任何上市公司董事/顧問身份

### 5.3 三個合作題目建議

| 編號 | 題目 | 對應軸 | 適合 sponsor |
|------|------|--------|------------|
| **題 A** | **CoWoS / SoIC 先進封裝 TSV 線上 OCD 量測系統開發**——直接延伸其 2022 未來科技獎技術，從 batch metrology 推進至 in-line 量產系統；對 OSAT（日月光、矽品）與 TSMC 封裝部門皆為剛需 | M1+M2 | OSAT 廠、TSMC 封裝、HBM 封裝廠 |
| **題 B** | **EUV 高 NA 節點 stochastic defect AI 量測平台**——以陳亮嘉 transformer-augmented OCD 模型為基礎，延伸至 stochastic defect inspection；可與蔡坤諭（本批另一位）DFM 模型協同 | M4+M5 | 設備商（KLA/AMAT 替代研究）、IDM 客戶、NSTC 前瞻計畫 |
| **題 C** | **AI-driven 共焦／白光干涉量測探頭在 backside power delivery / hybrid bonding 製程之應用**——對應其 NSTC 3 年期高速色彩共焦探頭計畫；hybrid bonding 為 2nm+ 量產關鍵 | M3+M6 | TSMC 設備工程、Bonder 設備商（EVG、SUSS）、NSTC |

### 5.4 建議合作型態

- **主要**：**B 型（加入 NTU AOIEC 聯盟成為會員企業）**——成本最低、最快進入；可從聯盟年會 + 共同 demo 起步，無需排他承諾
- **進階**：**E 型（冠名講座或 Joint Lab）**——若驗證後值得長期投資，建立「[公司名稱]-NTU 先進封裝量測研究中心」；參考其與 TU Ilmenau 國際合作模式
- **快速成果**：**D 型（短期 6–12 個月委託案）**——以特定 TSV/Hybrid Bonding 量測 deliverable 切入

### 5.5 第一次聯絡 Email（建議草稿）

```
Subject: 合作洽詢 — [公司名稱] × NTU 陳亮嘉教授 先進封裝光學量測合作

陳教授，您好：

[公司名稱] 長期關注先進封裝量測的學術前沿，特別是您 2022 年榮獲 NSTC 未來科技獎
的 AI-powered TSV OCD 量測系統，以及 AOIEC 聯盟在台灣 metrology 生態系所建立
的整合平台。

我們目前正在推進 [CoWoS TSV in-line metrology / Hybrid Bonding inspection /
EUV stochastic defect AI 量測] 相關研究，希望能與您及精密量測實驗室團隊進行
30–45 分鐘的線上交流，了解 PMLab 目前研究方向、AOIEC 聯盟加入機制以及產學
合作之可能切入點。

時間由您決定，可配合您的行程。

期待您的回覆。

[您的姓名] | [公司] | [Email]
```

---

## §6 Reference URL 清單

| # | 資料 | URL | 訪問日期 |
|---|------|-----|---------|
| 1 | 陳亮嘉 NTU Scholars 學術頁 | https://scholars.lib.ntu.edu.tw/entities/person/ecdafa66-0e5d-4172-aeeb-fa67cc78bda5 | 2026-04-24 |
| 2 | 台大精密量測實驗室 NTU PMLab 官網 | https://sites.google.com/view/ntupmlab | 2026-04-24 |
| 3 | NTU Lab Spotlight – Precision Metrology Laboratory | https://labspotlight.ntu.edu.tw/labs/108 | 2026-04-24 |
| 4 | NTU 官網報導：AI-powered Optical Measurement System for Advanced Package CD（2022 未來科技獎）| https://www.ntu.edu.tw/english/spotlight/2023/2159_20230511.html | 2026-04-24 |
| 5 | NTU AOIEC 聯盟簡介 | https://sites.google.com/g.ntu.edu.tw/ntu-aoiec | 2026-04-24 |
| 6 | SPIE 個人 Profile（Liang-Chia Chen）| https://spie.org/profile/Liang-Chia.Chen-163642 | 2026-04-24 |
| 7 | ResearchGate Profile | https://www.researchgate.net/profile/Liang-Chia-Chen-2 | 2026-04-24 |
| 8 | SPIE 2024 論文：Advancements in metrology for advanced semiconductor packaging | https://www.spiedigitallibrary.org/conference-proceedings-of-spie/12997/129970R/Advancements-in-metrology-for-advanced-semiconductor-packaging/10.1117/12.3024745.short | 2026-04-24 |
| 9 | SPIE 2023 論文：AI-guided OCD metrology for single HAR sub-micron via | https://www.spiedigitallibrary.org/conference-proceedings-of-spie/12496/124961A/AI-guided-OCD-metrology-for-single-HAR-sub-micron-via/10.1117/12.2658279.short | 2026-04-24 |
| 10 | 大紀元報導：台大跨國團隊突破半導體封裝光學量測瓶頸（國科會團隊新聞）| https://www.epochtimes.com/b5/23/4/26/n13982165.htm | 2026-04-24 |

### 資料缺口

| 缺失項目 | 原因 |
|---------|------|
| AOIEC 聯盟 43 家會員企業詳細名單 | 部分公開、TSMC 是否為會員需直接面談確認 |
| 個人是否為 SPIE Fellow / Optica Fellow | SPIE Profile 頁未明示，建議面談直接詢問 |
| 個人董事/顧問身份 | WebSearch 範圍內無公開資料 |
| 與 TSMC 直接合作之確切計畫 | 「first tier semiconductor companies」屬模糊表述，需直接詢問 |
| Lab 21 人之精確角色分布（博士/碩士/博後）| Lab Spotlight 僅報總人數 |

---

*本報告由 Phase 4 補強研究員產出。陳亮嘉為兩位 Phase 4 PI 中的優先推薦對象，建議從備選池直接升入 Top 15，補完先進封裝量測與製程設備軸雙缺口。*
