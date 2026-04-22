# Phase 2 深度 Profile：楊佳玲 Chia-Lin Yang

**建檔日期**：2026-04-22
**評估等級**：Phase 1 🟢 Open → Phase 2 需重新評估（見下）

---

## ⚠️ 重大異動警示：政府職位衝突

**楊佳玲於 2026 年 2 月 2 日正式就任數位發展部政務次長（借調出任）。**

這是 Phase 2 最重要的發現。她目前身兼：
- 數位發展部政務次長（現任，2026.02 起）
- NTU 資工系特聘教授（借調，身分保留）
- 電機資訊學院副院長（借調前職）

政務次長為政治任命職位，任期受政府施政週期影響，非學術綁定，但代表她的精力已大幅移往政策面，短期內主導研究計畫的能量降低。建議評為 **🟡 條件性可行**，需評估借調期長短。

---

## 1. 隱形綁定檢查

### 企業綁定
| 合作方 | 性質 | 時間 | 現況 |
|--------|------|------|------|
| IBM | Faculty Award（2005、2010）| 學術榮譽獎 | 無持續性企業合約跡象；兩次獎項間隔 5 年，屬獨立授予 |
| 台達電（Delta Electronics） | Delta-NTU 聯合研發中心主任 | 2020–2023 | 已卸任主任一職；研究聚焦電動車、IoT 安全，非 AI chip |
| TSMC | 無直接證據顯示合約或兼職 | — | 研究偏架構層，非 fab 端 |
| NVIDIA-NTU | NVIDIA-NTU AI Joint Innovation Center 存在，但楊佳玲未列名參與者 | — | 無顯著綁定 |

**結論**：IBM 獎項為歷史性學術榮譽，無延續企業合作跡象；台達電合作於 2023 前結束且領域不重疊；TSMC 直接合作無證據。**企業綁定風險低。**

### 政府綁定（重要）
- **國科會科技政策諮議室副主任**（Phase 1 已知）：政策諮詢角色，非全職
- **數位發展部政務次長**（2026.02 起，借調）：**現為全職政府職務**，是實質性時間衝突

---

## 2. 技術契合度

### 研究主軸
楊佳玲獲選 IEEE Fellow 2026 的貢獻認定為：**「memory hierarchy 與 compute-in-memory 系統跨層設計方法論」**，完全覆蓋 T7b（AI accelerator）與 T5（NVM/CIM）兩個 Tier。

### 2022–2026 代表論文

| 年份 | 論文 | 場地 | 技術重點 |
|------|------|------|----------|
| 2026 | CIMNet: Joint Search for Neural Network and Computing-in-Memory Architectures | IEEE Micro 46(1) | CIM 架構 + NAS 協同搜索 |
| 2024 | PointCIM: A Computing-in-Memory Architecture for Accelerating Deep Point Cloud Analytics | MICRO 2024 | memristor crossbar 架構、點雲 AI 加速 |
| 2024 | Co-Designing NVM-based Systems for Machine Learning and In-memory Search | ICCAD 2024 | NVM 系統與 ML 協設計 |
| 2023 | Tensor Movement Orchestration in Multi-GPU Training Systems | HPCA 2023 | 多 GPU 訓練記憶體調度 |
| 2023 | Impact of Non-Volatile Memory Cells on Spiking Neural Network Annealing Machine | IEEE TCAS-I 70(11) | NVM + SNN 可靠性 |

**附加 2025 成果**：
- DATE 2025：Incremental Learning 模型剪枝（Filter-Based Adaptive Pruning）
- DATE 2025：REAP-NVM — NVM-based PUF 安全性（與德國 KIT Jörg Henkel 合作）
- ASP-DAC 2025：In-Storage 讀取中心化基因組比對加速

### 技術強項摘要
1. **CIM 架構**：memristor crossbar + 周邊邏輯自動化設計，是台灣學術界 CIM 先驅
2. **NVM 系統**：NAND Flash/ReRAM 在 AI inference 的系統整合、耐久性、安全性
3. **Edge AI**：點雲分析、SNN 低功耗推論（自動駕駛、AR/VR 場景）
4. **跨層協設計**：ML 演算法 + 硬體架構聯合搜索（CIMNet 方向）

**相對張孟凡（🔴 非 TSMC）的差異化**：張孟凡偏 circuit 實作與 tape-out 執行；楊佳玲偏架構層系統設計，不做 tape-out，擅長 NVM/CIM 軟硬協設計。與 TSMC 合作的切入點是技術 spec 定義與系統驗證，而非 PDK 層實作。

---

## 3. 學生工程素質

### Lab 規模
- 研究室：**Embedded Computing Lab**，NTU 資工系
- 近期論文共同作者（常見學生）：Xuan-Jun Chen（PointCIM、CIMNet 第一作者）、Ming-Liang Wei（多篇 NVM 安全類）、Han-Ping Chen、You-Kai Zheng、Jing-Jia Hung
- 2025 DBLP 統計顯示仍有 4-5 篇/年產出，lab 正常運作（即便借調中）

### 學生競賽與發表
- 學生直接在 MICRO（頂會）發表一作論文（PointCIM 2024）：代表學生有獨立完成頂會論文的能力
- IEEE Micro 期刊文章由學生主導撰寫（CIMNet 2026）

### 畢業生去向
無法取得完整名單，但從合作網絡推測：
- 與德國 KIT（Jörg Henkel 組）有長期交流，學生可能有海外博後機會
- 台達電合作期間（2020–2023）可能有學生進入台達 R&D
- Lab 屬 CIM/NVM 小眾高精度方向，典型去向：IC 設計公司 R&D（NVIDIA、Intel Labs）、學術界

---

## 4. 合作優缺點與建議

### 優點
1. **IEEE Fellow + 國科會傑出研究獎（2024）**：學術聲望最高等級，論文審查速度與 PI credit 強
2. **IEEE Computer Architecture Letters EIC**：掌握架構領域頂尖資訊流，合作論文 visibility 高
3. **DAC 2025 Program Co-chair**（注：原 Phase 1 資料標示 DAC 2024，實際為 DAC 2025）：對 EDA + 架構社群人脈廣
4. **CIM 先驅地位**：台灣學術界少數同時懂 NVM 物理特性 + 系統架構 + ML 演算法的學者
5. **台達電合作歷史**：熟悉產學合作 mode，不怕 deliverable 壓力

### 缺點 / 風險
1. **政務次長借調（2026.02–?）**：短期內 PI 時間嚴重壓縮，合作計畫可能由學生代理推進，風險視借調長度而定
2. **無 tape-out 能力**：研究停在架構/系統層，若需 silicon demo 需另找 circuit 合作者
3. **Lab 規模中等**：學生數量推估 5-8 人，非超大型 lab，並行計畫承載量有限
4. **TSMC 無直接合作痕跡**：需要從零建立合作管道，沒有既有信任基礎

### 3 個建議合作題目

**題目 A：Edge AI Chip for Autonomous Systems（CIM for Point Cloud）**
基於 PointCIM (MICRO 2024) 延伸，定義針對 TSMC N3/N2 製程最佳化的 CIM 架構規格。楊佳玲提供架構設計方法論，TSMC 提供製程參數與記憶體 cell 特性（RRAM/FeRAM）。適合 TSMC-NTU 聯合研究計畫格式。

**題目 B：NVM-based CIM 可靠性與安全性聯合設計**
結合 REAP-NVM（DATE 2025）的 PUF 安全方向與 NVM 耐久性（endurance）議題，設計在 TSMC 先進 NAND/RRAM 上的安全 CIM 架構。可延伸至 AI 推論晶片的硬體安全認證。

**題目 C：DTCO（Design-Technology Co-Optimization）for CIM**
利用 CIMNet（NAS + CIM 聯合搜索）框架，對接 TSMC N2P 製程的記憶體密度與功耗參數，形成 DTCO 方法論工具鏈。定位：非 circuit 實作，而是 system-level design space exploration。

---

## 5. 最終評估

| 面向 | 評分 | 說明 |
|------|------|------|
| 技術契合度（T7b+T5） | ★★★★★ | IEEE Fellow 認定的 CIM 先驅，完全命中 |
| 學術聲望 | ★★★★★ | Fellow + 傑出研究獎 + EIC |
| 可用時間 | ★★☆☆☆ | 借調政務次長，短期嚴重受限 |
| 企業綁定風險 | ★★★★★（低風險）| 無 TSMC 競爭性合作，無 NVIDIA 顯著綁定 |
| 學生工程素質 | ★★★★☆ | 頂會一作能力佳，規模中等 |
| 合作可行性 | 🟡 條件性可行 | 待確認借調結束時間 |

**建議**：暫緩啟動新研究計畫至借調結束（預估 1-2 年政府任期），或以「顧問角色」輕量接觸，由其核心學生（Xuan-Jun Chen 等）主導執行。若 2027 年後回歸學術，優先等級應升為 🟢 高優先。

---

## 6. 資料來源

- [Chia-Lin Yang 個人頁（NTU CSIE）](https://www.csie.ntu.edu.tw/~yangc/)
- [NTU CSIE 教師頁面](https://csie.ntu.edu.tw/en/member/Faculty/Chia-Lin-Yang-61108798)
- [Google Scholar](https://scholar.google.com/citations?user=NBjBhsEAAAAJ&hl=en)
- [DBLP 完整著作列表](https://dblp.org/pid/03/711.html)
- [NSTC 傑出研究獎 2024](https://web.nstc.gov.tw/cen/oaa/award_112/Chia-Lin-Yang.html)
- [維基百科（楊佳玲）](https://zh.wikipedia.org/wiki/%E6%A5%8A%E4%BD%B3%E7%8E%B2)
- [數位發展部正副首長頁](https://moda.gov.tw/aboutus/principal-officers/deputy-minister-yang/1761)
- [TechNews：數發部政務次長任命](https://technews.tw/2026/01/01/moda-deputy-minister/)
- [中央社：楊佳玲出任數發部次長](https://www.cna.com.tw/news/afe/202602020284.aspx)
- [IEEE CEDA Profile](https://ieee-ceda.org/contact/chia-lin-yang)
- [PointCIM @ Semantic Scholar](https://www.semanticscholar.org/paper/PointCIM:-A-Computing-in-Memory-Architecture-for-Chen-Chen/f0348eecdbe9346e40d6bebe076b9b6de37de95c)
- [台達臺大聯合研發中心](https://dnc.ntu.edu.tw/zh-TW)
- [MICRO 2024 主程式](https://microarch.org/micro57/program/)
- [IEEE Fellow Class of 2026 列表](http://cnste.org/uploads/2025/1204/b4fc73d1962b09f29ad52db208416e03.pdf)
- [DSET 科技民主研究院 profile](https://dset.tw/en/teams/chia-lin-yang/)
