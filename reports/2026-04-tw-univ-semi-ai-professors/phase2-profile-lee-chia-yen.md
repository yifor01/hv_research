# Phase 2 深度 Profile：李家岩 Chia-Yen Lee

**查詢日期**：2026-04-22
**評級**：Tier-S #2（Phase 1 結論）
**單位**：NTU 資訊管理系 & 研究所 教授 / 管院副院長 / EiMBA Director

---

## 1. 技術契合度（深度）

### 研究方向與定位

李家岩的核心研究橫跨三軸：

- **T1（排程 / OR）**：隨機最佳化、多目標 MILP、reticle 排程、化工 MFI 生產排程
- **T3（預測性維護 / 品質）**：軸承退化健康指標、autoencoder 異常偵測、Real Options PM 排程
- **T6（深度強化學習 / 多智能體）**：DRL 預防性維護、MARL chiller 能源優化、Cyclic RL T/C 平衡

他的研究特點是**由 OR 理論出發，逐步向 DL/RL 延伸**，保留強烈的可解釋性與最佳化導向，而非純 end-to-end 黑盒。

### 2023–2026 代表論文（5 篇精選）

| 年份 | 標題 | 期刊 | Citation |
|------|------|------|----------|
| 2025 | Multi-agent reinforcement learning for chiller system prediction and energy-saving optimization in semiconductor manufacturing | *Int'l J. Production Economics*, 280 | 7 |
| 2024 | Deep reinforcement learning-based preventive maintenance for repairable machines with deterioration in a flow line system | *Annals of Operations Research* | 6 |
| 2024 | Robust-optimization-guiding deep reinforcement learning for chemical material production scheduling | *Computers & Chemical Engineering*, 187 | 16 |
| 2024 | BMB-LIME: LIME with modeling local nonlinearity and uncertainty in explainability | *Knowledge-Based Systems*, 294 | 42 |
| 2024 | Autoencoder-based detector for distinguishing process anomaly and sensor failure | *Int'l J. Production Research*, 62(19) | 9 |

> 備注：
> - MARL chiller paper 原為 2024 發表，Google Scholar 列為 *IJPE* 2025（vol 280）；引用數 7 已屬快速累積。
> - BMB-LIME 的 42 citations 顯示其在可解釋 AI（XAI）方向已打入非製造社群，跨域影響力強。
> - 2025 年另有 IEEE TASE 封裝缺陷識別（多分支 UNet）論文，顯示向半導體封測延伸。

### 2023–2026 NSTC 計畫

- 確認計畫編號：**NSTC112-2221-E-002-003**（以 BMB-LIME、robust DRL 排程等為核心成果）
- 擔任 **NSTC 工工管理學門召集人**（確認，Phase 1 資料），具政府計畫 channel 優勢
- 具體計畫名稱與期限因 NSTC 網站未完全開放，無法確認（建議直接向李教授詢問）

### 產學合作細節

根據 AIF 顧問資料及成大訪談，歷史合作產業廣泛：
- **台積電**：清大碩士期間即有合作接觸（台積電工作經驗）；後期學術合作以半導體製程排程（reticle）、能源管理為主
- **日月光**：Wafer Bin Map autoencoder paper 明確以半導體封裝為場景，與日月光生產情境高度吻合
- **台達電**：微電網能源管理、伺服馬達等方向
- **AUO（友達）**：智慧排程顧問、TFT-LCD T/C balance 排程（CIIE2024 Best Paper 主題）
- **華邦電子**：智慧製造中心科技顧問
- **Profet AI（杰倫智能）**：2023 年起擔任顧問，聚焦工業 AI 落地推廣

> 重要發現：合作名單顯示他不只是學術研究者，而是**同時持有顧問職務**，顯示與業界有實質且持續的雙向流動。

### 期刊 AE / Editorial Board

- **IEEE Transactions on Automation Science and Engineering (T-ASE)**：副編輯 (2020–2022)
- **IEEE Transactions on Semiconductor Manufacturing (TSM)**：副編輯（確認現任，CIIE2024 資料揭露其參與 TSM best paper 評選）
- **Flexible Services and Manufacturing Journal**：副編輯 (2016–2019)
- **台灣人工智慧科技基金會（AIF）**：顧問

### 2023–2026 獎項

| 年份 | 獎項 |
|------|------|
| 2024 | Best Paper Award @ CIIE2024（RL T/C balance scheduling in TFT-LCD） |
| 2024 | 擔任 IEEE TSM Best Paper 選拔委員（側面認證其在 TSM 的核心地位） |
| 2021 | IEEE Senior Member（2023 後仍活躍發表） |
| 2017 | 吳大猷紀念獎（科技部傑出青年學者） |
| 2019 | 馮樹藻紀念獎（中華管理學會） |

---

## 2. 學生工程素質 & Lab 文化

### PoLab 規模（2024–2025 估算）

- PoLab 網站（polab.im.ntu.edu.tw）因技術原因無法直接抓取，以下資訊來自 GitHub、Profet AI、及學術論文共著推估：
- **GitHub（po-lab organization）**：10+ 開源 repo，其中活躍者：
  - `Manufacturing-Data-Science`：⭐93（2025/02 最後更新）— 教學素材，HTML/Jupyter，持續維護
  - `Operations-Research-Applications`：⭐46（2024/01）
  - `Python-Gurobi-Pulp`：⭐54（2023/09）
  - `Intelligent-Manufacturing-Systems`：⭐29（MATLAB，已趨靜止）
- 研究分組推估（基於論文主題）：**排程 OR** / **預測維護 PHM** / **深度強化學習**，與 T1/T3/T6 完全對應
- 碩博士規模：**推估 12–18 人**（NTU 資管熱門實驗室，但副院長職務可能壓縮直接指導時間）

### 學生競賽 & 開源

- GitHub repo 活躍度顯示 lab 有**教學導向開源文化**，但 star 數主要來自外部使用者，非 lab 自身 contribution
- CIIE2024 Best Paper 有學生共著（TFT-LCD scheduling）
- 2024 IEEE CASE（Automation Science and Engineering）有 real options 維護論文，顯示學生參與會議發表
- AICUP / Kaggle 得獎記錄：**未找到確認資料**（非 PoLab 公開宣傳焦點）

### 畢業生去向

- 訪談與 AIF 資料顯示 lab 學生有接觸台積電、友達、化工業等場景；具體 LinkedIn 畢業生去向**未能系統確認**
- 李教授 **曾任職台積電**（碩士後），業界人脈含台積電背景的業師圈（EiMBA 管道）

### EiMBA 高管班

- EiMBA 業師名單龐大（100+ 業師），李教授擔任 Director，有機會將高管班中的**半導體廠 VP/Director 級人脈**轉化為研究合作入口
- 這是不同於一般學術 lab 的特殊人脈槓桿

---

## 3. 合作優缺點 & 建議切入方式

### 優點

1. **方法論完整**：從 OR、統計到 DRL、Multi-agent，可接不同層次的技術需求
2. **書作者背書**：《製造數據科學》（2022，全市面唯一中文專書）自帶業界公信力，降低開場溝通成本
3. **多業態合作非綁定**：同時與台積電（半導體）、友達（面板）、化工業合作，不存在單一廠商排他風險
4. **雙 channel 人脈**：NSTC 召集人（政府計畫）+ EiMBA Director（高管）→ 兩條獨立的資源放大路徑
5. **Profet AI 顧問**：已建立商業化 AI 落地視角，合作時對「可交付物」有實際認識
6. **TSM AE**：對 semiconductor manufacturing 論文的技術標準有直接話語權

### 缺點 / 風險

1. **行政雙重負擔**：管院副院長 + EiMBA Director，**每週實際可用研究時間被壓縮**；直接指導密度可能不及純研究型 PI
2. **學門邊界模糊**：NTU 資管 vs. 工工所 — 與 NTU 工工（陳正剛）、電機（洪英超等）方向有部分重疊；合作需界定各自貢獻，避免論文掛名衝突
3. **排程優先**：他目前排期可能偏向已有 NSTC 計畫的題目；新合作需等計畫空窗期
4. **Deep Learning 非第一主力**：T6（DRL/MARL）強，但 T5（大型 Foundation Model 半導體）尚未見到論文，可能不是最適合 LLM-for-fab 方向的合作對象

### 建議合作型態

**推薦：聯合 NSTC 計畫（共同主持人）**

原因：
- 李教授擁有工工管理學門召集人背景，申請 NSTC 工工/AI 相關計畫有優勢
- 「共主持」模式確保雙方各有貢獻空間，避免成為「在李教授計畫下做事」的附屬角色
- EiMBA 和 AIF 人脈可自然帶動業界 dataset 提供，降低 data access 障礙

### 具體可切入題目（3 個）

**T1：半導體智慧排程 × Robust Optimization**
> 題目：「Wafer Fab 多車型 AGV 動態派工 × robust DRL（考慮不確定設備故障率）」
> 銜接點：李教授 2024 robust-optimization-guiding DRL 論文（Comp & Chem Eng.）+ reticle 排程論文；可直接往 FOUP/AGV 方向延伸。

**T3：封裝缺陷 Multi-task 視覺 × 主動學習**
> 題目：「少樣本封裝缺陷辨識：unpaired image fusion + active learning with uncertainty quantification」
> 銜接點：2025 IEEE TASE unpaired image denoising/fusion 論文；可搭配日月光 data 做 real case。

**T6：Fab 能源管理 Multi-agent RL × Digital Twin**
> 題目：「Semiconductor fab 冷凍機 + 空壓機聯合優化：MARL × digital twin 驗證平台」
> 銜接點：MARL chiller 論文（IJPE 2025）是直接前作；台積電廠務能源為國際熱點。

### 第一次聯絡建議

**推薦：學會 channel（中國工業工程學會）+ NSTC 計畫動機**

步驟：
1. 以「工業工程學會會員 / 研究者」身份寄信，提及對其 MARL chiller paper 的具體問題（非泛泛讚美）
2. 說明研究方向與 T6/T3 的交集，提出「一個具體 research question」
3. 附上一份簡短研究提案（1 頁），建議合寫 NSTC 計畫

> 不建議先從 EiMBA 高管班切入（因為那是業界人脈，進入門檻高且路徑較長），也不建議走學生 RA 路線（因為他行政負擔重，RA 需求可能已有固定來源）。

---

## 4. 風險評估

| 維度 | 評級 | 說明 |
|------|------|------|
| 技術排他風險 | 🟢 低 | 多業態合作，非單一廠商綁定 |
| 行政執行風險 | 🟡 中 | 副院長 + EiMBA Director，可用時間有限 |
| IP / 保密風險 | 🟡 中 | 台積電 / 友達既有合作可能有 NDA；新題目需確認是否進入已有 NDA 範圍 |
| 學門重疊風險 | 🟡 中 | NTU 資管 vs. 工工所邊界需在合作初期確認 |
| 人才培育品質 | 🟢 高 | GitHub 開源文化 + OR × DL 雙軌訓練，學生工程素質有保證 |
| 合作可成功率 | 🟢 高 | 書作者 + AIF 顧問 = 對合作化有正向態度 |

---

## 5. 資料來源清單

| 來源 | URL | 訪問日期 |
|------|-----|----------|
| Google Scholar 個人頁（論文清單） | https://scholar.google.com/citations?user=M_DB0CQAAAAJ&hl=en&sortby=pubdate | 2026-04-22 |
| NTU 管院個人頁 | https://management.ntu.edu.tw/en/IM/faculty/teacher/sn/388 | 2026-04-22 |
| PoLab GitHub 組織 | https://github.com/po-lab | 2026-04-22 |
| AIF 人工智慧科技基金會顧問頁 | https://aif.tw/about/team/chiayen-lee/ | 2026-04-22 |
| NCKU 李家岩訪談（職涯歷程） | https://web.ncku.edu.tw/p/404-1000-173602.php?Lang=zh-tw | 2026-04-22 |
| Profet AI 顧問公告 | https://profetai.com/newsroom/chia-yen-lee-announcement/ | 2026-04-22 |
| Profet AI 爐邊談話重點 | https://profetai.com/crossover-talks/0124-fireside-chat-highlight/ | 2026-04-22 |
| IEEE Xplore 作者頁 | https://ieeexplore.ieee.org/author/37086788510 | 2026-04-22 |
| PoLab 網站（ECONNREFUSED，無法抓取） | http://polab.im.ntu.edu.tw/ | 2026-04-22 |
| NTU EiMBA 業師名單 | https://management.ntu.edu.tw/EIMBA/page/index/menu_sn/1277 | 2026-04-22 |
| Manufacturing-Data-Science GitHub | https://github.com/PO-LAB/Manufacturing-Data-Science | 2026-04-22 |

> **注意**：PoLab 主站（polab.im.ntu.edu.tw）在本次查詢中回應 ECONNREFUSED，多數 people.html 資料無法直接確認。學生人數、競賽獎項等數據為根據論文共著與 GitHub 活躍度之推估，建議實地 follow-up 確認。

---

## 總結評語

李家岩是**台灣製造 AI 研究最系統化的學者之一**：書作者身份代表他已完成方法論整合，而非仍在摸索；多業態顧問代表他對「研究 → 落地」的完整路徑有具體認識。技術上 T1+T3+T6 全覆蓋，且各方向都有 2024–2025 年的高品質論文支撐，不是曇花一現。

主要挑戰是**行政負擔**：副院長 + EiMBA Director 的雙重角色若在任期中，可能使他的研究推進變慢。建議在聯繫前先確認其行政職是否即將卸任（台大副院長通常 3–4 年一輪），若時機好，卸任後的李教授研究動能將大幅釋放。
