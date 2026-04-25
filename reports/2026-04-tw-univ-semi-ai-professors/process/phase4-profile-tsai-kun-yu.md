# 深度 Profile：蔡坤諭 Kuen-Yu Tsai
**Phase 4 補強 PI — NTU EE 微影／DFM 軌道**
*產出日期：2026-04-24 | 資料截止：2026-04-24*

---

## 結論先行

| 項目 | 內容 |
|------|------|
| **Tier 評等** | 🟡 **Tier-2（建議納入備選池上層）** |
| **核心定位** | 不是 VLSI Test／DFT 教授，而是台灣**少見的 EUV 微影 ＋ DFM ＋ 多 e-beam direct-write** 學界專家；前 Intel 微影製程工程師（193nm + EUV 缺陷檢測） |
| **與題目契合度** | 與原 Phase 1 假設「EE Test 軌道」**錯配**；但對 TSMC 而言其價值可能**高於** Test 教授——因為 EUV / DFM 是 2nm/A14 節點的核心瓶頸 |
| **TSMC 隱形綁定** | 🟡 **TSMC-NTU 聯合研究中心成員（2013–至今）**；雖非主導 PI，但長期掛名意味存在 JDP 級合作管道 |
| **學界頭銜** | 副教授 14 年未升等（2005 入職，2013 升副教授）；H-index 12，總引用 503 — **學術指標相對保守** |
| **獨家價值** | 唯一具 Stanford EUV + Intel 193nm 雙背景、又同時掛 NTU EE / GIEE / SoC Center / TSMC-NTU Center / ITRI 的台灣學者 |

> **重要修正**：本 PI 的真實研究方向為 **Nanolithography / EUV / DFM / e-beam direct-write / Ion Beam Patterning**，不是原任務假設的 VLSI Test／DFT。題目假設來自系所人事表的命名相近誤判（同系另有 VLSI Testing 課程由李建模 Cheng-Wen Wu 等人開設）。對 TSMC PI 盤點而言，蔡坤諭應歸入 **T0 微影／製程設備** 軸，補強的是「先進製程節點之 design-process co-optimization」缺口，而非 Test 缺口。

---

## §1 隱形綁定檢查

### 1.1 已知學術／企業關聯

| 機構 | 關係 | 期間 | 強度 |
|------|------|------|------|
| **Intel Corporation**（Hillsboro, OR）| 前 Senior Process Engineer，193nm 微影 + EUV 缺陷檢測 | 2002–2005 | 🟡 歷史關係（已 21 年），無現任顧問公開紀錄 |
| **TSMC-NTU Research Center** | Faculty member | 2013–至今（13 年） | 🟢 直接綁定，但非主導 PI |
| **NTU GIEE 電子所**（合聘）| Joint Associate Professor | 2008–至今 | — |
| **NTU SoC Center**（系統晶片中心）| Faculty | 2008–至今 | — |
| **ITRI 機械與機電系統研究所** | Faculty 合作 | 2016–至今 | 🟡 與工研院機械所有結構性合作 |
| **Stanford 校友網絡** | PhD 校友（航太博士 + EE minor） | — | — |

### 1.2 隱形綁定風險評估

| 競爭情境 | 風險程度 | 說明 |
|---------|---------|------|
| **與 ASML/應材/KLA 直接競爭** | 🟢 低 | 無公開設備商顧問記錄；研究偏方法論 |
| **與 Intel 直接競爭** | 🟡 中 | Intel 為其 BG；雖已 21 年離職，但情感聯繫可能存在；若 sponsor 為三星/Intel 對家方需評估 |
| **與 TSMC 平行合作** | 🟡 中 | 已掛 TSMC-NTU Center；非競爭性題目（如材料、設備、metrology）可並行；**競爭性 DFM 題目**可能受限 |
| **顧問私約／企業借調** | ⚠️ 不可驗證 | WebSearch 範圍內無公開資訊；建議首次面談直接詢問 |

> **3 個必問防禦題**：
> 1. 「您目前在 TSMC-NTU Center 內主持的計畫主題是？」（探 JDP 邊界）
> 2. 「Intel 離職後是否仍有任何形式之顧問或股權關係？」
> 3. 「實驗室現有計畫的設備供應商來源？」（探 ASML/AMAT/KLA 設備借用關係）

---

## §2 技術契合度

### 2.1 真實研究主軸（依其官方簡傳 + Google Scholar）

| 軸 | 關鍵字 | 對應 TSMC 痛點 |
|----|--------|---------------|
| **L1 微影模型與校正** | Lithography simulation, Model calibration, RET (Resolution Enhancement Techniques), OPC | 2nm/A14 節點 OPC 模型誤差控制；EUV mask 3D effects |
| **L2 多帶電粒子束直寫** | MCPBDW (Multi-Charged-Particle Beam Direct Write), Multi e-beam | 替代/補完 EUV 的次世代節點選項；mask making |
| **L3 EUV 微影系統** | EUV mask shadowing correction, EUV proximity effects, EUV 缺陷檢測 | 直接對應 TSMC 2nm/A14 量產 |
| **L4 離子束圖案化** | Helium/Neon ion beam imaging, Ion beam patterning | 量子元件、單原子層工藝（前瞻） |
| **L5 DFM／製造可行性設計** | Design for Manufacturability, Sub-wavelength parasitics extraction | EDA-foundry 介面；2nm 設計規則演化 |
| **L6 高效能伺服／量測系統** | High-performance servo, 5nm interferometer, piezo-driven fine stage | 微影機台精密定位（與設備商相關） |

### 2.2 代表論文（依引用排序）

| 標題 | 期刊／類型 | 年份 | 引用 |
|------|----------|------|------|
| Fully model-based methodology for simultaneous correction of EUV mask shadowing and proximity effects | （SPIE 系列）| 2011 | 47 |
| Servo system design of a high-resolution piezo-driven fine stage for step-and-repeat microlithography systems | （IEEE/ASME） | 1999 | 34 |
| Method for improving accuracy of parasitics extraction considering sub-wavelength lithography effects | **US Patent 8,438,505** | 2013 | 20（patent cite） |
| Impacts of point spread function accuracy on patterning prediction and proximity effect correction in low-voltage EBDW | *J. Vacuum Science & Technology B* | 2013 | 19 |

**Google Scholar 指標**：總引用 503、H-index 12、i10-index 20、自 2021 起新引用 7（h-index since 2021）→ **近 5 年產出顯著放緩**。

> 📉 **學術產量警示**：2021 後新引用占比偏低，可能反映：(a) 微影領域純方法論論文發表週期長；(b) 重心轉向產學保密案；(c) 行政或教學負擔上升。需面談時釐清。

### 2.3 與 Phase 1/2 候選池的軸交叉

| 軸 | 既有 Top 15 涵蓋 | 蔡坤諭補位價值 |
|----|-----------------|----------------|
| **T0 微影／DFM**（原本未明確列入軸） | ❌ Top 15 無人 | ⭐⭐⭐⭐ **補完 EUV/DFM 缺口** |
| **T2 AI-EDA** | Kai-Chiang Wu、林嘉文（光刻 EDA） | 🟡 與林嘉文部分重疊（光刻 EDA），但蔡坤諭偏物理／製程端，林偏 AI 演算法端，可協作非競爭 |
| **T1 良率／缺陷** | 簡禎富、銀慶剛、詹寶珠 | 🟡 蔡的 EUV 缺陷檢測經驗為 metrology 上游 |
| **設備／量測整合** | 段維新、顏家鈺 | 🟢 **與陳亮嘉（本批另一位）形成「設計端蔡坤諭 + 量測端陳亮嘉」雙人組合** |

---

## §3 學生 Lab 規模

### 3.1 三個自建 Lab

蔡坤諭官方簡傳載明其為 **三個 Lab 的創辦主任**：

| Lab | 縮寫 | 研究方向 |
|-----|------|---------|
| Nanoscale Design and Fabrication Systems Lab | **NDFSL** | 奈米尺度設計／製造系統 |
| Particle Beam Precision Patterning and Imaging Lab | **PBPPIL** | 帶電粒子束精密圖案化／成像 |
| High-Performance Servo Systems Lab | **HPSSL** | 高效能伺服系統 |

> ⚠️ **三 Lab 並非獨立大型實驗室**——以一位副教授（h-index 12、年發表量低）的產出量推估，三個 Lab 實質為 **同一團隊的三個研究面向標籤**，總實質規模估約：

### 3.2 規模估算（公開資料推估）

| 角色 | 人數估計 | 備註 |
|------|---------|------|
| 博士生 | 2–4 人 | 副教授配額有限；產出論文共作者重複名單 |
| 碩士生 | 6–10 人 | NTU EE 副教授常見規模 |
| 博士後 | 0–1 人 | 未見公開招聘訊息 |
| 業界訪問 | 不定 | TSMC-NTU Center / ITRI 合作可能有 |

### 3.3 學生去向／競賽

- **無公開 GitHub 組織**（微影／DFM 研究天然不開源，IP 多為企業案）
- **無公開競賽得獎**（領域非 Kaggle/AICUP 導向）
- **畢業生去向推估**：TSMC 微影部、ASML/Synopsys/Mentor 微影解決方案、ITRI 機械所；學界出路有限（領域窄）

---

## §4 5 維度評分明細

| 維度 | 分數 | 理由 |
|------|------|------|
| **1. 技術命中度（Test/DFT/良率/3D AOI）** | **0** | 完全錯位——蔡坤諭不做 Test／DFT；但若**重新定義為「製程端 DFM／EUV」**則為 ⭐⭐ 強命中（TSMC 2nm 核心痛點） |
| **2. 5 年學生招募潛力** | **1** | Lab 小（估 2–4 博士生），副教授配額有限；學生領域窄但稀缺度高 |
| **3. 企業共建長期 Lab 開放度** | **1** | 已有 TSMC-NTU Center 經驗，理論上開放；但同時也意味產能已被部分占用 |
| **4. 資源未被搶佔程度** | **1** | TSMC 已綁定（中等占用）；Intel 歷史關係（已淡）；ASML/AMAT/KLA 設備商關係不明 |
| **5. 個人黃金期剩餘** | **1** | 1973 年生，2026 年 53 歲；副教授 13 年未升等暗示產出瓶頸；EUV 領域剛進入熱點，仍有 5–8 年活躍期 |

**加權總分**：**4 / 10**（依原任務 Test 軌道評）；**6 / 10**（若重新對位 EUV/DFM 軸）

> **關鍵判讀**：以「補強 EE Test 軌道」目的看蔡坤諭，**完全失準**；以「補完 TSMC 上游微影／DFM 缺口」目的看，**價值高於原 Top 15 任一位 EE 教授**。

---

## §5 合作優缺點 ＋ 3 個合作題目建議

### 5.1 優點

1. **唯一性**：台灣學界 EUV 微影 + Intel 製程工程實戰背景的組合極稀有
2. **跨域整合**：機械（B.Sc/M.Sc）+ 航太（PhD）+ EE（合聘）+ EE Process — 可橋接設計與機台兩端
3. **TSMC 既有管道**：TSMC-NTU Center 13 年成員身份意味有合作基礎設施（保密、合約框架已建立）
4. **與設備商中立性高**：未見公開 ASML/AMAT/KLA 顧問綁定，可作為 sponsor 觀察設備商技術動態的中立窗口
5. **與陳亮嘉（本批另一位）形成設計-量測雙人組合**：DFM 模型輸出 ↔ OCD 量測驗證

### 5.2 缺點

1. **學術產出減速**：H-index 12、近 5 年新引用占比低；可能反映科研活力不在頂峰
2. **Lab 規模小**：三個 Lab 實為一團隊的三個標籤，總博士生估 2–4 人；難承接大型多站合作
3. **TSMC-NTU Center 邊界不明**：若 sponsor 為 TSMC 競爭者，JDP 條款可能限制可合作主題
4. **領域窄**：EUV/DFM 為高度專門化軸，難以延伸到 AI 應用或封裝等鄰近題目
5. **副教授長期未升等**：可能反映校內競爭弱勢，主導大型計畫能力受限

### 5.3 三個合作題目建議

| 編號 | 題目 | 對應軸 | 適合 sponsor |
|------|------|--------|------------|
| **題 A** | **2nm/A14 節點 OPC 模型在 EUV stochastic effects 下的校正方法**——以蔡坤諭 2011 年 EUV mask shadowing correction 方法論為基礎，延伸至高 NA EUV 與 stochastic noise 共存場景 | L1+L3 | 設備商（ASML、KLA）、IDM 客戶（非 TSMC 直接競爭者） |
| **題 B** | **Multi-electron-beam direct-write 在 mask making 良率提升的應用評估**——蔡坤諭為台灣此領域少見專家；對 sponsor 而言是觀察 EUV 替代/補完路線的低成本前哨 | L2 | 半導體設備新創、政府前瞻計畫（NSTC） |
| **題 C** | **Sub-wavelength 寄生效應感知的 DFM 規則自動生成**——直接延伸其 US Patent 8,438,505；對 EDA 工具供應商（Synopsys、Cadence）有商業價值 | L5 | EDA 廠、IP 公司 |

### 5.4 建議合作型態

- **主要**：**A 型（NSTC 產學聯合計畫，公司合聘 30% PI 工時）**——避免單一企業冠名引發 TSMC-NTU Center 邊界爭議
- **輔助**：**D 型（短期單案 deliverable）**——以 6–12 個月 single-objective 委託案先試水溫，驗證實際 Lab 產出能量

### 5.5 第一次聯絡 Email（建議草稿）

```
Subject: 合作洽詢 — [公司名稱] × NTU 蔡坤諭教授 EUV/DFM 研究合作

蔡教授，您好：

[公司名稱] 長期關注先進節點微影與 DFM 的學術前沿，特別是您在 EUV mask shadowing
correction、sub-wavelength 寄生效應 DFM 等方向的開創性貢獻。

我們目前正在推進 [2nm 節點 OPC / EUV stochastic / multi-e-beam 評估] 相關研究，
希望能與您進行 30 分鐘線上交流，了解 NDFSL 目前的研究方向以及產學合作之可能性。

時間由您決定，可配合您的行程。

期待您的回覆。

[您的姓名] | [公司] | [Email]
```

---

## §6 Reference URL 清單

| # | 資料 | URL | 訪問日期 |
|---|------|-----|---------|
| 1 | 蔡坤諭 NTU EE 官方簡傳（中文）| http://www.ee.ntu.edu.tw/bio1.php?id=674 | 2026-04-24 |
| 2 | 蔡坤諭 NTU EE 教師個人頁（英文）| https://ee.ntu.edu.tw/en/article/teacher.person/jobSN/3/navSN/356/webSN/385/teacherSN/119 | 2026-04-24 |
| 3 | 蔡坤諭 NTU Scholars 學術頁 | https://scholars.lib.ntu.edu.tw/entities/person/3dfdfd8e-e9c8-465d-acbc-952cf547943b | 2026-04-24 |
| 4 | Google Scholar Profile（Kuen-Yu Tsai）| https://scholar.google.com/citations?user=U2qcl4wAAAAJ&hl=en | 2026-04-24 |
| 5 | ResearchGate Profile | https://www.researchgate.net/profile/Kuen-Yu-Tsai | 2026-04-24 |
| 6 | NTU GIEE EDA Faculty 列表 | https://giee.ntu.edu.tw/en/eda_faculty.php | 2026-04-24 |
| 7 | NTU EE 著作列表 | http://www.ee.ntu.edu.tw/publist1.php?id=674 | 2026-04-24 |

### 資料缺口

| 缺失項目 | 原因 |
|---------|------|
| 確切博士生／碩士生名冊 | 三 Lab 無獨立官網 |
| TSMC-NTU Center 內部計畫名稱與預算 | 屬保密；無公開文件 |
| 2024–2026 期刊發表清單 | 公開搜尋未返回；需直接信問或翻 NTU Scholars 出版頁 |
| ASML/AMAT/KLA 顧問狀態 | WebSearch 未返回；需面談確認 |
| 副教授未升等之原因 | 屬個人事務，無公開資料 |

---

*本報告由 Phase 4 補強研究員產出。重要修正：原任務假設「VLSI Test / DFT」與本 PI 實際研究方向不符，已於結論先行段落明確標示並重新對位至「微影／DFM」軸。*
