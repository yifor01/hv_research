# Phase 2 深度 Profile — 胡璧合 (Vita Pi-Ho Hu)

**研究日期**：2026-04-22
**Phase 1 評定**：Tier-1 #5（FeFET × Monolithic 3D IC × CIM 三方交集）
**綁定狀態**：🟢 Open（確認）

---

## 1. 基本資訊

| 項目 | 內容 |
|------|------|
| 現職 | 教授，台大電機系（2024.08 起升等為 Full Professor） |
| Lab | Nanoelectronics and Memory Research Lab（辦公室 EE2-545，學生室 EE2-452） |
| 個人頁 | https://sites.google.com/site/vitapihohu |
| 學歷 | B.S.（2004）、Ph.D.（2011），均畢業於交通大學 |
| 職涯 | 交大助理研究員（2011-15）→ 中央助理/副教授（2015-20）→ 台大副教授（2020-24）→ 台大教授（2024-） |
| 訪問學者 | UC Berkeley EECS（2017, 2018）、澳洲國立大學（2019） |

---

## 2. 隱形綁定檢查 ⚠️

**結論：無發現隱性業界綁定，🟢 Open 評定確認。**

檢查項目與結果：

- **TSMC 全職/顧問職**：未發現任何 TSMC 研究部門職銜、顧問聘任或 Research Director 身份。LinkedIn 顯示職銜為純 NTU 教授。
- **冠名講座/Chair Professor**：持有 **Micron Foundation Chair Professor**（2024），由美光基金會贊助，**非 TSMC 冠名**；另有 Ren Min Outstanding Young Chair Professorship（2021）。
- **TSMC 學術合作關係**：屬於正常公開學術合作性質 —— 2020 年 IEEE TED 合作論文（TSMC 製程支援）；三位博士生分別獲 TSMC Ph.D. Scholarship（吳承鴻 2022、呂育誠 2023、曾翊銘 2024），代表 TSMC 認可學生素質，屬個人獎學金而非排他性研究綁定。
- **Lam Research**：學生呂育誠獲 Lam Research Paper Award，亦屬公開競賽型贊助。
- **Nature/IEDM 論文 Acknowledgments**：IEEE Xplore 論文因付費牆無法完整讀取，但公開資訊未顯示非一般性贊助條款。

---

## 3. 技術契合度

### 3.1 四大研究方向

1. **FeFET 與記憶體電路** — HfZrO/HZO 基 FeFET 設計、可靠性、多位元儲存，用於低功耗 Edge AI
2. **矽/Ge/III-V/2D 材料奈米電子** — CFET、Nanosheet FET、MoS₂/MoTe₂ channel，面向 Ångström 節點
3. **高效能低功耗 SRAM** — CFET SRAM、非揮發性 SRAM（FeFET-SRAM 混合），兼顧 cell stability 與速度
4. **Monolithic 3D IC 與 DTCO** — BEOL FeFET + FEOL CMOS 堆疊，M3D-FACT 架構，CIM macro 整合

### 3.2 2023–2026 代表論文（五篇）

| 年份 | 論文題目（摘要） | 發表 |
|------|---------------|------|
| 2024 | "Projected performance of Si- and 2D-material-based SRAM circuits ranging from 16 nm to 1 nm technology nodes"（2DM SRAM 效能投影，對應 1nm 節點的競爭力分析） | **Nature Nanotechnology**（IF ~40） |
| 2024 | CFET SRAM Paper（Yu-Cheng Lu & Meng-Lin Wu）| **IEDM 2024**（入選） |
| 2024 | "Monolithic 3D Integration using BEOL FeFET: Reliability, Thermal Effects, and DNN Accuracy"（BEOL FeFET 可靠性 + DNN 精度協同驗證） | IEEE 會議 |
| 2023 | "Monolithic 3D Integration of FeFET, Hybrid CMOS Logic and Analog RRAM Array for Energy-Efficient Reconfigurable Computing-In-Memory Architecture"（M3D-FACT 架構首次展示） | IEEE VLSI/IEDM 會議 |
| 2025 | IEDM 2025 接受論文 × 2（吳承鴻；曾翊銘、黃漢霖等） | **IEDM 2025**（入選） |

> **補充**：一篇 Advanced Materials（IF 30.8）論文亦已接受（2DM 相關）；一篇 Nature Scientific Reports 探討 3-Tier CFET 6T-SRAM with 2D-TMD channels（Ångström 節點，2026 年發表）。

### 3.3 TSMC / Applied Materials 製程紀錄

- 2020 IEEE TED 論文明確標註與 TSMC 合作之 energy-efficient M3D SRAM（TSMC 提供製程支援）
- 多位 TSMC Ph.D. Scholarship 得主（暗示 TSMC 對 lab 輸出方向的肯定，同時學生有進入 TSMC 實習/就業的管道）
- Lam Research Paper Award（學生呂育誠）— 代表沉積製程相關性

---

## 4. Lab 規模、學生素質與工程文化

### 4.1 現有 Lab 規模（2025 年）

- **博士生**：5 人（吳承鴻、呂育誠、曾翊銘、吳孟霖、黃漢霖）
- **碩士生**：約 17 人
- **畢業生**：2017–2025 大量校友（名單公開於個人網站）

### 4.2 學生工程素質指標

| 指標 | 佐證 |
|------|------|
| IEDM 學生入選（頂會） | IEDM 2024（2 篇）、IEDM 2025（2 篇）— 競爭最激烈的 device 頂會 |
| TSMC Ph.D. Scholarship | 連續三屆（2022/23/24）獲獎，罕見 |
| Lam Research Paper Award | 呂育誠 2023 |
| Nature Nanotechnology | 博士生 Yu-Cheng Lu 為第一作者（2024） |
| IEDMS Excellent Paper Award | 吳承鴻 2025 |

### 4.3 Lab 文化觀察

- **Device 設計主導**：從 BEOL 製程設計到電路模擬均在 lab 完成，重 pre-silicon 模型而非 tape-out 驗證
- **DTCO 導向**：每篇論文均包含 layout/area 估算與系統效能連結，工程感強
- **高發表頻率**：100+ 篇累積，且仍維持 Nature 與 IEDM 雙線並行，量質並重
- **女性 PI 代表性**：為台灣半導體圈少見的女性 PI，具有多元領導示範效應

---

## 5. 合作優缺點與建議

### 5.1 優點

**技術契合度極高（三方交集）**
- FeFET 是 2nm+ Post-SRAM/Post-Flash 的核心器件方向
- Monolithic 3D IC 是晶圓廠下一代 3D 整合路線（vs. Chiplet/Heterogeneous 3D）
- CIM AI 加速器與 FeFET M3D 結合，正是 TSMC N2/A16 製程的 BEOL 研究前沿

**L'ORÉAL-UNESCO Award（DEI 加分）**
- 2023 年獲獎為全球女科學家最高榮譽之一，對公司 DEI KPI 及對外發表有正面效益
- 台灣半導體學術圈中女性 Full Professor 比例低，能見度高

**Micron Chair Professor（非 TSMC 冠名，自由度高）**
- 由美光基金會贊助，與記憶體/DRAM 方向相符，但不妨礙與競爭方合作

**技術委員會滲透度**
- IEDM TC（2022-2026）、ISSCC TC（2026）、VLSI TC（2026）— 同時坐擁三大 Device+Circuit 頂會委員席位，情報與合作觸角廣

### 5.2 相對弱點（vs 競爭對手）

- **無自有 fab / PDK 直接存取**：研究仍以模擬為主，tape-out 依賴 TSMC/外部製程，不如有自建製程 lab 的團隊即時
- **Lab 規模中等（5 博士）**：輸出速度受限，同時承接大型合作項目的人力有壓力
- **Material 廣度 vs 深度**：同時研究 Si、Ge、2D、FeFET，廣泛但分散，合作聚焦點需事先對齊

### 5.3 與張孟凡的互補關係

| 面向 | 胡璧合 | 張孟凡 |
|------|--------|--------|
| 定位 | Pre-silicon Device 設計＋DTCO | Post-tape-out Circuit 驗證 |
| 強項 | FeFET 器件物理 / M3D BEOL 整合 | CIM Macro 電路 / 良率分析 |
| 代表作 | IEDM 2024 CFET SRAM（器件） | ISSCC CIM macro（電路） |
| 合作切入 | 提供新器件規格與模型 | 接收器件模型→電路實現 |

**理想合作模式**：胡璧合提供 FeFET BEOL M3D 器件設計 + SPICE model，張孟凡接手 CIM macro 電路設計 + tape-out，形成完整的 device-to-chip 研究鏈。

### 5.4 三個具體合作題目

**題目 A：BEOL FeFET 可靠性模型標準化**
研究 BEOL HZO FeFET 的 cycling endurance / data retention / variability，建立可供電路設計端直接使用的緊湊可靠性模型（SPICE-compatible）。目標：發表 IEDM/IEEE TED，提供業界 BEOL FeFET PDK 參考。

**題目 B：FeFET-based M3D CIM Macro 功耗-精度-面積協同最佳化**
結合胡璧合 M3D-FACT 架構與 AI inference workload，定量評估 FeFET multi-bit weight mapping 對 DNN top-1 accuracy 的影響，並以 TSMC 製程設計 proof-of-concept macro。目標：VLSI 2026 or ISSCC 2027。

**題目 C：2D 材料 CFET × FeFET 整合的 Ångström 節點非揮發性 SRAM**
探索 MoS₂ n-FET + MoTe₂ p-FET 搭配 HZO FeCap 實現三態 NV-SRAM，面向 A7/A5 節點。目標：Nature Electronics or IEDM 2026/2027。

---

## 6. 總結評分

| 評估維度 | 評分 | 說明 |
|----------|------|------|
| 技術契合度 | ⭐⭐⭐⭐⭐ | FeFET×M3D×CIM 三方完整交集，業界最前沿 |
| 學術聲望 | ⭐⭐⭐⭐⭐ | Nature Nanotech + IEDM 常駐，TC 席位三頂會 |
| 學生素質 | ⭐⭐⭐⭐ | 連續 TSMC Scholarship + Nature 第一作者 |
| 隱性綁定風險 | 🟢 Low | Micron Chair（非 TSMC），無發現排他性協議 |
| DEI 加分 | ⭐⭐⭐⭐⭐ | L'ORÉAL-UNESCO 全球獎項，台灣半導體女 PI 代表 |
| 合作門檻 | ⭐⭐⭐ | 需對齊 Device 設計方向，pure circuit 合作不直接 |

**綜合建議**：優先接觸，以「題目 B（M3D CIM Macro 功耗-精度協同）」為切入點，聯合張孟凡形成 device-circuit 完整研究鏈，爭取提交 VLSI 2026 或 ISSCC 2027。

---

## 7. 資料來源

| 來源 | 網址 | 查閱日期 |
|------|------|----------|
| 胡璧合個人網站（首頁） | https://sites.google.com/site/vitapihohu | 2026-04-22 |
| 胡璧合個人網站（Bio） | https://sites.google.com/site/vitapihohu/bio | 2026-04-22 |
| 胡璧合個人網站（Research Group） | https://sites.google.com/site/vitapihohu/research-group | 2026-04-22 |
| 胡璧合個人網站（Awards） | https://sites.google.com/site/vitapihohu/honor-award | 2026-04-22 |
| NTU 電機系教授個人資料 | https://www.ee.ntu.edu.tw/profile1.php?id=1080918 | 2026-04-22 |
| NTU 校方 Spotlight（L'ORÉAL 獎） | https://www.ntu.edu.tw/english/spotlight/2023/2139_20230316.html | 2026-04-22 |
| NTU Scholars | https://scholars.lib.ntu.edu.tw/entities/person/13c990a2-a3cf-4470-a58f-c65d06280be8 | 2026-04-22 |
| IEEE CASS Profile | https://ieee-cas.org/contact/vita-pi-ho-hu | 2026-04-22 |
| IEEE Nanotech Magazine Bio | https://inm.ieeenano.org/biography-of-professor-vita-pi-ho-hu/ | 2026-04-22 |
| Nature Nanotechnology 2DM SRAM 論文 | https://www.nature.com/articles/s41565-024-01693-3 | 2026-04-22 |
| IEEE Xplore — M3D BEOL FeFET Reliability | https://ieeexplore.ieee.org/document/10511909/ | 2026-04-22 |
| IEEE Xplore — M3D-FACT CIM | https://ieeexplore.ieee.org/document/10185221/ | 2026-04-22 |
| ACM — Spatial-Designed M3D CIM | https://dl.acm.org/doi/10.1145/3611315.3633240 | 2026-04-22 |
| TSMC Ph.D. Scholarship 官方 | https://www.tsmc.com/english/event/scholarship_apply25 | 2026-04-22 |
