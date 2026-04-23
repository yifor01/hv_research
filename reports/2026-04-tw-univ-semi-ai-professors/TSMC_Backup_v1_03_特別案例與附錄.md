# B4 特別案例與附錄

---

## §1 已失效候選（5 位）

下列 5 位在評估過程中曾被列為候選或初步推薦，但後續核實後**不可作為學界合作對象**，從主名單與備選名單皆移除。列於此處是為了：
1. 保留決策記錄，避免後續重複評估
2. 向主管說明「為何公開資料看似可行但實際不可」
3. 記錄能力限制（資料盲區）供未來改進

---

### 案例 1：彭文志 Wen-Chih Peng（NYCU 資工）— 已借調 TSMC 當處長

**原評分**：7.0 / 10（TSMC 5 維度評分，原為第一波立即接觸推薦）  
**原定位**：SIGIR 2025 "Template-Based Financial Report Generation in Agentic and Decomposed IR" 作者，直接對應「製程 SOP / 文件 agentic 查詢」範式。原列為 Top 16 第 14 名。

**失效原因**：**2026 年 Q1 起借調至 TSMC 擔任處長職，已是 TSMC 內部員工**，不再是學界合作候選。此訊息透過業界內部管道於 2026-04-23 確認，非公開 web 可查。

**原評估內容摘要**（僅供參考，實際已作廢）：
- 前 NYCU 資工系主任（2019-2022）、前電資學院副院長、前 E-SUN-NCTU Fintech and AI Center Director（2021-2024，2024 卸任）
- 2025 年單年在 SIGIR、ACL、AAAI、EMNLP、CIKM main conference 各 1 篇
- ADSL Lab 15 人規模（5 博 + 10 碩），中大型 Lab
- 原評估認為 E.SUN Fintech Center Director 剛卸任 = TSMC 接手「剛釋出的 senior PI 資源」是時機窗口

**能力限制備註**：
此類**企業內部借調/任命動態公開 web 不可見**：
- WebSearch 無法抓到 — LinkedIn 不會即時更新「借調」，大學網頁仍列教授職
- Google Scholar 仍列 NYCU，publications 持續（有可能已撰寫但未發表的論文仍陸續公告）
- **唯一可查來源**：業界內部消息、人事異動口耳相傳
- 後續產業洞察類驗證**必須倚靠業界內部管道**，而非依賴 web search agent

**補位建議**：
若 TSMC 仍需 **Agentic IR 方向**，有兩條替代路徑：
1. 從主名單 #14 **黃瀚萱**（CAG 專長）延伸，由黃瀚萱擔任該題目主 PI；或從主名單 #14 **蔡銘峰**（純 IR 深度）延伸
2. 掃本備選池類別一 **高宏宇**（Retrieval Domain Adaptation）作為次遞補

---

### 案例 2：水野潤 Jun Mizuno — 實為早稻田大學教授

**原推測**：NCKU 先進封裝中心教授（初輪評估列為 T4 封裝候選）

**失效原因**：深度核實後，**水野潤實為日本早稻田大學（Waseda）正職教授**，NCKU 僅為客座/訪問身份。非台灣學界 PI，**從台灣學界名單剔除**。

**補位建議**：
若 TSMC 對水野潤的封裝研究（異質整合、3D TSV 等）確有興趣，應以 **TSMC ↔ Waseda 直接協議**方式接觸，而非透過 NCKU 學界合作框架。

---

### 案例 3：張孟凡 Meng-Fan Chang — TSMC Corporate Research Director 兼任

**原推測**：NTHU 電機 Tier-S CIM 先驅；初輪評定為 Tier-S #4

**失效原因**：深度核查發現其**現任 TSMC Corporate Research Director（兼任）**，即 TSMC 已獨佔其合作資源。對**非 TSMC / 非 MediaTek 的半導體主管視角**已失去獨占性。

**原核查內容**：
- NTHU 電機系 特聘教授 / TSMC Corporate Research Director（兼任）
- CIM 硬體、Neuromorphic、ReRAM 領域頂級產出；ISSCC 連年多篇
- 核查後判定為 🔴 Deep Bound

**補位建議**：
主名單 **#10 鄭桂忠**（NTHU 電機）在 CIM 方向是可接觸的替代者，為 TSMC-NTHU JDP 教授 🟡（非正式職務，僅研究經費依賴）。Top 15 v3 中已以鄭桂忠替補張孟凡位置。

---

### 案例 4：張耀文 Yao-Wen Chang — MediaTek 獨立董事

**原推測**：NTU 電機 EDA Lab 領導者；初輪列為 Tier-1 #6

**失效原因**：深度核查發現其**2024-05 就任 MediaTek 獨立董事**；對非 MediaTek 立場有重大利益衝突風險。

**原核查內容**：
- NTU EDA Lab 核心 PI；EDA 業界多方整合
- 核查後判定為 🔴（對非 MediaTek 的半導體主管）

**補位建議**：
EDA 軸主名單已由 **#10 鄭桂忠（CIM EDA）** + **#13 林嘉文（光刻 EDA）** 雙軸覆蓋；另備選池 **#6 吳凱強**（EDA + LLM 跨界）可考慮但需確認 Neuchips 顧問排他條款。

---

### 案例 5：林勇志 Yeong-Jyh Lin — 前 TSMC 13 年 + 商秘獎

**原推測**：NSYSU SAT 先進半導體封測研究所；初輪列為 Tier-1 #9（T4 3D 晶圓接合、異質整合）

**失效原因**：深度核查發現：
- **前 TSMC 13 年**任職紀錄
- **2 項專利共同發明人**（TSMC 擁有）
- **2021 商秘獎**（商業秘密保護法相關獎項）

離職後受競業條款與商秘保護期限制，為**主要法務排除案例**。

**補位建議**：
T4 先進封裝軸主名單由 **#4 陳冠能**（NYCU ICST Dean）、**#6 陳智**（NYCU 材料系主任）、**#8 江國寧**（NTHU PME）、**#9 宋振銘**（NCHU 研發長）4 位覆蓋，封裝是主名單最厚的題目。無需備選池補強。

---

## §2 能力限制總結（給後續評估者）

從 5 個失效案例可歸納 4 類「WebSearch 難以抓到」的盲區：

| 盲區類型 | 具體範例 | 唯一驗證方式 |
|---|---|---|
| **企業內部借調/任命** | 彭文志借調 TSMC | 業界內部消息 / 電話確認 |
| **客座 vs 正職身份混淆** | 水野潤（Waseda 正職、NCKU 客座） | 讀其 CV 首頁的「Current Affiliation」+ 交叉比對多份 recent 論文掛名機構順序 |
| **董事/顧問/技術長等兼任職** | 張耀文（MediaTek 獨董）、張孟凡（TSMC Director）| 上市公司年報、公司治理頁、新聞稿 |
| **商秘/專利綁定**（離職後仍受限） | 林勇志（前 TSMC 13 年）| LinkedIn + 專利局檢索 + 業界人脈 |

**對後續 Phase 建議**：
1. **所有 🟢 Free Agent 結論**應在正式接觸前 24-48 小時透過**至少 2 個獨立管道**再次核實
2. **Top 15 主報告附錄已列出**建議 double-check 項目；本備選名單在正式聯絡任一位前同樣建議 double-check
3. **WebSearch 不可信**用於：2025-2026 新任董事、處長、政務職、借調動態

---

## §3 資料來源

### 類別一：差一點（4 位）

**高宏宇 Hung-Yu Kao（NTHU 資工）**
- NTHU ISA 高宏宇起聘通告（2024/8/1）：https://isa.site.nthu.edu.tw/p/406-1182-272217,r4919.php?Lang=en
- IKM Lab（NTHU）：https://ikmlab.cs.nthu.edu.tw/advisor.html
- ACL Anthology 作者頁：https://aclanthology.org/people/h/hung-yu-kao/

**連震杰 James Lien（NCKU 資工）**
- NCKU 資工系（副院長兼主任身份）：https://csie.ncku.edu.tw/
- GitHub CVDL-NCKU（2023 Fall 課程）

**楊佳玲 Chia-Lin Yang（NTU 資工，借調中）**
- NTU CSIE 個人頁：https://www.csie.ntu.edu.tw/~yangc/
- DAC 2025 Program Co-chair 公告：https://dac.com/
- IEEE Fellow 2026 公告
- MICRO 2024 PointCIM 論文

**簡禎富 Chen-Fu Chien（NTHU 工工 / CEO 兼任）**
- NTHU DALab：https://www.dalab.ie.nthu.edu.tw/
- Stanford 全球前 2% 科學家榜單（2023 年版）
- NTHU-TSMC Center 介紹頁

---

### 類別二：方向對但待觀察（6 位）

**Jakey Blue 藍啓航（NTU 工工）**
- NTU 工工系教師頁：https://www.ie.ntu.edu.tw/
- Mines Saint-Étienne-NTU 合作頁
- 2020 ESWA / 2020 IEEE TASE / 2024 ISSM 論文

**吳凱強 Kai-Chiang Wu（NYCU 資工）**
- NYCU 資工吳凱強個人頁：https://people.cs.nycu.edu.tw/~kcw/
- ICCAD 2025 CAD Contest Problem A 頁面
- ICLR 2025 Palu / Quamba 論文

**楊素芬 Su-Fen Yang（NCCU 統計）**
- NCCU 統計系師資頁：https://stat.nccu.edu.tw/zh/faculty/
- 2025 Sci Reports AEWMA Gamma 論文
- 2025 Processes Bayesian EWMA 論文

**鄭少為 Shao-Wei Cheng（NTHU 統計）**
- NTHU 統計所：https://stat.site.nthu.edu.tw/
- 2019 AoS Signal Aliasing in GRF 論文
- Bilibili 教學影片

**陳正剛 Argon Chen（NTU 工工）**
- NTU 工工 Argon Chen（achen@ntu.edu.tw）：https://www.ie.ntu.edu.tw/
- Google Scholar 引用紀錄（全期 vs 近 5 年對比）

**洪英超 Ying-Chao Hung（NTU 工工）**
- NTU 工工洪英超：https://www.ie.ntu.edu.tw/
- LinkedIn：https://www.linkedin.com/in/ying-chao-hung-118020261/
- 2022-2024 NSTC 計畫查詢（EV 充電站區位途程最佳化）

---

### 類別三：方向偏（3 位）

**柏林 Berlin Chen（NTNU 資工）**
- NTNU 資工柏林個人頁：https://www.csie.ntnu.edu.tw/~berlin/
- Interspeech 2025 S&I Challenge 結果公告
- 2026 arXiv Phi-4 MLLM + wav2vec 2.0 融合論文

**王振興 Jeen-Shing Wang（NCKU 電機）**
- NCKU 電機王振興：https://www.ee.ncku.edu.tw/
- AI4DT 中心頁面（NCKU 自設）
- NSTC 未來科技獎 2023/2024 獲獎公告

**李祈均 Chi-Chun Lee（NTHU 電機）**
- NTHU BIIC Lab：https://biic.ee.nthu.edu.tw/
- IEMOCAP 資料集：https://sail.usc.edu/iemocap/
- NTHU-Novatek Distinguished Talent Chair 2025 公告

---

### 已失效候選（5 位）

**彭文志 Wen-Chih Peng**
- DBLP：https://dblp.org/pid/92/1623.html
- NYCU CS Profile：https://www.cs.nycu.edu.tw/members/detail/wcpeng?locale=en
- ADSL Lab 成員頁：https://nycu-adsl.cc/members/
- **借調 TSMC 處長**：業界內部消息（2026-04-23 確認，無公開 web 來源）

**水野潤 Jun Mizuno**
- 早稻田大學教授頁（Waseda 正職確認）
- NCKU 先進封裝中心客座頁

**張孟凡 Meng-Fan Chang**
- NTHU 電機系特聘教授頁
- TSMC Corporate Research Director（兼任）— 新聞稿 / 公司治理資料

**張耀文 Yao-Wen Chang**
- NTU 電機 EDA Lab
- MediaTek 獨立董事公告（2024-05）

**林勇志 Yeong-Jyh Lin**
- NSYSU SAT 先進半導體封測研究所
- 2021 商秘獎公告
- TSMC 專利發明人清單（美國專利局檢索）

---

## §4 使用本備選名單的最終提醒

1. **時效性**：本文件資料截止 2026-04-23。Top 15 主報告附錄已列出建議 double-check 項目；本備選池同樣建議任一位正式聯絡前透過業界管道再次核實現職狀態。

2. **PI 沒有好壞之分**：本文件以「此題目匹配度」高低分類，不代表學術水準排序。例如：
   - 陳正剛（類別二 #9）學術上曾是台灣 T1 SPC 權威，分類二並非貶低
   - 李祈均（類別三 #13）h=36 是頂尖 speech AI 學者，分類三只反映「與半導體 domain 距離遠」

3. **不建議的使用方式**：
   - ❌ 不要把分數低的 PI 直接否決，而不看「可取代主名單誰」映射
   - ❌ 不要跳過類別一直接用類別三（跨域成本高）
   - ❌ 不要把「方法論顧問池」（陳正剛、洪英超）誤當作新合作 PI

4. **建議的使用方式**：
   - ✅ 主名單某位婉拒時，優先看「可取代主名單誰」欄位的 1:1 映射
   - ✅ 若 1:1 無直接替代，考慮「合作者而非替代者」模式（如連震杰配合詹寶珠做 T3 AOI 工程落地）
   - ✅ 陳正剛、洪英超、鄭少為這類「方法論顧問池」可用於「歷史文獻諮詢」，不用於「新合作啟動」

---

*本文件（B1 + B2 + B3 + B4）與主報告（Top 15 v3）合計構成 2026-04 台灣 AI × 半導體 PI 完整盤點成果。*
