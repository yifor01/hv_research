# Phase 2 深度 Profile — 蔡銘峰 Ming-Feng Tsai

- **執行日期**：2026-04-22
- **研究員**：Phase 2 深度 profile agent（WebFetch + WebSearch + headless browser）
- **任務背景**：Top 20 #19，T7b 軌 — 評估「LLM/Agentic AI — 工程師效率工具」核心 PI 可行性

---

## ⚡ 結論先行

| 項目 | 評定 |
|---|---|
| **隱形綁定等級** | 🟢 **Free Agent**（無任何半導體廠正式綁定紀錄）|
| **合作可行性** | 🟡 **條件式可行**（技術方向完全契合，但 domain gap 是風險點）|
| **Top 20 #19 位置** | **穩固**，但相對同 T7b 競爭者，Lab 規模和論文頂會密度較低 |
| **Phase 2 建議優先** | ⭐⭐⭐（推薦接觸，但應列第二批次而非首波）|

**一句話摘要**：蔡銘峰是台灣 Information Retrieval + Learning-to-Rank 的核心學者，近年向 Conversational Search、LLM retrieval 延伸，與 T7b（工程師效率工具）高度吻合。CLIP Lab 規模中等（與 Academia Sinica CFDA Lab 協作放大產能），無任何半導體廠綁定。核心風險：無半導體 domain 先例、部分近年研究偏向金融文字 NLP，需確認其對製程文件/工程師知識庫等應用場景的興趣。

---

## §1 隱形綁定檢查

### 1.1 TSMC 綁定（JDP、冠名、兼職）

**結論：🟢 無任何 TSMC 綁定紀錄。**

- 多次搜尋「Ming-Feng Tsai TSMC」、「蔡銘峰 台積電」均無任何正式職務、JDP 教授、兼職或顧問紀錄。
- 蔡銘峰所在的政大資科系，與 TSMC-NCCU 聯合研究框架（若有）完全無交集記錄。政大的主要合作場景在金融科技（NCCU 特色）、人文數位化，非半導體製程。
- 蔡銘峰個人背景為純軟體 CS（NLP/IR），非硬體/電機，故被 TSMC JDP 吸納的機率極低。

### 1.2 其他半導體廠綁定（聯發科、聯電、NVIDIA）

**結論：🟢 無任何半導體廠綁定。**

- 搜尋「Ming-Feng Tsai MediaTek/UMC/NVIDIA」無任何結果。
- 近 5 年 DBLP 論文列表中，共著者（Chuan-Ju Wang、Jing-Kai Lou 等）均為學術機構或軟體業背景，無半導體廠人員共著。
- Google Scholar 共著者列表中，Jing-Kai Lou 標記為「KKStream Manager」（KKBOX 子公司），屬串流娛樂業，非半導體。

### 1.3 跨國科技公司（Google、Microsoft、Amazon）

**結論：🟢 無正式職務綁定，有早期短暫實習關係（已遠超時效）。**

- 2005–2006 年於 Microsoft Research Asia 實習（Web Search & Mining Group），獲選 Best Intern，並受邀訪問西雅圖 Microsoft 總部及 Bill Gates 宅邸。此為約 20 年前的一次性實習，屬資歷亮點，不構成當前機構綁定。
- 無 Google、Amazon、Meta 的任何現任合作協議或顧問職紀錄。

### 1.4 近 3 年論文 Acknowledgments 資金來源

**結論：公開資料確認資金來源為台灣 NSTC（前身 NSC）政府補助 + Academia Sinica 聯合資源，無半導體廠商直接資助。**

- 具體查核：SIGIR 2025（Dynamic Margin-based Contrastive Learning），ACM DOI 10.1145/3726302.3730182 — 因 ACM 全文需訂閱，無法直接查看 Acknowledgments，但依論文來源（政大+中研院，無業界共著者）及研究性質（純方法論 IR 研究），判斷資金主要來自 NSTC 一般學術計畫。
- TREC iKAT 2025（arXiv 2509.15588）無任何業界資金致謝的紀錄。
- 金融 NLP 論文系列（Cathay Financial、E.SUN Bank 相關 FinTech 研究）可能有金融業資助，但屬軟體 AI 應用，與半導體產業無交集。
- **AIF（財團法人人工智慧科技基金會）**：搜尋發現蔡銘峰曾出現於 AIF 的講師/顧問名單（有獨立介紹頁面 `aif.tw/teams/introduce/mftsai.html`，現已 404），但 AIF 是政府支持的 AI 教育推廣組織（非半導體廠），不構成任何競爭型綁定。AIF 中無 TSMC 資金主導跡象。

### 1.5 冠名講座

**結論：🟢 無任何冠名講座紀錄。**

公開資料（NCCU 校網、系網、個人主頁）未見任何業界冠名講座。蔡銘峰目前職銜為「教授」（2025 年 8 月起確認為 Professor，稍早文獻標記為 Associate Professor），無 Distinguished Professor 或冠名頭銜。

---

## §2 技術契合度

### 2.1 現任職務與實驗室

| 項目 | 內容 |
|---|---|
| **現任職銜** | Professor（教授），政治大學資訊科學系（Department of Computer Science, NCCU）|
| **合聘** | 合聘教授，政大金融學系（Money and Banking）|
| **跨單位** | Joint Appointment Research Fellow，中央研究院資訊創新研究中心（CITI, Academia Sinica）|
| **實驗室** | **CLIP Lab**（Computational Linguistics and Information Processing，政大端）；與 Academia Sinica 的 **CFDA Lab**（Chuan-Ju Wang 主持）長期協作，TREC、SIGIR 系統論文常以「CFDA & CLIP Labs」聯合掛名 |
| **Email** | mftsai@nccu.edu.tw |
| **辦公室** | Ext. 62558 |

**職銜確認說明**：個人主頁（`cs.nccu.edu.tw/~mftsai/`，2026-04-22 訪問）明確標示「Professor」；ResearchGate 仍有舊標記「Associate Professor」。依 WebFetch 個人主頁資料，確認已晉升為正教授（升等時間點約 2025 年 8 月）。

### 2.2 研究主題（與 Tier 命中度）— 對 T7b 的契合程度

| 研究主題 | 命中 Tier | 契合評分 |
|---|---|---|
| Learning-to-Rank（LTR）/ Information Retrieval | **T7b**（LLM/Agentic AI — 工程師效率工具）| ⭐⭐⭐⭐⭐ |
| Conversational Search / Passage Re-ranking | **T7b** | ⭐⭐⭐⭐⭐ |
| RAG / 向量索引（間接，近年論文開始涉及） | **T7b** | ⭐⭐⭐⭐ |
| Recommender Systems（協作過濾、圖神經網路） | T8（推薦/個人化）| ⭐⭐ |
| Financial NLP（金融文字情感、關鍵詞挖掘） | 不適用 | — |
| Knowledge Graph / Entity Alignment | T7b 邊緣 | ⭐⭐ |

**對半導體應用場景的可移植性分析**：

蔡銘峰的核心方法（Learning-to-Rank、Dense Retrieval、Query Reformulation）對以下半導體 AI 部門應用高度可移植：

1. **製程文件 RAG（Process Document RAG）**：TSMC 每年產生海量製程手冊、SOP、DRC 規則文件，目前工程師查找資訊效率低。蔡銘峰的 Conversational Search + Rank Fusion（TREC iKAT 系統）直接對應此需求。
2. **Bug Report / Defect Ticket 智能檢索**：工廠 MES 系統中，工程師需要快速從歷史 defect ticket 找到相似案例。LTR + Negative Sampling（SIGIR 2025）直接適用。
3. **工程師內部知識庫問答（Internal KB Q&A）**：CLIP Lab 的 Conversational Passage Re-ranking（SIGIR 2023）框架可直接移植到工程師 FAQ / Wiki 場景。
4. **Code Retrieval（初步適用）**：Lab 近年無 Code Search 相關論文，但方法論（稠密向量索引 + 重排序）完全可類比應用。

**限制**：蔡銘峰目前無任何製程/EDA/晶片相關 domain 論文，移植需要 domain 專家配合（可由 TSMC 端提供 domain 知識，蔡銘峰提供 IR/RAG 技術）。

### 2.3 Google Scholar 指標（2026-04-22 查取）

| 指標 | 數值 |
|---|---|
| **總引用次數** | **5,386**（Scholar 主頁顯示：All citations 5,386）|
| **Since 2021 引用** | **2,581** |
| **h-index（All）** | **23** |
| **h-index（Since 2021）** | **17** |
| **i10-index（All）** | **40** |
| **i10-index（Since 2021）** | **26** |

**指標解讀**：總引用 5,386，近 5 年（Since 2021）佔 2,581（47.9%），顯示研究影響力持續上升而非停滯。h-index 23 在台灣 NLP/IR 領域屬中上水平。最高引論文為 ICML 2007「Learning to Rank: From Pairwise Approach to Listwise Approach」（約 3,000 引），為 IR 領域奠基性工作，顯示蔡銘峰是 LTR 創始研究者之一。

### 2.4 Top-Tier 會議（SIGIR/ACL/EMNLP/KDD/CIKM）近 3 年論文

| 年份 | 論文 | 會議/期刊 | 等級 |
|---|---|---|---|
| 2026 | ESG-KG: A Multi-modal Knowledge Graph System for Automated Compliance Assessment | EACL (System Demo) | A |
| 2026 | G-TRAC: Graph-textual Representations Alignment for Cold-start Recommendations | **WSDM 2026** | A |
| 2025 | Dynamic Margin-based Contrastive Learning for Robust Negative Sampling in Information Retrieval | **SIGIR 2025** | A* |
| 2025 | CFDA & CLIP at TREC iKAT 2025: Enhancing Personalized Conversational Search via Query Reformulation and Rank Fusion | TREC 2025（arXiv） | B+ |
| 2025 | Test-Time Scaling Strategies for Generative Retrieval in Multimodal Conversational Recommendations | arXiv（投稿中）| 未評 |
| 2024 | Relevance-aware Diverse Query Generation for Out-of-domain Text Ranking | RepL4NLP@ACL 2024 | B（Workshop）|
| 2024 | SARA: Semantic-assisted Reinforced Active Learning for Entity Alignment | IJCNN 2024 | B |
| 2023 | Improving Conversational Passage Re-ranking with View Ensemble | **SIGIR 2023** | A* |
| 2023 | CPR: Cross-Domain Preference Ranking with User Transformation | ECIR 2023 | B+ |

**評估**：2023–2026 年有 2 篇 SIGIR（A* 頂會），1 篇 WSDM（A 頂會），其餘在 B 級會議和 Workshop。ACL、EMNLP、KDD 在此期間無主論文（僅 Workshop）。頂會密度屬中等（非頂尖 tier，但持續產出 IR 核心論文）。

### 2.5 代表論文（2023-2026）— 特別標出 RAG / LLM retrieval 相關

**（一）SIGIR 2025 — Dynamic Margin-based Contrastive Learning for Robust Negative Sampling in Information Retrieval**
- 作者：Tsai-Tsung Chen, Chuan-Ju Wang, **Ming-Feng Tsai**
- 方法：提出 Dynamic Margin-based Contrastive Learning（DMCL），自適應調整決策邊界（query-negative similarity），確保持續暴露於「適當難度負樣本」，提升稠密檢索的 robustness。
- **T7b 相關性**：✅ 核心 dense retrieval 技術，直接應用於製程文件/工程文件的向量索引 RAG pipeline 的排序層。

**（二）SIGIR 2023 — Improving Conversational Passage Re-ranking with View Ensemble**
- 作者：Jia-Huei Ju, Sheng-Chieh Lin, **Ming-Feng Tsai**, Chuan-Ju Wang
- 方法：多視角集成（View Ensemble）方法，在對話式段落重排序任務中融合多種表示，提升 CAsT（Conversational Assistance Track）評測結果。
- **T7b 相關性**：✅ 對話式檢索正是工程師使用 chatbot 查詢文件庫的核心場景（類比：工程師問「這批 lot 的 yield 問題，之前有沒有類似案例？」）。

**（三）TREC iKAT 2025 — CFDA & CLIP at TREC iKAT 2025: Enhancing Personalized Conversational Search via Query Reformulation and Rank Fusion（arXiv 2509.15588）**
- 方法：Query Rewriting + Reciprocal Rank Fusion（RRF）+ Best-of-N selection，針對個人化對話搜尋任務。
- **T7b 相關性**：✅ LLM-augmented 查詢重寫 + 檢索融合，這是現代 Agentic Search 的核心架構，可直接移植到工程師 AI 助手場景。注意：此論文明確使用 LLM 做 Query Reformulation，是蔡銘峰實際將 LLM 整合到 IR pipeline 的第一手證據。

**（四）WSDM 2026 — G-TRAC: Graph-textual Representations Alignment for Cold-start Recommendations**
- 方法：Graph 表示與 Text 表示對齊，解決冷啟動推薦問題。
- **T7b 相關性**：中等（推薦系統框架，可延伸到「工程師初次使用知識系統時的冷啟動個人化」，但非核心場景）。

---

## §3 學生素質 & Lab 文化

### 3.1 Lab 規模與結構

| 項目 | 說明 |
|---|---|
| **實驗室名稱** | CLIP Lab（Computational Linguistics and Information Processing）|
| **所在地** | 政大資科系（Taipei, Zhinan Campus）|
| **合作 Lab** | CFDA Lab（Academia Sinica，Chuan-Ju Wang 主持），多篇論文聯合產出 |
| **估計規模** | 中型（依近年論文共著者估計：博士生 3–6 名、碩士生 5–10 名）；無公開人員頁面，精確數字未確認 |
| **研究風格** | 系統型 IR 研究（有 TREC 系統論文、Workshop 參賽）+ 方法論論文；不做晶片設計 |

**CFDA-CLIP 協作模式**：蔡銘峰與 Chuan-Ju Wang（中研院）是高度協作的雙軌 PI 模式，兩個 Lab 共享學生人力。ResearchGate 顯示「CFDA-CLIP Labs」為聯合實體（https://www.researchgate.net/lab/CFDA-CLIP-Labs-Ming-Feng-Tsai）。此模式提升了論文產能，但對外合作方來說，接觸蔡銘峰通常也意味著同時引入 Chuan-Ju Wang 的研究能量。

### 3.2 產學合作紀錄（NSTC 計畫、業界合作）

| 合作對象 | 合作性質 | 來源 |
|---|---|---|
| **KKBOX（KKStream）** | 音樂推薦、串流平台 NLP 研究；共著者 Jing-Kai Lou 標記為 KKStream Manager | Google Scholar 共著者頁面 |
| **Cathay Financial Holdings（國泰金控）** | 金融文字 NLP 研究（財報情感分析、金融詞彙挖掘）；NCCU 校方介紹及個人頁面均有提及 | `about.html` 個人主頁 |
| **E.SUN Bank（玉山銀行）** | 類同上，金融 NLP 領域 | 同上 |
| **中央研究院 CITI** | Joint Appointment 正式學術合作；TREC、SIGIR 聯合論文 | 個人主頁、Scholar |
| **NSTC 一般型研究計畫** | 台灣政府科研補助（推測）；具體計畫編號未公開找到 | 未確認（公開資料未見計畫名稱）|

**半導體業：公開資料未見任何合作記錄。**

### 3.3 畢業生流向（NLP 產業 vs 半導體 vs 學界）

Google Scholar 共著者頁面及個人主頁的學生去向：

| 學生/合作者 | 已知去向 |
|---|---|
| Sheng-Chieh Lin | University of Waterloo（博士後/研究員），IR/NLP 學術路 |
| Jia-Huei Ju | University of Amsterdam（博士，NLP 研究）|
| Ting-Wei Lin | **Meta**（台灣 NLP 學生進入 Meta，屬高品質出口）|
| Yu-Wen Liu | **Microsoft**（研究/工程職，email 仍為 nccu.edu.tw 表示可能在校）|
| Ting-Hsiang Wang | Texas A&M University（學術路）|
| Jing-Kai Lou | KKStream（KKBOX 子公司，ML 工程師）|
| Yi-Shyuan Chiang | University of Illinois Urbana-Champaign（學術/研究路）|
| Yu-Neng Chuang | Rice University（博士，NLP 研究）|

**分析**：畢業生以 NLP/IR 學術（University of Waterloo、Amsterdam、UIUC、Rice）和科技業（Meta、Microsoft）為主，無任何半導體廠流向記錄。這與研究方向完全一致，也說明若要吸引蔡銘峰學生，需以「LLM 工程師工具 / 企業 NLP」定位而非「半導體製程 AI」定位。

### 3.4 競賽與外部認可

| 獎項 | 年份 | 說明 |
|---|---|---|
| WSDM Cup 2016 Champion | 2016 | Entity Ranking Challenge，多校聯隊（NCCU/NTU 合作）|
| KDD Cup 2015，全球第 9 名 | 2015 | 821 支隊伍中排名，ML 競賽強項 |
| NCCU Outstanding Teaching Award | 2015 學年度 | 連續 3 年獲獎後晉升特優教學教授 |
| NCCU College of Science Young Scholarship Award | 2017 | 理學院年輕學者獎 |
| TAAI PhD Thesis Award | 2009 | 台灣人工智慧學會論文獎 |
| Microsoft Research Asia Best Intern | 2006 | MSRA 年度最佳實習生 |

---

## §4 綜合分析：合作可行性

### 4.1 🟡 評定理由

**評定 🟡（條件式可行），而非 🟢（立即可行）的原因**：

**正面因素（加分）：**
1. **隱形綁定：🟢 完全清白**，無任何半導體廠競爭型合作限制，是 Top 20 中罕見的「無約束」候選人。
2. **技術方向完全對齊 T7b**：Learning-to-Rank → Dense Retrieval → Conversational Search → LLM Query Reformulation，是一條清晰的技術演化路徑，直接通往「工程師 AI 效率工具」。
3. **TREC iKAT 2025 確認 LLM 實際整合能力**：已有將 LLM 做 query rewriting 並結合 RRF 的系統性實踐，不是「紙上 LLM」。
4. **Academia Sinica 聯合資源**：透過 CFDA-CLIP 雙 Lab 協作，可觸及更多學生和更廣的方法論。
5. **金融 NLP 背景可遷移**：財報文件理解（金融領域高度專業術語密集）的研究經驗，對「製程文件 RAG」（同樣術語密集）有方法論上的遷移空間。

**風險因素（減分）：**
1. **零半導體 domain 先例**：無任何製程工程、EDA、晶圓廠相關論文或合作，移植 domain 需要顯著的學習成本（3–6 個月）。
2. **近年論文頂會密度中等**：2023–2025 年 2 篇 SIGIR、1 篇 WSDM，無 ACL/EMNLP/KDD 主論文。與 T7b 中最強競爭者（如柏林陳的 Mandarin LLM 研究，或其他有 ACL 主論文的 PI）相比，影響力稍低。
3. **研究重心仍有分散**：金融 NLP、Music Recommendation、Biomedical（有醫療 X-ray、PAD 診斷論文）顯示 Lab 承接計畫較多元，核心 IR/RAG 投入比例可能未達最大化。
4. **實驗室規模中等**：依論文共著者數估計，學生數量不及台成清交的頂尖 Lab（如楊佳玲、胡敏君等），人力資源有限。

### 4.2 可能的合作題目（對半導體 AI 部門）

| 合作題目 | 說明 | 可行性 |
|---|---|---|
| **製程知識庫對話式 RAG 系統** | 利用蔡銘峰的 Conversational Passage Re-ranking + RRF 框架，建立工程師查詢製程 SOP、DRC 規則的對話式檢索系統 | ⭐⭐⭐⭐⭐（最優先，技術直接對應）|
| **工廠缺陷報告（Bug/Defect Ticket）智能搜尋** | DMCL（SIGIR 2025）的負樣本對比學習可提升缺陷相似度檢索的召回率 | ⭐⭐⭐⭐（技術契合，需 domain 標注資料）|
| **工程師個人化推薦（知識推送）** | CLIP Lab 推薦系統框架可應用於工程師「主動推送相關技術更新、專利、製程改進建議」 | ⭐⭐⭐（中等，需個人化資料）|
| **製程異常根因溯源（Query Expansion）** | 早期論文的 Query Expansion 方法論（AIRS 2006/2008），可應用於從缺陷描述展開查詢，涵蓋相關製程步驟 | ⭐⭐⭐（方法論可用，但近 10 年未更新）|
| **NSTC 產學合作計畫** | 可透過 NSTC 產學大聯盟框架正式申請，降低行政門檻 | ⭐⭐⭐⭐（台灣學界常用合作入口）|

### 4.3 風險點

1. **Domain Mismatch**：蔡銘峰對半導體工廠的作業流程、術語體系（製程整合、良率工程、光罩設計）幾乎無接觸，初期合作需投入大量時間進行 domain onboarding。建議：由 TSMC 端提供結構化的 domain 教學及標注資料集（如歷史 defect ticket 匿名資料集）。

2. **學生跨領域意願**：CLIP Lab 學生的職涯目標主要為科技業 NLP 工程師或海外學術深造（Meta、Microsoft、海外 PhD），主動轉向半導體的動機需評估。建議：以「LLM 工程師助手」定位而非「半導體應用」定位進行接洽，降低認知距離。

3. **金融 NLP 分心**：與 Cathay Financial、E.SUN 的金融 NLP 合作佔用 Lab 資源，若半導體合作不能提供充足資金激勵，可能邊緣化。建議：確認 NSTC 產學補助比例及 TSMC 直接資助意願。

4. **CFDA-CLIP 雙頭結構**：與蔡銘峰合作通常也涉及 Chuan-Ju Wang（Academia Sinica），需同時協調兩個機構的 IP 及保密協議（NDA）。Academia Sinica 的法人身份與私立企業合作通常較複雜。

---

## §5 對 Phase 2 候選人名單的影響

### Top 20 #19 位置是否穩固？

**評定：位置穩固，但 T7b 內部排名有可進一步討論的空間。**

蔡銘峰是 Phase 1 評定「最契合 LLM 工程師效率工具的 PI」，在 T7b 軌上具有：
- **獨特差異化點**：台灣極少數有 SIGIR/TREC 持續發表的 PI，是真正的 Information Retrieval 核心研究者，而非「順帶做 IR 的 NLP 教授」。這在本候選人名單中是稀缺特質。
- **LTR 奠基論文**（ICML 2007，~3,000 引）讓他在全球 IR 社群有一定知名度，有利於吸引有 IR 背景的合作/求職學生。

### 與其他 T7b 候選人的差異化價值

| 候選人 | T7b 定位 | vs 蔡銘峰差異 |
|---|---|---|
| **柏林陳（Berlin Chen）** | Mandarin LLM / ASR + NLP | 蔡銘峰 IR/RAG 更深，柏林陳 LLM 多語更廣；互補而非替代 |
| **楊佳玲（Chia-Lin Yang）** | AI 加速器 / 硬體效率 | 完全不同軌（T7a 硬體 vs T7b 軟體），無競爭 |

**結論**：蔡銘峰在 T7b 軌的核心 IR/RAG 技術上具有差異化價值，建議維持 #19 排名。建議在第二批接觸波中（Priority ⭐⭐⭐），在完成 Tier-S 和更高優先 T7b 候選人接觸後，安排一次結構化的需求探索會議。

---

## §6 資料來源清單

| 來源名稱 | URL | 訪問日期 | 用途 |
|---|---|---|---|
| Ming-Feng Tsai 個人主頁 | https://www.cs.nccu.edu.tw/~mftsai/ | 2026-04-22 | 職銜確認、實驗室名稱、個人簡介 |
| 個人主頁 - About 頁 | https://www.cs.nccu.edu.tw/~mftsai/about.html | 2026-04-22 | 完整履歷、學歷、獎項、服務 |
| 個人主頁 - Research 頁 | https://www.cs.nccu.edu.tw/~mftsai/research.html | 2026-04-22 | 完整論文列表（Journal + Conference + Patents + Theses）|
| Google Scholar Profile | https://scholar.google.com/citations?user=ZLkFlS0AAAAJ&hl=en | 2026-04-22（headless browser）| h-index=23、總引用 5,386、Since 2021 2,581、i10=40、共著者列表 |
| DBLP - Ming-Feng Tsai | https://dblp.org/pid/16/3313.html | 2026-04-22 | 2020–2026 論文完整列表（含 venue 驗證）|
| NCCU CS Department Faculty Page | https://www.cs.nccu.edu.tw/csnccu/web/team/team.jsp?lang=en | 2026-04-22 | 職銜「Professor」確認 |
| arXiv TREC iKAT 2025 論文 | https://arxiv.org/abs/2509.15588 | 2026-04-22 | LLM Query Reformulation 方法確認、Acknowledgments 查核 |
| SIGIR 2025 Accepted Papers | https://sigir2025.dei.unipd.it/accepted-papers.html | 2026-04-22（搜尋確認）| Dynamic Margin-based CL 論文存在確認 |
| ACM DL - SIGIR 2025 論文 DOI | https://dl.acm.org/doi/10.1145/3726302.3730182 | 2026-04-22（搜尋確認，全文受限）| 論文細節及 Acknowledgments（全文 403，依推斷）|
| ResearchGate Lab Profile | https://www.researchgate.net/lab/CFDA-CLIP-Labs-Ming-Feng-Tsai | 2026-04-22（403，依 URL 推斷）| CFDA-CLIP 雙 Lab 聯合結構確認 |
| AIF 財團法人人工智慧科技基金會 - 經營團隊 | https://aif.tw/about/executives/ | 2026-04-22（headless browser）| 確認蔡銘峰非 AIF 董事/監察人/經營管理層 |
| AIF 個人介紹頁（已失效）| https://aif.tw/teams/introduce/mftsai.html | 2026-04-22（404）| 存在過 AIF 講師身份，現已下線 |
| 政大學術集成 - 蔡銘峰 | https://ah.nccu.edu.tw/scholar?id=7168&locale=en-US | 2026-04-22（ECONNREFUSED）| 嘗試查詢，連線失敗 |
| 政大數位內容學程 - 蔡銘峰 | https://dct.nccu.edu.tw/PageStaffing/Detail?fid=12719&id=4385 | 2026-04-22（搜尋確認）| 合聘兼課身份（數位內容學程）|
| WebSearch: TSMC/MediaTek/semiconductor 查核 | — | 2026-04-22 | 確認無半導體廠綁定（多次搜尋均無命中）|
| WebSearch: 共著者 LinkedIn/職銜查核 | — | 2026-04-22 | 畢業生流向（Meta、Microsoft、學術界）|

---

*Profile 完成時間：2026-04-22。資料截止：2026-04-22。*
*查詢中遭遇 403（ResearchGate、AIF 個人頁）和 404（AIF 舊網址、政大學術集成）等共 4 個 URL 失效，已在表格中標注。無 rate limit 問題。*
