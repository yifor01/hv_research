# Phase 2 深度 Profile：洪英超 Ying-Chao Hung

**查詢日期**：2026-04-22  
**評級**：T1 SPC / Profile Monitoring 主命中（Phase 1 結論：🟢 Open）  
**單位**：NTU 工業工程學研究所 教授  

---

## 1. 隱形綁定檢查

### TSMC / 半導體業界連結
- **搜尋結果：無明顯綁定**。搜尋「洪英超 TSMC」、「Ying-Chao Hung semiconductor industry」均無相關結果。
- CV 中列出之業界合作僅有：
  - 醫療財團法人血液基金會（2012，問卷統計分析）
  - Microsoft Corporation 訪問學者（2018/7–8，Membership Knowledge & Growth 部門）
  - 政大 EMBA / NTU EMS 教學
- **2023–2025 NSTC 研究計畫全為電動車充電站區位途程最佳化**（非半導體）。
- **結論**：無與 TSMC 或半導體廠的直接產學合作紀錄。隱形綁定風險 🟢 極低。

### LinkedIn / 論文致謝
- LinkedIn 頁面存在（https://www.linkedin.com/in/ying-chao-hung-118020261/），但未能抓取詳細內容（429 error）。
- 從 CV 及公開資料中無法確認半導體廠致謝。需入學後自行確認 acknowledgement。

---

## 2. 技術契合度

### 研究方向現況（CV + NTU 頁面確認）

洪英超的官方研究興趣列為六項：
1. 統計計算與模擬（Statistical Computing & Simulation）
2. 應用機率（Applied Probability）
3. 隨機控制與最佳化（Stochastic Control & Optimization）
4. 統計機器學習（Statistical Machine Learning）
5. 格蘭傑因果關係檢定（Granger Causality Testing）
6. 資料科學應用

**重要發現：Profile Monitoring / SPC 已明顯淡出主線研究**。

洪英超在 2012–2013 年有兩篇 Profile Monitoring 代表作（SVR + 非參數），但 2013 年後研究重心完全轉移至隨機控制、EV 最佳化、Granger 因果等方向。2022 年後 NTU 時期的論文清一色為 EV 充電站最佳化和 Granger 因果（Time Series Analysis 2024、WIREs Computational Statistics 2024）。

### 代表論文（依時序確認研究軌跡）

| 年份 | 標題 | 期刊 |
|------|------|------|
| 2024 | A Review of Monte Carlo and Quasi-Monte Carlo Sampling Techniques | *WIREs Computational Statistics*, 16(1) |
| 2024 | Granger Causality Tests Based on Reduced Variable Information | *Journal of Time Series Analysis*, 45(3) |
| 2022 | A Novel Data-Driven Approach for Solving the EV Charging Station Location-Routing Problem | *IEEE Trans. Intelligent Transportation Systems*, 23(12) |
| 2022 | Optimal Routing and Design of EV Charging Systems with Stochastic Demands | *European Journal of Operational Research*, 299(2) |
| 2019 | Modeling and Optimization of Time-of-Use Electricity Pricing Systems | *IEEE Trans. Smart Grid*, 10(4) |
| 2013 | A Framework for Nonparametric Profile Monitoring | *Computers & Industrial Engineering*, 64 |
| 2012 | Nonparametric Profile Monitoring in Multi-dimensional Data Spaces | *Journal of Process Control*, 22(2) — **代表作** |

**Profile Monitoring 研究已為 10 年前成果**，現任 NTU 時期（2022 起）研究聚焦於 EV/交通網絡最佳化與時間序列統計方法，與半導體製程監控距離較遠。

### 研究主軸 × 半導體 AI 題目契合度

| 研究主軸 | 與半導體 AI 的契合度 | 說明 |
|----------|---------------------|------|
| EV 充電站最佳化（2021–2025 NSTC 主計畫） | ⚠️ 低 | 最近期主力，與製程無關 |
| 統計機器學習 + 隨機控制 | 🟡 中 | 可轉化至製程控制，但非現有研究重心 |
| Granger 因果關係 | 🟡 中 | 可用於製程參數因果分析 |
| Profile Monitoring（舊作） | 🟢 高 | 但已 10+ 年未發表 |
| 蒙地卡羅方法論 | 🟡 中 | 偏理論，可搭配模擬研究 |

**結論**：若要跟洪英超做 SPC/Profile Monitoring × AI 題目，需主動引導；若做統計理論或最佳化方向則更自然契合。

---

## 3. 學生工程素質

### Lab 規模與定位
Lab 名稱為「Data Analytics and Optimization Laboratory」，CV 描述為：
> "interdisciplinary team collaborating at the intersection of data science, optimization, and machine learning"

公開資料無法取得學生名單及人數。從 NTU 工工所官方頁面、ResearchGate lab 頁面（403 blocked）均未能取得詳細學生資訊。

### 學生競賽記錄
- 無 IISE Student Paper Competition 獲獎紀錄出現於搜尋結果。
- 洪英超在政大時期多次獲得「教學優良獎」（2010、2012、2014、2015、2016 教學特優），顯示教學品質良好。
- 2022 年轉至 NTU（相對較新），學生 track record 尚在累積中。

### 畢業生去向
- 無法從公開資料確認。
- 合作教授 G. Michailidis（University of Michigan）顯示有留學/國際合作管道。
- EV 最佳化方向的學生可能傾向業界軟體/顧問/能源公司，而非半導體。

---

## 4. 合作優缺點 & 差異化分析

### 與同系相關教授的差異化

| 面向 | 洪英超（Hung） | 李家岩（Lee） | 陳正剛→生醫轉向 |
|------|-------------|-------------|----------------|
| 統計背景深度 | ⭐⭐⭐⭐⭐ 頂尖（Michigan PhD Statistics） | ⭐⭐⭐ 中等 | — |
| SPC/Profile Monitoring | 有舊作但已淡出 | 無正統 SPC | 無 |
| 製程 × AI | 🟡 間接相關 | 🟢 直接相關（半導體 fab） | 生醫方向 |
| 最新半導體發表 | ❌ 無 | 🟢 有（wafer bin map、chiller） |  — |
| EV / 運籌 | 🟢 2021–2025 主力 | ❌ 無 | — |
| 統計理論 / 方法論 | 🟢 強（Granger、MC/QMC、SVR） | ❌ 偏應用 | — |
| 國際合作網絡 | 🟢 Michigan（Michailidis），日本 ISM | 🟡 國內為主 | — |

**核心差異**：
- 洪英超是**純統計理論出身的方法論學者**，與李家岩的「應用 OR × DRL」路線完全不同。
- 若研究主題需要嚴謹的統計方法論基礎（如 Phase I/II 管制、distribution-free SPC），洪英超指導品質遠勝其他同系教授。
- 但若目標是半導體製程直接應用，李家岩（與半導體廠合作 chiller、wafer）更有直接連結。

### 合作優點
1. **統計嚴謹度最高**：密西根統計系 PhD，IEEE TAC、EJOR、IEEE TSG 等頂刊發表能力強，統計理論訓練扎實。
2. **無半導體綁定，彈性最大**：無 TSMC 附屬計畫，研究方向自由度高，容易開拓新題目。
3. **方法論遷移潛力**：Granger 因果 + 統計機器學習 + MC 模擬，可遷移至半導體製程因果分析與最佳化。

### 合作缺點
1. **Profile Monitoring 已非主力**：最近期代表作（2022–2024）集中在 EV 最佳化，若期望延續其 SPC 代表作方向，需主動推動轉型。
2. **半導體業界連結薄弱**：無 TSMC/UMC/fab 合作計畫，相較於其他半導體 AI 教授，業界資源較少。
3. **NTU 工工 轉籍時間短（2022）**：學生 track record 與 NTU 資源整合仍在建立，相比在 NTU 耕耘多年的教授，外部評審能見度稍弱。
4. **研究主題漂移廣**：從 SPC → 隨機控制 → EV → Granger 因果，研究聚焦度較低，對學生的方向感可能需要自己建立。

---

## 5. 具體合作題目建議（3 個）

### 題目 A：Profile Monitoring × Conformal Prediction（統計嚴謹路線）
**題目方向**：利用 Conformal Prediction 框架重構 nonparametric profile monitoring 的 Phase I/II 控制圖，解決傳統 SVR-based 方法對分布假設的敏感性問題。  
**為何適合**：直接延伸洪英超 2012 代表作，補上 10 年理論進展（conformal inference），既能讓他回歸 SPC 強項，也契合半導體製程曲線監控需求。  
**期刊目標**：*Technometrics*（洪英超曾擔任 reviewer）、*Journal of Quality Technology*

### 題目 B：Granger Causality × 製程因果診斷（方法延伸路線）
**題目方向**：將洪英超擅長的 Granger 因果架構（含 trimmed/reduced variable 版本）應用於半導體蝕刻/沉積製程的多感測器時序數據，建立可解釋的設備故障前驅因果圖。  
**為何適合**：直接利用洪英超現有研究主力（Granger + 統計機器學習），不需轉型，且半導體的 APC（Advanced Process Control）場景有強烈需求。  
**期刊目標**：*IISE Transactions*、*IEEE Trans. Automation Science and Engineering*

### 題目 C：Stochastic Optimization × 半導體量產排程（最佳化轉化路線）
**題目方向**：將洪英超的 stochastic control / heavy traffic approximation 方法（已發表於 EJOR 2022）延伸至晶圓廠 lot dispatching 問題，納入製程變異與 yield 不確定性。  
**為何適合**：洪英超的 EV routing 框架數學上與 fab scheduling 同構（both = stochastic service systems），方法遷移難度低，且 NTU 工工所有 fab 相關校友資源。  
**期刊目標**：*European Journal of Operational Research*、*IISE Transactions*

---

## 6. 綜合評估

| 面向 | 評分（/5） | 說明 |
|------|-----------|------|
| 統計方法論深度 | ⭐⭐⭐⭐⭐ | Michigan PhD，方法論最扎實 |
| SPC/Profile Monitoring 現況 | ⭐⭐ | 代表作已 10 年前，主力已轉移 |
| 半導體業界連結 | ⭐ | 無直接 TSMC/fab 合作 |
| 隱形綁定風險 | 🟢 極低 | 無半導體產學計畫 |
| 學生培育環境 | ⭐⭐⭐ | NTU 環境好，但 lab 資訊少 |
| 研究自由度 | ⭐⭐⭐⭐⭐ | 無半導體綁定，方向可塑性高 |

**建議策略**：洪英超適合**以統計方法論為出發點、主動提案 SPC 或 Granger 應用題目**的學生。若期望由指導教授主導半導體 AI 方向，或需要業界資源對接，建議將李家岩（T1 SPC × 半導體直接應用）列為優先。洪英超則是**統計背景深厚、無利益衝突、可培養出高品質方法論論文**的選擇，適合學術路線。

---

## 7. 資料來源

| 來源 | URL | 取得日期 |
|------|-----|---------|
| NTU IE 洪英超教授頁面 | https://ie.ntu.edu.tw/News_Photo_Content_n_44392_s_214735.html | 2026-04-22 |
| NTU 工學院 IET 頁面 | https://www.eng.ntu.edu.tw/iet/News_Content_n_182589_s_234981.html | 2026-04-22 |
| 洪英超 CV（NTU 上傳 PDF） | https://ie.ntu.edu.tw/001/Upload/809/ckfile/91ab999b-9d96-4a27-9876-6587c5f90fe8.pdf | 2026-04-22 |
| ResearchGate Profile | https://www.researchgate.net/profile/Ying-Chao-Hung | 2026-04-22（403 blocked） |
| LinkedIn | https://www.linkedin.com/in/ying-chao-hung-118020261/ | 2026-04-22（999 blocked） |
| NCTU 統計演講公告（2024-12-13） | https://stat.site.nthu.edu.tw/p/406-1327-279032,r585.php?Lang=zh-tw | 2026-04-22 |
| 李家岩 NTU 管院頁面（對照用） | https://management.ntu.edu.tw/en/faculty/teacher/sn/388 | 2026-04-22 |
| WebSearch：多輪關鍵字查詢 | — | 2026-04-22 |
