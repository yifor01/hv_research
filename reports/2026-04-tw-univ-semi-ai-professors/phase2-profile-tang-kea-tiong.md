# Phase 2 深度 Profile — 鄭桂忠（Kea-Tiong Samuel Tang）

- **執行日期**：2026-04-22
- **研究員**：Phase 2 深度 profile agent（WebFetch + WebSearch）
- **任務背景**：張孟凡確認 🔴 Deep Bound（TSMC CR Director），需評估鄭桂忠能否替補 Tier-S #4

---

## ⚡ 結論先行

| 項目 | 評定 |
|---|---|
| **隱形綁定等級** | 🟡 **Partial Bound（TSMC-JDP + ITRI 雙重關係）** |
| **能否替補張孟凡** | **條件式可行**（非完全 🔴，但需先確認合作意願與項目範疇）|
| **Phase 2 建議優先** | ⭐⭐⭐⭐（第一線替補，但需做綁定確認對話）|

---

## §1 隱形綁定檢查（Batch 1 教訓 — 最優先核實）

### 1.1 TSMC-JDP 教授身份（確認）

**發現：鄭桂忠確認列名 TSMC-NTHU 聯合研發中心「台積電專屬 JDP 教授」名單中。**

來源：`nthu-tsmc.site.nthu.edu.tw/p/412-1578-20665.php`，27 位 JDP 教授完整名單，鄭桂忠（Kea-Tiong Tang）明確在列（電機系），計畫類型標記為「產學大聯盟、JDP、ARP」。

**嚴重性評估（與張孟凡對比）：**

| 綁定指標 | 張孟凡（🔴）| 鄭桂忠（🟡）|
|---|---|---|
| 兼任 TSMC 正式職務 | ✅ TSMC Corporate Research Director | ❌ 無 |
| 列名 JDP 教授 | ✅ | ✅ |
| 最新論文致謝 TSMC 部門 | 4 個部門（Nature 2025）| 一般製程服務（非資金致謝）|
| 畢業生首大流向 | TSMC | 未確認（可能分散）|
| 冠名講座由 TSMC 設立 | 未確認 | ❌ 無（Delta 台達冠名先例）|

**結論**：JDP 教授身份屬「產學合作計畫補助」性質（每期最多 3 年、TSMC 出資並配內部 Sponsor），並非正式受僱或 Executive 職務。相較張孟凡的 Research Director 兼職，**鄭桂忠的 TSMC 綁定層級低 1-2 級**，屬於「研究經費依賴」而非「機構忠誠義務」。

### 1.2 ITRI Technical Director 兼職（確認，需進一步評估）

**發現：鄭桂忠自 2017 年起兼任工研院（ITRI）電子與光電系統研究所「生醫暨產業 IC 技術組技術長（Technical Director）」。**

同時擔任「NTHU/ITRI 聯合研究中心主任（Chief Director）」（itri.site.nthu.edu.tw）。

**評估**：ITRI 為政府法人（非私人公司），技術長屬兼任（part-time）行政職，台灣學界慣例，類似 NTHU 教授兼任 MOE/NSTC 委員。ITRI 不直接競爭半導體業務，**不構成商業競爭型綁定**。但需留意：ITRI 與 TSMC 長期有技術轉移關係，部分 ITRI 計畫確實對接 TSMC 需求。

### 1.3 MediaTek / NVIDIA 綁定

搜索「Kea-Tiong Tang MediaTek」、「Kea-Tiong Tang NVIDIA」均無任何正式職務紀錄。論文致謝中亦未見 MediaTek 或 NVIDIA 資金來源。

**結論：MediaTek / NVIDIA 方向無綁定。**

### 1.4 Nature / Science 論文 Acknowledgments TSMC 程度

- **Nature Electronics 2019** (`s41928-019-0288-0`)：確認致謝「NVM-DTP of TSMC, TSMC-JDP and MOST-Taiwan」—— 主要共著者中有 TSMC 工程師（Win-San Khwa 等），鄭桂忠以 NTHU 教授身份掛名，屬 CIM 技術聯合開發。
- **Science 2024** (`adf5538`)：共著者包含 TSMC 作者，致謝 TSMC-CR / TSMC-DTP / TSMC-JDP，但主導學術方向仍在 NTHU 端（Meng-Fan Chang 為通訊作者之一）。
- **ISSCC 2024/2025**：22nm 與 16nm 晶片明確採用 TSMC 製程——此為台灣頂尖 IC 設計教授的通例，**使用 TSMC 製程服務不等於機構綁定**。

### 1.5 冠名講座

目前找到的唯一冠名關係：**台達電子（Delta）飛雁計畫特聘（2022）**。TSMC 無冠名講座。**正面訊號：先例證明鄭桂忠可接受非 TSMC 廠商的冠名資助（類似簡禎富的美光先例）。**

---

## §2 技術契合度

### 2.1 現任職務與實驗室

- **職銜**：NTHU 電機系特聘教授（Distinguished Professor）；IEEE Fellow（2024 Class）
- **實驗室**：Neuromorphic and Biomedical Engineering Laboratory（**NBME Lab**）
- **兼職**：ITRI 生醫暨產業 IC 技術組技術長（2017-）；NTHU/ITRI 聯合研究中心主任；NTHU College of Semiconductor Research 教授
- **IEEE 領導職**：IEEE CASS VP-Conferences（2025 當選，接任 VP-RAM 4 年任期後）；前 IEEE TBioCAS 主編（2022-2023）；前 IEEE Taipei Section 主席（2021-2022）

### 2.2 研究主題（與 Tier 命中度）

| 研究主題 | 命中 Tier |
|---|---|
| Neuromorphic & AI Inference Chip（CIM, ReRAM, SRAM）| **T5（NN AI IC）**⭐⭐⭐⭐⭐ |
| Deep Learning ASIC / Model Compression | **T2（NN 方法論）**⭐⭐⭐ |
| TinyML / In-Sensor Computing | **T5 Edge AI**⭐⭐⭐⭐ |
| Electronic Nose / Gas Sensing IC | T6 周邊（非核心）|
| Biomedical Implants（DBS）| T6 周邊（非核心）|

**主命中：T5 + T2**，與 Phase 1 評定一致。

### 2.3 Google Scholar 指標

| 指標 | 數值 |
|---|---|
| 總引用 | 9,195（截至 2026-04）|
| 近 5 年引用 | 7,186 |
| h-index | 49 |
| h-index（近 5 年）| 42 |
| 2024 年新增引用 | 574 |

**分析**：h-49 / 近 5 年 7,186 引用，引用增速強勁（5 年佔總引用 78%），顯示處於學術生涯高峰。

### 2.4 ISSCC / VLSI / IEDM 近 3 年論文

| 年份 | 會議 | 貢獻（重點）|
|---|---|---|
| ISSCC 2025 | 2 篇 | 22nm STT-MRAM CIM Macro（Bayesian NN）；16nm Microscaling Multi-Mode Gain-Cell CIM |
| ISSCC 2024 | 3 篇 | 16nm dual-mode Gain-Cell CIM；22nm ReRAM CIM；NIRS Readout IC |
| VLSI 2023 | 2 篇 | ReRAM AI edge processor；Spiking NN olfactory processor |

**共 7 篇 ISSCC/VLSI 近 3 年**，密度屬台灣前段班。曾任 ISSCC ML/AI Subcommittee 委員（2021-2024），表示熟悉前沿研究方向。

### 2.5 代表論文（2023-2026）

1. 22nm 832kb Hybrid-Domain Floating-Point SRAM In-Memory-Compute Macro（IEEE JSSC 2023）
2. A 16nm dual-mode Integer/Floating-Point Gain-Cell Computing-in-Memory Macro（ISSCC 2024）
3. A 22nm STT-MRAM CIM Macro for Noise-Tolerant Bayesian Neural Networks（ISSCC 2025）
4. Fusion of memristor and digital CIM for energy-efficient edge computing（Science 2024，共著）
5. A mixed-precision memristor and SRAM CIM AI processor（Nature 2025，共著）

---

## §3 學生工程素質 & Lab 文化

### 3.1 Lab 規模

- 網頁顯示「2-4 位碩博班為主導，帶若干大學部專題生」
- 三大研究主線各有 2-3 組並行
- 規模偏精英小而精，**非大量產出學生型 Lab**

### 3.2 Tape-out 紀錄

ISSCC 2024 × 3 + ISSCC 2025 × 2 + VLSI 2023 × 2，顯示每年至少 2-3 次晶片下線，22nm / 16nm 節點均有紀錄。學生直接參與量產等級先進製程實作，**工程深度紮實**。

### 3.3 畢業生流向

目前無法從公開資料直接確認 LinkedIn 佈局，但綜合以下觀察：
- 主要下線製程為 TSMC 22nm/16nm（JDP 框架），TSMC 招募管道順暢
- Delta 冠名顯示有非 TSMC 產業連結
- 生醫 + AI IC 雙主線，畢業生可能分流至醫療器材、AI Chip 新創、TSMC 三方向
- **預估 TSMC 比例：35-50%（低於張孟凡 Lab 的 70%+，但仍高）**

### 3.4 競賽與外部認可

- 多次「國家新創獎」（2012-2021，第 8 至 21 屆，至少 8 次得獎）
- 2025/2026 NSTC 傑出研究獎（Phase 1 標記）
- IEEE Fellow 2024 Class（全球電機工程最高殊榮之一）
- 台達電子飛雁計畫特聘（2022）

---

## §4 綜合分析：合作可行性

### 4.1 🟡 評定理由（非 🔴 的關鍵差異）

1. **無正式 TSMC 職務**：張孟凡有 TSMC Corporate Research Director 兼職，鄭桂忠無。JDP 教授是「受資助計畫主持人」，非受僱員工，IP 歸屬與忠誠義務不同。
2. **Delta 先例**：已有非 TSMC 廠商冠名紀錄，顯示可接受多元合作來源。
3. **研究主線獨立性**：Neuromorphic + eNose + Biomedical 三主線中，後兩者完全不依賴 TSMC 資金，顯示學術議程不完全被 TSMC 控制。
4. **IEEE CASS 大量外部義務**：VP-Conferences 意味大量國際義務，研究目標傾向多元合作，非單一廠商綁定。

### 4.2 風險點

1. **JDP 框架 IP 約束**：若合作題目與現有 JDP 計畫重疊（如 CIM macro 設計），TSMC 可能對 IP 有主張。**需明確確認合作題目是否在 JDP 保護範圍之外**。
2. **ITRI 技術長角色**：ITRI 與半導體業界有廣泛技術轉移關係，合作成果可能受政府法人規定限制。
3. **Lab 規模小**：2-4 名主要學生，大型合作計畫（需 5+ 人力）可能不適合。
4. **生醫偏向**：若合作目標是純 AI 晶片（非 biomedical 場景），部分 Lab 能量未必完全對齊。

### 4.3 建議合作題目（🟡 條件下可操作）

**題目 A（最低風險）：eNose + AI 晶片整合平台**
- 完全 biomedical 域，TSMC JDP 覆蓋範圍最小
- 鄭桂忠的獨特優勢（eNose + CIM 整合），市面上競爭者少
- 適合合作夥伴：医療器材商、穿戴設備公司、農業科技（氣體偵測）

**題目 B（中風險）：Spiking Neural Network 加速器 Chip**
- SNN 仍屬 neuromorphic 前沿，非 TSMC 主要 JDP 方向
- 發表數較少（現有 1-2 篇），成長空間大
- 適合合作夥伴：邊緣 AI 晶片新創、國防/太空應用

**題目 C（確認 IP 後可行）：Bayesian NN + 製程變異容忍 CIM**
- ISSCC 2025 已有成果（STT-MRAM CIM Macro）
- **需先確認該成果是否在 JDP IP 框架外，或 JDP 期限已結束**
- 若 IP 清晰，可作為 AI 晶片可靠性提升的差異化題目

---

## §5 對 Phase 2 候選人名單的影響

### 鄭桂忠能否替補張孟凡（Tier-S #4）？

| 評估維度 | 鄭桂忠 | 張孟凡（原 #4）|
|---|---|---|
| AI IC 技術深度 | ⭐⭐⭐⭐（CIM + Neuromorphic）| ⭐⭐⭐⭐⭐（CIM + Nature/Science 雙刊）|
| 學術聲望 | h-49，IEEE Fellow 2024 | h-41，IEEE Fellow 2026；Nature+Science |
| 綁定風險 | 🟡（JDP + ITRI，無正式 TSMC 職）| 🔴（TSMC CR Director 兼職）|
| 合作可行性（對非 TSMC）| **中-高**（需確認 JDP IP 邊界）| **低**（機構衝突）|
| Lab 學生產量 | 小（精英 2-4 名）| 中等（10-15 名博）|

**建議**：**可作為 Tier-S #4 的條件式替補**。建議在初次接觸時，明確詢問：
1. 現有 JDP 計畫的主題範圍（確認 IP overlap 風險）
2. ITRI Technical Director 兼職是否對外部 NDA 有限制
3. 合作預算規模（Lab 小，可能適合精品型合作而非大規模人力投入）

若以上三點確認清晰，鄭桂忠的 h-49 + ISSCC 7 篇 / 3 年 + IEEE Fellow + eNose 獨特技術優勢，**足以勝任替補角色，甚至在 biomedical AI 晶片場景下超越張孟凡的可合作程度**。

---

## §6 資料來源清單

| 來源 | URL | 訪問日期 | 用途 |
|---|---|---|---|
| NBME Lab 主頁 | https://nbme.ee.nthu.edu.tw/ | 2026-04-22 | Lab 概況、規模、最新動態 |
| NBME Advisor 頁 | https://nbme.ee.nthu.edu.tw/advisor.html | 2026-04-22 | 職銜、研究方向、產業經歷 |
| NBME Publications | https://nbme.ee.nthu.edu.tw/publication.html | 2026-04-22 | 2023-2026 論文清單 |
| NTHU Knowledge Hub | https://khub.nthu.edu.tw/researcherProfile?uuid=12B0B786-2743-44C5-8315-2CD760E17380 | 2026-04-22 | 完整職務清單（ITRI Director 確認）|
| Google Scholar | https://scholar.google.com/citations?user=DiSis28AAAAJ&hl=en | 2026-04-22 | 引用指標、h-index、共著者 |
| IEEE CASS 頁面 | https://ieee-cas.org/contact/kea-tiong-samuel-tang | 2026-04-22 | VP-Conferences 職務確認 |
| TSMC-NTHU JDP 教授名單 | https://nthu-tsmc.site.nthu.edu.tw/p/412-1578-20665.php | 2026-04-22 | **JDP 教授身份確認** |
| TSMC-NTHU 大聯盟論文 | https://nthu-tsmc.site.nthu.edu.tw/p/412-1578-20652.php | 2026-04-22 | 鄭桂忠論文出現在 TSMC-NTHU 聯盟清單 |
| NTHU/ITRI 聯合研究中心 | https://itri.site.nthu.edu.tw/p/405-1202-200994,c6907.php | 2026-04-22 | ITRI Chief Director 職務確認 |
| LinkedIn 動態（VP-Conferences）| https://www.linkedin.com/posts/kea-tiong-samuel-tang-80a7b418_after-4-years-of-service-as-vp-ram | 2026-04-22 | IEEE CASS 最新選舉確認 |
| Nature Electronics 2019 | https://www.nature.com/articles/s41928-019-0288-0 | 2026-04-22 | TSMC 致謝文字核實 |
| PubMed — Nature 2025 | https://pubmed.ncbi.nlm.nih.gov/40044859/ | 2026-04-22 | 共著者 TSMC 工程師確認 |
| Science 2024 | https://www.science.org/doi/10.1126/science.adf5538 | 2026-04-22 | TSMC-CR/DTP/JDP 致謝確認 |
| NTHU EE — National Innovation Award | https://dee.site.nthu.edu.tw/p/406-1175-291610,r3748.php | 2026-04-22 | 第 21 屆國家新創獎得獎確認 |
| dblp | https://dblp.org/pid/14/9801.html | 2026-04-22 | 完整論文清單 |
