# 主管摘要

## 研究方法

本研究從 150+ 台灣「AI × 半導體」交叉領域 PI 候選池出發，系統盤點其近 3 年頂會論文（IEDM / VLSI / ISSCC / ISCA / SIGIR / WWW / AAAI / JASA 等）、產業合作紀錄、實驗室學生產出與獎項認可。針對每位候選人以 **5 維度評分**（技術契合 / 產業落地 / 學生素養 / 合作開放性 / 長期可持續）逐項打分並交叉驗證，最終篩出 **Top 15（並列 1 位，共 16 位）** 優先合作對象。針對公司兩個策略題目——**CoWoS/先進封裝**與**工程師人員效率**——各自盤點「材料 / 系統 / AI 方法論」三層的互補 PI 組合，避免單點依賴。

---

## 關鍵發現

- **前段製程 2nm Device 鏈完整**：王俊明（OPC/AI 光刻）+ 馬誠佑（FeFET Device）+ 胡璧合（CIM/CFET/M3D）三位形成從光罩到 BEOL 的完整 Device 設計鏈，南北地緣互補（南 NSYSU、北 NTU）

- **CoWoS/先進封裝題目從 1 位擴充到 4 位互補**：陳冠能（系統整合層，IEDM/VLSI 2024 Hyper RDL 頂會領袖）+ 陳智（材料層，Science 2012 nt-Cu 發現人，Chemleader 技轉量產）+ 江國寧（AI 方法論層，ASME EPPD Excellence 最高獎 + ML × FEA 疲勞預測）+ 宋振銘（線上量測層，Cu-Cu bonding 感測 AI）四位 PI，覆蓋「CoWoS-L / SoIC / HBM」三大題目

- **工程師人員效率題目從 1 位擴充到 4 位平行啟動**：蔡銘峰（傳統 RAG + Learning-to-Rank，SIGIR 主場）+ 黃瀚萱（CAG 新範式，WWW 2025 論文 81 citations）+ 彭文志（Agentic Decomposed IR，SIGIR 2025 財報生成範式可直接改裝為製程月報/良率週報自動生成）+ 鄭桂忠（Neuromorphic/CIM 硬體層互補）

- **統計方法論最深端未被識別但至關重要**：銀慶剛（NTHU 清華講座，2025 IMS Fellow 台灣唯一入選）在 Model Selection / 時間序列 Knockoffs / 高維變數選擇方法論上有 2014 TSMC 落地先例（不良率降 11-14%）及 2025 JCGS 論文明確標示「識別半導體製程缺陷機台」應用場景，為 fab SPC / VM / 異常追因的方法論金礦

- **三類法務風險需先 check 定案**：(a) 王俊明 TSMC 前職綁定（需確認離職年數 + 商秘獎 / 專利綁定）；(b) 銀慶剛 US12354122B2 與成大鄭芳田 IP 共有狀態；(c) 通用所有 PI 現任產業顧問 conflict of interest 清單

- **5 位 PI 屬於「行政 + 頂級學術雙重身份」**：陳冠能（ICST Dean）、詹寶珠（NCKU 電資院長）、宋振銘（NCHU 研發長）、李家岩（NTU 管院副院長 + EiMBA Director）、江國寧（先進封裝研究中心主任）——合作層級可提升至「院級 / 中心級」Joint Lab，而非只是個人 PI 專案

---

## 投資建議（接觸順序）

### 第一波（6 位，3-6 個月內啟動）

**王俊明 / 馬誠佑 / 胡璧合 / 陳冠能 / 銀慶剛 / 江國寧**

理由：
- 前段製程（王俊明、馬誠佑、胡璧合）三位一起啟動可在 2nm 節點建立完整 Device 研究鏈
- CoWoS 主力（陳冠能、江國寧）兩位一起啟動可在 CoWoS-L / HBM 疲勞預測建立系統層 + AI 方法論層雙線
- 銀慶剛（統計方法論）為 fab SPC/VM 異常追因的底層工具，可平行開啟「數據整備與初步 PoC」
- 王俊明前職綁定法務 check 完成後再簽正式合約；若有阻礙則由馬誠佑獨佔 #1

### 第二波（7 位，6-12 個月補上）

**陳智 / 詹寶珠 / 宋振銘 / 李家岩 / 鄭桂忠 / 蔡佩璇 / 蔡銘峰 / 黃瀚萱**（8 位並列第二波）

理由：
- 封裝材料（陳智）+ 線上量測（宋振銘）接續第一波的陳冠能 / 江國寧 系統框架，形成完整封裝 4 人組
- AOI / Digital Twin / Reinforcement Learning（詹寶珠、蔡佩璇、李家岩、鄭桂忠）為 fab 應用層主力
- 工程師效率（蔡銘峰 + 黃瀚萱）在第二波啟動「傳統 RAG vs CAG」雙軌 PoC 對照實驗

### 第三波（2 位，12-18 個月補位）

**林嘉文 / 彭文志**

理由：
- 林嘉文（光刻 EDA 原型）需 12 個月 PoC 驗證可行性後再正式擴大
- 彭文志（Agentic IR）與蔡銘峰 / 黃瀚萱方法論有部分重疊，等第二波對照實驗結果決定是否深化

---

## 5 年預算估算

| 階段 | 人數 | 合計區間（5 年，新台幣） | 說明 |
|---|---|---|---|
| 第一波 | 6 位 | **2,000 - 3,500 萬** | Joint Lab 或院級合作 2 位（陳冠能、江國寧）單點 500-800 萬，其他 4 位個人級 300-500 萬 |
| 第二波 | 7-8 位 | **1,500 - 2,500 萬** | 個人級專案 200-350 萬/位 × 7-8 位 |
| 第三波 | 2 位 | **500 - 1,000 萬** | PoC 先導 100-200 萬/位 + 成功後擴大 |
| **總計** | **15-16 位** | **4,000 - 7,000 萬 NTD / 5 年** | 不含學生獎學金、設備 CapEx、實習員工薪資 |

**預算配置原則**：
- 封裝 4 人組（陳冠能 + 陳智 + 江國寧 + 宋振銘）建議合併為一個「封裝 AI 中心」統籌預算，約 1,500 萬 / 5 年
- 工程師效率 4 人組（蔡銘峰 + 黃瀚萱 + 彭文志 + 鄭桂忠周邊）合併為「RAG PoC 對照實驗計畫」，約 800 萬 / 5 年
- 其餘個別 PI 以專案制委案或 JDP 計畫辦理

---

## 本報告結構

| 章節 | 內容 |
|---|---|
| §01 | Top 15 一覽大表（16 位並列）—— 11 欄綜覽、排序可快速比較 |
| §02 | Top 1-8 教授深度檔案 —— 5 維度評分 + 學生素養 + 合作優缺點 + 建議預算 / KPI |
| §03 | Top 9-16 教授深度檔案 —— 同上格式 |
| §04 | 關鍵字矩陣 —— 16 位 × 20 個技術關鍵字，快速查找專長對應 |
| §05 | 附錄 —— 接觸策略詳表、預算分配明細、法務 pre-flight check list、5 維度評分框架說明 |


---


# Top 15 一覽大表

> **說明**：下表共 16 位（含並列），依 5 維度總分降序排列。「長期投資」欄依接觸優先順序分為第一波（3-6 月啟動）/ 第二波（6-12 月）/ 第三波（12-18 月）。大廠綁定欄位僅記錄「可能影響合作開放度」者；空白代表無相關綁定紀錄。

| # | 教授 | 校系 | 專長領域 | 代表實績（近 3 年） | 合作企業紀錄 | 落地程度 | 製程/封裝應用點 | 學生素養 | 長期投資 | 競爭大廠綁定 | 補充備註 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1* | 王俊明 | NSYSU SAT ISMID 所長 | AI 光刻 / OPC / RET / DFM | SPIE Photomask Japan 2025 ML 光刻 hotspot 預測；Caltech 博士 | 前 TSMC 製程部（年數不明）；KLA Corp. | 實戰量產級（業界 13 年訓練） | 2nm EUV OPC 核心 / 光罩修正 | 前 TSMC 工程團隊 bar，SPIE 一作學生產出 | 第一波*（法務 check 後定案） | 無（但需驗證 TSMC 商秘獎/專利綁定） | ISMID 所長，結構性連結 TSMC，法務優先級最高 |
| 2 | 馬誠佑 | NSYSU 電機 + SAT 合聘 | FeFET / HfZrO TFT / Neuromorphic | IEEE TED 2025/01 junctionless FeFET；68 篇期刊 / 9 專利 | 前 UMC 28/20nm 工程師（5 年） | 研究級 → 可原型 | 2nm NVM / neuromorphic 邊緣 AI | 連續 5 次教學獎；ADDA Lab 50-60 人 | 第一波 | 無 | 南科 40min 地緣優勢；UMC 離職 13 年 |
| 3 | 胡璧合 | NTU 電機 | FeFET × M3D × CIM × CFET SRAM | Nature Nanotech 2024 2DM SRAM；IEDM 2024/2025 各 2 篇；L'ORÉAL-UNESCO Women in Science 2023 | 美光 Chair Prof. 2024；TSMC PhD Scholarship × 3 屆；Lam Research | 頂會原型 + TSMC 製程支援 | N2/A16 BEOL FeFET / CIM macro | 3 位連續 TSMC PhD Scholarship；IEDM 頂會一作 | 第一波 | 美光 Chair（非排他） | IEDM/ISSCC/VLSI 技術委員三頂會；DEI 加分 |
| 3 | 陳冠能 | NYCU ICST Dean（2025/02-）+ 電子所講座 | Hybrid Bonding / 3D IC / Layer Transfer / Hyper RDL | IEDM 2024 × 2 + VLSI 2024 × 2（Hyper RDL interposer、25×33mm² 3DIC）；400+ 論文、87 專利 | NCTU-TSMC JRC 成員；前 Micron Chair（2018-21 結束）；ITRI Adjunct；NSTC 微電子學門召集人 | 國際頂會系統整合領袖 | CoWoS-L 下一代 / SoIC / HBM 層間對準 | IEDM/VLSI 年均 6+ 篇一作；ICST Dean 院級合作 | 第一波 | 無 | MIT EECS PhD；IEEE/IET/IMAPS/NAI/CIEE 五重 Fellow |
| 5 | 銀慶剛 | NTHU 清華講座 統計 | Time Series Knockoffs / Model Selection / 高維變數 | 2025 IMS Fellow（台灣唯一）；JASA 2024/2025 × 2；JCGS 2025 明確半導體缺陷機台應用；2024 教育部學術獎 | 2014 TSMC × 高雄大學（不良率降 11-14%）；2022 成大 IYM（鄭芳田）US12354122B2 | 方法論直接落地 fab | VM / SPC 方法論 / 缺陷機台識別 | h-17；統計頂刊深度研究型 | 第一波 | 無 | IP 需查 US12354122B2 NCKU 共有狀態 |
| 6 | 陳智 | NYCU 材料系主任 + 特聘 | nt-Cu 奈米雙晶銅 / Hybrid Bonding / Electromigration | Science 2012 (111) nt-Cu 發現人；Nano Letters 2025；2023 NSTC 學術研究獎；Chemleader 2016 技轉量產 | TSMC / MediaTek / Applied Materials / Lam Research / SRC 3yr | 技轉量產級 | SoIC Hybrid Bonding 核心材料 | h-55 / i10-200；UCLA King-Ning Tu 學派正統 | 第二波 | 中性（Chemleader 材料技轉） | 封裝材料最穩選手 |
| 6 | 詹寶珠 | NCKU 電機特聘 + 電資院長（2021/08-） | Domain Adaptation / GAN / 醫學影像 DL | IEEE Fellow；ACC-GAN / A-ReSEUnet 2024；Knowledge-Based Systems 2024；院長 | 無半導體廠綁定（零 domain 先例） | 方法論遷移需 PoC | 後段 AOI 跨製程 adaptation | NCKU 電資學院院級資源 | 第二波 | 無 | 醫療 DL → 半導體 AOI 方法論可遷移 |
| 8 | 江國寧 | NTHU PME 清華講座 + 先進封裝研究中心主任 | AI × FEA / 封裝疲勞壽命 / WLP ML 預測 | ASME EPPD Excellence in Mechanics Award 2021；iMAPS Fellow；Scientific Reports 2022 3D IC DL；Materials 2024 solder joint fatigue ML | 無 TSMC JDP（完全自由 PI）；ASME/iMAPS 頂會體系 | AI × 封裝方法論第一人 | CoWoS 翹曲預測 / HBM 疲勞壽命 | 350+ 論文 + 43 國際專利 | 第一波 | 無 | 完全無競爭方綁定；first mover 窗口 |
| 9 | 宋振銘 | NCHU 材料系 + 研發長 | Cu-Cu Bonding / 表面改質 / 電化學感測 / AI 預測平台 | 2025 未來科技獎；i-ONE 儀器創新獎；JMRT / JJAP 2025 多篇；光誘導表面改質專利 | CCNRIA 聯盟；跨彰師大（AI 演算法） | 量測/感測 TRL 4-5 | Hybrid Bonding 線上感測 / 接合強度預測 | PCB 學生優秀論文金獎 2025；跨校 AI 協作 | 第二波 | 無 | 研發長身份制度對接快 |
| 9 | 李家岩 | NTU 資管 + 管院副院長 + EiMBA Director | DRL / MARL / 製造 OR / 排程 / 預測性維護 | MARL chiller IJPE 2025；BMB-LIME 42 引用；IEEE TASM AE；2024 CIIE Best Paper；Profet AI 顧問 | 台積電（碩士後工作）、日月光、台達、友達、華邦、Profet AI | 多業態實戰；《製造數據科學》作者 | fab reticle 排程 / 異常偵測 / 預測性維護 / chiller 能源 | GitHub 開源（93⭐）；PoLab 12-18 人；EiMBA 業師槓桿 | 第二波 | 無 | 行政負擔重（副院長 + EiMBA）需排期 |
| 9 | 鄭桂忠 | NTHU 電機 | Neuromorphic / CIM / ReRAM / TinyML | IEEE Fellow 2024；2025 國科會傑出研究獎；ISSCC 2024/2025 各 3/2 篇；Nature/Science 2024-2025 共著 | TSMC-NTHU JDP 教授；ITRI 技術長（2017-）；台達飛雁特聘 2022 | ISSCC/VLSI 頂會晶片 tape-out | CIM 22→7nm 延伸 / AI 推論晶片 | h-49；NBME Lab；IEEE CASS VP | 第二波 | TSMC-JDP（研究經費依賴非機構忠誠） | 與張孟凡不同 tier；綁定比張低 1-2 級 |
| 12 | 蔡佩璇 | NCKU IMIS + CSIE | Digital Twin / CPS / SOP 視覺驗證 / 多模態感測 | 2024-2025 Fulbright Senior Scholar（Pittsburgh）；IEEE IoT J 2025 Multi-Objective DT；Applied Intelligence 2024 | NCKU 內部（無半導體廠綁定） | 醫療/災防 DT 方法論強；製程 DT 需遷移 | fab Edge DT / AMR/AMHS / SOP 視覺驗證 | CPS Lab（1 博 + 12 碩）；畢業生進 TSMC 有紀錄 | 第二波 | 無 | Fulbright 期間可能部分時間在美 |
| 13 | 林嘉文 | NTHU 電機特聘 + AI 研發中心副主任 | Vision Transformer / Computer Vision / Video | IEEE Fellow 2018；2024 NSTC 傑出研究獎；2021 K.T. Li Breakthrough；h-69 / 總引用 17.4k | 無企業獨佔綁定；研發 EDA tool 基於電腦視覺做 IC 製程模擬與光罩修正 | EDA 原型級（待產業化） | 光刻失真預測 / 光罩修正 EDA / AOI 缺陷檢測 | 國際一流發表量；8-12 人 Lab | 第三波 | 無 | 多媒體核心轉向半導體；需 12 個月 PoC |
| 14 | 蔡銘峰 | NCCU 資科正教授 + AS CITI 合聘 | Learning-to-Rank / RAG / Conversational Search | SIGIR 2025 DMCL；TREC iKAT 2025；AIF 講師（已離開）；MS Research Asia Best Intern（2005-06） | 金融業（國泰、玉山）；Profet AI（生態相關）；KKBOX 系 | 純方法論（製程 domain 零先例） | 製程文件 RAG / Bug Ticket 檢索 / 內部 KB QA | CLIP Lab 5-8 人 + AS CFDA Lab 協作 | 第二波 | 無 | 需配 TSMC 端 domain 專家合作 |
| 14 | 黃瀚萱 | Academia Sinica 資訊所副研究員 | CAG / RAG / LLM Eval / Discourse / Chinese NLP | WWW 2025 "Don't Do RAG: CAG"（81 引用）；AAAI 2025；NAACL 2025；ACL 2024 Findings（57 引用） | TAIDE 顧問（政府 AI 生態，非競爭大廠） | 2025 RAG 新範式提出者 | 封閉 SOP 語料 CAG（免 retrieval 基建） | AS 精英 Lab（跨校共指導 5 人）；Google 早年實習（已過時效） | 第二波 | 無 | AS 機構本就鼓勵企業 Joint Lab |
| 16 | 彭文志 | NYCU 資工正教授（前系主任 / 前 E.SUN Fintech Director 已卸任 2024） | Data Mining / Agentic IR / Time Series / Tabular ML | SIGIR 2025 Agentic Decomposed IR 財報生成；AAAI 2025 APAR；ACL 2025 MedPlan；EMNLP 2025；CIKM 2025；WSDM 2026 | 前 E.SUN Fintech Center Director（2021-24 卸任） | 企業共建 Lab 制度有先例 | 製程月報 / 良率週報 Agentic 自動生成 | ADSL Lab 5 博 + 10 碩（15 人）；KT Li Award 2019 | 第三波 | 無 | 與蔡銘峰 / 黃瀚萱 方法論部分重疊 |

---

## 大表解讀

### 分數分佈
- **9.0**：1 位（王俊明）
- **8.7-8.9**：3 位（馬誠佑、胡璧合、陳冠能）
- **8.3-8.5**：3 位（銀慶剛、陳智、詹寶珠）
- **8.0-8.1**：4 位（江國寧、宋振銘、李家岩、鄭桂忠）
- **7.5-7.7**：2 位（蔡佩璇、林嘉文）
- **7.0-7.2**：3 位（蔡銘峰、黃瀚萱、彭文志）

### 校系分佈
- NTU × 2（胡璧合、李家岩）
- NYCU × 3（陳冠能、陳智、彭文志）
- NTHU × 4（銀慶剛、江國寧、鄭桂忠、林嘉文）
- NSYSU × 2（王俊明、馬誠佑）
- NCKU × 2（詹寶珠、蔡佩璇）
- NCHU × 1（宋振銘）
- NCCU × 1（蔡銘峰）
- Academia Sinica × 1（黃瀚萱）

避免單一校系集中風險；南北地緣均衡（NSYSU / NCKU / NCHU 南部 5 位；NTU / NYCU / NTHU / NCCU / AS 北部 11 位）。

### 隱形綁定風險分佈
- **🟢 完全自由**：11 位
- **🟡 需確認但非致命**：4 位（王俊明 TSMC 前職年數、鄭桂忠 TSMC-JDP 研究經費依賴、胡璧合 美光 Chair 非排他、陳智 Chemleader 技轉）
- **🔴 法務 check 後定案**：1 位（王俊明）

### 題目覆蓋完整性
- **前段 2nm Device**：王俊明 + 馬誠佑 + 胡璧合（3 位完整鏈）
- **CoWoS / 封裝**：陳冠能 + 陳智 + 江國寧 + 宋振銘（4 位材料-系統-AI 方法論完整鏈）
- **fab SPC / VM / 異常**：銀慶剛 + 李家岩 + 詹寶珠（3 位統計-OR-影像完整鏈）
- **AI 晶片 / CIM / Neuromorphic**：胡璧合 + 鄭桂忠（2 位 device-circuit 完整鏈）
- **Digital Twin / 排程**：蔡佩璇 + 李家岩 （2 位）
- **光刻 / EDA**：王俊明 + 林嘉文（2 位）
- **工程師 RAG / 效率工具**：蔡銘峰 + 黃瀚萱 + 彭文志（3 位方法論互補）


---


# 教授深度檔案（Top 1-8）

---

## #1*. 王俊明 Chun-Ming (Albert) Wang（NSYSU 半導體及重點科技研究學院 / ISMID 所長）

**分數**：9.0 | **接觸建議**：第一波（法務 check 後定案）

### (1) 教授技術領域的契合度

- **AI 架構能力**：CNN / ML 深度網路應用於 semiconductor lithography hotspot prediction；DFM（Design for Manufacturability）資料流
- **半導體 AI 相關計畫**：ISMID 創新半導體製造研究所所長（2023/08 起），統籌 NSYSU × TSMC 南科培訓中心實習計畫；NSTC 一般型研究計畫（具體編號未公開）
- **產業合作**：前 TSMC 製程部（具體年數待確認）；KLA Corp.（Arthur Lin 共著 SPIE 2025 論文）；ISMID 結構性對接 TSMC 南科
- **研究成果與貢獻**：**OPC（Optical Proximity Correction）、RET（Resolution Enhancement Technology）、EUV 光刻、DFM、Machine Learning for Lithography Hotspot Prediction**；先進記憶體技術
- **落地使用**：業界實戰級訓練（Caltech 應用物理博士 + 前 TSMC 製程部 + 現任 ISMID 所長跨業界與學界）；SPIE Photomask Japan 2025 論文直接對應 ArF immersion 光刻實戰
- **獲得肯定**：「教授級專業技術人員（Professor of Practice）」職銜；2023 NSYSU 招攬為 ISMID 首任所長

### (2) 學生工程素養與實驗室文化

- **系統化能力**：Caltech 應用物理博士訓練 + TSMC 製程部實戰經驗，雙重工程嚴謹度
- **團隊合作**：SPIE 2025 一作學生 Bo-Yin Tseng + KLA 工業合作方，顯示有跨界共著訓練模式
- **產學合作經驗**：ISMID 學生直送 TSMC 南科培訓中心暑期實習（中部科學園區台積電新人訓練中心）
- **獲得肯定**：Lab 規模未公開；學生競賽獎項公開資料有限（資料有限，需訪談補齊）

### (3) 合作分析

**優點**
- 技術契合度 ★★★★★：AI 光刻 / OPC / RET 直球對決 2nm EUV 節點題目
- ISMID 所長身份 = 可動員整個 NSYSU SAT 的研究所資源、TSMC 南科人才共育管道
- Caltech 學術訓練品質保證（論文嚴謹度高）
- NSYSU 南科地緣，畢業生就業出口穩定
- KLA 業界合作已建立，非紙上研究

**缺點 / 風險**
- **前 TSMC 年數不明**：若超過 10 年且有商秘協議，風險升高至 🔴 Deep Bound
- **ISMID 結構性 TSMC 依附**：所長身份使其難以完全獨立於 TSMC 立場，若雇主與 TSMC 為競爭關係可能引起敏感
- 論文數量偏少（公開資料僅 SPIE 2025 × 1 篇），學術能量待確認
- 記憶體專長聲稱但佐證不足

**建議合作方式**
- 合作類型：**個人級專案制委案 + 後續視法務結果擴大至 ISMID 院級 Joint Lab**
- 預算區間：5 年 300-500 萬 NTD（個人級）→ 若院級擴大 800-1200 萬 NTD
- 期程：第一年 PoC（6-12 月）→ 年度 review → 續約
- **KPI**：(1) SPIE Photomask 一作論文 1-2 篇/年；(2) 公開發表 2nm EUV OPC ML 演算法 benchmark；(3) 實際 TSMC 製程 data 上的 hotspot prediction 準確率 ≥ 95%
- 交付物：演算法 code + 論文 + 學生派遣（2-3 名/年碩博實習）
- **前置法務 check 優先**：離職年數、商秘獎、專利 assignee 清點

---

## #2. 馬誠佑 William Cheng-Yu Ma（NSYSU 電機 + SAT 合聘）

**分數**：8.9 | **接觸建議**：第一波

### (1) 教授技術領域的契合度

- **AI 架構能力**：物理導向建模 + 少量 ML（neural network-based device model 可能需外援）；Silvaco TCAD / Synopsys HSPICE 工程實踐
- **半導體 AI 相關計畫**：NSTC 多年計畫；SAT 合聘後可動用創新半導體製造研究所設備與經費；ADDA Lab（Advanced Device Design & Analysis Lab）
- **產業合作**：前 UMC 資深工程師/經理（2008-2013，5 年，Advanced Process Development Division，28nm/20nm 製程）；現無現役合作契約
- **研究成果與貢獻**：**FeFET（Ferroelectric FET）、HfZrO 鐵電膜、TFT（LTPS-TFT）、Neuromorphic Computing、Non-Volatile Memory、Cycling Endurance Reliability**；IEEE TED 2025/01 junctionless ferroelectric TFT；IEDM / VLSI / ISQED 54 篇會議論文
- **落地使用**：研究級 FeFET / neuromorphic prototype；HfZrO cycling endurance > 10¹² cycles fatigue-free（全球稀缺研究）
- **獲得肯定**：68 篇國際期刊論文（IEEE TED、Applied Physics Letters、ACS Applied Materials & Interfaces）；9 項專利（US + 中華民國）；連續 5 次 NSYSU 傑出教學獎（2017-2019, 2021-2022, 2024）；NSYSU 工學院傑出導師 + 校級傑出導師

### (2) 學生工程素養與實驗室文化

- **系統化能力**：semiconductor device fabrication process 一條龍訓練（fabrication → electrical measurement → reliability analysis）
- **團隊合作**：ADDA Lab 50-60 人規模，跨越 13+ 個級別（103-115 級）顯示長期經營
- **產學合作經驗**：UMC 歷史經驗 + 南科 40min 地緣優勢 + SAT 合聘帶來 TSMC 人才共育管道；學生畢業進 TSMC、MediaTek、UMC、日月光都有紀錄
- **獲得肯定**：連續 5 年教學獎、7 年電機系傑出導師、校級傑出導師（2018）；ADDA Lab 學生有 IEDM/VLSI/IEEE TED 第一作者論文

### (3) 合作分析

**優點**
- 純 Device 物理深度一流（HfZrO FeFET cycling reliability 全球稀缺）
- 與胡璧合形成南北 T5 Device 雙軸：馬（新材料驗證）+ 胡（AI-assisted design）完全互補
- 南科 40min 地緣優勢，實驗室可實際支援 fab test chip 流片
- SAT 合聘可協同王俊明（先進製程）、黃義佑（SEMI 業界學界貢獻獎）
- 教學素質連續 5 年穩定（表示 Lab 日常運作良好）

**缺點 / 風險**
- SAT 合聘帶來隱形綁定風險（若 SAT-TSMC 合約含獨占性研究限制，馬可能受影響；但證據不足）
- Lab 規模中等偏小（相較 NTU 大 Lab 80-120 人），若需深度 AI/ML 工具鏈可能需外援
- AI/ML 滲透度相對低（純 physics characterization 為主）
- NSYSU 知名度 vs NTU/NTHU 較低，國際招生受限
- FeFET/TFT 是小眾領域，若 TSMC 未來轉向 3DIC chiplet，產業相關性需重評

**建議合作方式**
- 合作類型：**專案制委案**（優先）+ 碩博暑期實習（補充）
- 預算區間：5 年 300-500 萬 NTD
- 期程：12-18 個月主計畫 + 可續約 2 期
- **KPI**：(1) FeFET compact model SPICE 釋出（可授權/公開）；(2) IEEE TED 或 IEDM 共著論文 1-2 篇；(3) HfZrO cycling endurance 物理模型 + 可靠性測試方法交付
- 交付物：SPICE compact model + 論文 + 2-3 名碩博生派駐 TSMC Device 部門暑期

---

## #3. 胡璧合 Vita Pi-Ho Hu（NTU 電機正教授 + 美光 Chair Professor）

**分數**：8.7 | **接觸建議**：第一波

### (1) 教授技術領域的契合度

- **AI 架構能力**：AI-driven reliability prediction、DNN accuracy 協同驗證、parameter extraction framework；SPICE 模擬 + Python/ML 雙棲
- **半導體 AI 相關計畫**：2020 IEEE TED TSMC 製程支援 energy-efficient M3D SRAM；3 位博士生獲 TSMC PhD Scholarship（2022/2023/2024 連續）；Lam Research Paper Award；Global Undergraduate Program in Semiconductors (GUPS) Director（2025/08 起）
- **產業合作**：美光 Foundation Chair Professor（2024-）；TSMC 學術合作（製程支援型）；Lam Research（學生獎）
- **研究成果與貢獻**：**FeFET、HZO、Monolithic 3D IC (M3D)、Computing-in-Memory (CIM)、CFET SRAM、GAA Nanosheet FET、2D Materials (MoS2/MoTe2)、DTCO、Ångström 節點、BEOL FeFET 可靠性**
- **落地使用**：頂會原型（IEDM 2024 × 2 + IEDM 2025 × 2 + VLSI + ISSCC）；Nature Nanotechnology 2024 2D 材料 SRAM 效能投影 1nm；2020 TSMC 製程 tape-out 紀錄
- **獲得肯定**：**L'ORÉAL-UNESCO Award For Women in Science 2023**（全球女科學家最高榮譽）；美光 Chair Professor 2024；Ren Min Outstanding Young Chair Professorship 2021；2025 NTU Academic Excellence Young Lecturer Award；IEEE CAS NG-TC Chair-Elect 2025-2027；IEDM/ISSCC/VLSI 技術委員三頂會

### (2) 學生工程素養與實驗室文化

- **系統化能力**：Device 設計 + 電路模擬 + DTCO layout/area 估算，pre-silicon 工程感強
- **團隊合作**：5 博 + 17 碩 Lab，跨材料 (Si/Ge/III-V/2D) + Device + SRAM + M3D 多線並行；IEEE CASS NG-TC 國際委員會
- **產學合作經驗**：3 位連續 TSMC PhD Scholarship 代表 TSMC 認可學生素質且有實習/就業直接管道；美光 Chair 建立記憶體產業合作；Lam Research 代表沉積製程橋梁
- **獲得肯定**：**IEDM 2024 × 2 + IEDM 2025 × 2 入選**（器件頂會競爭最激烈）；IEDMS Excellent Paper Award 2025（吳承鴻）；Nature Nanotechnology 博士生 Yu-Cheng Lu 一作 2024

### (3) 合作分析

**優點**
- 技術契合度三方交集（FeFET × M3D × CIM）— 正是 2nm+ Post-SRAM / Post-Flash 核心器件方向
- L'ORÉAL-UNESCO Award DEI 加分（全球女科學家最高榮譽之一）
- 美光 Chair 非 TSMC 冠名 → 合作自由度高，與 TSMC 競爭關係中性
- 技術委員會三頂會席位（IEDM + ISSCC + VLSI）→ 情報與合作觸角廣
- 與鄭桂忠形成 device-to-chip 完整研究鏈（胡 pre-silicon Device + 鄭 post-tape-out Circuit）

**缺點 / 風險**
- 無自有 fab / PDK 直接存取，tape-out 依賴 TSMC / 外部製程
- Lab 規模中等（5 博），輸出速度受限
- Material 廣度 vs 深度：同時研究 Si / Ge / 2D / FeFET，需事先對齊合作聚焦點
- 美光 Chair 2024 冠名，合作時需確認無記憶體方向排他條款

**建議合作方式**
- 合作類型：**Joint Lab + 多年期 JDP 計畫**
- 預算區間：5 年 500-800 萬 NTD
- 期程：3 + 2 年分段驗收
- **KPI**：
  - 題目 A：BEOL HZO FeFET 可靠性 SPICE compact model 產業級釋出
  - 題目 B：FeFET-based M3D CIM Macro 功耗-精度-面積協同最佳化（VLSI 2026 or ISSCC 2027 目標）
  - 題目 C：2D CFET × FeFET A7/A5 節點 NV-SRAM 探索（Nature Electronics or IEDM 2026/2027）
- 交付物：SPICE compact model + 頂會論文 2-3 篇/年 + 2-3 名 TSMC PhD Scholarship 續約

---

## #3. 陳冠能 Kuan-Neng Chen（NYCU ICST Dean + 電子所講座教授）

**分數**：8.7 | **接觸建議**：第一波

### (1) 教授技術領域的契合度

- **AI 架構能力**：系統整合層設計為主；AI 交集需引入合作夥伴（方法論基礎已備）
- **半導體 AI 相關計畫**：NSTC 微電子學門召集人（政策級話語權）；NCTU-TSMC Joint Research Center 成員；ITRI Adjunct R&D Director；ICST Dean（院級對接）
- **產業合作**：NCTU-TSMC JRC；前 Micron Chair Professor（2018-2021 結束）；Institute of Science Tokyo Specially Appointed Professor（2017-）；前 TRON FUTURE TECH VP & Chief Scientist
- **研究成果與貢獻**：**Hybrid Bonding、低溫 Cu-Cu bonding with passivation metals、3D IC、Layer Transfer、Hyper RDL (HRDL) Interposer、Heterogeneous Integration、Embedded Multi-Die Active Bridge (S-EMAB)、Monolithic 3D with Stacked FinFET**
- **落地使用**：IEDM 2024 × 2 + VLSI 2024 × 2 頂會直接對應 CoWoS-L / SoIC / HBM；Hybrid Bonding 低溫工藝 Cu 氧化阻障 10nm 基礎論文被引 300+ 次；IBM T.J. Watson Research Center 實戰經驗
- **獲得肯定**：**MIT EECS PhD + MSE MS（材料+電機雙棲）**；IEEE / IET / IMAPS / NAI / CIEE **五重 Fellow**；IEEE EPS Exceptional Technical Achievement Award；IMAPS William D. Ashmon Award 2021；National Industrial Innovation Award 2021；MOST Outstanding Research Award × 2；h-47, 總引用 8,713（2021+ 4,018）；400+ 論文、87 專利

### (2) 學生工程素養與實驗室文化

- **系統化能力**：3DIC Lab 是國際知名品牌，Device-level 設計 + 系統整合雙棲
- **團隊合作**：Lab 規模推估 12-20 人（5-8 博 + 8-12 碩）；ICST 院級影響整個半導體產業學院
- **產學合作經驗**：NCTU-TSMC JRC 學術合作通路；ITRI 共投研究；Institute of Science Tokyo 國際交流；畢業生流向 TSMC / 聯發 / ASE 常見
- **獲得肯定**：LinkedIn 顯示年度 IEDM / VLSI 各 6+ 篇學生一作；SEMICON Taiwan / SEMICON China 固定講者；ISES Global Speaker

### (3) 合作分析

**優點**
- IEDM/VLSI 頂會每年命中 4-6 篇，國際話語權級選手
- ICST Dean 身份 → TSMC 可建立院級 Joint Lab（非單一 PI 專案）
- NSTC 微電子學門召集人 → 可影響未來 5 年半導體研究資源分配方向
- 五重 Fellow 國際聲望一流
- 零 NVIDIA / Intel / Samsung 深度綁定；Micron Chair 已結束
- 合作與 TSMC 視角友好（NCTU-TSMC JRC + ITRI + NSTC 三重政策背景）

**缺點 / 風險**
- Dean 行政負擔 30-40%（但 3DIC Lab 仍產出旺盛）
- AI 交集需 TSMC 主導引入（陳冠能本身方法論為系統整合非 ML）
- 可能需處理「ICST Dean 合作需不只單一 PI 受惠」的院級政治（正面解讀 = 資源更多）

**建議合作方式**
- 合作類型：**ICST 院級 Joint Lab + 年度技術委員會**
- 預算區間：5 年 800-1200 萬 NTD（院級預算）
- 期程：5 年滾動；每年 review + 續約
- **KPI**：
  - CoWoS-L 下一代層轉移技術 JDP（超薄對準 + HBM 堆疊誤差補償）
  - IEDM/VLSI 共著論文 4-6 篇/年
  - 每年 6+ 位一作頂會學生通道至 TSMC 暑期實習
- 交付物：IEDM/VLSI 論文 + 院級技術年報 + 學生招募管道

---

## #5. 銀慶剛 Ching-Kang Ing（NTHU 清華講座教授 統計所）

**分數**：8.5 | **接觸建議**：第一波

### (1) 教授技術領域的契合度

- **AI 架構能力**：**Model Selection / 高維變數選擇 / Time Series Knockoffs / Subset Selection / Cox regression** 統計方法論（非深度學習，但為 fab 資料分析根基）
- **半導體 AI 相關計畫**：2025 IMS Fellow（唯一來自台灣機構）；2024 教育部學術獎；NSTC 一般型計畫（JCGS 2025 應用場景明確「identify defective tools during semiconductor manufacturing process」）
- **產業合作**：**2014 TSMC × 高雄大學**（不良率降 11-14%，1000 次實驗 980 次命中，準確率 98%，自由時報報導）；**2022 成功大學 × 鄭芳田**（IEEE TASE Golden Path Search + US12354122B2 專利，半導體 bumping 製程應用）
- **研究成果與貢獻**：**Stepwise Regression、Subset Selection、Time Series Knockoffs、FDR 控制、Heteroscedastic Regression、Forward Selection for Cox Models、Multi-Armed Bandit**；JASA 2024/2025 × 2；JCGS 2025；IEEE TASE 2022；Statistica Sinica 2023
- **落地使用**：2014 TSMC 製程落地紀錄完整；2022 Golden Path Search 專利已發佈；2025 JCGS 論文應用場景明確指向「識別半導體製程缺陷機台」
- **獲得肯定**：**IMS Fellow 2025**（For fundamental and pioneering contributions to model selection and prediction in time series analysis）；教育部學術獎 2024；中山學術獎 2020；傑出人才發展基金會特聘 2017；Statistica Sinica AE；清華講座教授（校方最高職稱）

### (2) 學生工程素養與實驗室文化

- **系統化能力**：純方法論理論深度（JASA / Annals / Biometrika 頂刊訓練）；學生具備快速學習新問題能力
- **團隊合作**：統計所通用研究室規格（無獨立命名 Lab）；估計博士 3-6 名 + 碩士 4-8 名；中山合聘身份可帶來中山端學生協作；成大鄭芳田合作引入 IYM Lab 資源
- **產學合作經驗**：2014 TSMC 實戰（身為中研院時期）+ 2022 跨校跨機構合作（清大 + 成大 + IEEE TASE）+ NSTC 計畫
- **獲得肯定**：清華講座教授（非企業冠名 → 無 NDA 風險）；歷任所長（2018-2021）；Statistica Sinica / Journal of Time Series Analysis / Japanese Journal of Statistics AE

### (3) 合作分析

**優點**
- 方法論可直接落地 fab（不需「翻譯」）—— 他的方法就是 fab 資料分析的直接工具
- 2014 TSMC 合作經驗驗證可跨界，且成果量化明確（不良率 11-14% 降幅）
- 2022 跨校合作驗證可與非學術方合作
- 2025 新作持續聚焦半導體缺陷機台，研究方向未偏移
- 零排他性綁定（非 TSMC-NTHU JDP，無企業冠名）
- 所長任期已 2021 結束，現在時間彈性較佳

**缺點 / 風險**
- **US12354122B2 與成大鄭芳田 IP 共有狀態需法務確認**（若共有，合作範圍需界定）
- 方法論學者性格需強調「提供真實 fab 資料 × 共同發表頂刊」雙贏框架
- 鄭芳田與 TSMC 關係密切（AVM 系統），若雇主為非 TSMC 廠商需確認鄭芳田 channel 排他條款
- 學生 Lab 規模偏小（統計所規格）

**建議合作方式**
- 合作類型：**NSTC 計畫伴投 + fab 資料合作**
- 預算區間：5 年 300-500 萬 NTD + 另提供匿名化 fab sensor log 資料
- 期程：題目 A/B/C/D 平行或分階段
- **KPI**：
  - 題目 A：高維異方差迴歸應用於 2nm sensor feature selection（JCGS / Statistica Sinica 論文）
  - 題目 B：Time Series Knockoffs 在 sensor trace 異常監控（Annals of Statistics / JASA）
  - 題目 C：缺陷機台識別（延續 2014 成果，2nm 版本 upgrade）
  - 題目 D：Statistical × ML 融合特徵工程（培訓統計 + ML 雙能力博士生進 TSMC）
- 交付物：頂刊論文 + fab 可落地的 feature selection 工具 + 2-3 名跨領域學生

---

## #6. 陳智 Chih Chen（NYCU 材料系主任 + 特聘教授）

**分數**：8.3 | **接觸建議**：第二波

### (1) 教授技術領域的契合度

- **AI 架構能力**：目前無直接 AI/ML 論文；nt-Cu 屬性控制（電鍍參數最佳化）是 AI 標準題目，需 TSMC 引入 AI 方法論
- **半導體 AI 相關計畫**：2023 NSTC 學術研究獎；US SRC 3 年合作計畫（2022-）；Chemleader 添鴻科技 nt-Cu 電鍍液技轉量產（2016）
- **產業合作**：**TSMC / MediaTek / Applied Materials / Lam Research / Formosa Plastics / Entegris / US SRC / Chemleader**（廣且均衡，無單一獨占）
- **研究成果與貢獻**：**Science 2012 Cu (111) nt-Cu 發現人、Nanotwinned Copper、Low-Temperature Cu-Cu Bonding、Hybrid Bonding、Electromigration、Nanocrystalline Copper、CO2 Reduction to Methane on nt-Cu**；JMRT 2022-2025 多篇；Materials Characterization 2025 in-situ AFM via 熱膨脹；Nano Letters 2025 metastable nanocrystalline Cu
- **落地使用**：**Chemleader 2016 技轉量產**（nt-Cu 電鍍液已商業化）；Adeia / Sony / TSMC Hybrid Bonding 路線圖直接使用 nt-Cu 基礎；SRC 3 年合作
- **獲得肯定**：h-55 / i10-200 / 總引用 10,296（2021+ 4,992）；2023 NSTC 學術研究獎；UCLA King-Ning Tu（塗經詒）正統學派（封裝材料學界傳奇）

### (2) 學生工程素養與實驗室文化

- **系統化能力**：CCLAB（Advanced Packaging and Metallization Lab）2000 年成立，25+ 年 Lab；材料學派正統訓練
- **團隊合作**：Lab 規模推估 15-25 人（材料 Lab 典型規模）；系主任身份 = 半導體主流材料 Lab 資源
- **產學合作經驗**：技轉 Chemleader 2016 業界實戰經驗；TSMC / MediaTek / AMAT 多方合作紀錄；畢業生流向 TSMC / MediaTek / Applied Materials / Chemleader 皆常見
- **獲得肯定**：2023 NSTC 學術研究獎；ICEP-IAAC 2025 多篇亞洲封裝頂會

### (3) 合作分析

**優點**
- **Science 2012 Face-level 發現**（全球封裝學界舉足輕重）
- 技轉 Chemleader 量產 → TSMC 採用機率最高的材料學派
- UCLA King-Ning Tu 正統學派國際聲望
- 2025 年多篇持續輸出（Nano Letters / Materials Characterization / JMRT）
- 與 TSMC 已有合作歷史（既有合作深化而非冷啟動）

**缺點 / 風險**
- AI 交集需 TSMC 主導引入（陳智本身非 AI PI）
- 合作廣但 Chemleader 技轉可能半深度綁定材料廠（需確認是否影響 TSMC 客製化需求）
- 系主任行政負擔 20-30%
- 年齡約 55-60 歲，長期黃金期剩 10-15 年

**建議合作方式**
- 合作類型：**SoIC Hybrid Bonding 材料 JDP + HBM via 熱管理 in-situ AFM + AI 預測**
- 預算區間：5 年 400-600 萬 NTD
- 期程：3 年主計畫 + 2 年延伸
- **KPI**：
  - TSMC SoIC 下一代 Hybrid Bonding 材料最佳化（nt-Cu 電鍍參數）
  - in-situ AFM + AI 線上 anomaly detection PoC
  - 透過 Chemleader 技轉路徑做 TSMC 材料客製化
  - Nano Letters / JMRT 共著 2-3 篇/年
- 交付物：TSMC-fab-compatible nt-Cu 配方 + 量測流程 + 學生 TSMC 直送

---

## #6. 詹寶珠 Pau-Choo Chung（NCKU 電機特聘 + 電資學院院長）

**分數**：8.3 | **接觸建議**：第二波

### (1) 教授技術領域的契合度

- **AI 架構能力**：**GAN、CycleGAN、Feature Disentanglement、Annotation Consistency、Self-Supervised Learning、Domain Generalization**；深度學習方法論深厚
- **半導體 AI 相關計畫**：NSTC 一般型計畫（全部政府補助，無廠商資助）；前教育部資訊及科技教育司司長；IEEE CIS Vice President of Education
- **產業合作**：**零半導體廠綁定**（完全自由）；醫療機構、放射科醫師為主合作對象
- **研究成果與貢獻**：**Pathology Image Segmentation、Cross-Scanner Robustness、Domain Adaptation (Medical → Industrial)、No-Label / Weak-Label Segmentation、Feature Disentanglement**；ACC-GAN 2024 JISE；A-ReSEUnet 2024 Knowledge-Based Systems；Domain Generalization 2023
- **落地使用**：醫療 domain 成熟方法論（跨掃描器魯棒性）；半導體 AOI 應用為方法論遷移而非直接先例
- **獲得肯定**：**IEEE Fellow**；台灣醫學影像 DL 先驅；NCKU 電機系主任（2011-2014）→ 電資副院長 → 電資院長（2021/08 起）+ 敏求智慧運算學院院長；傑出資訊人才獎 2021

### (2) 學生工程素養與實驗室文化

- **系統化能力**：IEEE Fellow 級別方法論訓練；Intelligent Computing Lab（智慧運算實驗室）+ NCKU 明沺計算與網路中心（Miin Wu School of Computing）
- **團隊合作**：Lab 8-12 位（3-4 博 + 4-6 碩）；院長身份可動員全電資學院資源
- **產學合作經驗**：跨醫療 / 政府 / 校內（教育部司長經驗）；半導體 domain 無先例
- **獲得肯定**：院長 / 特聘教授；110 年傑出資訊人才獎；IEEE CIS 國際服務角色

### (3) 合作分析

**優點**
- IEEE Fellow 級別深度 DL 方法論
- 跨掃描器 / 跨機構 domain adaptation 是半導體 AOI 跨製程魯棒性的直接類比
- 零半導體廠綁定 → TSMC 獨占窗口
- 院長身份 → 可建立院級合作（NCKU 電資學院整體）
- 國際 IEEE CIS 服務角色（聲望加分）

**缺點 / 風險**
- 無半導體 domain 先例（條件式可行，需 PoC 驗證遷移效果）
- 行政負擔重（院長 + 敏求學院院長雙院長）
- 需 TSMC 端提供應用場景定義 + domain 專家配合
- Lab 規模中等

**建議合作方式**
- 合作類型：**半導體 AOI Cross-Process Domain Adaptation PoC**
- 預算區間：5 年 300-500 萬 NTD
- 期程：第一年 PoC 驗證遷移可行性（6-12 月）→ 續約擴大
- **KPI**：
  - 題目：「N7 → N5 → N3 AOI 缺陷檢測模型」跨節點遷移 PoC
  - 跨 Line 驗證（Line A 訓練 → Line B 無需重新標籤）準確率 ≥ 90%
  - Knowledge-Based Systems / Pattern Recognition 共著 1-2 篇/年
- 交付物：模型 + 論文 + 2-3 名學生進 TSMC AOI 部門

---

## #8. 江國寧 Kuo-Ning Chiang（NTHU PME 清華講座 + 先進封裝研究中心主任）

**分數**：8.1 | **接觸建議**：第一波

### (1) 教授技術領域的契合度

- **AI 架構能力**：**K-medoids clustering + ANN + ensemble learning、Random Forest、Polynomial Regression + Unsupervised ML、Deep Learning metamodel**；FEA × ML metamodel 雙棲能力
- **半導體 AI 相關計畫**：NTHU 先進封裝研究中心主任（校級平台）
- **產業合作**：**完全無 TSMC JDP / OSAT / 大廠深度綁定 = 最自由 PI**；ASME / iMAPS 體系國際合作
- **研究成果與貢獻**：**Solder Joint Fatigue Life Prediction、Small Database Adaptive Data Selection、Wafer-Level Packaging ML Reliability Prediction、3D IC Deep Learning Reliability、MEMS、Electronic Packaging、TSV**
- **落地使用**：Materials 2024 AI × 封裝疲勞壽命論文（直接對應 TSMC 良率 AI）；Journal of Mechanics 2024 wafer-level packaging ML；Scientific Reports 2022 3D IC × DL（Nature 子刊）
- **獲得肯定**：**ASME EPPD Excellence in Mechanics Award 2021**（ASME 電子封裝領域最高學術獎）；ASME Fellow 2004；iMAPS Fellow 2019；兩次 NSC 傑出研究獎（2003-2006、2010-2013）；350+ 論文 + 43 項國際專利（TW 31 + US 9 + CN 2 + JP 1 + KR 1 + SG 1）；清華講座教授（NTHU 最高榮譽）

### (2) 學生工程素養與實驗室文化

- **系統化能力**：CSML Lab（Computational Solid Mechanics Lab）@ PME NTHU，2000 年代建立大 Lab；FEA + ML 雙棲訓練（fab data scientist 最稀缺的 profile）
- **團隊合作**：推估 15-25 人；先進封裝研究中心主任 → 跨系資源整合（材料系、電機系、資工系學生可跨 Lab 合作）
- **產學合作經驗**：NTHU PME 傳統學生流向 TSMC、聯電、日月光、台達電；先進封裝研究中心主任身份擴大影響範圍
- **獲得肯定**：350+ 論文；43 項國際專利；ASME EPPD Excellence 2021；ASME + iMAPS 雙 Fellow

### (3) 合作分析

**優點**
- **完全無 TSMC JDP 記錄 = 零既有綁定 + 最佳 TSMC 新合作 first mover advantage**
- AI × 封裝 FEA 方法論 100% 命中 TSMC 良率 AI 原題目
- 先進封裝研究中心主任 → 可建立中心級合作（非單一 PI）
- ASME EPPD Excellence 最高學術獎背書
- 學生 FEA + ML 雙棲 = TSMC 良率工程師稀缺 profile

**缺點 / 風險**
- 年齡約 65+ 歲（1985 博士），**時間風險高**，黃金期估算剩 5-8 年
- 少 ISSCC/IEDM 頂會（但 ASME/iMAPS 頂刊量大）
- 不涉及 Cu-Cu bonding 材料層（需配陳智補強材料端）

**建議合作方式**
- 合作類型：**先進封裝研究中心級 Joint Lab + TSMC 冠名年度技術獎**
- 預算區間：5 年 600-1000 萬 NTD（中心級預算）
- 期程：5 年滾動；年度 review
- **KPI**：
  - TSMC CoWoS / HBM 疲勞壽命 AI 預測 JDP（小樣本學習 + FEA metamodel）
  - 每年 FEA × ML 博士生 3-5 人直送 TSMC 良率工程師
  - 冠名封裝年度獎項（類似 Micron Chair 模式）
  - 共著 ASME / iMAPS / Materials 論文 3-4 篇/年
- 交付物：FEA + ML metamodel 工具 + 論文 + 學生通道

---


---


# 教授深度檔案（Top 9-16）

---

## #9. 宋振銘 Jenn-Ming Song（NCHU 材料系教授 + 研發長）

**分數**：8.0 | **接觸建議**：第二波

### (1) 教授技術領域的契合度

- **AI 架構能力**：**Random Forest、Decision Tree、Neural Network、LSTM** 四種演算法整合；跨彰師大鐘冠榮合作負責 AI 演算法
- **半導體 AI 相關計畫**：中興大學研發長；工學院智慧封裝研究中心主任；前瞻理工科技中心主任；CCNRIA 中彰投區域產學合作聯盟成員
- **產業合作**：無 TSMC / 日月光 排他性綁定紀錄；跨校合作為主（NCHU × 彰師大）
- **研究成果與貢獻**：**光誘導 Cu 表面改質（VUV/HCOOH）、Cu-Cu 直接接合、Hybrid Bonding、Al-Al 超音波接合、微型電化學即時感測、Constant-Current Coulometry 可攜式模組、3D 封裝接合、Warpage / Stress AI 量測（DL-DIC 跟進中）**
- **落地使用**：TRL 4-5 級線上量測（非破壞性偵測 Cu 氧化層種類與厚度，適合產線即時監控）；AI 預測平台整合 4 種演算法預測 Cu-Cu 接合強度；**2025 未來科技獎**（國科會）；專利多項（光誘導表面改質技術）
- **獲得肯定**：**2025 PCB 學生優秀論文獎金獎**；**第 16 屆 i-ONE 儀器科技創新獎 2024**；華力創新材料競賽獎；中興大學研發長職銜

### (2) 學生工程素養與實驗室文化

- **系統化能力**：先進導線實驗室（Advanced Wire Laboratory）；三層架構工程實作（表面改質 → 電化學感測 → AI 預測）
- **團隊合作**：跨系整合（材料 + 電機 + 機械 + 化工）；跨校 AI 協作（彰師大鐘冠榮）
- **產學合作經驗**：研發長身份 = 制度對接快；CCNRIA 聯盟框架；產學合作分三類（歸學校、共有、委託）
- **獲得肯定**：i-ONE 儀器科技創新獎（自製儀器競賽國家級）；PCB 學生論文金獎（封裝/電路板領域學生競賽頂獎）；期刊 Materials Chemistry and Physics 編輯；Microelectronics Reliability 編輯顧問

### (3) 合作分析

**優點**
- **研發長角色 = 制度對接快**（校級行政職可直接統籌產學合作）
- 三層技術架構完整（表面改質專利 + 感測硬體 + AI 軟體）
- 線上即時感測技術 TRL 4-5（接近量產），適合產線導入
- 跨校 AI 合作模式驗證可行
- 無排他性綁定
- 學生 PCB 金獎 + i-ONE 儀器創新獎顯示工程實作能量強

**缺點 / 風險**
- 行政負擔重（研發長 + 智慧封裝研究中心主任 + 前瞻理工科技中心主任三重行政職）
- Warpage / Stress AI 量測為延伸方向，代表性論文較少
- X-ray + DL 封裝缺陷方向尚無代表性論文
- NCHU 知名度與 NTU/NYCU/NTHU 有差距，國際招生受限
- AI 演算法深度依賴彰師大鐘冠榮（若合作拆分需考量）

**建議合作方式**
- 合作類型：**Hybrid Bonding 線上量測感測器 + AI 預測平台合作**
- 預算區間：5 年 300-500 萬 NTD
- 期程：3 年主計畫 + 2 年擴大
- **KPI**：
  - Cu-Cu 接合強度線上感測器原型（TRL 6 量產前驗證）
  - AI 預測模型（接合強度 / 失效模式）準確率 ≥ 90%
  - 專利 + 期刊 2-3 篇/年（JMRT / JJAP / Materials Chem. & Phys.）
  - 學生派駐 TSMC / 日月光 封測 AP 部門暑期
- 交付物：感測器硬體 + AI 預測軟體 + 光誘導表面改質技術授權

---

## #9. 李家岩 Chia-Yen Lee（NTU 資管教授 + 管院副院長 + EiMBA Director）

**分數**：8.0 | **接觸建議**：第二波

### (1) 教授技術領域的契合度

- **AI 架構能力**：**Deep Reinforcement Learning (DRL)、Multi-Agent RL (MARL)、Autoencoder、Cyclic RL、Robust-Optimization-Guided DRL、BMB-LIME (XAI)、Multi-Objective MILP**
- **半導體 AI 相關計畫**：NSTC 112-2221-E-002-003（BMB-LIME、robust DRL 排程）；NSTC 工工管理學門召集人；IEEE TASE AE（2020-2022）+ IEEE TSM AE（現任）；AIF 顧問；Profet AI 顧問（2023-）；華邦電子智慧製造中心顧問
- **產業合作**：**台積電（碩士後工作經驗）、日月光、台達電、AUO 友達、華邦電子、Profet AI**（多業態但無排他）
- **研究成果與貢獻**：**製造 OR、DRL 預防性維護、MARL chiller 能源、Cyclic RL T/C 平衡、Autoencoder 異常偵測、BMB-LIME XAI、Reticle Scheduling、Real Options PM、Wafer Bin Map Autoencoder**
- **落地使用**：《製造數據科學》2022 中文專書全市面唯一；MARL chiller 應用於半導體 manufacturing（IJPE 2025）；AUO TFT-LCD T/C 平衡排程 CIIE2024 Best Paper；Wafer Bin Map autoencoder 對應半導體封裝場景
- **獲得肯定**：**2017 吳大猷紀念獎**（科技部傑出青年學者）；IEEE Senior Member 2021；CIIE2024 Best Paper（RL T/C 排程）；馮樹藻紀念獎 2019；IEEE TSM Best Paper 選拔委員；h-index 未直接查獲（高）

### (2) 學生工程素養與實驗室文化

- **系統化能力**：PoLab（Productivity Optimization Lab）；GitHub open source（Manufacturing-Data-Science 93⭐、Operations-Research-Applications 46⭐、Python-Gurobi-Pulp 54⭐）
- **團隊合作**：推估 12-18 人（NTU 資管熱門 Lab）；研究分組明確（排程 OR / 預測維護 PHM / DRL）
- **產學合作經驗**：多業態實戰；EiMBA 高管班業師人脈（100+ 業師含半導體廠 VP/Director 級）
- **獲得肯定**：GitHub 開源教學素材持續維護；CIIE2024 學生共著 Best Paper；2024 IEEE CASE real options 維護論文；曾任職台積電（碩士後）業界實戰經驗

### (3) 合作分析

**優點**
- 方法論完整（OR → 統計 → DRL → MARL 多層次技術堆疊）
- 《製造數據科學》書作者背書降低業界溝通成本
- 多業態合作非綁定（台積 / 友達 / 台達 / 化工業）
- 雙 channel 人脈（NSTC 召集人 + EiMBA Director）
- Profet AI 顧問帶來商業化 AI 落地視角
- IEEE TSM AE（半導體製造頂刊話語權）

**缺點 / 風險**
- **行政雙重負擔（管院副院長 + EiMBA Director）** → 每週實際可用研究時間受壓縮
- 排期可能優先 NSTC 既有計畫，新合作需等窗口
- 學門邊界模糊（資管 vs 工工所 vs 電機），合作需事先界定論文掛名
- 需確認 Profet AI 顧問角色與 TSMC 合作是否 conflict

**建議合作方式**
- 合作類型：**fab reticle 排程 DRL + chiller MARL 能源管理 JDP**
- 預算區間：5 年 400-600 萬 NTD
- 期程：3 年主計畫 + 2 年擴大
- **KPI**：
  - fab reticle scheduling DRL 原型（MILP baseline 比較改善 ≥ 10%）
  - chiller MARL 能源節約 PoC（IJPE 發表 + 實廠驗證）
  - IEEE TASE / TSM / IJPE 共著 2 篇/年
  - EiMBA 高管班交流（TSMC VP / Director 互訪）
- 交付物：DRL/MARL 演算法 code + 論文 + 2-3 名學生進 TSMC IE / FIT 部門

---

## #9. 鄭桂忠 Kea-Tiong Tang（NTHU 電機特聘教授）

**分數**：8.0 | **接觸建議**：第二波

### (1) 教授技術領域的契合度

- **AI 架構能力**：**Spiking Neural Network、Neuromorphic Architecture、In-Sensor Computing、Deep Learning ASIC、Model Compression、Bayesian Neural Network、Mixed-Precision Memristor、Gain-Cell CIM**
- **半導體 AI 相關計畫**：**TSMC-NTHU JDP 教授**（27 位名單之一，計畫類型「產學大聯盟、JDP、ARP」）；ITRI 生醫暨產業 IC 技術組技術長（2017-）；NTHU/ITRI 聯合研究中心主任；NTHU College of Semiconductor Research 教授；2025 國科會傑出研究獎
- **產業合作**：TSMC-JDP（研究經費依賴而非機構忠誠）；ITRI 技術長；台達電子飛雁計畫特聘 2022
- **研究成果與貢獻**：**Neuromorphic & AI Inference Chip (CIM / ReRAM / SRAM)、Deep Learning ASIC、TinyML、In-Sensor Computing、Electronic Nose / Gas Sensing IC、Biomedical Implants (DBS)**
- **落地使用**：**22nm STT-MRAM CIM Macro for Bayesian NN (ISSCC 2025)**；**16nm Microscaling Multi-Mode Gain-Cell CIM (ISSCC 2025)**；16nm dual-mode Integer/FP Gain-Cell CIM (ISSCC 2024)；Nature Electronics 2019 + Science 2024 + Nature 2025 共著
- **獲得肯定**：**IEEE Fellow 2024**；**2025 國科會傑出研究獎**；h-49 / 近 5 年 7,186 引用（5 年佔總引用 78% 動能強）；ISSCC / VLSI 近 3 年 7 篇；曾任 ISSCC ML/AI Subcommittee 委員 2021-2024；前 IEEE TBioCAS 主編；前 IEEE Taipei Section 主席；**IEEE CASS VP-Conferences（2025 當選）**

### (2) 學生工程素養與實驗室文化

- **系統化能力**：NBME Lab（Neuromorphic and Biomedical Engineering Laboratory）；ISSCC/VLSI 一作訓練；tape-out 實戰
- **團隊合作**：ITRI 聯合中心帶來跨法人資源；跨校 NTHU 半導體學院
- **產學合作經驗**：TSMC-JDP 每期最多 3 年（非排他）；ITRI 技術長 part-time；台達電子飛雁 2022 冠名（非 TSMC，證明可接受多廠商冠名）
- **獲得肯定**：ISSCC 2024 × 3 + 2025 × 2；台灣電路設計頂尖前段班密度

### (3) 合作分析

**優點**
- ISSCC / VLSI 頂會密度台灣前段班
- IEEE CASS VP-Conferences（國際話語權級）
- IEEE Fellow 2024 + 2025 國科會傑出研究獎雙重認可
- ITRI 技術長 → 跨法人資源通路
- 與胡璧合形成 device-to-chip 完整研究鏈（胡 pre-silicon + 鄭 post-tape-out CIM macro）
- 近 5 年動能強（5 年佔總引用 78%）

**缺點 / 風險**
- **TSMC-JDP 教授身份**（非排他但研究經費依賴，需確認現任 JDP 計畫題目是否與 TSMC 新合作 conflict）
- Nature/Science 論文致謝 TSMC-CR / TSMC-DTP 部門（顯示既有合作深）
- ITRI 部分計畫對接 TSMC 需求，需確認不重疊
- 行政雙職（IEEE CASS VP + NTHU/ITRI 中心）

**建議合作方式**
- 合作類型：**CIM 22→7nm 延伸 JDP + edge AI 加速器 tape-out**
- 預算區間：5 年 500-800 萬 NTD
- 期程：3 年主計畫 + 2 年延伸
- **KPI**：
  - 22→7nm CIM macro tape-out 原型（功耗 vs 精度 trade-off 驗證）
  - ISSCC / VLSI 共著 2-3 篇/年
  - 與胡璧合 device-to-chip 聯動研究鏈（至少 1 篇跨校合作）
  - TinyML / In-Sensor Computing 邊緣 AI 示範平台
- 交付物：tape-out 晶片 + 論文 + 博士生通道至 TSMC CR

---

## #12. 蔡佩璇 Pei-Hsuan Tsai（NCKU IMIS + CSIE 教授）

**分數**：7.7 | **接觸建議**：第二波

### (1) 教授技術領域的契合度

- **AI 架構能力**：**Digital Twin 架構、多模態感測融合、Graph Convolutional Network (GCN)、邊緣運算資源分配、Multi-Objective Optimization、即時路徑規劃、行為分析**
- **半導體 AI 相關計畫**：NSTC 一般型計畫；**2024-2025 Fulbright Senior Research Scholar @ University of Pittsburgh**（AI 醫療導引系統）
- **產業合作**：**零半導體廠綁定**；NCKU 內部 + 醫療機構合作為主
- **研究成果與貢獻**：**Healthcare Digital Twin、Fire Safety CPS、Robot Self-Evacuation、Smart Manufacturing (SOP Verification)、Edge-Cloud Computing、Skeleton-Based Dynamic Hand Gesture Recognition**
- **落地使用**：方法論可遷移（醫療 DT → 製程 DT；火災路徑規劃 → fab 動線優化）；畢業生進 TSMC 有紀錄（林映君、呂承翰、陳彧庭 2024 屆）
- **獲得肯定**：**IEEE Internet of Things Journal 2025 Multi-Objective Resource Allocation DT**；Applied Intelligence 2024（49 引用）；IEEE Systems Journal 2024（4 引用）；IEEE Transactions on Cognitive and Developmental Systems 2023（28 引用）；**Fulbright Senior Research Scholar 2024-2025**

### (2) 學生工程素養與實驗室文化

- **系統化能力**：CPS Lab（Cyber-Physical System Lab，2011 起）；清大資工 PhD + Cornell 資工 MS 學術訓練
- **團隊合作**：1 博 + 約 12 碩 + 1 助理；CPS Lab 跨 IMIS + CSIE 雙系
- **產學合作經驗**：CPS Lab 2024 屆畢業生 3 人進 TSMC（顯示學生人才輸送穩定）
- **獲得肯定**：NCKU 明沺計算與網路中心團隊成員；IEEE 期刊持續發表

### (3) 合作分析

**優點**
- Digital Twin 架構設計核心能力
- 多模態感測融合（IoT + 視覺 + 語義）
- 即時排程 + 電腦視覺 SOP 直接對應 fab 需求
- 零半導體廠綁定 → TSMC 獨占窗口
- Cornell + 清大 PhD 雙重國際訓練
- Fulbright 背書（在美合作經驗有助於未來 TSMC 美國廠合作）

**缺點 / 風險**
- 製程模擬（DES）無明確發表 → Fab 深度知識需補
- MES 整合無相關論文 → 關鍵缺口需合作方補足
- Fulbright 期間（2024-2025）部分時間在美國匹茲堡大學
- Lab 規模中等
- Domain 從醫療遷移到製程需 PoC 驗證時間

**建議合作方式**
- 合作類型：**fab Digital Twin PoC + SOP 視覺驗證系統**
- 預算區間：5 年 300-500 萬 NTD
- 期程：第一年 PoC（等 Fulbright 結束 2025）+ 3 年擴大
- **KPI**：
  - fab Edge Node 多目標資源分配 DT 原型
  - 作業員 SOP 視覺驗證系統（GCN + skeleton）準確率 ≥ 95%
  - IEEE IoT J / Applied Intelligence / IEEE Systems 共著 2 篇/年
  - 學生直送 TSMC FIT / IE 部門
- 交付物：DT 架構 + SOP 驗證系統 + 論文 + 學生通道

---

## #13. 林嘉文 Chia-Wen Lin（NTHU 電機特聘教授 + AI 研發中心副主任）

**分數**：7.5 | **接觸建議**：第三波

### (1) 教授技術領域的契合度

- **AI 架構能力**：**Vision Transformer、Mamba、Token Selective Transformer、CNN、Single Image Rain Removal、Super-Resolution、Image Dehazing**
- **半導體 AI 相關計畫**：2024 NSTC 傑出研究獎（提及「電腦視覺 EDA 工具用於 IC 製程模擬、光刻失真預測與光罩自動修正」—— 主動研發）
- **產業合作**：**零企業獨佔綁定**；主要資金為教育部、NSTC、NTHU 內部
- **研究成果與貢獻**：**Multimedia、Computer Vision、Video Coding、Super-Resolution、Image Dehazing、Rain Removal、Vision Transformer**；Frequency-Assisted Mamba for Remote Sensing Image SR (2025)；TTST: Top-k Token Selective Transformer (2024)；terahertz + 材料物理結合新方法
- **落地使用**：EDA tool 基於電腦視覺做 IC 製程模擬 + 光刻失真預測 + 光罩自動修正（原型級，待產業化）；2030.tw 深偽技術門檻社會討論角色
- **獲得肯定**：**IEEE Fellow 2018**（Contributions to multimedia work）；**2024 NSTC 傑出研究獎**；**2021 K.T. Li Breakthrough Award**；h-69 / 總引用 17.4k（國際一流）；AI Research Center 副主任 + Multimedia Center 主任

### (2) 學生工程素養與實驗室文化

- **系統化能力**：推估 8-12 人 Lab（NTHU Delta 大樓 922）；CV / Video 核心訓練
- **團隊合作**：AI R&D Center 副主任身份 → 跨系資源整合潛力
- **產學合作經驗**：未見與特定半導體廠商的聯合論文
- **獲得肯定**：IEEE Fellow；國際一流發表量與影響力；NTHU AI R&D Center 副主任

### (3) 合作分析

**優點**
- 國際一流發表量（h-69 / 17.4k 引用）
- IEEE Fellow + NSTC 傑出研究獎 + K.T. Li Award 多重認可
- Vision Transformer 核心方法論可遷移到 AOI / 光刻 EDA
- AI R&D 副主任身份跨系影響
- 零企業獨占綁定

**缺點 / 風險**
- 核心仍在多媒體（視頻 / 去雨 / 超解析度），非半導體主力
- 半導體 domain 應用處於「原型級」，需產業化轉化
- AOI / EDA 具體應用案例需更多發表佐證
- Lab 規模中等

**建議合作方式**
- 合作類型：**光刻 EDA 原型 PoC（12 個月驗證）**
- 預算區間：5 年 300-500 萬 NTD（第一年 100 萬 PoC → 成功後擴大）
- 期程：PoC 12 個月 → 續約擴大
- **KPI**：
  - 電腦視覺 EDA 工具應用於 IC 製程模擬原型
  - 光刻失真預測 + 光罩自動修正 benchmark（vs 現有 OPC 工具）
  - IEEE TIP / CVPR / ICCV 共著 1-2 篇/年（半導體應用 track）
  - 學生輸送至 TSMC / KLA / ASML AOI 部門
- 交付物：EDA 工具原型 + 論文 + 學生通道

---

## #14. 蔡銘峰 Ming-Feng Tsai（NCCU 資科正教授 + AS CITI 合聘）

**分數**：7.2 | **接觸建議**：第二波

### (1) 教授技術領域的契合度

- **AI 架構能力**：**Learning-to-Rank (LTR)、Dense Retrieval、Conversational Search、Passage Re-ranking、Query Reformulation、Recommender Systems、Contrastive Learning、Negative Sampling**
- **半導體 AI 相關計畫**：NSTC 一般型計畫為主；AIF 講師（已離開）；曾於 Microsoft Research Asia 實習（2005-06，Best Intern 已遠超時效）
- **產業合作**：**零半導體廠綁定**；金融業（國泰、玉山）、KKStream 系；無當前企業冠名
- **研究成果與貢獻**：**LTR、IR、Conversational Search、RAG、Rank Fusion、Passage Re-ranking、Financial NLP（金融文字情感/關鍵詞挖掘）**
- **落地使用**：純方法論（製程 domain 零先例）；**SIGIR 2025 "Dynamic Margin-based Contrastive Learning for Robust Negative Sampling in Information Retrieval"**；**TREC iKAT 2025 LLM Query Reformulation**；SIGIR 2023 Conversational Passage Re-ranking
- **獲得肯定**：政大資科正教授（2025/08 升等）；**Academia Sinica CITI 合聘**；與 Chuan-Ju Wang（AS CFDA Lab）長期協作發表 TREC / SIGIR 系統論文

### (2) 學生工程素養與實驗室文化

- **系統化能力**：CLIP Lab（Computational Linguistics and Information Processing）；與 AS CFDA Lab 協作放大產能
- **團隊合作**：推估 5-8 人（政大）+ 中研院協作；共著以學術機構 / 軟體業為主
- **產學合作經驗**：金融業（FinTech）；KKStream 生態；AIF 教育推廣
- **獲得肯定**：SIGIR 主場持續產出；MS Research Asia Best Intern（2005-06，榮譽價值，非現任關係）

### (3) 合作分析

**優點**
- 台灣 IR + LTR 核心學者（SIGIR 主場）
- 方法論（LTR、Dense Retrieval、Query Reformulation）對製程文件 RAG 高度可移植
- 零半導體廠綁定
- AS CITI 合聘 → 可利用 AS 精英 Lab 資源
- 純軟體背景，不與硬體 PI 競爭

**缺點 / 風險**
- 無半導體 domain 先例 → 需配 TSMC 端 domain 專家
- Lab 規模偏小（5-8 人 + AS 協作）
- 部分近年研究偏金融文字 NLP，非製程直接命中
- 需確認對製程文件 / 工程師知識庫等應用場景的興趣

**建議合作方式**
- 合作類型：**製程文件 RAG PoC（與黃瀚萱 CAG 對照實驗）**
- 預算區間：5 年 300-500 萬 NTD
- 期程：第一年 PoC（6-12 月）→ 3 年擴大
- **KPI**：
  - TSMC 內部 Wiki + Confluence + 製程 SOP 10k 份文件的 LTR 檢索基準
  - Bug Report / Defect Ticket 智能檢索（LTR + Negative Sampling）準確率 ≥ 85%
  - SIGIR / CIKM 共著 1-2 篇/年
  - Top-5 Accuracy 與 CAG 路線對照 benchmark
- 交付物：檢索系統 + 論文 + 2-3 名學生實習

---

## #14. 黃瀚萱 Hen-Hsen Huang（Academia Sinica 資訊所 副研究員）

**分數**：7.2 | **接觸建議**：第二波

### (1) 教授技術領域的契合度

- **AI 架構能力**：**Cache-Augmented Generation (CAG)、RAG、LLM Evaluation、Discourse Analysis、Information Retrieval、Chinese Processing、Figurative Language、Multimodal (VLM + Text-to-Image)**
- **半導體 AI 相關計畫**：AS 資訊所副研究員；TAIDE 模型鑄造組顧問（2024-，政府 AI 生態）
- **產業合作**：**零大廠綁定**（Google 早年實習已超 10 年超時效）；TAIDE 為政府計畫非私人大廠
- **研究成果與貢獻**：**"Don't Do RAG: When CAG is All You Need" (WWW 2025, 81 引用)**；AAAI 2025 Conversational Adaptability；NAACL 2025 LLM Language Varieties；ACL 2024 Findings LLM Selection Biases（57 引用）；IJCAI 2024 LLM+VLM+Text-to-Image
- **落地使用**：**CAG 為 2025 RAG 領域新範式**（目前被廣泛討論，被視為挑戰 RAG 正統）；特別適合封閉且有限的 domain corpus（製程 SOP 正是這類）；NTU CSIE PhD；曾 NCCU 助理教授（~2018-2022）
- **獲得肯定**：WWW / AAAI / NAACL 三個 A*/A main conference 連續產出（2025）；TAIDE 顧問背書；ACL Findings 57 引用

### (2) 學生工程素養與實驗室文化

- **系統化能力**：Language and Knowledge Technologies Lab；從 NCCU 時期到 AS 時期的持續 Lab 經營
- **團隊合作**：AS 精英型 Lab（跨機構共指導 5 人透過 AS-TIGP 或 NTU/NCCU/NCTU）
- **產學合作經驗**：TAIDE 政府 AI 生態；NCCU 時期學生多進金融科技（國泰、玉山、中信）與 AI 新創
- **獲得肯定**：AS 資訊所副研究員（升等中）；2024-2025 三篇主會議；TAIDE 顧問團成員

### (3) 合作分析

**優點**
- 2025 RAG 領域新範式提出者（CAG 論文 81 引用）
- 特別適合 TSMC 製程 SOP 封閉語料場景（免 retrieval 基建 + 低延遲）
- AS 機構本就鼓勵與業界共建 Joint Lab（官方框架）
- TAIDE 顧問 → 政府 AI 生態同陣營（類似 SAT 定位，中性偏加分）
- 零大廠綁定 → 對 TSMC 最乾淨
- 跨機構共指導彈性高

**缺點 / 風險**
- 非半導體 domain，需 TSMC 引入應用場景
- AS 體制學生量中等（AS 無學位，需透過共指導）
- TAIDE 顧問可能佔部分時間
- 若 CAG 範式在 1-2 年被 RAG 新變種反超，獨占價值折損

**建議合作方式**
- 合作類型：**CAG vs 傳統 RAG 對照實驗（與蔡銘峰平行啟動）**
- 預算區間：5 年 300-500 萬 NTD + 提供 TSMC 工程師諮詢資料集（去敏感化）
- 期程：第一年 PoC 對照 → 3 年擴大
- **KPI**：
  - 2-day workshop：CAG vs 傳統 RAG 在 TSMC Wiki/Confluence/SOP 上的 Accuracy / Latency / Cost 比較
  - WWW / AAAI / NAACL 共著 1-2 篇/年
  - 透過 AS-TIGP 接 2-3 位跨機構博生設立 TSMC RAG 計畫
  - TSMC 內部使用者滿意度 ≥ 80%
- 交付物：CAG 系統 + 對照研究論文 + 學生

---

## #16. 彭文志 Wen-Chih Peng（NYCU 資工正教授）

**分數**：7.0 | **接觸建議**：第三波

### (1) 教授技術領域的契合度

- **AI 架構能力**：**Data Mining、Deep Learning、Time Series、Agentic AI、Decomposed Information Retrieval、Tabular Regression、Multi-Granularity Segmentation、Test-Time Expert Aggregation**
- **半導體 AI 相關計畫**：NYCU 資工正教授（2022 起）；前資工系主任（2019-2022）、前電資學院副院長、**前 E-SUN-NCTU Fintech and AI Center Director（2021-2024 卸任）**；KT Li Award 2019
- **產業合作**：前 E.SUN Bank Fintech Center Director（2024 卸任，企業共建 Lab 制度有先例）；無當前半導體廠綁定
- **研究成果與貢獻**：**Agentic Decomposed IR、Financial Report Generation、MedPlan RAG、Tabular Pre-training (APAR)、Time Series Segmentation (PromptTSS)、Book-Length Document MT Evaluation、Test-Time Expert Aggregation for Imbalanced Regression、Sports Data Analysis**
- **落地使用**：**SIGIR 2025 Template-Based Financial Report Generation in Agentic and Decomposed IR**（可直接改裝為「製程異常報告自動生成」、「良率週報自動產生」）；**ACL 2025 Industry Track MedPlan Two-Stage RAG**（可對應個人化製程調機建議 / Per-tool Recipe）；AAAI 2025 APAR Tabular Regression（對應 VM / 良率預測）
- **獲得肯定**：**2025 年單年 SIGIR + AAAI + ACL + EMNLP + CIKM main conference 各 1 篇**（本批次會議深度最深 PI）；2019 KT Li Award；WSDM 2026 Expert Aggregation

### (2) 學生工程素養與實驗室文化

- **系統化能力**：ADSL Lab（Advanced Database System Laboratory，2003 成立）；**15 人中大型 Lab（5 博 + 10 碩 + 0 博後）**
- **團隊合作**：5 位博生中 3 位為東南亞/國際學生（越南背景），國際化程度高
- **產學合作經驗**：E.SUN Fintech Center Director（企業共建 AI Center 實戰經驗）；雲端運算協會顧問（2014-2016 已過期）
- **獲得肯定**：KT Li Award 2019；前 NYCU 資工系主任 + 電資副院長行政資歷；h-index 高（research.com 資料）

### (3) 合作分析

**優點**
- **唯一一位已操盤過 E.SUN 企業共建 AI Center 的候選人**（制度面最容易複製）
- SIGIR 2025 Agentic Decomposed IR 直接就是 TSMC 要的範式（財報 → 製程報告）
- Lab 規模 15 人大（4x 蔡銘峰）
- 2025 單年 5 篇 main conference 會議深度最深
- 0 大廠綁定 + 2024 年剛卸任 E.SUN 的窗口黃金期
- 與李家岩有互動（社群關係近）

**缺點 / 風險**
- 無半導體 domain 先例
- 年齡推估 ~55 歲，黃金期剩 10 年
- 與蔡銘峰 / 黃瀚萱方法論部分重疊（需等第二波對照結果再決定是否深化）
- 金融業與半導體不競爭但 fintech 合作慣性可能延續 1-2 年
- 學生非硬體背景，進 TSMC 需經過軟體 / IT 職缺

**建議合作方式**
- 合作類型：**Agentic + Decomposed IR for Fab Report Generation**
- 預算區間：5 年 500-800 萬 NTD（比蔡銘峰 / 黃瀚萱高，因 Lab 規模大可支撐 3-4 位全職博生）
- 期程：12-18 個月 PoC（等第二波對照結果）→ 成功後擴大
- **KPI**：
  - 把 SIGIR 2025 財報範式改裝成「TSMC 月度良率報告自動生成 + 根因追查」
  - SIGIR / AAAI / ACL / EMNLP 共著 2-3 篇/年
  - 5 位博生中鎖定 1-2 位 2028 畢業 → TSMC FIT / 良率部門
  - APAR Tabular + LLM 在 VM 應用 benchmark
- 交付物：Agentic 報告生成系統 + 論文 + 學生通道

---


---


# 關鍵字矩陣

> **用法**：橫向 16 位教授、縱向 20 個技術關鍵字。✅ 代表該教授在此關鍵字上有 2023-2026 期間的代表性發表或產業落地。方便主管根據特定技術需求快速查找對應 PI。

## 關鍵字分群

- **前段 Device / 製程**：GAA FET、FeFET、CIM、AI-assisted EDA、TCAD、DTCO
- **AOI / 缺陷**：AOI / Vision、Domain Adaptation、Yield Prediction
- **封裝**：CoWoS / 3D-IC、Hybrid Bonding、nt-Cu / 材料、Warpage Prediction
- **fab 方法論**：Virtual Metrology、R2R / SPC、Reinforcement Learning for Scheduling、Digital Twin、Multi-Armed Bandit / Bayesian
- **LLM / 軟體**：LLM / RAG、Agentic AI、Vision Transformer

## 矩陣（16 位 × 20 關鍵字）

| 教授 \ 關鍵字 | FeFET | GAA / CFET | CIM / Neuromorphic | AI-EDA / 光刻 | DTCO | TCAD | AOI / Vision | Domain Adaptation | Yield Prediction | CoWoS / 3D-IC | Hybrid Bonding | nt-Cu / 材料 | Warpage / FEA | Virtual Metrology | SPC / Knockoffs | RL Scheduling | Digital Twin | LLM / RAG | Agentic AI | Vision Transformer |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **王俊明**（#1*）| | | | ✅ | | | | | | | | | | | | | | | | |
| **馬誠佑**（#2）| ✅ | | ✅ | | | ✅ | | | | | | | | | | | | | | |
| **胡璧合**（#3）| ✅ | ✅ | ✅ | | ✅ | ✅ | | | | ✅ | | | | | | | | | | |
| **陳冠能**（#3）| | | | | | | | | | ✅ | ✅ | | | | | | | | | |
| **銀慶剛**（#5）| | | | | | | | | ✅ | | | | | ✅ | ✅ | | | | | |
| **陳智**（#6）| | | | | | | | | | ✅ | ✅ | ✅ | | | | | | | | |
| **詹寶珠**（#6）| | | | | | | ✅ | ✅ | | | | | | | | | | | | |
| **江國寧**（#8）| | | | | | | | | ✅ | ✅ | | | ✅ | | | | | | | |
| **宋振銘**（#9）| | | | | | | | | | ✅ | ✅ | ✅ | | ✅ | | | | | | |
| **李家岩**（#9）| | | | | | | | | ✅ | | | | | | | ✅ | | | | |
| **鄭桂忠**（#9）| | | ✅ | | | | | | | | | | | | | | | | | |
| **蔡佩璇**（#12）| | | | | | | ✅ | | | | | | | | | | ✅ | | | |
| **林嘉文**（#13）| | | | ✅ | | | ✅ | | | | | | | | | | | | | ✅ |
| **蔡銘峰**（#14）| | | | | | | | | | | | | | | | | | ✅ | | |
| **黃瀚萱**（#14）| | | | | | | | | | | | | | | | | | ✅ | | |
| **彭文志**（#16）| | | | | | | | | ✅ | | | | | | | | | ✅ | ✅ | |

## 補充：每個關鍵字對應的 PI 快速索引

### 前段 Device / 製程
- **FeFET**：馬誠佑、胡璧合
- **GAA / CFET / Nanosheet**：胡璧合
- **CIM / Neuromorphic**：馬誠佑、胡璧合、鄭桂忠
- **AI-EDA / 光刻 / OPC**：王俊明、林嘉文
- **DTCO**：胡璧合
- **TCAD**：馬誠佑、胡璧合

### AOI / 缺陷
- **AOI / Computer Vision 缺陷**：詹寶珠、蔡佩璇（SOP）、林嘉文
- **Domain Adaptation**：詹寶珠（醫療 → AOI 方法論遷移）
- **Yield Prediction**：銀慶剛、江國寧、李家岩、彭文志（tabular ML）

### 封裝
- **CoWoS / 3D-IC / SoIC**：陳冠能、陳智、江國寧、胡璧合（M3D）
- **Hybrid Bonding / Cu-Cu Bonding**：陳冠能、陳智、宋振銘
- **nt-Cu / 封裝材料**：陳智、宋振銘
- **Warpage Prediction / FEA × ML**：江國寧

### fab 方法論
- **Virtual Metrology（VM）**：銀慶剛、宋振銘（線上量測）
- **SPC / Knockoffs / 統計異常追因**：銀慶剛
- **Reinforcement Learning for Scheduling**：李家岩
- **Digital Twin**：蔡佩璇、彭文志（Agentic Report 類比）
- **Multi-Armed Bandit / Bayesian**：銀慶剛（JASA 2024 MAB）、鄭桂忠（Bayesian NN CIM）

### LLM / 軟體層
- **LLM / RAG**：蔡銘峰、黃瀚萱、彭文志
- **Agentic AI / Tool Use**：彭文志（SIGIR 2025 Agentic Decomposed IR）
- **Vision Transformer / Multimodal**：林嘉文、黃瀚萱（IJCAI 2024 VLM + Text-to-Image）

---

## 矩陣解讀

### 每位 PI 的主要 3-4 個關鍵字（專長焦點）

| PI | 主要關鍵字 |
|---|---|
| 王俊明 | AI-EDA / 光刻 |
| 馬誠佑 | FeFET + CIM + TCAD |
| 胡璧合 | FeFET + GAA/CFET + CIM + 3D-IC + DTCO |
| 陳冠能 | 3D-IC + Hybrid Bonding |
| 銀慶剛 | Yield Prediction + VM + SPC/Knockoffs |
| 陳智 | Hybrid Bonding + nt-Cu + 3D-IC |
| 詹寶珠 | AOI/Vision + Domain Adaptation |
| 江國寧 | Warpage/FEA + Yield Prediction + 3D-IC |
| 宋振銘 | Hybrid Bonding + nt-Cu + 3D-IC + VM |
| 李家岩 | RL Scheduling + Yield Prediction |
| 鄭桂忠 | CIM / Neuromorphic |
| 蔡佩璇 | Digital Twin + AOI/Vision |
| 林嘉文 | Vision Transformer + AI-EDA + AOI |
| 蔡銘峰 | LLM / RAG |
| 黃瀚萱 | LLM / RAG |
| 彭文志 | LLM / RAG + Agentic AI + Yield Prediction |

### 關鍵字覆蓋完整性
所有 20 個關鍵字皆有至少 1 位 PI ✅；部分熱門題目（CIM、3D-IC、Hybrid Bonding、Yield Prediction、LLM/RAG）有 3-4 位 PI 覆蓋，適合做 PoC 對照實驗或多 PI 互補合作。


---


# 附錄

---

## 附錄 A：接觸策略詳表

### A.1 第一波（6 位，3-6 個月內啟動）

| 教授 | 接觸 owner 建議 | 優先合作題目（1-2 個）| 預估預算 5 年（NTD）| 關鍵 KPI |
|---|---|---|---|---|
| 王俊明（NSYSU SAT）| 法務 + R&D Director 雙頭接觸（法務先 clear，R&D 後談技術）| (1) 2nm EUV OPC ML hotspot prediction；(2) Curvilinear mask + RET 協同最佳化 | 300-500 萬（個人級）→ 若 ISMID 院級擴大 800-1200 萬 | SPIE 一作 1-2 篇/年；TSMC 製程 data 上 hotspot prediction ≥ 95% |
| 馬誠佑（NSYSU ADDA）| Device R&D 接觸 | (1) FeFET compact model SPICE 產業級釋出；(2) HfZrO cycling reliability 物理模型 | 300-500 萬 | IEEE TED / IEDM 共著 1-2 篇/年；SPICE model 交付 |
| 胡璧合（NTU）| Device R&D + 美光關係確認後接觸 | (1) BEOL HZO FeFET 可靠性 SPICE；(2) M3D CIM Macro 功耗-精度-面積協同；(3) 2D CFET × FeFET A7/A5 NV-SRAM | 500-800 萬 | VLSI 2026 / ISSCC 2027；PhD Scholarship 3 位續約 |
| 陳冠能（NYCU ICST）| VP-level / Dean-to-Dean 接觸（ICST 院級合作需高層主導）| CoWoS-L 下一代層轉移 JDP；Hyper RDL 升級路徑 | 800-1200 萬（院級）| IEDM/VLSI 共著 4-6 篇/年；每年 6+ 位頂會一作學生通道至 TSMC |
| 銀慶剛（NTHU 統計）| 數據科學 R&D + 法務（IP 共有 check）雙管 | (1) 2nm sensor feature selection 高維異方差迴歸；(2) TSKI sensor trace 異常監控；(3) 缺陷機台識別 2nm 升級（延續 2014 成果）| 300-500 萬 + fab sensor log 匿名化資料 | JCGS / Statistica Sinica / JASA 共著；fab 可落地 feature selection 工具 |
| 江國寧（NTHU PME）| VP 封裝 R&D 接觸（先進封裝研究中心級合作）| (1) CoWoS/HBM 疲勞壽命 AI 預測（小樣本學習 + FEA metamodel）；(2) wafer-level packaging ML | 600-1000 萬（中心級）| 每年 FEA + ML 博士生 3-5 人直送 TSMC 良率；ASME/iMAPS/Materials 共著 3-4 篇/年 |

**第一波合計**：**2,700 - 4,200 萬 NTD / 5 年**（視 ICST 院級、先進封裝中心級是否正式成立）

### A.2 第二波（7-8 位，6-12 個月補上）

| 教授 | 接觸 owner 建議 | 優先合作題目（1-2 個）| 預估預算 5 年（NTD）| 關鍵 KPI |
|---|---|---|---|---|
| 陳智（NYCU 材料）| Packaging R&D | (1) SoIC Hybrid Bonding nt-Cu 電鍍參數最佳化；(2) 透過 Chemleader 客製化 TSMC 配方 | 400-600 萬 | TSMC-fab-compatible nt-Cu 配方；Nano Letters / JMRT 共著 2-3 篇/年 |
| 詹寶珠（NCKU 電資院長）| 院長級接觸（Dean-to-Dean）| N7→N5→N3 AOI 缺陷檢測模型跨節點遷移 PoC | 300-500 萬 | 跨 Line 遷移準確率 ≥ 90%；Knowledge-Based Systems 共著 |
| 宋振銘（NCHU 研發長）| 封裝 R&D + 校級研發長 | (1) Cu-Cu 線上感測器 TRL 6；(2) AI 預測平台（接合強度）整合 | 300-500 萬 | 感測器硬體 + AI 軟體交付；學生進 TSMC AP / 日月光暑期 |
| 李家岩（NTU 資管）| Manufacturing Science 接觸 | (1) fab reticle DRL 排程；(2) chiller MARL 能源 | 400-600 萬 | MILP baseline 改善 ≥ 10%；IEEE TASE / TSM / IJPE 2 篇/年 |
| 鄭桂忠（NTHU 電機）| IC R&D（確認 TSMC-JDP 現任題目不 conflict）| 22→7nm CIM macro tape-out；邊緣 AI 加速器 | 500-800 萬 | tape-out 晶片 + ISSCC/VLSI 2-3 篇/年 |
| 蔡佩璇（NCKU IMIS）| FIT / IE R&D（等 Fulbright 結束 2025）| fab Edge DT 原型；SOP 視覺驗證系統 | 300-500 萬 | SOP 驗證準確率 ≥ 95%；IEEE IoT J 共著 |
| 蔡銘峰（NCCU 資科）| IT / FIT（RAG PoC 主導部門）| 製程文件 LTR 檢索基準；Defect Ticket 檢索 | 300-500 萬 | TSMC Wiki/Confluence Top-5 Accuracy ≥ 85%；SIGIR/CIKM 共著 |
| 黃瀚萱（AS 資訊所）| IT / FIT（與蔡銘峰對照組） | CAG vs 傳統 RAG 對照實驗（2-day workshop kickoff）| 300-500 萬 + 去敏感化資料集 | Accuracy/Latency/Cost 對照；WWW/AAAI 共著 |

**第二波合計**：**2,800 - 4,500 萬 NTD / 5 年**

### A.3 第三波（2 位，12-18 個月補位）

| 教授 | 接觸 owner 建議 | 優先合作題目 | 預估預算 5 年（NTD）| 關鍵 KPI |
|---|---|---|---|---|
| 林嘉文（NTHU 電機）| EDA 部門 | 電腦視覺 EDA 工具（IC 製程模擬 + 光刻失真預測）| 300-500 萬（第一年 100 萬 PoC）| PoC vs 現有 OPC 工具 benchmark；IEEE TIP/CVPR 共著 |
| 彭文志（NYCU 資工）| IT / FIT（等第二波對照結果）| Agentic + Decomposed IR for Fab Report Generation | 500-800 萬 | 月度良率報告自動生成 PoC；SIGIR/ACL 2-3 篇/年 |

**第三波合計**：**800 - 1,300 萬 NTD / 5 年**

---

## 附錄 B：5 年預算分配明細

### B.1 總預算彙總

| 階段 | PI 人數 | 預算區間（5 年）| 累積合計 |
|---|---|---|---|
| 第一波 | 6 位 | 2,700 - 4,200 萬 NTD | 2,700 - 4,200 萬 |
| 第二波 | 7-8 位 | 2,800 - 4,500 萬 NTD | 5,500 - 8,700 萬 |
| 第三波 | 2 位 | 800 - 1,300 萬 NTD | **6,300 - 10,000 萬 NTD / 5 年** |

**實務保守估計**：主要預算約 **4,000 - 7,000 萬 NTD / 5 年**（不含院級 / 中心級擴大 option）

### B.2 分類別預算分配（5 年保守估計）

| 類別 | PI 人數 | 合計（5 年）| 備註 |
|---|---|---|---|
| 前段 Device / 製程（王俊明、馬誠佑、胡璧合）| 3 位 | 1,100 - 1,800 萬 | 胡璧合預算佔大頭（頂會密度高）|
| 封裝 AI 中心合併預算（陳冠能、陳智、江國寧、宋振銘）| 4 位 | 2,100 - 3,100 萬 | 建議合併為單一中心運作 |
| fab SPC/VM/OR 方法論（銀慶剛、李家岩、詹寶珠、蔡佩璇）| 4 位 | 1,300 - 2,100 萬 | 其中銀慶剛需 fab 資料提供 |
| AI 晶片 / CIM（鄭桂忠）| 1 位 | 500 - 800 萬 | tape-out 成本較高 |
| 工程師效率 RAG 對照實驗合併（蔡銘峰、黃瀚萱、彭文志）| 3 位 | 1,100 - 1,800 萬 | 建議合併為單一 PoC 計畫 |
| 光刻 EDA PoC（林嘉文）| 1 位 | 300 - 500 萬 | 先 PoC 成功再擴大 |
| **總計** | **16 位** | **6,400 - 10,100 萬** | **保守估計 4,000 - 7,000 萬** |

### B.3 學生獎學金 / CapEx 不含項目

本報告預算不含以下項目，實際執行時需額外編列：
- 博士生獎學金（TSMC PhD Scholarship 類似制度，每位 100-150 萬/年）
- fab test chip tape-out 費用（視 node 不同，每次 200-2000 萬）
- 跨國差旅 / 國際頂會參與補助
- TSMC 內部 IT / 資料平台建置（RAG 對照實驗等）

---

## 附錄 C：法務 Pre-flight Check List

### C.1 王俊明（第一波 blocker）

- [ ] TSMC 離職年數確認（離職滿 X 年無競業限制？需查看原合約的競業條款）
- [ ] TSMC 期間商業機密獎項清點（比對林勇志 2021 Gold Trade Secret Silver Award 先例）
- [ ] Google Patents / Justia 等公開資料庫再次確認王俊明名下以 TSMC 為 assignee 的光刻專利（已初查無結果，需進一步核對中文資料庫）
- [ ] NSYSU 中文版官方簡歷 TSMC 任職年份（目前網頁 404，待網站恢復）
- [ ] 合約終止條款 + NDA 有效期限解讀
- [ ] ISMID 所長身份與雇主產業立場潛在衝突評估
- [ ] 若在職期間曾接觸 TSMC 南科相關 2nm 核心工藝，需評估「回流禁止期」

### C.2 銀慶剛（第一波）

- [ ] **US12354122B2 與 NCKU 鄭芳田 IP 共有狀態**確認（此為關鍵 blocker）
- [ ] 若共有 → 合作範圍界定（避免 TSMC 新合作成果又自動授權給鄭芳田 / IYM 系統生態）
- [ ] 鄭芳田與 TSMC 的 AVM 系統合作條款確認（雇主若非 TSMC 或為 TSMC 競爭方特別重要）
- [ ] 清華講座教授（校方冠名非企業）無 NDA 風險，但建議文件化

### C.3 鄭桂忠（第二波）

- [ ] 現任 TSMC-NTHU JDP 題目清單盤點（與新合作是否 conflict）
- [ ] Nature 2025 / Science 2024 共著 TSMC 工程師名單（既有合作深度評估）
- [ ] ITRI 技術長（2017-）part-time 兼職對新合作的影響評估
- [ ] 台達飛雁計畫 2022 冠名條款查閱

### C.4 胡璧合（第一波）

- [ ] 美光 Foundation Chair Professor 2024 條款確認（是否有記憶體方向排他）
- [ ] 3 位 TSMC PhD Scholarship 學生（2022-2024 得主）畢業後 TSMC 優先僱用條款
- [ ] IEEE CAS NG-TC Chair-Elect 身份對新合作資源的影響（正面意義大）

### C.5 通用檢查

- [ ] 所有 16 位 PI 當前產業顧問身分清點（conflict of interest）
  - 李家岩 Profet AI 顧問（2023-）→ 是否與 TSMC 合作方向衝突
  - 詹寶珠 IEEE CIS VP-Education 義務角色 → 無衝突
  - 蔡銘峰 AIF 講師（已離開）→ 無衝突
  - 黃瀚萱 TAIDE 顧問 → 政府 AI 生態非競爭大廠，中性偏加分
  - 彭文志 前 E.SUN Fintech Center Director（2024 卸任）→ 無衝突

- [ ] NTU / NTHU / NSYSU / NYCU / NCKU / NCHU / NCCU / AS 各校產學合作 overhead 比例確認
  - NTU：約 15-20%
  - NTHU：約 15-20%
  - NSYSU：約 10-15%
  - NYCU：約 15-20%
  - NCKU：約 15-20%
  - NCHU：約 10-15%
  - NCCU：約 10-15%
  - AS：約 5-10%（中研院通常較低）

- [ ] IP 歸屬模板選擇（每個合作需擇一）
  - 完全歸學校（default）
  - TSMC-學校共有
  - TSMC 獨占（委託研究）
  - 開源發布（論文 + code）

- [ ] NDA 範圍（每位 PI 簽署）
  - fab data 去敏感化等級
  - TSMC 內部流程 / 製程 recipe 不對外
  - 論文發表前 TSMC 審閱期（通常 30-60 天）

- [ ] 利益衝突申報（每年更新）

- [ ] 共同發表授權（author 順序 / 致謝條款）

---

## 附錄 D：研究方法論（5 維度評分框架）

本研究評分採用「TSMC 視角 5 維度」框架（每維度 0-2 分，總分 0-10）：

### D.1 維度 1：技術契合度（Technology Fit）

評分邏輯：
- **2.0 分**：近 3 年 IEDM / VLSI / ISSCC / SIGIR / JASA 等頂會頂刊直接命中目標題目（前段 Device、封裝、fab 方法論、工程師效率）
- **1.5 分**：頂刊發表但應用層面（非純方法論）；或頂刊但非命中核心題目
- **1.0 分**：次級會議 / 方法論可遷移但無半導體先例
- **0.5 分**：方向邊緣相關

### D.2 維度 2：產業落地（Industry Landing / Student Pipeline）

評分邏輯：
- **2.0 分**：Lab 規模 15+ 人、IEDM/ISSCC/SIGIR 一作學生每年 4+ 位、畢業生進 TSMC / 設備商有穩定紀錄
- **1.5 分**：Lab 10-15 人、頂會一作學生 2-3 位/年、畢業生進業界有紀錄
- **1.0 分**：Lab 5-10 人、中型產出、畢業生以學術 / 軟體業為主
- **0.5 分**：Lab < 5 人、或 Lab 重組中

### D.3 維度 3：企業共建 Lab 開放度（Openness to Corporate Partnership）

評分邏輯：
- **2.0 分**：已有企業 Joint Lab / Center Director 實戰經驗、或機構本就鼓勵（如 AS）
- **1.5 分**：有 JDP / 冠名 / 產學合作先例、院級 / 中心級身份
- **1.0 分**：有 NSTC 計畫 + 個案合作經驗
- **0.5 分**：純學術導向、無企業合作先例

### D.4 維度 4：資源未被搶佔程度（Uncaptured Resource）

評分邏輯：
- **2.0 分**：完全無大廠綁定、無企業冠名、無 JDP / 顧問職
- **1.5 分**：有 1 個非競爭廠商綁定（如美光 Chair 對 TSMC 邏輯製程為中性）
- **1.0 分**：有 TSMC-JDP 研究經費依賴（非機構忠誠）、或多方均衡合作
- **0.5 分**：深度綁定競爭方（NVIDIA Director / Intel CR / Samsung Executive 等）—— 此類直接剔除

### D.5 維度 5：長期可持續性（Long-term Golden Period）

評分邏輯：
- **2.0 分**：40-55 歲、無重大行政職、研究動能強（近 5 年引用增長 ≥ 50% 總引用）
- **1.5 分**：45-60 歲、有行政職但研究動能維持
- **1.0 分**：60-65 歲、行政職佔比高、或轉校 Lab 重組中
- **0.5 分**：65+ 歲、預期黃金期 < 5 年

### D.6 評分資料來源

每位 PI 的 5 維度分數來自以下交叉驗證：
- Google Scholar h-index + 近 5 年引用
- DBLP / ACL Anthology 近 3 年頂會論文
- 學校官網職銜 / 實驗室資訊
- NSTC GRB 計畫紀錄
- LinkedIn / 個人首頁
- 新聞公開報導（業界合作紀錄）
- WebSearch 驗證（2026-04-23）

詳細方法論可參考：`templates/pi-due-diligence-framework.md`（本 repo 內）

---

**本報告完成時間**：2026-04-23  
**下一步**：主管圈選第一波 6 位後啟動正式 outreach 流程；法務同步 C.1 / C.2 pre-flight check
