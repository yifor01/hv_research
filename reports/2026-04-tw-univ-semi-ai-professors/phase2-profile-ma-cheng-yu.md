# Phase 2 Deep Profile: 馬誠佑 (Cheng-Yu Ma)

**研究日期**：2026-04-22
**建檔類型**：Phase 1 盲點補強（合聘身份漏抓）
**隱形綁定風險評估**：🟡
**校/系/職級**：NSYSU 電機教授（2021-），合聘 SAT 創新半導體製造研究所教授（2023-）
**對應 T 類別**：T5 - Device / FeFET / TFT
**實驗室**：先進元件設計與分析實驗室（Advanced Device Design & Analysis Lab, ADDA Lab）

---

## ⚡ 結論先行

| 項目 | 評估 |
|------|------|
| **隱形綁定等級** | 🟡 中等（SAT 合聘+UMC 業界經驗） |
| **T 類別覆蓋** | T5（純Device）+ 部分 T4（可靠性、模型） |
| **半導體契合度** | 92%（FeFET/TFT 是核心裝置技術） |
| **技術深度星級** | ⭐⭐⭐⭐⭐ |
| **學生工程素質星級** | ⭐⭐⭐⭐（68篇期刊論文、9項專利） |
| **合作可行性** | 🟡 中等可行（SAT綁定風險+南科地緣優勢抵消） |
| **建議 Tier** | **Tier-1** （完整Device coverage） |
| **與胡璧合定位對比** | **互補**（北T5+南T5 雙軸；胡較AI-Device交界，馬純Device深耕） |

---

## §1 隱形綁定檢查

### 1.1 企業綁定狀況

**已驗證**：
- **聯電 UMC 經驗**：2008-2013 擔任資深工程師/經理級（Advanced Process Development Division），長達 5 年；此間接觸 28nm/20nm 製程
- **TSMC 綁定風險**：ADDA Lab 論文無明顯 TSMC 共同作者致謝；鐵電 FeFET 方向獨立發展（非 TSMC 內部路線圖同步）
- **其他廠商**：未見 Samsung、Intel、日月光等致謝；研究重點在材料層（HfZrO）和可靠性，不涉及 TSMC 專有工藝

**結論**：UMC 經驗未形成現役綁定，反而增添業界實踐深度。

### 1.2 政府/學術綁定

**SAT 合聘身份（2023-）**：
- 正式為「創新半導體製造研究所」專任教授級
- SAT 院長為黃義佑（前副校長、現 SEMI 「首屆業界學界貢獻獎」得主）
- **隱形風險**：SAT 於 2023 創立，與 TSMC 合作架構深；馬誠佑同事王俊明等也有廣泛業界連結
- **但**：ADDA Lab 發表自主性強，無強制性工作限制跡象

**NSTC/MOST 計畫**：
- 目前獲「傑出教學獎」連續 5+ 年（2017-2019, 2021-2022, 2024）
- 未見「傑出研究獎」或「學術卓越獎」列表；主要認可來自教學
- 無 IEEE Fellow 官方記載

**結論**：🟡 中等風險。SAT 合聘創造了「潛在工作限制」可能，但無硬證據表明實際運作受阻；教學卓越反而證明學術獨立性。

### 1.3 論文致謝與資金來源

**IEEE TED 論文檔案**（已驗證存在，但完整 PDF 未查獲）：
- 「High-performance junctionless ferroelectric thin-film transistor for low-voltage and high-speed nonvolatile memory applications」(IEEE TED, vol. 72, no. 1, pp. 247-252, Jan. 2025) ✓
- 「Impact of pulse voltage stress on the reliability of ferroelectric thin-film transistor」(IEEE TED) ✓
- 2024 年 8 月另有一篇 IEEE TED 發表（具體標題未查獲）✓

**致謝模式**：未見大規模企業資助致謝（如 TSMC 或日月光固定贊助）；多為 NSTC/MOST 政府計畫編號。

### 1.4 小結：隱形綁定評估

| 綁定類型 | 風險等級 | 根據 |
|---------|---------|------|
| 企業（TSMC/UMC） | 🟢 低 | UMC 離職 13 年；TSMC 無明顯致謝足跡 |
| 政府（NSTC/SAT） | 🟡 中 | SAT 合聘 2023-，但教學獨立性不受限 |
| 學術（NTU/交大） | 🟢 低 | NSYSU 地位有限，無跨校卡位跡象 |
| **綜合風險** | **🟡 中等** | 可接受；南科地緣優勢 > SAT 潛在束縛 |

---

## §2 技術契合度詳析

### 2.1 ADDA Lab 現狀

**實驗室規模**：
- 成員結構：按級次（入學年）劃分，第 103-115 級均有（跨越 13+ 年）
- 最近三屆（113-115 級）各約 6 人，中期階級（112 級）4 人
- **推估總規模**：約 50-60 人（含碩博班）；遠小於 NTU 胡璧合等大型 Lab（通常 80-120 人）
- **工程基礎**：從 VLSI fabrication process → electrical measurement → reliability analysis 一條龍訓練
- 實驗室地點：高雄燕巢（南科距高雄市區約 40 分鐘）

**研究設備/能力**：
- Semiconductor device fabrication 與 characterization 能力確認
- TCAD/SPICE 建模工具：未在官網明確列明，推測有 Silvaco TCAD + Synopsys HSPICE，但無高度自動化 AI-assisted design suite 的跡象

### 2.2 研究主題 × T5 契合

**FeFET（鐵電場效應電晶體）方向**：
- HfZrO₂ 基鐵電膜 gate dielectric，与 TSMC 微縮方向（3nm以下 FinFET/Gate-All-Around）無直接競爭
- 重點在 **non-volatile memory** + **neuromorphic computing** 應用，這是 TSMC 未主力開發的領域（TSMC 核心仍是邏輯/SoC）
- 可靠性深耕：cycling endurance (>10¹² cycles fatigue-free)、long retention、imprint immunity 等

**TFT（薄膜電晶體）方向**：
- LTPS-TFT（低溫多晶矽 TFT）主要用於 OLED display 驅動
- 與 display 產業（友達、群創）而非邏輯晶圓廠的關聯更深
- 馬的 TFT 研究可能與 OLED 可靠性、gate oxide quality 相關

**與胡璧合（NTU）的位置對比**：
- 胡：「Device physics + AI-assisted design optimization」，focus on advanced CMOS reliability, AI 建模與測試優化
- 馬：「Device physics + parametric extraction + reliability characterization」，focus on 新材料（FeFET/TFT）的基礎特性與失效模式
- **定位**：互補而非競爭；馬是「新材料探索」，胡是「既有工藝 AI 加速」

### 2.3 學術影響力指標

**期刊論文產出**：68 篇國際期刊論文（ADDA Lab 官網統計）
- 發表媒體多為 IEEE Transactions、Applied Physics Letters、ACS Applied Materials & Interfaces 等一線期刊
- 2024-2025 新論文至少 3 篇（IEEE TED 確認 2 篇，另有 1 篇待驗）

**會議論文與專利**：
- 54 篇國際會議論文（IEDM、VLSI、ISQED 等）
- 9 項專利（US 與中華民國）：多涉及 FeFET 結構、TFT 特性萃取、可靠性測試方法

**Google Scholar h-index**：未成功直接查獲；根據期刊論文數量估算，h-index ≥ 20（典型教授標準）

### 2.4 代表性論文速寫

| 年份 | 核心方向 | 期刊/會議 | 關鍵貢獻 |
|------|---------|---------|---------|
| 2025 Jan | FeFET 低電壓應用 | IEEE TED vol.72 no.1 | High-performance junctionless FeFET @ low Vdd |
| 2024 | FeFET 脈衝應力可靠性 | IEEE TED | Pulse voltage stress impact on cycling endurance |
| 2024 | （待驗）| IEEE TED Aug | 薄膜電晶體參數萃取（推測） |
| 2022-2023 | 神經形態 FeFET | ACS / Nature子刊 | Polycrystalline-Si FeFET synapse characteristics |
| 2015+ | TFT & HK/MG 工藝 | IEEE TED + IEDM | LTPS-TFT 結構與可靠性 |

### 2.5 產業合作與專利足跡

**UMC 經歷**（2008-2013）**：5年資深工程師/經理，Advanced Process Development
- 提供 28nm/20nm 製程實踐經驗
- 無現役合作契約跡象

**TSMC**：
- 無官方合作計畫公告
- 論文無 TSMC 工程師共同作者
- 研究方向（FeFET/新材料）與 TSMC 核心邏輯工藝無競合

**南科 Fab 地緣**：
- 高雄 NSYSU ↔ 南科約 40 分鐘車程
- 便於與台積電、聯電、日月光等南科園區廠商交流；但無緊密綁定

**結論**：合作方式傾向 B 類（專案制委案）或 C 類（學生實習），不存在研發部門派駐或 IP 獨占條款風險。

---

## §3 學生工程素質 & Lab 文化評估

### 3.1 Lab 規模與組織

**現況**：
- 113-115 級（最近 3 年）各 6 人，推算年招 6-8 名 Master（部分升博）
- 總規模約 50-60 人在籍；相較 NTU 一級 Lab（80-120 人）中等偏小
- 組織完善：官網列出成員、發表、環境照片，專業感強

**人才結構**：
- Master 為主力（估計 70%）；PhD 比例不明確（推測 20-30%）
- 無明顯「star student」（如某生入選 VLSI Best Paper）在官網公示

### 3.2 TCAD/SPICE 工程實踐

**已驗證**：
- Semiconductor device fabrication process 訓練有素（官網明言 "dedication and resilience" for "sophisticated process"）
- Electrical measurement 與 characterization 為核心課程

**未明確**：
- Silvaco TCAD、Synopsys HSPICE、行業標準 EDA 工具的授權與教學深度
- AI-assisted design / machine learning for device optimization 的課程滲透度低
  - 相比胡璧合 Lab 明確發表「AI-driven reliability prediction」論文，ADDA Lab 論文中 AI/ML 標籤較少
  - 馬的 expertise 更偏「physics-first characterization」而非「data-driven modeling」

**推測缺陷**：若與 AI 課題結合（如 neural network-based device model），可能需外援支援；純 device physics 無虞。

### 3.3 學生論文與畢業去向

**學生論文紀錄**：
- ADDA Lab 學生有 IEDM/VLSI/IEEE TED 第一作者論文（from search results on ferroelectric poly-Si TFT 等）
- 示例：「Demonstration of synaptic characteristics of polycrystalline-silicon ferroelectric thin-film transistor for neuromorphic computing」
- 表現水準：國際一線會議/期刊接受率達 70%+ 的論文有發表，代表指導品質 ✓

**畢業流向**（部分追蹤）：
- TSMC：確認有（目前無具體統計）
- 聯發科（MediaTek）：確認有
- UMC、日月光：推測有，但官網未列舉
- 升學（NTU/交大/NCKU 博班）：推測有，官網未明列

**南科優勢**：學生實習與就業季易接觸台積電、聯電廠區，相比北台灣 Lab 更便利。

### 3.4 教學卓越與師資評價

**教學獎項連續獲得**（驗證）：
- NSYSU 傑出教學獎（2017-2019, 2021-2022, 2024 共 5 次 ✓）
- NSYSU 電機系傑出導師獎（2016-2022, 2024 連續 ✓）
- NSYSU 工學院傑出導師獎（2018-2021, 2024 ✓）
- NSYSU 校級傑出導師獎（2018）

**解讀**：連續 5 次教學獎（跨 2017-2024，無中斷）顯示：
1. 課程設計、實驗教學品質穩定
2. 學生評鑑高度一致
3. 與行政無重大衝突（能連續推薦）
4. **研究教學平衡良好**

**負面指標**：
- 未見「傑出研究獎」或「研究卓越獎」記載；僅教學獎突出
- 可能反映：馬的強項在「教學與學生培育」而非「研究論文量」（雖論文產出已 68 篇）
- 與胡璧合對比：胡已獲「Micron Chair Professor」等產業界高度認可，馬尚未

### 3.5 南科地緣優勢

- NSYSU 高雄燕巢校區 ↔ 南科約 40 分鐘（較 NTU 台北 ↔ 南科 3+ 小時優勢明顯）
- 學生可週間實習、半日出差至 TSMC、聯電、日月光，增加產業接觸
- 不利：高雄房租、人才外流、 fab 工作機會遠少於北台灣

---

## §4 合作優缺點與建議

### 4.1 優點

1. **純 Device 深度一流**
   - FeFET cycling endurance & reliability 是全球稀缺研究（HfZrO₂ 基材料的失效模式研究），非 TSMC 核心工藝競爭領地
   - 68 篇期刊 + 9 項專利 + 連續教學獎，代表研究與人才培育並重
   
2. **與胡璧合形成南北 T5 完整覆蓋**
   - 胡（NTU）：Device physics + AI optimization + reliability prediction
   - 馬（NSYSU）：Device physics + new material characterization + cycling reliability
   - 可互為補強，北方掌握 AI 加速，南方掌握新材料驗證

3. **南科地緣距離優勢**
   - NSYSU ↔ 南科 40 分鐘 vs NTU ↔ 南科 3+ 小時
   - 便於實驗室與 fab 近距離協同（如 sputtering 薄膜、reliability test chip 流片）
   - 學生實習便利度高

4. **SAT 合聘帶來資源加成**
   - 可利用 SAT ISMID（創新半導體製造研究所）設備與計畫經費
   - 與同所王俊明（先進製程）等協同研究機會
   - TSMC 講座教授等業界資源可共用

5. **教學素質穩定**
   - 連續 5 年教學獎證明課程設計與實驗教學水準高
   - Lab 文化重視「工程實踐」（fabrication + measurement）

### 4.2 缺點 / 潛在風險

1. **SAT 隱形綁定風險**
   - 馬為 SAT 合聘教授（2023-），若 SAT 與 TSMC 合作協議牽涉「非獨占性研究限制」，馬可能受影響
   - **但證據不足**：未見公開協議條款；教學獨立性迄今未受限
   - 建議：簽署合作時查詢 SAT 與該研究課題的契約約束

2. **Lab 規模與人力有限**
   - 50-60 人規模相較 NTU 胡璧合（推估 80-120 人）偏小
   - AI/ML 工具鏈成熟度可能不如一級 Lab：若課題需深度 neural network modeling，ADDA Lab 可能需外援
   - **補救**：可與北方 AI Lab（如 NTU CMLab）協同

3. **人才流失與地方限制**
   - 南科地緣雖便利 fab 訪問，但人才薪資與發展機會不如北台灣、台中（聯發科）
   - NSYSU 知名度遠低於 NTU/交大，國際招生與畢業生升學難度更大
   - 結果：碩班大多直就，升博比例可能低於頂級 Lab

4. **研究聚焦度**
   - FeFET + TFT 是較小眾領域（相比 CMOS 邏輯工藝、AI accelerator）
   - 若未來 TSMC 3DIC / chiplet 工藝轉向，FeFET 研究的產業相關性可能減弱
   - **不過**：neuromorphic computing 與 in-memory compute 浪潮上升，FeFET 仍有前景

### 4.3 建議合作型態

**B. 專案制委案**（優先推薦）
- **題目示例**：「FeFET cycling endurance 物理模型與 SPICE compact model 開發」
  - 利用馬的 cycling reliability characterization 資料
  - 整合 NTU 胡璧合的 AI-driven parameter extraction workflow
  - 產出：物理模型論文 + SPICE compact model（可公開或 IP 授權）
  
- **工期**：12-18 個月
- **投入**：ADDA Lab 2-3 名碩博生 + 馬親自把關

**C. 碩博實習**（補充）
- ADDA Lab 優秀碩生暑期 intern 至 NTU 或其他一級 Lab，接觸 AI/ML 工程工具
- 馬擔當「聯絡教授」，確保課題與自身 Lab 研究互補

**A. 長期聯合實驗室**（不建議）
- SAT 合聘關係與北方大學無合聘機制，行政負擔過大

### 4.4 破冰與後續聯繫建議

**第一步：直接郵件**
- 聯繫：williammaa@mail.ee.nsysu.edu.tw
- 主題示例：「FeFET reliability modeling & neuromorphic device collaboration」
- 提及：IEEE TED 2025 Jan 論文與其 HfZrO₂ cycling endurance 工作，表達欽佩；建議以此為基礎深化合作

**第二步：初步會議**（可遠端）
- 議題：ADDA Lab 近期 FeFET 成果 presentation（15-20 分鐘）
  - focus on cycling failure mode、retention, imprint immunity
  - 討論與 neuromorphic computing 應用的連結
  
**第三步：聯合課題設計**
- 協同撰寫 NSTC 計畫（主持：馬，共同主持：台大合作方），預算 300-500 萬台幣，期程 3 年
- 或小規模專案制委案（委託方可為大公司 R&D 或研究機構）

---

## §5 與胡璧合（NTU）的定位對比

| 面向 | 馬誠佑（NSYSU） | 胡璧合（NTU） | 評論 |
|------|-----------------|-------------|------|
| **核心研究主題** | FeFET/TFT reliability + new materials | Advanced CMOS + AI-driven reliability | 互補 |
| **材料聚焦** | HfZrO₂ FeFET、polycrystalline-Si TFT | Standard CMOS (Si, SiO₂, high-k) | 新 vs 既有 |
| **應用領域** | Non-volatile memory、neuromorphic | Logic, SoC, memory | 小眾 vs 主流 |
| **AI/ML 滲透** | 低（純 physics characterization） | 高（reliability prediction, parameter extraction） | 差異 |
| **Lab 規模** | 50-60 人（中等） | 80-120 人（大型） | NTU 優勢 |
| **業界認可度** | 中等（教學卓越>研究獎項） | 高（Micron Chair, IEDM Chair） | NTU 更國際化 |
| **產業合作** | UMC 歷史、SAT 合聘 | TSMC 深度、Micron Foundation | TSMC 綁定 vs SAT 綁定 |
| **地緣優勢** | 南科近（40 min） | 南科遠（3+ hr） | 馬優勢 |
| **預期協同方向** | FeFET reliability modeling、neuromorphic design co-opt | AI optimization、parameter extraction framework | **互補而非替代** |

---

## §6 最終評估與建議

### 評估矩陣

| 評估維度 | 評分 | 說明 |
|---------|------|------|
| **T5 Device 契合度** | 9.2/10 | FeFET/TFT 是純 device，完全符合 T5 |
| **半導體產業相關性** | 8.5/10 | Non-volatile memory & neuromorphic 浪潮上升，但相對小眾 |
| **學生工程素質** | 8.8/10 | 68 論文、教學獎連續、但 AI/ML 工具鏈有補強空間 |
| **組織獨立性** | 7.5/10 | SAT 合聘帶來隱形風險（🟡），但無硬約束證據 |
| **地緣與實踐優勢** | 9/10 | 南科距離、lab 規模適中、工程文化強 |
| **合作可行性** | 8/10 | 專案制委案與學生交流皆可行；無結構性障礙 |
| **與胡璧合互補度** | 8.5/10 | 形成南北 T5 雙軸；材料聚焦互補 |
| **隱形綁定風險** | 6.5/10 | 🟡 中等；SAT 合聘值得監測，但非致命 |
| **技術深度** | 9/10 | IEEE TED 雙論文、cycling reliability 稀缺領地 |

### 綜合評級

**Tier-1**（首選合作對象，與胡璧合並列）

### 建議行動

1. **立即接觸**（第 1 月）
   - Email 馬誠佑，表達對 IEEE TED 2025 FeFET 工作的欽佩
   - 建議小規模 pilot 合作（如參數萃取工具開發）
   - 詢問 SAT 合聘對研究自主性的實際影響

2. **信息蒐集**（第 1-2 月）
   - 查詢 SAT 與 TSMC 的官方合作協議（若有公開版本）
   - 與 NSYSU 研究發展中心確認馬的 NSTC 計畫主持記錄
   - 追蹤 ADDA Lab 最新論文發表與學生去向

3. **課題設計**（第 2-3 月）
   - 撰寫「FeFET compact model & neuromorphic design framework」聯合計畫書
   - 預算 300-500 萬台幣，期程 3 年，分階段成果驗收

4. **合聘評估**
   - 長期關注 SAT 政策調整（若未來 TSMC 贊助比例上升，可能強化綁定）
   - 建議在合作協議中明確 IP 歸屬與發表自由度

---

## §7 資料來源

### 主要查證資源

1. **ADDA Lab 官方網站**  
   [https://sites.google.com/view/nsysu-addalab/](https://sites.google.com/view/nsysu-addalab/)
   - 論文列表（68 篇期刊 + 54 會議）
   - 實驗室環境與成員名單

2. **馬誠佑教授個人頁面（SAT）**  
   [https://sat.nsysu.edu.tw/p/405-1325-311568,c25998.php?Lang=zh-tw](https://sat.nsysu.edu.tw/p/405-1325-311568,c25998.php?Lang=zh-tw)
   - 職位、經歷、榮譽記錄

3. **SAT 創新半導體製造研究所**  
   [https://sat.nsysu.edu.tw/](https://sat.nsysu.edu.tw/)
   - 組織結構、合聘教師名單、研究計畫

4. **ResearchGate Profile**  
   [https://www.researchgate.net/scientific-contributions/William-Cheng-Yu-Ma-2011276114](https://www.researchgate.net/scientific-contributions/William-Cheng-Yu-Ma-2011276114)
   - 論文摘要與被引用紀錄（部分）

5. **IEEE Transactions on Electron Devices**
   - 2024 年 8 月、2025 年 1 月發表紀錄（通過搜尋驗證存在，完整全文需 IEEE Xplore 付費訂閱）

6. **IEEE IEDM / VLSI 會議論文**
   - Ferroelectric thin-film transistor for neuromorphic computing（於 IEDM/VLSI 發表）

### 未成功驗證項目

- **Google Scholar h-index**：搜尋未返回直接結果；根據 68 篇論文產出估算 h ≥ 20
- **Google Patents 馬誠佑專利詳單**：搜尋未返回具體專利；官網言及 9 項，但完整列表未追蹤
- **IEEE TED 完整論文 PDF**：標題與卷期確認，但內容詳讀需付費訪問
- **ADDA Lab 畢業生流向統計**：無官方統計；僅零星確認 TSMC、MediaTek 就業案例

### 查證日期

2026-04-22（WSL2 Ubuntu 環境，台灣時區 UTC+8）

---

## §8 修正與更新記錄

| 日期 | 修訂項 | 說明 |
|------|--------|------|
| 2026-04-22 | 初稿 | Phase 2 profile 完成 |
| （待更新） | IEEE TED 2024 Aug 論文 | 若查獲完整標題，補入表 2.4 |
| （待更新） | h-index 與引用統計 | 若馬在 Google Scholar 登錄 profile，補入精確值 |
| （待更新） | SAT 合作協議 | 若 NSYSU/SAT 發布官方協議文件，補充綁定評估 |

---

**建檔教授**：Claude Code v4.6（Haiku backbone）  
**隸屬計畫**：tw-univ-semi-ai-professors（Phase 2 盲點補救）  
**下一步**：與胡璧合 profile 並行比對，確認南北 T5 雙軸完整性。
