# Phase 2 深度 Profile — 鄭少為 Shao-Wei Cheng

- **執行日期**：2026-04-22
- **研究員**：Phase 2 深度 profile agent（WebFetch + WebSearch + headless browse）
- **任務背景**：Top 20 #15（替補唐麗英位置），T1 軌（SPC/DoE/製程最佳化）— 評估「DoE × ML 製程窗口模擬」核心 PI 可行性

---

## ⚡ 結論先行

| 項目 | 評定 |
|---|---|
| **隱形綁定等級** | 🟢 **Free Agent（無任何半導體廠正式綁定）** |
| **合作可行性** | 🟡 **條件式可行**（技術核心方向吻合但近年論文產出偏少；需確認是否有意轉向應用） |
| **Phase 2 建議優先** | ⭐⭐⭐（T1 DoE 理論背景紮實，但半導體應用場景啟動摩擦較高） |

**一句話摘要**：鄭少為是台灣學界 DoE 理論的重要代表人物，師出 C.F. Jeff Wu 門下，2001-2019 年間有若干高品質期刊論文，但近年（2020-2026）無可追溯的新頂期刊論文；無 TSMC/聯發科/聯電任何正式綁定；工業合作以新竹科學園區廠商與中科院為主，非半導體晶圓廠層級。

---

## §1 隱形綁定檢查

### 1.1 TSMC-NTHU JDP 教授身份（最高優先 — 清大教授常見綁定）

**查驗結果：確認「未列名」。**

親自爬取 `nthu-tsmc.site.nthu.edu.tw/p/412-1578-20665.php` 完整 JDP 教授名單（27 位），涵蓋電機系、材料系、動機系、化工系、資工系、物理系教授，**鄭少為（Statistics 統計所）未在其中**。名單中另有一位「鄭桂忠」（電機系），為不同人物，已確認。

**意涵**：統計所教授不屬於 TSMC-NTHU JDP 合作的自然招募對象（JDP 以 EE/ME/材料/ChemE 為主），**此綁定路徑排除**。

### 1.2 其他半導體廠兼職/顧問（聯發科、聯電、美光、ASML）

多重搜尋（英文姓名 + 機構名、中文姓名 + 廠商名稱）均無命中。

**查驗結論（各廠商）：**

| 廠商 | 搜尋結果 |
|---|---|
| TSMC 台積電 | 無任何正式職務紀錄 |
| MediaTek 聯發科 | 無 |
| UMC 聯電 | 無 |
| Micron 美光 | 無 |
| ASML | 無 |

**整體結論：無任何半導體廠兼職/顧問/正式職務。**

### 1.3 論文 Acknowledgments 資金來源（近 3 年）

由於 2020-2026 年間**無可在公開資料庫中找到的新頂期刊論文**（見 §2.4），此欄位**無法直接查驗**。

**已知事實**：2019 年 Annals of Statistics 論文（與 Ming-Chung Chang、Ching-Shui Cheng 共著）未涉及任何半導體廠資金；通過 Academia Sinica 的計畫資助。Epoch Times 2007 年報導明確提及他與「新竹科學園區廠商」及「中山科學研究院（中科院）」有產學合作，但均非 TSMC/聯發科等晶圓廠。

### 1.4 冠名講座

查驗結果：**無**。NTHU 統計所的冠名講座機制（如有）未查到鄭少為相關紀錄。

### 1.5 NSTC 計畫主持紀錄中的業界合作方

直接查驗 NSTC 學術補助獎勵查詢系統（wsts.nstc.gov.tw）因介面限制無法直接搜尋個人紀錄。

**已知間接資訊**：
- 2005 年獲「吳大猷先生紀念獎」（國科會），顯示過去有 NSTC 計畫主持資歷
- 2007 年 Epoch Times 訪談：「回台後與新竹科學園區廠商、中山科學研究院合作，解決各類工業問題」—— 此為 **工業統計/DoE 顧問性質**，而非晶圓製程產學計畫
- NSTC 統計學門教授 NSTC 人才查詢頁面（需 Google 帳號登入）未能訪問，**業界合作方未確認**

---

## §2 技術契合度

### 2.1 現任職務與實驗室

- **職銜**：副教授（Associate Professor）—— **注意：現為副教授，不是教授，17 年未晉升正教授**
- **機構**：國立清華大學理學院統計與數據科學研究所
- **辦公室**：綜合三館 818 室
- **聯絡**：swcheng@stat.nthu.edu.tw | 03-5715131 #33162
- **個人頁面**：`http://www.stat.nthu.edu.tw/~swcheng/`（外部無法連線，僅校內可達）
- **ORCID**：0000-0002-6618-6755 | **Scopus Author ID**：7404684695
- **Lab 結構**：無獨立命名實驗室，屬統計所通用研究室規格

**同所競業分析**：同所 Ray-Bing Chen（陳瑞彬）教授（正教授）研究領域為「Industrial Statistics, Design of Experiment, Statistical Computing and Modeling, Statistical and Machine Learning」，與鄭少為**高度重疊且層級更高**，是統計所 DoE × ML 方向的主力。

### 2.2 研究主題（與 Tier 命中度）— T1 DoE/GP 對半導體製程最佳化的對口

| 研究主題 | 技術命中 | Tier 命中 |
|---|---|---|
| 因子篩選（Factor Screening）+ 反應曲面（RSM）| ⭐⭐⭐⭐⭐ | **T1 DoE 核心** |
| 分次因子設計（Fractional Factorial Design）最佳化 | ⭐⭐⭐⭐⭐ | **T1** |
| Gaussian Random Field（Gaussian Process 前身概念）| ⭐⭐⭐⭐ | **T1 GP Emulator 邊緣** |
| 質性因子（Qualitative Factors）在 GP 模型中的 Aliasing | ⭐⭐⭐⭐ | **T1 Computer Experiment** |
| 功能性線性模式（Functional Linear Model）本質編碼 | ⭐⭐ | **T1 邊緣（偏理論）** |
| 半導體製程直接應用（Virtual Metrology、Plasma Etch DoE）| ⭐（未確認）| **T1 應用層待建立** |

**技術優勢**：DoE 理論基礎深厚，師出 Jeff Wu（密西根大學，國際 DoE 宗師）門下，發表過 Statistica Sinica（SCI, 2001）、Technometrics（SCI, 2002, 2004 ×2）、Annals of Statistics（Top-3 統計期刊, 2019）等高品質論文。

**技術缺口**：現有公開記錄無具體半導體製程應用（TSMC 製程窗口、Virtual Fab、etch optimization 等），且 2010-2018 年間論文可見度極低，近年方向轉向功能性資料分析（Functional Linear Model），**與 T1 製程應用的鏈結需重新建立**。

### 2.3 Google Scholar 指標

鄭少為**無可確認的公開 Google Scholar 個人頁面**（搜尋多次未找到，或未建立）。以下為透過 Scopus Author ID（7404684695）和論文引用資料估算：

- **ResearchGate 顯示**：「8 研究成果，315 引用次數」（截至搜尋日期）
- **主要引用來源**：早期 Technometrics / Statistica Sinica / Annals of Statistics 論文
- **h-index**：**未確認**（無公開頁面，訓練資料無可靠資訊）

**注意**：315 次引用對應 17-25 年的論文，平均年引用率偏低，**在台灣統計界中屬中等量級**（對比同所陳瑞彬等正教授）。

### 2.4 頂級期刊（Technometrics/JQT/JASA/Biometrika/Bayesian Analysis）近 3 年論文

**查驗結果：近 3 年（2023-2026）無可追溯的新頂期刊論文。**

近年**唯一可確認的學術呈現**為 EcoSta 2019 的口頭報告（E0551），題目「Identifying essence codings and effects in functional linear models」——屬功能性線性模型方向，而非 DoE/GP 方向。

**ResearchGate（8 篇列表）與 DBLP（3 篇，最新至 2006 年）一致顯示**：自 2019 年 Annals of Statistics 論文後，無新的已知頂期刊論文記錄。**此為本 Profile 最大的不確定性警示。**

可能解釋：
1. 期刊論文在審查中（under review），尚未公開
2. 研究方向轉換期（功能性資料分析 → ？），產出空窗
3. 副教授晉升正教授壓力減少（長期停留副教授，無升等急迫性）

### 2.5 代表論文（歷史紀錄，2001-2019）

以下為確認有記錄的論文，按年份排列：

| 年份 | 論文標題 | 期刊 | 共著者 |
|---|---|---|---|
| 2001 | Factor Screening and Response Surface Exploration (with discussion) | *Statistica Sinica*, 11, 553-604 | **C.F.J. Wu**（密大） |
| 2002 | Choice of Optimal Blocking Schemes in Two-Level and Three-Level Designs | *Technometrics*, 44(3), 269-277 | **C.F.J. Wu** |
| 2003 | Finding Defining Generators with Extreme Lengths | *J. Statistical Planning and Inference*, 113, 315-321 | （未確認共著者）|
| 2004 | Blocked Nonregular Two-Level Factorial Designs | *Technometrics*, 46(3), 269-279 | William Li, Kenny Q. Ye |
| 2004 | Optimal Projective Three-Level Designs for Factor Screening and Interaction Detection | *Technometrics*, 46(3), 280-292 | Hongquan Xu, **C.F.J. Wu** |
| 2006 | Statistical Modeling for Experiments with Sliding Levels | *IMS Lecture Notes-Monograph Series*, 52, 245-256 | **C.F.J. Wu**, L. Huwang |
| 2019 | Signal Aliasing in Gaussian Random Fields for Experiments with Qualitative Factors | *Annals of Statistics*, 47(2), 909-935（DOI: 10.1214/18-AOS1682） | Ming-Chung Chang（NCU）, Ching-Shui Cheng（UC Berkeley/Sinica）|

**特別標注**：
- 2019 Annals of Statistics 論文是目前找到的**最高影響力近期論文**，涉及 Gaussian Random Field 中的 Signal Aliasing 問題，是 GP Emulator for Computer Experiments 的理論基礎工作，**與 T1 Computer Experiment 方向直接相關**
- 2001 Statistica Sinica 論文被邀請討論（invited discussion paper），顯示在 DoE 領域的學術地位
- 2004 年在 *Technometrics* 同期（Vol 46 No 3）有**兩篇論文**，為生涯高峰

---

## §3 學生素質 & Lab 文化

### 3.1 Lab 規模與結構

- **無獨立命名實驗室**，屬統計所一般辦公室研究環境
- **Lab 規模**：依副教授通例推估，同一時期指導 2-5 位碩士生，博士生數量不確定（可能 0-2 位）
- **已知畢業博士生（確認）**：**Ming-Chung Chang（張明中）** —— NTHU 統計所碩士（鄭少為指導）→ NTHU 統計所博士（鄭少為指導）→ Academia Sinica 博後 → NCU 助理教授 → **現為 Academia Sinica 副研究員（Associate Research Fellow, from 2023）**。Chang 的碩士與博士論文均獲台灣統計學會獎項。
- **知名課程輸出**：機率論/統計學 OCW 課程（Bilibili 超過 10 萬觀看），顯示教學影響力遠超學術論文，是清大最廣為人知的基礎課教授之一

### 3.2 業界合作紀錄（替代 Tape-out）

**已確認的業界互動（依可靠度排序）：**

| 合作對象 | 性質 | 時期 | 可靠度 |
|---|---|---|---|
| 新竹科學園區廠商（未具名） | 工業統計 / DoE 顧問 | ~2005-2010 | 中（Epoch Times 訪談引述） |
| 中山科學研究院（CSIST/中科院）| 國防相關統計應用（推測為可靠度/品質管制）| ~2005-2010 | 中（Epoch Times 訪談引述） |
| 2004 年 *Technometrics* 邀請演講 | 美國工業統計最頂尖期刊認可 | 2004 | 高（Epoch Times 訪談確認）|

**未確認的業界合作**：NSTC 計畫業界共同主持方、近年（2015 後）的產學計畫狀況均**未確認**。

**評估**：業界合作深度顯著低於 T1 的理想要求。相比簡禎富（SMART Lab × TSMC 產學計畫）、洪英超（TSMC 製程品質監控應用），鄭少為的業界連結以**一般性工業統計顧問**為主，而非直接的晶圓廠製程資料合作。

### 3.3 畢業生流向（推估）

由於缺乏系統性的學生流向資料，以下為推估：

- **已確認路徑（1 人）**：Ming-Chung Chang → Academia Sinica（學界路徑）
- **統計所碩士生通常流向**：科技業（含 TSMC、聯發科）資料分析/BI 職位為主；少數進 Ph.D.
- **進入 TSMC/聯發科品質/統計方法部門的直接對口人數**：**未確認**

**注意**：清大統計所整體（非僅鄭少為 lab）有部分校友在 TSMC 製程整合/良率提升/品質統計部門工作，但無法確認哪些畢業自鄭少為實驗室。

### 3.4 外部認可（期刊 Editorial Board、統計學會、NSTC 獎項）

| 類別 | 記錄 | 狀態 |
|---|---|---|
| 中華統計學會 | 參與 CSA 2023（清大統計所35週年）組織委員會（清大會務委員） | 確認 |
| 校傑出教學獎 | NTHU 113 學年度（2024-2025）**校教師傑出教學獎**（2025-06-09 公告）| 確認 |
| NSTC 傑出研究獎 | **未列名** NTHU 理學院統計類歷屆名單（Chao, Tseng, Ing, Hwang, L.S. Huang）| 確認「未得獎」|
| NSC 吳大猷先生紀念獎 | 2005 年獲獎 | 確認 |
| Academia Sinica 年輕學者研究獎 | 2006 年獲獎 | 確認 |
| *Technometrics* 期刊邀請演講 | 2004 年受邀 | 確認 |
| 台灣十大潛力人物 | 2007 年獲選 | 確認 |
| 期刊 Editorial Board | **未查到任何期刊 editorial board 任職記錄** | 未確認 |

---

## §4 綜合分析：合作可行性

### 4.1 🟡 評定理由

**正面因素：**
1. **T1 理論基礎最紮實**：師出 Jeff Wu（國際 DoE 宗師），Technometrics × 3 + AoS × 1 + Statistica Sinica × 1 的學術組合是台灣統計界少數人能達到的水準
2. **完全自由身**：無任何半導體廠綁定，合作架構設計靈活度最高（與鄭桂忠的 TSMC-JDP 相比，鄭少為的合作窗口毫無束縛）
3. **GP 理論連結**：2019 AoS 論文直接碰觸 Gaussian Random Field for Computer Experiments，與 2nm GP Emulator 需求有理論對口
4. **副教授獨立運作**：無大型研究計畫牽制，有彈性加入新方向

**風險因素：**
1. **近年論文空窗（2020-2026）**：無法確認目前主力研究方向，可能已轉向其他領域
2. **副教授停留 17+ 年**：自 2007 年加入 NTHU 至今仍為副教授，職涯軌跡顯示研究產出不足以晉升；**合作廠商需評估學術生命力**
3. **無半導體應用記錄**：從未做過晶圓製程相關的 DoE/Emulator 應用，需從頭建立上下文
4. **Lab 規模微小**：學生輸出能力有限，作為 RD 儲備渠道效益低於簡禎富 SMART Lab
5. **教學導向偏重**：OCW 課程聲譽遠超研究聲譽，可能研究動能不足

### 4.2 可能的合作題目

以下合作題目依「技術可行性」由高至低排列：

1. **GP Emulator 加速 2nm 製程窗口探索**：以鄭少為的 GP/GRF 理論背景為基礎，設計能有效探索高維製程參數空間的 Computer Experiment Design，驗證 Virtual Metrology 場景
2. **DoE for Recipe Optimization**：在新製程配方（new recipe）開發階段導入最優化分次因子設計，縮短 Screening 實驗輪次
3. **Qualitative × Quantitative 混合因子的 GP 設計**：製程中常有類別型控制因子（不同蝕刻氣體組合）+ 連續型因子（功率、壓力），直接對口 2019 AoS 論文成果
4. **田口方法（Robust Parameter Design）與 GP 結合**：以 Cheng-Wu 2001 因子篩選框架延伸，應用於 plasma etch 或 CMP 製程的變異容忍度最佳化

### 4.3 風險點

| 風險 | 程度 | 緩解方式 |
|---|---|---|
| 研究方向已偏離 DoE（轉向 Functional Data Analysis）| 高 | 先以小型顧問形式確認現在研究重心 |
| Lab 規模不足以支撐大型合作計畫 | 中 | 聯合計畫模式（co-PI 與陳瑞彬教授或其他統計所教授）|
| 半導體場景學習曲線長 | 中-高 | 提供廠商端資料與場景定義，降低應用層啟動成本 |
| 副教授長期無升等（17 年）| 低-中 | 不直接影響合作品質，但顯示研究生態位置偏低 |

---

## §5 對 Phase 2 候選人名單的影響

**Top 20 #15 位置是否穩固？**

在現有資訊下，**鄭少為的 #15 位置合理但偏向保守**。

與同 T1 其他候選的差異化分析：

| 候選人 | 主要優勢 | 鄭少為對比 |
|---|---|---|
| **#1 簡禎富（SMART Lab）** | SMART 智慧製造、TSMC 深度產學、大型 Lab + 學生儲備渠道 | 鄭少為在 lab 規模/業界連結遠低於簡禎富，但**完全自由身**是差異化優勢 |
| **#14 洪英超（SVR Profile Monitoring）** | TSMC/聯發科製程品質監控直接應用、近年活躍論文 | 洪英超的應用落地能力更強；鄭少為在 GP 理論深度略佔優勢 |

**建議**：
- 若合作目標是「理論驗證型合作（Academic Proof-of-Concept）」：鄭少為適合，可快速產出 GP Emulator 設計方法論成果
- 若合作目標是「直接量產改善（Production Ramp 良率提升）」：建議優先洪英超或簡禎富，鄭少為需較長的應用場景啟動時間

**行動建議**：在正式接觸前，先透過共同認識人（如 Ming-Chung Chang 或 Ray-Bing Chen）非正式探詢鄭少為近期研究方向，確認是否仍在 DoE/GP 軌道上，再決定是否列為主動接觸對象。

---

## §6 資料來源清單

| 來源名稱 | URL | 訪問日期 | 用途 |
|---|---|---|---|
| NTHU 統計所全職教師頁面（英文）| `https://stat.site.nthu.edu.tw/p/403-1327-406-1.php?Lang=en` | 2026-04-22 | 確認職銜（副教授）、研究領域、聯絡方式 |
| NTHU KHub 研究者 Profile | `https://khub.nthu.edu.tw/researcherProfile?uuid=F372F93A-A717-4A22-B0D7-6C23F0E14091` | 2026-04-22 | 教育背景、工作經歷、ORCID、Scopus ID、教授課程清單 |
| TSMC-NTHU 聯合研發中心 JDP 教授名單 | `https://nthu-tsmc.site.nthu.edu.tw/p/412-1578-20665.php` | 2026-04-22 | 確認鄭少為**未列名** JDP 教授（綁定查驗） |
| DBLP 個人頁面 | `https://dblp.org/pid/184/5234.html` | 2026-04-22 | 確認 Technometrics 2002、2004 論文及共著者 |
| Project Euclid — AoS 2019 論文 | `https://projecteuclid.org/euclid.aos/1547197243` | 2026-04-22 | 確認 Annals of Statistics 2019 論文全文細節 |
| EcoSta 2019 Book of Abstracts（PDF）| `https://www.cmstatistics.org/EcoSta2019/docs/BoA_EcoSta2019.pdf` | 2026-04-22 | 確認 EcoSta 2019 口頭報告（E0551，功能性線性模式）|
| Ming-Chung Chang 個人頁面 Publications | `https://sites.google.com/view/mcchang/publications` | 2026-04-22 | 確認 AoS 2019 共著關係及學術師承 |
| Ming-Chung Chang Biography | `https://sites.google.com/view/mcchang/biography` | 2026-04-22 | 確認鄭少為是 Chang 博士指導教授 |
| 大紀元/Epoch Times 訪談（2007） | `https://www.epochtimes.com/b5/7/1/25/n1601933.htm` | 2026-04-22 | 業界合作（新竹科學園區、中科院）、學術獎項、師承背景 |
| NTHU 統計所榮譽公告 | `https://stat.site.nthu.edu.tw/p/403-1327-892-1.php?Lang=zh-tw` | 2026-04-22 | 確認 113 學年度校傑出教學獎 |
| ResearchGate 研究成果頁 | `https://www.researchgate.net/scientific-contributions/Shao-Wei-Cheng-13384348` | 2026-04-22 | 論文引用次數（8 篇，315 引用） |
| NTHU College of Science NSTC 傑出研究獎名單 | `https://science.site.nthu.edu.tw/p/412-1069-17882.php?Lang=en` | 2026-04-22 | 確認鄭少為**未列名** NSTC 傑出研究獎得主 |
| CSA 2023 組織委員會 | `https://sites.google.com/gapp.nthu.edu.tw/csa2023/%E5%A7%94%E5%93%A1%E6%9C%83` | 2026-04-22 | 確認參與中華統計學會年會組織（清大委員）|
| WebSearch — 多次查詢 | （內部工具）| 2026-04-22 | 姓名查核、期刊論文搜尋、TSMC 綁定查驗等多筆查詢 |
