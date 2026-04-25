# Phase 2 深度 Profile — 林勇志（Yeong-Jyh Lin）

- **執行日期**：2026-04-22
- **研究員**：Phase 2 深度 profile agent（WebFetch + WebSearch）
- **任務背景**：Tier-1 #9，NSYSU SAT 先進半導體封測研究所，T4（3D 晶圓接合、異質整合）

---

## ⚡ 結論先行

| 項目 | 評定 |
|---|---|
| **隱形綁定等級** | 🔴 **Deep Bound（前 TSMC 13 年 + 現行 TSMC 共同發明人）** |
| **能否自由合作** | **高風險** — 需明確確認離職後保密協議範圍及智財歸屬 |
| **技術契合度** | ⭐⭐⭐⭐⭐（T4 完美命中：Hybrid Bonding、SoIC、CoWoS、晶圓對準） |
| **Phase 2 最終建議** | ⚠️ **先做法務確認再接觸**，否則存在 IP 洩露風險 |

---

## §1 隱形綁定檢查（⚠️ 重點警示）

### 1.1 TSMC 深度綁定（確認 🔴）

**林勇志在 TSMC 任職長達 13 年（2010–2023），職位持續晉升至處長層級：**

| 期間 | 職位 | 部門 |
|---|---|---|
| 2004/06–2007/03 | 研發工程師 | 南茂科技（Chipbond Technology）|
| 2009/06–2010/04 | 副理 | 聯相光電（Acer Display Technology）|
| 2010/05–2016/07 | 主任工程師 | TSMC 導線/封裝技術整合部 |
| 2016/07–2023/08 | **技術副理 → 主任工程師 → 特殊模組處經理** | TSMC 特殊模組處 |
| 2023/08–至今 | 副教授級專業技術人員 | NSYSU SAT 先進半導體封測研究所 |

**TSMC 任職 13 年**（2010–2023），從基層工程師升至「特殊模組處經理」。「特殊模組處」在 TSMC 架構中負責的正是 3D IC、SoIC、CoWoS、Hybrid Bonding 等先進封裝模組整合。

### 1.2 現行共同發明人身份（確認 🔴）

以下 TSMC 專利確認 Yeong-Jyh Lin 為發明人（assignee: TSMC）：

| 專利號 | 標題 | 申請年份 | 技術關鍵字 |
|---|---|---|---|
| US20240186258A1 | Photolithography Alignment Process for Bonded Wafers | 2024 公開（申請更早） | 晶圓鍵合後微影對準 |
| US11688717B2 | Mechanical Wafer Alignment Detection for Bonding Process | 2021/08 申請，2023 核准 | 晶圓鍵合偏移偵測 |
| US11925033B2 | Embedded Backside Memory on a Field Effect Transistor | 2024 核准 | BSJ 記憶體整合 |
| US20240088103A1 | 3D Trench Capacitor for Integrated Passive Devices | 2024 公開 | 3D 電容整合 |

**US11688717B2 申請於 2021 年（TSMC 任職期間）**，2023 年核准，距他 2023/08 離職僅差數月。**US20240186258A1 屬後 TSMC 時代公開但原申請極可能仍在 TSMC 任職期間提交。**

### 1.3 TSMC x NSYSU 學程框架

NSYSU SAT 內部結構：
- **創新半導體製造研究所**：合作企業列名「台積電」
- **先進半導體封測研究所**（林勇志所在）：合作企業為「日月光、華泰電子、穎崴科技」

林勇志目前在封測所，**其所在研究所的官方標竿合作企業是日月光（ASE）**，而非 TSMC。但其個人背景仍與 TSMC IP 高度糾纏。

### 1.4 TSMC 黃金貿易秘密獎（2021 年）

林勇志獲得「TSMC 第 9 屆黃金貿易秘密獎 — 銀獎」（2021/12），顯示他在 TSMC 所持有的技術機密知識達到被公司正式表彰的等級。離職後的保密協議覆蓋範圍需要特別注意。

---

## §2 技術契合度分析

### 2.1 核心技術專長（官方聲明）

- 半導體封裝測試製程 / 材料 / 設備
- **3D 晶圓接合技術（Hybrid Bond）**
- **晶圓級異質整合（CoWoS / InFO / SoIC）**
- 有限元素分析模擬（FEA/FEM warpage 模擬）
- CIS（Camera Image Sensor）製程技術

### 2.2 代表論文（可確認）

| 論文標題 | 作者/發表 | 年份 | 意義 |
|---|---|---|---|
| Modeling of viscoelastic behavior of an epoxy molding compound during and after curing | YJ Lin, SJ Hwang, HH Lee / IEEE Components, Packaging | 2011 | 封裝材料機械模型，被引 36 次 |
| Structure deformation of leadframe in plastic encapsulation | Shen, Lee, Lin et al. | 2007 | 早期封裝變形分析 |
| Energy-Aware Design and Performance Analysis of Through-Oxide Thermal Vias | CC Wang, YJ Lin et al. | 2026 | 3D IC 熱管理（最新，加入 NSYSU 後產出）|

**說明**：林勇志在 TSMC 13 年主要貢獻以專利（共 4 件以上確認）而非期刊論文為主，這是業界研究員的典型模式。學術論文產量在轉職後（2023 後）才開始恢復，2026 年的熱通孔論文是轉職後最新確認的學術成果。

### 2.3 技術命中 T4 核心

| T4 技術項目 | 林勇志是否具備 | 依據 |
|---|---|---|
| Hybrid Bonding / Cu-Cu Bonding | ✅ 核心專長 | 官方研究領域聲明 + TSMC 特殊模組處 13 年 |
| 晶圓對準（Bonded Wafer Alignment）| ✅ 有專利 | US11688717B2、US20240186258A1 |
| CoWoS / InFO / SoIC | ✅ 直接點名 | 官方研究領域 |
| TSV / RDL / Chiplet | ✅（推測） | 特殊模組處業務範疇 |
| Warpage FEA 模擬 | ✅ 有期刊論文 | 2011 IEEE 論文（36 引）；2026 NSYSU 新作 |

**技術命中率：5/5。** 林勇志是此次 Tier-1 名單中技術契合度最高的 T4 候選人之一，但隱形綁定也最深。

---

## §3 學生工程素質

### 3.1 所在研究所規模

- **先進半導體封測研究所每年招收 80–90 位碩士生**（研究所級別，非個人 lab）
- 採「碩一大學授課 + 碩二碩三企業實習研究」三年制架構
- 學生可獲企業獎助金（上限 88–112 萬元 NTD，三年期）

**個人 lab 規模未揭露**，但林勇志 2023/08 加入，尚在建立研究室初期，預估個人指導學生數在 3–8 人之間（推測，非確認）。

### 3.2 實習/就業流向

- 所內官方標竿企業為**日月光（ASE）、華泰電子、穎崴科技**
- 學生碩二碩三前往這三家企業實習
- 林勇志個人的 TSMC 人脈可能形成額外的非官方通道

### 3.3 設備能量（推測）

- 林勇志研究室位於「電資大樓 F2019-1」，另有 IR6002 辦公室
- 官方聲明合作企業「提供實習場域（含先進設備與儀器）」
- **是否有自建 bonder、clean room 級量測設備未確認**
- 推測：初期以 FEA 模擬（軟體主導）為主，物理 bonding 設備依賴日月光廠區

---

## §4 合作優缺點分析

### 4.1 優點

| 優點項目 | 說明 |
|---|---|
| **技術精準度極高** | CoWoS warpage / SoIC 對準 / Hybrid Bonding 全部直接命中，無需補強技術背景 |
| **南科地緣優勢** | NSYSU 高雄距 TSMC 南科廠、日月光楠梓廠均在 15 分鐘車程內，田野調查成本極低 |
| **FEA 模擬能力** | 有 ASME/IEEE 論文佐證的 warpage 模擬背景，可做量化仿真而非只談工藝 |
| **業界語言** | 13 年 TSMC 資歷使他完全理解封裝廠內部術語、流程限制、量產考量，溝通無落差 |
| **日月光管道** | 所在研究所有日月光作為標竿企業，ASE 封測供應鏈研究有制度性通道 |
| **TSMC 人脈** | 非正式但實質的 TSMC 南科廠人脈網絡（前同事關係） |

### 4.2 缺點與風險

| 缺點/風險 | 嚴重程度 | 說明 |
|---|---|---|
| **TSMC IP 糾纏（隱形綁定 🔴）** | 🔴 高 | 2021 申請的晶圓對準專利至今仍掛名 TSMC；研究主題與 TSMC 核心技術高度重疊 |
| **保密協議未知範圍** | 🔴 高 | 黃金貿易秘密獎（2021）顯示他掌握 TSMC 正式機密；離職後的 NDA 期限與範圍未揭露 |
| **學術論文產量薄** | 🟡 中 | 轉職後不足 3 年，期刊論文僅 1 篇（2026）可確認；ECTC/IEEE Trans 論文空缺 |
| **研究室初建期** | 🟡 中 | 2023 年才加入 NSYSU，研究室設備、碩博生團隊仍在積累中 |
| **職稱為「專業技術人員」** | 🟡 中 | 非一般 tenure 教授，身份較特殊，長期留任穩定性略低 |

---

## §5 建議合作題目（若通過法務關卡）

### 題目 A：CoWoS Warpage 量化模型與良率改善

**核心問題**：CoWoS-S/L/R 的有機基板 + 矽中介層多材料堆疊在高溫製程後的翹曲量超出允收標準（< 100 μm），影響後續 flip-chip bonding 良率。

**林勇志切入優勢**：有 epoxy molding compound 黏彈性 FEA 建模論文（IEEE 2011，36 引），加上 TSMC 13 年封裝整合實務，可做數值仿真 + 材料選擇 + 製程視窗三合一。

**交付物**：CoWoS warpage FEA 模型 + 關鍵材料參數敏感度分析報告

---

### 題目 B：SoIC Hybrid Bond 晶圓對準偏移補償演算法

**核心問題**：Wafer-to-Wafer（W2W）SoIC 對準偏移若超過 44 μm（已有 US11688717B2 揭露此問題），後續微影補偶困難，需自動閉迴路補償。

**林勇志切入優勢**：US11688717B2 和 US20240186258A1 的共同發明人，對此問題的工程根因已有深度理解，轉型為演算法研究或次世代製程優化完全可行。

**注意**：此題目與林勇志的 TSMC 專利直接相關，**務必先做法務評估確認 IP 邊界**。

---

### 題目 C：AI Chiplet 異質整合封裝熱管理

**核心問題**：HPC/AI Chiplet（如 GPU + HBM + 矽光子）在 CoWoS/SoIC 封裝中的局部熱點超過 100°C，散熱路徑不均導致可靠度問題。

**林勇志切入優勢**：2026 年最新論文已做 Through-Oxide Thermal Via 的熱管理分析；CIS 製程背景可延伸至 3D 堆疊 IC 熱模擬；南科地緣使實際封裝樣品取樣容易。

**交付物**：3D 封裝熱阻網路模型 + 微流道冷卻可行性評估（搭配學界 cooling 研究）

---

## §6 資料來源清單

| 資料項目 | URL / 說明 | 查詢日期 |
|---|---|---|
| 林勇志個人頁面（NSYSU SAT） | https://sat.nsysu.edu.tw/p/405-1325-334976,c25997.php?Lang=zh-tw | 2026-04-22 |
| 林勇志研究著作頁 | https://sat.nsysu.edu.tw/p/404-1325-339789.php?Lang=zh-tw | 2026-04-22 |
| 林勇志經歷榮譽頁 | https://sat.nsysu.edu.tw/p/404-1325-339788.php?Lang=zh-tw | 2026-04-22 |
| 先進半導體封測研究所介紹 | https://sat.nsysu.edu.tw/p/412-1325-23155.php?Lang=zh-tw | 2026-04-22 |
| NSYSU SAT 合作企業清單 | https://sat.nsysu.edu.tw/p/412-1325-23164.php?Lang=zh-tw | 2026-04-22 |
| TSMC x NSYSU 學程說明 | https://sat.nsysu.edu.tw/p/406-1325-341356,r5006.php?Lang=zh-tw | 2026-04-22 |
| 專利 US20240186258A1（晶圓對準） | https://patents.google.com/patent/US20240186258A1/en | 2026-04-22 |
| 專利 US11688717B2（對準偏移偵測） | https://patents.google.com/patent/US11688717B2/en | 2026-04-22 |
| Justia 林勇志專利列表 | https://patents.justia.com/inventor/yeong-jyh-lin | 2026-04-22 |
| Google Scholar 搜尋結果 | scholar.google.com "Yeong-Jyh Lin" semiconductor packaging | 2026-04-22 |

---

*Profile 執行人：Phase 2 深度 profile agent / 2026-04-22*
