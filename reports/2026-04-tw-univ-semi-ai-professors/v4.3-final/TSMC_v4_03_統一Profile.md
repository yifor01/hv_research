# §3 統一 Profile（55 位，S+A+B 級）

> **格式說明**：每位採「基本資料卡（含 5 維度評分） → 核心專長 × 近 3 年代表實績 → 合作紀錄 × 與外部公司狀況 → 建議合作方式 × 公開連結」四區塊結構。
> **5 維度權重**：研究軌跡 20% / fab 應用 25% / Lab 深度 20% / 可接洽度 20% / 長期價值 15%。
> C 級 6 位（總分 < 5.5）+ 14 位延伸候選池詳大表 §2。

---

### S01. 王俊明（Chun-Ming Albert Wang）｜總分 **9.0**（S 級）｜第一波

| 校系職級 | NSYSU 半導體及重點科技研究學院 SAT ｜ Professor of Practice（實務教授）｜ PhD: 待核實 |
|---|---|
| 學術指標 | SPIE Photomask Japan 一作；業界實戰型（無公開 Google Scholar）|
| Lab | TSMC 南科訓練通道共用；中型實戰團隊 |
| **5 維度評分** | 研究 9 ｜ fab 9 ｜ Lab 9 ｜ 接洽 9 ｜ 長期 9 ｜ SPIE 一作 + TSMC SAT 體制內合作方 + 2nm/1.4nm EUV 持續剛需 |

**核心專長 × 近 3 年代表實績**
- AI 光刻 OPC（先進節點光罩演算）/ RET 解析度增強 / DFM 可製造性設計 / 2nm EUV 光罩修正核心方法學
- SPIE Photomask Japan 2025 ML 光刻 hotspot 預測（一作）；NSYSU SAT 中心體制內共同主持人（TSMC 高雄 2nm fab 周邊）；持續執行 NSTC 光刻 AI 相關計畫；學生進入 TSMC 南科訓練中心為常態
- TSMC SAT 中心主要主持人；KLA Corp. 量測設備體系合作

**製程/封裝應用點（詳述）**
- **節點 / 段別**：N2（2nm）/ A16（1.4nm）EUV 光刻段；前段微影（Litho）+ DFM / Mask 設計介面（design house ↔ mask shop 之橋接層）
- **痛點對應**：
  - **EUV hotspot 漏檢率上升**：N2 進入 EUV 雙重曝光 + 多重 mask layer 後，傳統 model-based OPC 在 sub-resolution corner case 收斂慢，邊界 hotspot 漏掉率偏高 → 王俊明 SPIE Photomask Japan 2025 一作的 ML hotspot 預測可作 OPC 後端 sanity check，於 tape-out 前 24-48 hr 補強漏檢
  - **OPC TAT（Turnaround Time）**：N2 full-chip OPC 動輒 7-10 天 + 5-8 次迭代；ML proxy + 自動化 RET 可加速 inverse OPC iteration，理論上可降 20-30% 收斂時間
  - **學界 DFM ↔ 量產 SOP 落差**：學術 DFM 多優化 GDS layout，fab 還要考慮 process window + OPC bias + mask manufacturing 限制；王俊明本身為業界訓練教練（Professor of Practice），內建 close-the-gap 能力，是 SAT 中心設立的核心訴求
  - **Mask shop ↔ design house 對齊**：南科 mask shop 與外部 design house 的 OPC 設定差異常導致 first-silicon 偏差；ML hotspot 模型可作 design 端「fab-aware DFM lint」前置驗證
- **可導入時程（TRL）**：**TRL 8-9 / 立即** — SAT 中心已有量產級訓練流程與南科 fab 共用通道，等同延伸現案；無需新立 MOU、無需新增專屬 lab，僅需編列下個年度 SAT 預算項
- **配合 fab 部門**：南科光罩部（Mask Operation）為主對口；微影製程整合（Litho PIE）/ DFM 規則 owner / RET R&D 為次對口；外部 KLA 量測 RD（OPC verification → 量測 feedback loop）為跨組整合點
- **預期成效**：
  - OPC 收斂迭代次數 −20-30%（從 7-10 天降至 5-7 天）
  - Tape-out 前 hotspot 漏檢率改善 0.5-1 個量級（依量產資料 baseline）
  - SAT 受訓學生轉任 TSMC 比例提升至 60-70%（現約 40-50%）
  - 與 KLA 量測迴圈整合後，OPC verification 在不同 mask vendor 間一致性提升

**合作紀錄 × 與外部公司狀況**
- TSMC（SAT 中心主要主持人，體制內長期合作）；KLA Corp.（量測設備體系合作）
- TSMC 體制內合作方，**非離職風險**；無其他大廠競業綁定 → 屬「現成合作管道」而非「需重新洽談」

**建議合作方式 × 公開連結**
- **題目**
  - **主題目 A — N2/A16 EUV ML hotspot 預測**：接續 SPIE Photomask Japan 2025 一作研究，目標將 ML hotspot 模型導入 N2 量產 mask shop SOP，作 tape-out 前漏檢補強層
  - **主題目 B — OPC iteration 加速**：以 ML proxy 取代部份 model-based OPC step，加速 inverse OPC 收斂；對齊 N2 / A16 節點 tape-out 時程
  - **延伸題目 C — fab-aware DFM lint**：將 ML hotspot 模型前置至 design house，作 design 端「mask-aware sanity check」工具（與 EDA 軌的江蕙如 S02 / 蔡坤諭 B46 可串題）
  - **延伸題目 D — KLA 量測 ↔ OPC feedback loop**：與 KLA 量測 RD 整合 mask CD/registration 結果回饋 OPC model 校正
- **制度與簽約**
  - **架構**：直接擴大 SAT 中心既有合作框架，**無需新立 MOU**；以 SAT 年度預算項 + PI 委案雙軌
  - **預算建議區間**：年 NT$ 1,500-2,500 萬（含學生獎助 + 設備 license + 教師研究費 + tape-out 試片預算）；3 年滾動（推估區間，非承諾數字，依 SAT 既有合作量級對標）
  - **簽約對象**：NSYSU SAT 中心（單位）+ 王俊明 PI（個人 PI 委案）雙軌，IP 走 SAT 既有歸屬框架
  - **學生通道**：南科訓練中心既有暑期實習 + 畢業綠燈通道；合約內可加碼學生獎助名額
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：ML hotspot 模型於 N2 dummy mask 上達 hit rate ≥ 85%；OPC TAT 降幅 ≥ 10%；至少 1 篇與 TSMC 工程師聯名 SPIE / IEDM 論文
  - **第 2 年**：模型導入 N2 量產 mask shop SOP；hotspot 漏檢率改善 ≥ 0.5 個量級；fab-aware DFM lint 工具進入 EDA 軌 PoC
  - **第 3 年**：擴展至 A16 節點；SAT 受訓學生轉任比例達 60-70%；KLA 量測 feedback loop 完成 1 個 production line 驗證
  - **Exit criteria**：第 1 年 hit rate < 70% 即終止主題目 A、僅保留延伸題目；TAT 降幅 < 5% 即重新評估 OPC iteration 主軸
- **執行對口與啟動條件**
  - **主對口**：南科 Mask Operation + Litho PIE
  - **次對口**：DFM 規則 owner + RET R&D；外部 KLA 量測 RD
  - **啟動條件**：SAT 年度預算編列確認（Q4）+ Q1 三方 kick-off（光罩部 / DFM / SAT 中心）+ 學生實習名額 alignment
- **風險與緩解**
  - **競業 / IP**：王俊明屬 SAT 體制內合作方，無大廠競業綁定；IP 走 SAT 既有歸屬框架（已有先例，風險低）
  - **學生流向**：SAT 訓練學生原即以 TSMC 為主要 destination，畢業流向風險低
  - **學界 vs 量產 SOP 落差**：王俊明 Professor of Practice 身份內建 close-gap 能力，落差風險由其本人吸收
  - **能力限制**：王俊明 Google Scholar 公開計量低（業界實戰型 PI 常見），學術 h-index 等指標不適用；以實際 mask shop 落地戰績取代學術指標衡量
- **連結**：[NSYSU SAT](https://sat.nsysu.edu.tw/) ｜ [NSYSU 官網教師頁](https://www.nsysu.edu.tw/) ｜ 代表論文：SPIE Photomask Japan 2025 Proceedings

---

### S02. 江蕙如（Hui-Ju Chiang）｜總分 **9.0**（S 級）｜第一波

| 校系職級 | NTU EE / GIEE 教授 ｜ PhD: NCTU 電子工程 2002 |
|---|---|
| 學術指標 | h-20；引用 1,492；i10-50；DAC/ICCAD 一作穩定 |
| Lab | IRIS Lab（智動化實驗室）；博碩生皆有頂會一作 |
| **5 維度評分** | 研究 9 ｜ fab 9 ｜ Lab 9 ｜ 接洽 9 ｜ 長期 9 ｜ DAC/ICCAD 一作 + 完全自由 PI + 40 歲黃金期 |

**核心專長 × 近 3 年代表實績**
- AI-EDA / GNN Placement & Routing / Transformer-based DFM / ML Routing 演算法
- DAC/ICCAD 2023-2025 連年 placement & routing 一作；GNN-based placement 系列論文；ML Routing Transformer 架構提出；NCTU 14 年培訓底子 + 轉 NTU 體系延續
- NTU EDA 研究中心（體系內）；無大廠 Director 綁定

**製程/封裝應用點（詳述）**

- **節點 / 段別**：N2（2nm）/ A16（1.4nm）；前段設計規則 ↔ EDA 流程介面（Design-to-Fab）+ DFM 後段（Layout Post-Processor）；重心在 GNN-based 物理設計（Placement & Routing）與 Transformer-based DRC/LVS 修補
- **痛點對應**：
  - **N2 P&R 時間爆炸**：N2 全晶片 Placement & Routing 面對 5-8 個 patterning layer + sub-7nm pitch，商用工具 runtime 動輒 2-4 週；GNN proxy 可對 intermediate placement 做品質預測（wirelength / timing / congestion），早期剪掉劣解，理論上縮短 P&R 迭代 20-40%
  - **DFM Hotspot 漏補問題**：N2 設計規則超過 2,000 條（估），傳統 rule-based DRC 修補在 corner case 遺漏率偏高；Transformer-based DFM（ICCAD 2024 Rectilinear Floorplan）可學習 rule 間交互作用，補強 rule-based 盲點
  - **Timing Macro Modeling 不準**：多角 PVT timing signoff 在 N2 因 gate-level parasitics 複雜化而模型誤差擴大；TCAD 2024 一作 multi-corner timing macro modeling with neural collaborative filtering 直接切入此痛點，可與 TSMC 簽核流程整合
  - **Layout Decomposition ↔ Mask Shop 對齊**：EDA layout decomposition 輸出與 mask shop OPC 假設不一致導致 first-silicon 偏移；與 S01（王俊明）OPC ML 模型串接可形成 EDA → Mask end-to-end 通道
- **可導入時程（TRL）**：**TRL 5-6 / 6-12 個月啟動 PoC**；GNN placement proxy 已有 ICCAD/DAC 頂會驗證（學術 baseline），需接入 TSMC N2 benchmark cell（保密協議後），估 6-12 個月完成內部 PoC → 1-2 年進入量產 signoff 輔助
- **配合 fab 部門**：設計規則 / DFM 部門（Design Enablement）為主對口；Litho PIE（DRC context 提供方）為次對口；TSMC EDA 合作夥伴（Synopsys/Cadence）生態系為跨組整合點
- **預期成效**：
  - N2 全晶片 P&R 總 runtime 降幅 ≥ 20%（benchmark cell 實測）
  - DFM hotspot 漏補率改善 ≥ 30%（對比 rule-based baseline）
  - multi-corner timing signoff 誤差縮小 ≥ 0.5 sigma（N2 PVT corner）
  - 與 S01 OPC ML 串接後，design-to-mask pipeline 驗證完成 1 條 N2 production line

**合作紀錄 × 與外部公司狀況**
- NTU EDA 研究中心（體系內）；無大廠 Director 綁定
- **無公開可見外部綁定**；無獨董、無顧問聘任、無 JDP 專屬關係 → 完全自由 PI

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — N2 GNN Placement & Routing 加速**：以 GNN proxy model 加速 N2 全晶片 P&R 迭代，目標縮短 runtime 20-40%；接續 ICCAD 2024 Rectilinear Floorplan 一作成果
  - **主題目 B — Transformer-based multi-corner Timing Signoff 輔助**：以 Neural Collaborative Filtering（TCAD 2024 一作）強化 N2 PVT timing macro 精度，直接嵌入 TSMC signoff 流程
  - **延伸題目 C — DFM Hotspot ML 修補工具**：Transformer DFM 模型與 rule-based DRC 並聯使用，補強 corner case 漏修（與 S01 王俊明 mask-aware hotspot 串題、與 A22 張耀文 / A25 李建模 EDA 群 cross-ref）
  - **延伸題目 D — EDA → Mask end-to-end Pipeline PoC**：與 S01 王俊明 OPC ML 整合，建立從 EDA layout 到 mask shop 的驗證通道（EDA 群 × OPC 群聯合題）
- **制度與簽約**
  - **架構**：NTU IRIS Lab 直屬委案（PI-level JDP）+ NTU EDA 體系共同研究計畫；3+2 滾動（前 3 年核心合作，後 2 年視成果決定延伸）
  - **預算建議區間**：年 NT$ 1,200-2,000 萬，3 年滾動（推估區間，非承諾數字，依 NTU EE 同規模 JDP（如台積電-台大 N2 EDA 合作）對標）
  - **簽約對象**：NTU 研發處（NTU OTT）+ 江蕙如 PI（個人委案）雙軌；IP 歸屬依 NTU 技轉標準協議，TSMC 取得 fab 內使用授權
  - **學生通道**：IRIS Lab 博士生優先推薦 TSMC 暑期研究（既有慣例）；合約內可加碼 1-2 名 PhD Scholarship 名額
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：GNN P&R proxy 在 N2 benchmark cell（保密）上 runtime 降幅 ≥ 10%；multi-corner timing model 誤差 < 2%（比商用工具 baseline）；至少 1 篇 TSMC 聯名 DAC/ICCAD
  - **第 2 年**：N2 production tape-out 輔助工具上線（design sign-off 輔助層）；DFM 修補工具進入 Design Enablement 測試環境；延伸 EDA-mask pipeline PoC 完成
  - **第 3 年**：P&R runtime 降幅穩定 ≥ 20%（量產晶片驗證）；工具移交 TSMC 內部 EDA 團隊維運；A16 節點延伸啟動
  - **Exit criteria**：第 1 年 runtime 降幅 < 5% 且 timing 誤差 > 5% 同時發生，則暫停主題目 A；單項未達標允許調整方法後繼續
- **執行對口與啟動條件**
  - **主對口**：TSMC Design Enablement / DFM 部門
  - **次對口**：Litho PIE（DRC rule 提供）；EDA 生態系合作夥伴（Synopsys/Cadence NTU 聯絡窗口）
  - **啟動條件**：N2 benchmark cell 保密協議簽署（estimated 4-8 週）→ Q1 kick-off workshop → IRIS Lab 2 名 PhD 配置確認
- **風險與緩解**
  - **競業 / IP**：無大廠獨家綁定；NTU OTT IP 框架成熟；工具類研究成果走 TSMC 使用授權而非轉讓，降低 IP 衝突
  - **學生流向**：IRIS Lab 學生高比例進入 EDA 工具商（Synopsys/Cadence）或 IC 設計公司，TSMC 需與 EDA 廠競才；建議以 TSMC PhD Scholarship 名額提前綁定
  - **學界 vs 量產 SOP 落差**：學術 benchmark（ISPD contest 公開 cell）與 TSMC N2 proprietary rule 存在 gap；需配置 TSMC DFM 工程師 20% 工時作 domain translation
  - **能力限制**：WebSearch 無法核實 IRIS Lab 與任何特定公司的非公開顧問協議或進行中 JDP；建議正式接洽前由 TSMC Legal 再確認無排他條款
- **連結**：[NTU EE 個人頁](https://www.ee.ntu.edu.tw/profile1.php?id=1060726) ｜ [Google Scholar](https://scholar.google.com/citations?user=vj9r7ywAAAAJ) ｜ [DBLP](https://dblp.org/pid/96/1943.html) ｜ [IEEE CEDA](https://ieee-ceda.org/contact/iris-hui-ru-jiang) ｜ 代表論文：ICCAD 2024 Rectilinear Floorplan；IEEE TCAD 2024 Multi-Corner Timing Macro Modeling with Neural Collaborative Filtering

---

### S03. 馬誠佑（Cheng-Yu Ma）｜總分 **8.9**（S 級）｜第一波

| 校系職級 | NSYSU 電機 + SAT 合聘 ｜ 教授（2021/08 升等正教授）｜ PhD: NCTU 電子工程 2008 |
|---|---|
| 學術指標 | IEEE TED 2025 一作；56 期刊 + 47 國際研討會（總 117 篇）/ 9 專利 |
| Lab | ADDA Lab 50-60 人（大型）|
| **5 維度評分** | 研究 9 ｜ fab 9 ｜ Lab 8 ｜ 接洽 9 ｜ 長期 9 ｜ IEEE TED 一作 + 前 UMC 5 年實戰（13 年前離職無競業）+ 2nm NVM 剛需 |

**核心專長 × 近 3 年代表實績**
- FeFET（Ferroelectric FET）/ HfZrO TFT 氧化物薄膜電晶體 / Neuromorphic 邊緣 AI 晶片 / 2nm NVM 核心元件
- IEEE Transactions on Electron Devices 2025/01 junctionless FeFET（一作）；連續 5 次教學獎；68 篇期刊 + 9 專利累計產出；ADDA Lab 50-60 人培育 TSMC / 封測廠人才
- 連續 5 次教學獎；ADDA Lab 大型實驗室主持

**製程/封裝應用點（詳述）**

- **節點 / 段別**：N2（2nm）/ A16（1.4nm）BEOL + 後段 NVM（Non-Volatile Memory）段；前段元件整合（FeFET gate stack）+ BEOL NVM 嵌入層（MFMIS 結構）+ Neuromorphic CIM 巨集（SRAM 同層或 3D 堆疊）；與 S05 胡璧合 CIM 群高度互補
- **痛點對應**：
  - **2nm BEOL NVM 缺口**：N2 以下 SRAM bitcell 面積縮減壓力大，embedded NVM（eNVM）成為主流補位方案；FeFET（HfZrO 基）可 BEOL 整合、熱預算低（< 400°C），避免 FEOL 污染 → 馬誠佑 IEEE TED 2025 junctionless FeFET 正好切入此痛點
  - **Neuromorphic Inference 效能 vs 精度 trade-off**：TSMC 客戶（如邊緣 AI SoC）需要 sub-mW neuromorphic inference macro；FeFET synapse 的 multi-level cell（MLC）操作面臨 endurance（10⁶ cycle）vs retention（10 年）拉鋸，ADDA Lab 的 128-level 精度研究直接對應
  - **HfZrO TFT 背板整合（3D 感知器陣列）**：HAR TSV 與 3D 堆疊架構下，氧化物 TFT 作為記憶體選擇器（selector）有低漏電優勢；ADDA Lab HfZrO TFT 研究可補位 M3D CIM 架構中的 selector 設計（與 S05 同 cluster 串題）
  - **UMC 世代遷移知識轉用**：馬誠佑前 UMC 28/20nm 元件工程師背景（閘極氧化層 / high-k 整合），與 TSMC 2nm HKMG 流程有高度知識相容性；fab 談合作時無需額外知識轉譯成本
- **可導入時程（TRL）**：**TRL 5-6（FeFET BEOL）/ TRL 3-4（Neuromorphic macro）/ 12-24 個月進入 N2 PoC**；FeFET 元件特性驗證成熟，BEOL 整合需 TSMC N2 代工片，估 12-24 個月完成 PoC → 2-3 年進入產品節點試產
- **配合 fab 部門**：N2 記憶體整合研發（Memory R&D / eNVM team）為主對口；前段元件整合（FEOL Integration）次對口；與 S05 胡璧合共同合作的 CIM macro 整合工程師為跨組整合點
- **預期成效**：
  - FeFET eNVM endurance ≥ 10⁶ cycle、retention ≥ 10 年（85°C）
  - Neuromorphic inference macro 功耗 < 1 mW（邊緣 AI target）
  - N2 BEOL FeFET first silicon 良率 ≥ 80%（初版 PoC）
  - ADDA Lab 學生轉任 TSMC / 封測廠比例提升至 60%（估現況 40-50%）

**合作紀錄 × 與外部公司狀況**
- 前 UMC 28/20nm 工程師（5 年實戰，13 年前離職，已無競業風險）；NSYSU-TSMC 高雄 2nm 周邊合作
- **無現役綁定**；UMC 背景屬「歷史資產」非現役身份；無其他顧問 Chair 或獨董職

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — N2 BEOL FeFET eNVM 整合**：以 HfZrO-based junctionless FeFET 做 N2 BEOL 嵌入式 NVM，目標 10⁶ cycle endurance + 10 年 retention；接續 IEEE TED 2025 一作成果
  - **主題目 B — Neuromorphic CIM Macro 邊緣 AI**：FeFET synapse multi-level cell（128 level）+ 邊緣 AI inference macro 設計；功耗目標 < 1 mW（與 S05 胡璧合 CIM 群串題，可同 cluster 協作）
  - **延伸題目 C — HfZrO TFT 作 3D M3D Selector**：氧化物 TFT 作為 M3D CIM 架構 selector layer，補位 3D 堆疊漏電問題（與 S05 同 cluster 可串題）
  - **延伸題目 D — NSYSU SAT 體制整合**：透過 NSYSU SAT 中心將 ADDA Lab 結果快速接入 TSMC 高雄 2nm fab 試驗通道（與 S01 王俊明 SAT 共用通道，降低協議成本）
- **制度與簽約**
  - **架構**：NSYSU ADDA Lab 專案委案（PI-level）+ NSYSU SAT 中心體制通道；3 年期 JDP，配合 TSMC N2 量產 2H'25 timing
  - **預算建議區間**：年 NT$ 1,500-2,500 萬，3 年滾動（推估區間，非承諾數字，依 NSYSU SAT 同規模元件研究 JDP 對標）
  - **簽約對象**：NSYSU 研發處（OTT）+ 馬誠佑 PI（委案）雙軌；若借道 SAT 中心，IP 框架沿用 SAT 既有協議
  - **學生通道**：ADDA Lab 50-60 人大型實驗室；建議每年 3-5 名暑期實習名額 + 1-2 名 TSMC PhD Scholarship
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：FeFET 元件在 TSMC N2 代工片上完成電性確認（I-V / C-V / endurance 初測）；至少 1 篇 IEDM/VLSI 聯名投稿
  - **第 2 年**：eNVM PoC endurance 達 10⁵ cycle、retention 通過 85°C/1,000 hr 初測；Neuromorphic macro 功能驗證（FPGA 模擬層）
  - **第 3 年**：N2 BEOL FeFET eNVM 良率 ≥ 80%；Neuromorphic macro tape-out；ADDA 學生轉任率目標 60%
  - **Exit criteria**：第 1 年代工片電性確認失敗（leakage > 10⁻⁸ A / endurance < 10³ cycle），則暫停主題目 A 重新設計 gate stack；第 2 年 retention < 1,000 hr 則降級為延伸題目
- **執行對口與啟動條件**
  - **主對口**：TSMC N2 記憶體整合研發（Memory R&D / eNVM team）
  - **次對口**：FEOL Integration（gate stack 協調）；NSYSU SAT 中心（試片通道）；S05 胡璧合 CIM 群聯絡窗口
  - **啟動條件**：NSYSU SAT 年度合作框架確認 → 代工片訂單（N2 shuttle）排程 → ADDA Lab 2-3 名 PhD 名單確認
- **風險與緩解**
  - **競業 / IP**：馬誠佑前 UMC 13 年前離職，無競業；無現役大廠綁定；9 件專利已在 NSYSU 名下，授權框架清晰
  - **學生流向**：ADDA Lab 大型實驗室，學生出路多元（TSMC / ASE / MediaTek 均有）；PhD Scholarship 可優先固定 TSMC 流向
  - **學界 vs 量產 SOP 落差**：馬誠佑前 UMC 實戰背景（28/20nm 元件工程師）縮短學術-量產知識 gap；BEOL 熱預算管控需 TSMC PIE 工程師協同
  - **能力限制**：WebSearch 無法核實 ADDA Lab 與其他廠商是否有進行中非公開 JDP；建議接洽前由 TSMC Legal 確認
- **連結**：[ADDA Lab 教授頁](https://sites.google.com/view/nsysu-addalab/%E6%8C%87%E5%B0%8E%E6%95%99%E6%8E%88-professor) ｜ [ADDA Lab 著作](https://sites.google.com/view/nsysu-addalab/%E8%91%97%E4%BD%9C%E5%88%97%E8%A1%A8-publications) ｜ [ResearchGate](https://www.researchgate.net/scientific-contributions/William-Cheng-Yu-Ma-2011276114) ｜ [NSYSU SAT](https://sat.nsysu.edu.tw/) ｜ 代表論文：IEEE TED 2025/01 Junctionless FeFET（一作）

---

### S04. 陳亮嘉（Liang-Chia Chen）｜總分 **8.9**（S 級）｜第一波

| 校系職級 | NTU 機械工程學系 特聘教授 + AOIEC 聯盟主持 ｜ 終身特聘教授 ｜ PhD: University of South Australia 先進製造與機械工程 2000 |
|---|---|
| 學術指標 | h 資深、SPIE MIPC 連發；2016 MOST 傑出研究獎；2022 NSTC 未來科技獎 |
| Lab | NTU ME PMLab（精密量測實驗室）21 人大型團隊 |
| **5 維度評分** | 研究 9 ｜ fab 9 ｜ Lab 9 ｜ 接洽 9 ｜ 長期 9 ｜ 2021 NSTC 傑出 + 2022 未來科技獎 + 量測設備量產級 + CoWoS 量測剛需 |

**核心專長 × 近 3 年代表實績**
- OCD scatterometry 光學臨界尺度量測 / HAR TSV 量測 / AI metrology / 共焦干涉 metrology
- 2022 NSTC 未來科技獎；2016 MOST 傑出研究獎；SPIE MIPC 2023-2026 連發；NTU AOIEC 聯盟（43 家企業 + 4 校）共主持
- 2022 NSTC 未來科技獎；2016 MOST 傑出研究獎；NTU ME PMLab Lab 21 人大型團隊

**製程/封裝應用點（詳述）**

- **節點 / 段別**：後段封裝段（Back-End / Advanced Packaging）；CoWoS-S/L（Chip-on-Wafer-on-Substrate）/ SoIC（System-on-Integrated-Chips）/ HBM stack 量測介面；具體量測目標：HAR（High-Aspect-Ratio）TSV、Hybrid Bonding CuCu 接合面、RDL 線寬線距、microbump 高度均勻度
- **痛點對應**：
  - **HAR TSV 量測盲區**：CoWoS TSV 深寬比達 10:1 以上（估 depth > 50 µm, pitch < 10 µm），現有商用 SEM/X-ray 量測 throughput 慢（< 100 via/hr）、且量測本身破壞性；陳亮嘉 OCD scatterometry + 共焦干涉 非接觸式可達 > 1,000 via/hr，直接解決 throughput 瓶頸
  - **Hybrid Bonding 接合均勻度 in-line 量測**：SoIC Cu-Cu Hybrid Bonding pad pitch 縮至 < 3 µm 後，接合凹陷（dishing）和 Cu protrusion 需 nm 級精度量測；現有量測工具在量測速度與精度 trade-off 難以兩全；PMLab AI metrology（2022 NSTC 未來科技獎核心）可結合 AI regression 做 in-line 高速推定
  - **Advanced Package AOI 跨製程遷移**：TSMC 封裝廠（CoWoS/SoIC）製程持續迭代，每代新工序需重新標定 AOI 規則；PMLab 在 AOIEC 聯盟框架（43 家企業）積累跨製程量測模型，可縮短 AOI 重校時間 50%+
  - **OCD 模型不確定性量化**：AI metrology 在新材料（如 low-k dielectric / CuSiO₂ hybrid）下模型外推不確定性高；PMLab 的 NSTC 未來科技獎技術已納入不確定性估計模型（confidence interval output），符合量產 spec 管控需求
- **可導入時程（TRL）**：**TRL 7-8（OCD + 共焦干涉系統）/ 立即-6 個月啟動**；PMLab 已有量測設備實體系統（非純軟體），可直接送入 TSMC CoWoS 封裝廠進行設備評估（Tool Qualification），估 6 個月內完成初步 TQ
- **配合 fab 部門**：CoWoS 封裝製程整合（Advanced Packaging Integration）為主對口；量測設備評估部門（Metrology / Equipment Engineering）次對口；AOIEC 聯盟中的 TSMC 上下游設備商（致茂、均豪）為跨組整合點
- **預期成效**：
  - HAR TSV 非接觸量測 throughput ≥ 1,000 via/hr（vs 現有 SEM < 100 via/hr）
  - Hybrid Bonding dishing 量測精度 ≤ 1 nm（3σ）
  - AOI 跨製程重校時間縮短 ≥ 50%（AOIEC 框架內跨廠驗證）
  - AI metrology 模型在新材料外推不確定性 CI 覆蓋率 ≥ 95%

**合作紀錄 × 與外部公司狀況**
- 致茂、均豪等設備商（中性，TSMC 上下游）；AOIEC 聯盟 43 家企業生態系
- 設備商合作為中性關係（TSMC 上下游，非競業）；**無獨家綁定**

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — CoWoS HAR TSV 非接觸式高速量測系統**：OCD scatterometry + 共焦干涉系統導入 CoWoS 封裝廠，取代現有 SEM 破壞性量測；目標 throughput ≥ 1,000 via/hr，接續 NSTC 未來科技獎技術
  - **主題目 B — SoIC Hybrid Bonding in-line AI Metrology**：AI regression 模型推定 CuCu pad 接合凹陷（dishing）/ protrusion，精度目標 ≤ 1 nm（3σ）；與 S08 陳智 nt-Cu 材料研究串題（量測 ↔ 材料雙向回饋）
  - **延伸題目 C — AOIEC 聯盟 TSMC 上下游量測標準化**：透過 AOIEC 43 家企業框架，推動 CoWoS/SoIC 量測規格跨廠商標準化（設備互換性 / 量測協議對齊），（與 B34 羅裕龍量測群 cross-ref）
  - **延伸題目 D — RDL 線寬 AI 快速量測**：Hyper RDL（CoWoS-L 下一代，< 2 µm 線距）線寬量測模型，配合 S06 陳冠能 Hyper RDL 封裝進度
- **制度與簽約**
  - **架構**：NTU AOIEC 聯盟框架下直接啟動 fab 量測案；無需新立 MOU（AOIEC 既有協議）；配合 Tool Qualification（TQ）流程簽設備評估協議
  - **預算建議區間**：年 NT$ 1,800-3,000 萬，3-5 年滾動（推估區間，非承諾數字，依 NTU AOIEC 設備類 JDP 同規模對標；含設備進廠費 + 工程師配置 + 聯名研究費）
  - **簽約對象**：NTU AOIEC 聯盟（聯盟合約）+ 陳亮嘉 PI（個人委案）雙軌；設備 IP 歸屬按 NTU OTT 標準協議，量產配方授權給 TSMC
  - **學生通道**：PMLab 21 人大型實驗室；建議每年 2-3 名暑期工廠實習（量測設備 TQ 期間 on-site）
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：HAR TSV 量測系統完成 TSMC CoWoS 封裝廠 Tool Qualification 初評；throughput 達 ≥ 500 via/hr（中期 milestone）；至少 1 篇 SPIE MIPC / ECTC 聯名
  - **第 2 年**：throughput 達 ≥ 1,000 via/hr；dishing 量測精度驗證（量測 30 批次，3σ ≤ 1.5 nm）；AOIEC 聯盟量測標準草案完成
  - **第 3 年**：系統進入 CoWoS production line 正式量測工序；Hyper RDL 量測模型 PoC 完成；技轉 / 設備授權談判啟動
  - **Exit criteria**：第 1 年 throughput < 200 via/hr 或量測重複性 Cpk < 1.33，則暫停主題目 A 重新評估光學系統設計
- **執行對口與啟動條件**
  - **主對口**：TSMC Advanced Packaging Integration（CoWoS 量測工序 owner）
  - **次對口**：Metrology / Equipment Engineering（TQ 流程 coordinator）；致茂、均豪（AOIEC 聯盟設備商接口）
  - **啟動條件**：AOIEC 聯盟 TSMC 成員資格確認 → Tool Qualification 申請提交（estimated 2-4 週流程）→ PMLab 量測設備進廠運輸安排
- **風險與緩解**
  - **競業 / IP**：致茂、均豪為 TSMC 上下游設備商（非競業），合作為中性；AOIEC 聯盟無獨家排他協議
  - **學生流向**：PMLab 學生多進入量測設備商或 TSMC 量測部門，流向高度吻合
  - **學界 vs 量產 SOP 落差**：陳亮嘉已有量測設備實體系統（非純學術），TQ 落差相對 EDA/元件類研究低；主要 gap 在廠內潔淨室（cleanroom）規範適配
  - **能力限制**：WebSearch 無法核實 PMLab 是否已有進行中的 TSMC 保密量測合作；建議 TSMC 量測設備部門先行內部 check
- **連結**：[NTU ME 教師頁](http://ai.robo.ntu.edu.tw/en/personal.php?id=32) ｜ [PMLab 官網](https://sites.google.com/view/ntupmlab) ｜ [NTU AOIEC 聯盟](https://sites.google.com/g.ntu.edu.tw/ntu-aoiec) ｜ [NTU Spotlight](https://www.ntu.edu.tw/english/spotlight/2023/2159_20230511.html) ｜ 代表論文：SPIE MIPC 系列 2023-2026；NSTC 未來科技獎 2022

---

### S05. 胡璧合（Vita Pi-Ho Hu）｜總分 **8.8**（S 級）｜第二波

| 校系職級 | NTU EE（2025/08 兼 GUPS 全球半導體學位學程 Director）｜ 教授（2024/08 升等正教授；Micron Foundation Chair Professor）｜ PhD: NCTU 電子工程 2011 |
|---|---|
| 學術指標 | IEDM 2024/2025 各 2 篇；Nature Nanotech 2024 |
| Lab | 奈米電子與記憶體實驗室；3 位連續 TSMC PhD Scholarship 學生 |
| **5 維度評分** | 研究 9 ｜ fab 9 ｜ Lab 9 ｜ 接洽 8 ｜ 長期 9 ｜ Nature Nanotech + IEDM + TSMC PhD ×3 屆 + N2/A16 FeFET 剛需 |

**核心專長 × 近 3 年代表實績**
- FeFET × M3D（Monolithic 3D）/ CIM（Compute-in-Memory）/ CFET SRAM（Complementary FET SRAM）/ 2D Material 元件
- 2024 升等正教授（Micron Foundation Chair Professor）；Nature Nanotechnology 2024 2D 材料 SRAM；IEDM 2025 × 2 篇 + IEDM 2024 × 2 篇；L'ORÉAL-UNESCO Women in Science 2023；ISSCC 2026 / VLSI 2026 / EDTM 2025-2026 技術委員；3 位連續 TSMC PhD Scholarship 學生
- IEEE CAS NG-TC Chair-Elect；IEEE INEC 2025 Invited Speaker；Micron Foundation Chair Professor

**製程/封裝應用點（詳述）**

- **節點 / 段別**：N2（2nm）/ A16（1.4nm）前段元件 + BEOL M3D（Monolithic 3D）整合段；核心：FeFET gate stack（FEOL）、M3D CIM macro（BEOL 疊加層）、CFET SRAM bitcell（N2/A16 架構研究）、2D material FET（前瞻研究）
- **痛點對應**：
  - **N2 SRAM bitcell 面積縮減極限**：N2 6T SRAM 因 FinFET scaling 接近極限，CFET（Complementary FET）SRAM 是下一代減面積方案；胡璧合 IEDM 2025 × 2 篇含 CFET SRAM 研究，直接對應 A16 CFET 整合設計空間探索
  - **CIM Macro 效能瓶頸（memory wall）**：AI 推論晶片（HBM + GPU 架構）受 memory bandwidth 瓶頸限制；M3D CIM（Compute-in-Memory 嵌於記憶體層）可在 BEOL 直接做向量 MAC 運算，減少 DRAM access 50%+；胡璧合 IEDM/ISSCC 系列論文直接切入此架構
  - **FeFET eNVM 與 CIM 雙用設計**：N2 BEOL FeFET 同時可作 eNVM（S03 馬誠佑主攻）與 CIM weight storage，胡璧合的 FeFET × CIM 整合方案可形成共用平台，避免兩套元件流程並行的重工
  - **2D Material SRAM 可靠性**：Nature Nanotech 2024（2D material SRAM 胡璧合學生一作）代表下一代 post-Si 記憶體元件潛力；但 2D material 在量產環境的 defect density 與 interface trap 問題仍需 fab 協同解決
- **可導入時程（TRL）**：**TRL 5-6（FeFET CIM macro）/ TRL 3-4（CFET SRAM / 2D material）/ 12-24 個月 N2 PoC**；FeFET CIM 元件特性驗證成熟，CFET SRAM 屬 A16 設計研究（量產 2027+），2D material 屬前瞻段（TRL 3-4）
- **配合 fab 部門**：N2 記憶體整合研發（eNVM / CIM team）為主對口；A16 CFET 元件工程（Device Integration）次對口；TSMC PhD Scholarship 學生通道（既有 × 3 屆）為跨組整合點
- **預期成效**：
  - N2 FeFET CIM macro 功耗效率 ≥ 10 TOPS/W（邊緣 AI inference 目標）
  - CFET SRAM bitcell 面積縮減 ≥ 20%（vs 同代 FinFET SRAM baseline，設計研究層）
  - Memory wall 改善：AI 推論 DRAM access 降低 ≥ 30%（M3D CIM macro 驗證）
  - TSMC PhD Scholarship 學生每屆至少 1 名轉任 TSMC 記憶體整合研發

**合作紀錄 × 與外部公司狀況**
- TSMC PhD Scholarship × 3 屆學生（強力人才管道）；Lam Research 合作紀錄；美光 Chair Professor（2024-）
- **美光 Chair Professor**（2024-）為榮譽性冠名講座，**非獨家顧問**，與 TSMC 合作不衝突；TSMC PhD Scholarship 學生反而顯示既有合作深度

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — N2 FeFET × M3D CIM Macro 設計**：FeFET 作 weight storage 的 M3D Compute-in-Memory macro，整合於 N2 BEOL；功耗目標 ≥ 10 TOPS/W；接續 IEDM 2025 / ISSCC 2026 成果（與 S03 馬誠佑 FeFET eNVM 共用元件平台，同 CIM cluster 可協作）
  - **主題目 B — A16 CFET SRAM 設計空間探索**：CFET bitcell 面積縮減方案設計研究；與 TSMC A16 元件工程共同探索 N/P 對齊方案（A16 量產預計 2027，研究提前 2-3 年）
  - **延伸題目 C — 2D Material SRAM 缺陷工程 + 可靠性**：MoS₂ / WSe₂ FET SRAM 在量產環境的 interface trap 降低方案；前瞻段，以聯名論文為主要 deliverable
  - **延伸題目 D — FeFET CIM × Neuromorphic 整合**：FeFET 同時作 eNVM 與 CIM weight storage 的共用設計框架（與 S03 馬誠佑 neuromorphic 串題，同 cluster cross-ref，建議設 cluster 協調會議）
- **制度與簽約**
  - **架構**：Joint Lab（NTU 奈米電子與記憶體實驗室 × TSMC 記憶體整合研發）+ 多年期 JDP；5 年期（3+2 滾動），配合 N2 量產 2H'25 + A16 量產 2027 雙節點時程
  - **預算建議區間**：年 NT$ 2,500-4,000 萬，5 年滾動（推估區間，非承諾數字，依 NTU Micron Chair 同規模 Joint Lab（Micron Foundation × NTU EE）對標；含 PhD Scholarship × 3 名 + 設備 + 代工片）
  - **簽約對象**：NTU 研發處（OTT）+ 胡璧合 PI（委案）雙軌；Micron Foundation Chair 為榮譽性，不影響 TSMC JDP 簽約；IP 走 NTU OTT 標準框架
  - **學生通道**：既有 TSMC PhD Scholarship × 3 屆（強力前例）；建議第 4 屆起擴至 4-5 名，鎖定 CIM / CFET 方向
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：FeFET CIM macro 在 N2 代工片完成元件電性確認；CFET SRAM 設計研究報告交付；至少 1 篇 IEDM/ISSCC 聯名
  - **第 2 年**：M3D CIM macro 功能驗證（ring oscillator + MAC 測試電路）；DRAM access 降低 ≥ 20%（模擬層驗證）
  - **第 3 年**：N2 FeFET CIM macro tape-out 完成；功耗效率 ≥ 10 TOPS/W 量測驗證；A16 CFET SRAM 設計方案提案至 TSMC A16 元件工程
  - **Exit criteria**：第 1 年 FeFET leakage > 10⁻⁸ A 或 CIM MAC 精度 < 95%，則重新審視 BEOL 熱預算設計；第 2 年 DRAM access 降低 < 10% 則降級延伸題目
- **執行對口與啟動條件**
  - **主對口**：TSMC N2 記憶體整合研發（eNVM / CIM team）
  - **次對口**：A16 元件工程（Device Integration）；TSMC PhD Scholarship 計畫辦公室（學生通道擴編）
  - **啟動條件**：N2 代工片 shuttle 排程確認 → PhD Scholarship 第 4 屆名額公告 → NTU OTT JDP 框架協商（estimated 4-8 週）
- **風險與緩解**
  - **競業 / IP**：Micron Foundation Chair 為榮譽性冠名，非獨家顧問；與 TSMC JDP 不衝突（已有 TSMC PhD Scholarship 三屆佐證）；Lam Research 合作記錄為設備公司（非 IC 廠），無競業問題
  - **學生流向**：既有 TSMC PhD Scholarship × 3 屆為最強綁定工具；主要風險是學生畢業後被 Micron 挖角（美光 Chair 效應）；建議 TSMC 在 PhD 期間提前鎖定 return offer
  - **學界 vs 量產 SOP 落差**：FeFET CIM 架構需 TSMC N2 PIE 工程師協同校正熱預算與 CMP planarity；胡璧合本人已有 ISSCC/IEDM 技術委員資格，學界-工業界 bridge 能力強
  - **能力限制**：WebSearch 無法核實胡璧合是否有進行中 Micron 獨家技術授權；建議 TSMC Legal 接洽前確認 Micron Chair 協議條款範圍
- **連結**：[NTU EE 個人頁](https://www.ee.ntu.edu.tw/profile1.php?id=1080918) ｜ [個人網站](https://sites.google.com/site/vitapihohu) ｜ [IEEE INEC 2025](https://ieeeinec.org/keynotes/invited-speaker-vita-pi-ho-hu/) ｜ [IEEE CAS](https://ieee-cas.org/contact/vita-pi-ho-hu) ｜ [NTU L'ORÉAL Spotlight](https://www.ntu.edu.tw/english/spotlight/2023/2139_20230316.html) ｜ 代表論文：Nature Nanotechnology 2024；IEDM 2025 × 2；IEDM 2024 × 2

---

### S06. 陳冠能（Kuan-Neng Chen）｜總分 **8.8**（S 級）｜第一波

| 校系職級 | NYCU ICST 智能科學與技術研究院 Dean（2025/02-）+ 電子所講座 ｜ 講座教授 / 院長 ｜ PhD: MIT EECS |
|---|---|
| 學術指標 | IEEE/IET/IMAPS/NAI/CIEE 五重 Fellow；400+ 論文、87 專利 |
| Lab | 大型；IEDM/VLSI 年均 6+ 篇一作 |
| **5 維度評分** | 研究 9 ｜ fab 9 ｜ Lab 9 ｜ 接洽 9 ｜ 長期 8 ｜ 五重 Fellow + IEDM/VLSI 系統整合領袖 + 前 Micron Chair 已 2021 結束 |

**核心專長 × 近 3 年代表實績**
- Hybrid Bonding 混合鍵合（SoIC 核心）/ 3D IC 整合 / Layer Transfer 層轉移 / Hyper RDL 超細線距 RDL（CoWoS-L 下一代）
- IEDM 2024 × 2 篇 + VLSI 2024 × 2 篇（Hyper RDL interposer / 25×33mm² 3DIC）；400+ 論文、87 專利累積；NSTC 微電子學門召集人；2025/02 就任 NYCU ICST Dean
- 五重 Fellow（IEEE/IET/IMAPS/NAI/CIEE）；NSTC 微電子學門召集人；NYCU ICST Dean

**製程/封裝應用點（詳述）**

- **節點 / 段別**：後段封裝段（Advanced Packaging）；主攻 CoWoS-L（Hyper RDL 下一代）/ SoIC（Hybrid Bonding 核心）/ HBM3E 疊層對準；具體技術點：Cu-Cu Hybrid Bonding 接合界面工程、Layer Transfer 良率工程、Hyper RDL（< 2 µm pitch）互連可靠性、3D 熱管理（BSPDN thermal）
- **痛點對應**：
  - **SoIC Cu-Cu Hybrid Bonding 良率瓶頸**：pad pitch 縮至 < 3 µm 後，Cu dishing / surface roughness 對接合強度影響劇增；陳冠能 NYCU 3DIC Lab 的低溫 Cu-Cu Bonding（passivation metal 薄膜法，< 200°C 實現）可降低 Cu oxide 風險，直接提升良率
  - **Hyper RDL 互連可靠性（CoWoS-L 下一代）**：IEDM 2024 Hyper RDL interposer（25×33mm² 3DIC）一作研究顯示線距縮至 < 2 µm 後 EM（Electromigration）和 stress migration 成為可靠性主要殺手；陳冠能與 S08 陳智 nt-Cu 材料組合可形成「材料 + 封裝」雙軸解方
  - **Layer Transfer 在 SoIC 的良率損耗**：M3D 中的 Layer Transfer 步驟（bonding + thinning + TSV reveal）每一步都有 ~0.5-1% 良率損耗；3DIC Lab 的 Layer Transfer 方法論積累（400+ 論文、87 專利）可提供良率改善路徑
  - **BSPDN 熱管理（IITC 2025 新前線）**：3D IC 堆疊後因晶片間熱阻累積，BSPDN（Backside Power Delivery Network）架構的熱傳導瓶頸成為限制頻率的關鍵因素；陳冠能 IITC 2025 multi-level thermal simulation 框架直接對應此問題
- **可導入時程（TRL）**：**TRL 7-8（Hybrid Bonding / Layer Transfer）/ TRL 5-6（Hyper RDL + BSPDN 熱管理）/ 立即-6 個月啟動**；Hybrid Bonding 方法論已量產驗證級，BSPDN 熱管理模型屬 PoC 階段
- **配合 fab 部門**：SoIC / CoWoS 封裝整合研發為主對口；CoWoS-L Hyper RDL 製程工程（Interconnect Engineering）次對口；TSMC-NCTU JRC（既有框架）為跨組整合點
- **預期成效**：
  - SoIC Cu-Cu Hybrid Bonding 良率提升 ≥ 3%（對比現有量產 baseline）
  - Hyper RDL EM 壽命延長 ≥ 20%（低溫 passivation 金屬法 + nt-Cu 串接方案）
  - Layer Transfer 每步良率損耗降低至 < 0.3%（方法論移轉後目標）
  - BSPDN 熱阻預測誤差 < 5%（multi-level thermal simulation 驗證）

**合作紀錄 × 與外部公司狀況**
- NCTU-TSMC JRC 成員（長期）；ITRI Adjunct；前 Micron Chair Professor（2018-2021 已結束）
- 前 Micron Chair 已於 2021 結束，**現無獨家綁定**；NCTU-TSMC JRC 為既有合作框架

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — SoIC Hybrid Bonding 良率工程**：低溫 passivation 金屬法提升 CuCu 接合強度與良率；pad pitch 目標 < 3 µm，良率提升 ≥ 3%；接續 IEDM 2024 × 2 成果
  - **主題目 B — Hyper RDL 互連可靠性 + 熱管理**：CoWoS-L 下一代 Hyper RDL（< 2 µm pitch）EM / stress migration 可靠性 + BSPDN 熱阻優化（接續 IITC 2025 thermal framework）；（與 S08 陳智 nt-Cu 材料串題，封裝群 cross-ref）
  - **延伸題目 C — Layer Transfer 良率改善方法論**：M3D Layer Transfer（bonding + thinning + TSV reveal）每步良率損耗降低；87 件專利中涵蓋 Layer Transfer 多項 IP
  - **延伸題目 D — ICST 院級學生 Pipeline 建立**：透過 NYCU ICST Dean 職位，將院級資源（電子所 + 材料所 + CS 跨領域）導入 TSMC 封裝群人才管道（與 S08/S11/S12/S13 封裝群 cross-ref，建議 cluster 聯合 pipeline）
- **制度與簽約**
  - **架構**：NCTU-TSMC JRC 既有框架直接擴大範圍（無需新立 MOU）+ NYCU ICST 院級 Joint Lab；5 年期，配合 CoWoS-L Hyper RDL 商用化 timing（估 2027-2028）
  - **預算建議區間**：年 NT$ 4,000-6,000 萬，5 年滾動（推估區間，非承諾數字，依 NCTU-TSMC JRC 院級封裝合作歷史量級對標；院長職位帶動多方資源整合）
  - **簽約對象**：NYCU ICST（院級）+ 陳冠能 PI（個人委案）雙軌；IP 走 JRC 既有歸屬框架（87 件專利中的封裝方法論按既有授權模式處理）
  - **學生通道**：ICST 院級資源（電子所 + 材料所）；建議每年 5-8 名封裝方向暑期實習 + 2-3 名 TSMC PhD Scholarship
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：低溫 passivation 金屬法在 TSMC SoIC PoC 批次上接合強度達標（pull force ≥ X MPa，依 TSMC 內部 spec）；BSPDN thermal model 驗證誤差 < 10%（模擬 vs 量測）；至少 2 篇 IEDM/VLSI 聯名
  - **第 2 年**：SoIC 良率提升 ≥ 1.5%（量測 50 批次統計）；Hyper RDL EM 壽命初測達標（125°C / 10 mA 條件）；ICST 院級學生 pipeline 首批（3 名）暑期完成
  - **第 3 年**：良率提升穩定 ≥ 3%；Layer Transfer 方法論移轉文件完成；Hyper RDL 可靠性進入 CoWoS-L 製程認證
  - **Exit criteria**：第 1 年接合強度 < 80% 目標值 OR thermal model 誤差 > 20%，則重新評估材料 / 模型假設；第 2 年良率提升 < 0.5%，則縮減預算至延伸題目層級
- **執行對口與啟動條件**
  - **主對口**：TSMC SoIC / CoWoS 封裝整合研發
  - **次對口**：CoWoS-L Interconnect Engineering（Hyper RDL）；TSMC-NCTU JRC 計畫辦公室（既有對口）
  - **啟動條件**：JRC 既有框架確認擴大範圍 → ICST 院級 MOU 簽訂（利用既有 JRC 加速）→ 首批 PoC 試片排程
- **風險與緩解**
  - **競業 / IP**：前 Micron Chair（2018-2021 已結束）無現役綁定；87 件專利中部分可能有 JRC 共有，需法務確認歸屬；ITRI Adjunct 為名義性，無排他
  - **學生流向**：ICST 院長職位有助集中院級人才流向 TSMC；主要風險是學生被 Intel / Samsung 封裝廠挖角；PhD Scholarship 提前鎖定為主要緩解手段
  - **學界 vs 量產 SOP 落差**：陳冠能 400+ 論文 / 87 專利積累，且 NCTU-TSMC JRC 長期合作已形成制度化 SOP translation 機制；落差風險較低
  - **能力限制**：WebSearch 無法核實 NYCU 3DIC Lab 與其他封裝廠（ASE / Intel Foundry）是否有非公開 JDP；建議 TSMC Legal 確認無排他條款後啟動
- **連結**：[NYCU ICST](https://icst.nycu.edu.tw/) ｜ [NYCU 電子所](https://ieee.nycu.edu.tw/) ｜ [Google Scholar](https://scholar.google.com/citations?user=Wbe4-IUAAAAJ) ｜ 代表論文：IEDM 2024 Hyper RDL 25×33mm² 3DIC；IITC 2025 BSPDN Thermal Framework；VLSI 2024 × 2

---

### S07. 銀慶剛（Ching-Kang Ing）｜總分 **8.5**（S 級）｜第一波

| 校系職級 | NTHU 統計與資料科學研究所 清華講座教授 ｜ 清華講座教授 ｜ PhD: 待核實 |
|---|---|
| 學術指標 | 2025 IMS Fellow；JASA × 2 近兩年；h-17 |
| Lab | 統計頂刊深度研究型；中型 |
| **5 維度評分** | 研究 9 ｜ fab 9 ｜ Lab 8 ｜ 接洽 9 ｜ 長期 8 ｜ IMS Fellow + JASA 頂刊 + 方法論直接落地 fab + 無其他 Chair |

**核心專長 × 近 3 年代表實績**
- Time Series Knockoffs 時間序列變數選擇 / Model Selection 高維模型選擇 / 高維變數選擇方法論 / SPC / VM 統計基礎
- 2025 IMS Fellow；JASA 2024 / 2025 各一作共 2 篇；JCGS 2025 半導體缺陷機台應用（精準命中）；2024 教育部學術獎；2022 美國專利 US12354122B2（NCKU IYM 合作共同發明人）
- 2025 IMS Fellow；2024 教育部學術獎；US12354122B2（NCKU IYM 合作）

**製程/封裝應用點（詳述）**

- **節點 / 段別**：跨節點通用（N3/N2/A16 均適用）；製程段：前段 SPC（Statistical Process Control）+ 測試段 Virtual Metrology（VM）+ 後段 APC（Advanced Process Control）；核心應用點在高維製程參數選變數（variable selection）與機台異常早期識別
- **痛點對應**：
  - **N2/N3 高維 SPC 失效**：N2 製程監控參數超過數千維（各段疊加），傳統 PCA / T² 統計量在高維下「維度詛咒」嚴重，漏掉早期偏移信號；銀慶剛 JASA 2025 Time Series Knockoffs（TSK）方法論專門處理高維時間序列變數選擇，直接切入此痛點
  - **Virtual Metrology 輸入變數爆炸**：VM 模型（預測量測值的 proxy）面臨每台機台 50-200 個製程參數作為 input，傳統逐步回歸易過擬合；TSK 方法可做 FDR 控制下的穩健變數選擇，提升 VM 模型泛化能力（JCGS 2025 半導體缺陷機台應用為直接先例）
  - **機台異常識別（2014 TSMC × 高雄大學 降不良率 11-14%）**：已有實績佐證；N2 製程複雜度遠超 2014 年，同樣方法論在新節點的提升空間估計更大；US12354122B2（NCKU IYM 2022 共同發明）證明方法可工業化
  - **SPC 跨機台一致性**：多機台（multi-tool）環境下各台 drift 方向不同；TSK 的 knockoff filter 可識別「哪些製程參數在統計意義上真正影響良率」（區分因果 vs 相關），避免誤觸發 SPC alarm 導致無效停機
- **可導入時程（TRL）**：**TRL 6-7（VM 高維變數選擇）/ TRL 7（機台異常識別，有 2014 TSMC 先例）/ 立即-6 個月可啟動 PoC**；方法論已有頂刊驗證 + 美國專利 + TSMC 合作先例，主要工作是接入 N2 製程資料（需資料合作協議）
- **配合 fab 部門**：製程整合統計分析部門（Process Statistics / SPC team）為主對口；VM 系統 owner（APC Engineering）次對口；資料科學部門（Data Science / Digital Transformation）為跨組整合點
- **預期成效**：
  - N2 SPC 高維監控誤報率（false alarm rate）降低 ≥ 30%（TSK vs PCA baseline）
  - VM 模型預測 MAE 降低 ≥ 15%（高維變數選擇後 vs full-feature 模型）
  - 機台異常早期識別率（precision）≥ 90%（對比 2014 年 TSMC 合作 baseline）
  - 製程資料分析 TAT 縮短 ≥ 40%（自動化 knockoff filter 取代手動逐步回歸）

**合作紀錄 × 與外部公司狀況**
- 2014 TSMC × 高雄大學（不良率降 11-14%）；2022 NCKU IYM 合作（US12354122B2）
- US12354122B2 與 NCKU 共有（待 IP check）；無其他大廠 Chair 或獨董；**半導體合作紀錄實績豐厚**（TSMC 2014、NCKU IYM 2022）

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — N2 高維 SPC Time Series Knockoffs 導入**：以 JASA 2025 TSK 方法論取代現有 PCA / T² 監控體系，目標降低誤報率 ≥ 30%；直接接續 US12354122B2 工業化路徑（與 SPC 群 S10/S14/A19/A24 cross-ref，可作群組方法論核心）
  - **主題目 B — VM 高維變數選擇框架**：以 Knockoff filter 做 FDR 控制下 VM 輸入變數選擇，提升 VM 模型跨機台泛化能力；接續 JCGS 2025 半導體缺陷機台應用（精準命中）
  - **延伸題目 C — 機台異常識別更新版（N2）**：延伸 2014 TSMC × 高雄大學合作方法（不良率降 11-14%）至 N2 節點新製程；（SPC 群 cluster 整合題，建議作為群組 baseline 更新計畫）
  - **延伸題目 D — 高維 Model Selection 跨段 APC 整合**：將 TSK 方法論推廣至 APC（Advanced Process Control）跨段參數優化，形成 SPC-VM-APC 統一統計框架
- **制度與簽約**
  - **架構**：NSTC 產學合作計畫（伴投）+ TSMC 製程資料合作協議（NDA + Data Agreement）；3 年期，配合 N2 量產時程
  - **預算建議區間**：年 NT$ 800-1,500 萬，3 年滾動（推估區間，非承諾數字，依 NTHU 統計方法論 × 半導體廠同規模合作（如 NCKU IYM 模式）對標；統計方法論類合作預算通常低於元件/封裝類）
  - **簽約對象**：NTHU 研發處 + 銀慶剛 PI（委案）雙軌；US12354122B2 為 NCKU 共有（IP 需確認 NTHU 個人研究部分的歸屬框架，或採全新研究方向迴避）
  - **學生通道**：統計所中型實驗室；建議每年 1-2 名博士生參與 fab 資料實習（保密協議下 on-site 分析）
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：TSK 方法論在 N2 歷史製程資料（保密）上完成回測；誤報率降低 ≥ 15%（保守目標）；VM MAE 降低 ≥ 8%；至少 1 篇 JASA / IEEE TSemi 聯名投稿
  - **第 2 年**：TSK SPC 進入 N2 製程線 shadow mode（監控但不實際 trigger alarm，持續比較）；機台異常識別 precision ≥ 85%
  - **第 3 年**：TSK SPC 取代部分現有 PCA 監控體系（選定 3-5 個關鍵製程段）；誤報率降低 ≥ 30% 量產驗證；延伸 APC 整合啟動
  - **Exit criteria**：第 1 年回測誤報率降幅 < 5% 且 VM MAE 降幅 < 3%，則重新評估 N2 製程資料是否與 TSK 假設（stationarity / sparsity）不符 → 調整方法論後繼續
- **執行對口與啟動條件**
  - **主對口**：TSMC 製程整合統計分析 / SPC team
  - **次對口**：APC Engineering（VM 系統 owner）；資料科學部門（資料管道打通）
  - **啟動條件**：N2 製程資料 NDA + Data Agreement 簽訂（estimated 4-8 週）→ 歷史資料 extract → NTHU 統計所環境建置（計算資源確認）
- **風險與緩解**
  - **競業 / IP**：US12354122B2 為 NCKU × IYM 共有，銀慶剛本人為共同發明人；新合作應以全新研究框架（N2 TSK 方法論）為基礎，迴避 NCKU 共有 IP 範圍；建議 TSMC Legal 預先確認
  - **學生流向**：統計所學生多進入金融、科技業資料科學職位，非 fab 人才直接流向；合作主要價值在方法論輸出而非人才 pipeline
  - **學界 vs 量產 SOP 落差**：統計方法論落地需 fab 資料工程師協助打通製程資料管道（OPC / SPC 資料格式標準化）；此為最主要落差；建議 TSMC 資料科學部門配置 0.5 FTE 協作
  - **能力限制**：WebSearch 無法核實 JCGS 2025 論文的具體半導體廠資料來源，以及是否有進行中的保密合作；銀慶剛個人主頁未列 2025 以後論文詳情，需直接詢問
- **連結**：[個人網頁](http://mx.nthu.edu.tw/~cking/) ｜ [NTHU 統計所](https://stat.site.nthu.edu.tw/p/403-1327-406-1.php?Lang=en) ｜ [IMS Fellow 公告](https://science.site.nthu.edu.tw/p/406-1069-291413,r8875.php?Lang=en) ｜ [Google Scholar](https://scholar.google.com/citations?user=ySSGqMcAAAAJ) ｜ [US12354122B2](https://patents.google.com/patent/US12354122B2) ｜ 代表論文：JASA 2025 High-Dimensional Knockoffs Inference for Time Series Data；JCGS 2025 半導體缺陷機台應用

---

### S08. 陳智（Chih Chen）｜總分 **8.4**（S 級）｜第二波

| 校系職級 | NYCU 材料系 講座教授（Chair Professor, 2023/03-；前系主任 2017-2023）｜ 講座教授 ｜ PhD: UCLA 材料（King-Ning Tu 門下）|
|---|---|
| 學術指標 | h-56 / i10-201；Google Scholar 10,310 引用；Science 2012 nt-Cu 發現人 |
| Lab | 大型；多屆 TSMC / MediaTek 學生 |
| **5 維度評分** | 研究 9 ｜ fab 9 ｜ Lab 9 ｜ 接洽 7 ｜ 長期 8 ｜ Science + h-55 + 技轉量產級 + UCLA 學派正統 |

**核心專長 × 近 3 年代表實績**
- nt-Cu 奈米雙晶銅（Science 2012 發現）/ Hybrid Bonding 核心材料 / Electromigration 電遷移 / 銅表面改質
- Science 2012 (111) nt-Cu 發現（奠基性論文）；Materials Characterization 2025/05（Vol. 223, 114925）；Applied Surface Science 2025/03（Vol. 685, 162023）；Nano Letters 2025；ICEP-IAAC 2025 / EDTM 2025 國際封裝研討會貢獻
- 2023 NSTC 學術研究獎；Chemleader 2016 技轉量產；UCLA King-Ning Tu 學派正統傳承

**製程/封裝應用點（詳述）**

- **節點 / 段別**：後段封裝段（Advanced Packaging）；主攻 SoIC Cu-Cu Hybrid Bonding 核心材料 + CoWoS/HBM EM 可靠性；具體技術點：(111)-oriented nt-Cu（奈米雙晶銅）電鍍製程、Hybrid Bonding 低溫接合（< 200°C）、Cu-Cu 接合界面 electromigration（EM）長期可靠性、in-situ AFM 觀測
- **痛點對應**：
  - **SoIC Hybrid Bonding Cu-Cu 接合低溫化需求**：SoIC pad pitch 縮至 < 3 µm 後，高溫退火（> 300°C）導致 SiO₂ / low-k 介電層膨脹變形；陳智 nt-Cu（111 面優先取向）可在 200°C 實現高強度接合（ACS Nano 2025 in-situ 原子級觀測佐證），直接解決低溫化瓶頸
  - **EM 可靠性在超細線距 RDL / microbump**：CoWoS-L Hyper RDL（< 2 µm 線距）電流密度大幅提升（> 10⁶ A/cm²），EM 成為主要可靠性殺手；陳智 ACS Nano 2025（in-situ Cu-Cu joint EM at high current density）直接量測 EM 行為，可提供 TSMC EM fail model 校正數據
  - **Cu 表面氧化管控（Hybrid Bonding 良率殺手）**：Cu 在 fab 環境暴露後快速氧化，氧化層阻礙 CuCu 接合；nt-Cu（111）面氧化速率比多晶 Cu 低 30-50%（表面能效應）；Materials Characterization 2025 + Applied Surface Science 2025 兩篇確認陳智近期仍在深化此問題
  - **In-situ AFM 量測方法學（與 S04 串接）**：ScienceDirect 2025（in-situ AFM in downscaled nt-Cu/SiO₂ vias）顯示陳智具備 in-situ 即時量測能力，可與 S04 陳亮嘉 OCD 量測互補（材料機制 ↔ 光學量測雙向驗證）
- **可導入時程（TRL）**：**TRL 7-8（nt-Cu 電鍍製程 + Hybrid Bonding）/ TRL 6-7（EM 可靠性模型）/ 立即-6 個月啟動**；Chemleader 技轉量產（2016）證明 nt-Cu 已達 TRL 9（商業化）；再導入 TSMC SoIC 流程主要工作是 fab 製程整合（鍍浴參數 + CMP 對齊）
- **配合 fab 部門**：SoIC / CoWoS Hybrid Bonding 製程整合為主對口；可靠性工程（Reliability Engineering / EM 模型 owner）次對口；與 S06 陳冠能 3DIC Lab 的封裝整合工程師為跨組整合點
- **預期成效**：
  - SoIC Cu-Cu 接合溫度降至 ≤ 200°C（nt-Cu 製程，現有多晶 Cu 需 300-400°C）
  - Hybrid Bonding 接合良率提升 ≥ 2%（Cu 氧化率降低 30-50% 效應）
  - Hyper RDL EM 壽命延長 ≥ 25%（nt-Cu vs 多晶 Cu，高電流密度條件）
  - EM fail model 校正精度：MTTF 預測誤差 < 10%（in-situ AFM 量測數據回饋）

**合作紀錄 × 與外部公司狀況**
- TSMC（多年合作）、MediaTek、Applied Materials、Lam Research、SRC（Semiconductor Research Corp）3 年期計畫、Chemleader（nt-Cu 材料技轉）
- Chemleader 為材料技轉商（中性、非競業）；多方合作顯示**開放度高，無獨家排他**

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — SoIC nt-Cu Hybrid Bonding 低溫製程整合**：(111)-oriented nt-Cu 電鍍製程導入 SoIC Cu-Cu Hybrid Bonding，目標接合溫度 ≤ 200°C；接續 ACS Nano 2025 in-situ 量測成果（與 S06 陳冠能 Hybrid Bonding 良率工程串題，封裝群 cross-ref）
  - **主題目 B — Hyper RDL / microbump EM 可靠性模型**：以 in-situ AFM EM 量測建立 TSMC Hyper RDL 高電流密度 EM fail model，提供 EM design rule 校正數據；接續 ACS Nano 2025 Cu-Cu joint EM at high current density
  - **延伸題目 C — Cu 表面改質（抗氧化）製程標準化**：nt-Cu 表面抗氧化機制（(111) 面能效應）導入 TSMC Hybrid Bonding 前處理 SOP，降低良率損耗；（與 S06 陳冠能低溫 passivation 金屬法形成材料 + 封裝雙軸，封裝群 cluster cross-ref）
  - **延伸題目 D — In-situ AFM × OCD 量測互補驗證**：nt-Cu 材料機制（in-situ AFM）與 OCD 光學量測（S04 陳亮嘉 PMLab）的雙向驗證通道；材料真值 ↔ 非接觸量測交叉校正（封裝群 × 量測群跨 cluster）
- **制度與簽約**
  - **架構**：SoIC 材料 JDP（NYCU CCLAB × TSMC Hybrid Bonding 製程整合）+ in-situ AFM PoC 合作；3-5 年滾動，配合 CoWoS-L / SoIC 下一代導入 timing（2026-2028）
  - **預算建議區間**：年 NT$ 1,500-2,500 萬，3 年滾動（推估區間，非承諾數字，依 NYCU 材料 × TSMC 封裝 JDP 同規模（如 SRC 3 年期計畫規模）對標；含電鍍設備 + in-situ AFM 使用費 + 學生獎助 + 代工片）
  - **簽約對象**：NYCU 研發處（OTT）+ 陳智 PI（委案）雙軌；Chemleader 技轉為獨立商業協議（與 TSMC JDP 不衝突，Chemleader 為材料技轉商非 IC 廠）
  - **學生通道**：CCLAB 大型實驗室（多屆 TSMC / MediaTek 學生）；建議每年 2-3 名材料所博士生暑期進入 CoWoS 封裝廠 on-site 實習
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：nt-Cu 電鍍製程在 TSMC SoIC 試片上完成接合強度確認（200°C / pull force ≥ 目標 MPa）；EM 量測 setup 建立（in-situ AFM 進廠或數據傳輸協議確認）；至少 1 篇 ECTC / IEDM 聯名
  - **第 2 年**：Hybrid Bonding 良率提升 ≥ 1%（量測 30 批次 PoC）；EM fail model 初版校正完成（MTTF 誤差 < 20%）；Cu 抗氧化前處理 SOP 草案提交 Hybrid Bonding 製程組
  - **第 3 年**：nt-Cu Hybrid Bonding 進入 SoIC production 製程認證；EM model 誤差 < 10%；良率提升 ≥ 2% 量產驗證
  - **Exit criteria**：第 1 年 200°C 接合強度 < 80% 目標值，則重新調整 nt-Cu 鍍浴參數（3 個月窗口）後繼續；若連續 2 次調整後仍未達標則終止主題目 A，轉延伸題目 C/D
- **執行對口與啟動條件**
  - **主對口**：TSMC SoIC / CoWoS Hybrid Bonding 製程整合
  - **次對口**：Reliability Engineering（EM model owner）；S06 陳冠能 3DIC Lab 聯絡窗口（封裝群 cluster 協調）
  - **啟動條件**：NYCU CCLAB nt-Cu 電鍍配方 NDA 確認 → SoIC 試片 shuttle 排程（estimated 4-8 週）→ in-situ AFM 進廠許可或數據傳輸協議簽訂
- **風險與緩解**
  - **競業 / IP**：Chemleader 技轉協議為 nt-Cu 量產授權，需確認是否有排他條款限制 TSMC 直接使用相同技術；建議 TSMC Legal 先查 Chemleader 授權範圍；Applied Materials / Lam Research 合作為設備商（非競業）
  - **學生流向**：CCLAB 學生已有 TSMC / MediaTek 流向紀錄（高吻合度）；主要競才對象是 ASE 封裝廠與設備商；PhD Scholarship 優先鎖定材料整合方向
  - **學界 vs 量產 SOP 落差**：nt-Cu 電鍍製程從實驗室到 fab cleanroom 的鍍浴穩定性管控需 TSMC 製程工程師協同（電鍍均勻性 ± 5% 以內）；Chemleader 量產先例縮短了 SOP 轉換時間
  - **能力限制**：接洽度評分 7（略低）反映陳智行政負擔重（前系主任 2017-2023）；建議以書面合作邀請信 + TSMC 內部引薦（若有既有合作工程師）雙管齊下提升接觸成功率；WebSearch 無法核實現有 TSMC 合作細節與保密協議狀態
- **連結**：[CCLAB 個人頁](https://cclab.web.nycu.edu.tw/prof-chen/) ｜ [NYCU 材料系](https://mse.nycu.edu.tw/en/%E9%99%B3%E6%99%BA-2/) ｜ [NYCU Academic Hub](https://scholar.nycu.edu.tw/en/persons/chih-chen/) ｜ [Google Scholar](https://scholar.google.com/citations?user=6z6TgWUAAAAJ) ｜ [Publications](https://cclab.web.nycu.edu.tw/journalpublications/) ｜ 代表論文：ACS Nano 2025 In-situ EM in Cu-Cu Joints；Materials Characterization 2025（Vol. 223）；Applied Surface Science 2025（Vol. 685）；ScienceDirect 2025 in-situ AFM nt-Cu/SiO₂ vias

---

### S09. 詹寶珠（Pau-Choo Chung）｜總分 **8.3**（S 級）｜第二波

| 校系職級 | NCKU EE 特聘教授（電資院長 2021-2024 + Miin Wu School 院長 2021-2023 任期已結束）｜ 特聘教授（Distinguished Professor, 2005-）｜ PhD: Texas Tech University EE 1991 |
|---|---|
| 學術指標 | IEEE Fellow 2008；h-34；Scopus 4,876 引用；近年 ACC-GAN 系列 |
| Lab | 院級資源；中大型 |
| **5 維度評分** | 研究 9 ｜ fab 8 ｜ Lab 9 ｜ 接洽 9 ｜ 長期 8 ｜ IEEE Fellow + 院級資源 + 完全自由 |

**核心專長 × 近 3 年代表實績**
- Domain Adaptation 跨領域自適應 / GAN 生成對抗網路 / 醫學影像 DL（主要背景）/ 半導體 AOI 跨製程遷移（目標應用）
- IEEE Fellow 2008；ACC-GAN / A-ReSEUnet 2024；Knowledge-Based Systems 2024；電資學院院長 2021-2024（已卸任）；Miin Wu School of Computing 院長 2021-2023（已卸任）
- IEEE Fellow 2008；Taiwan AI CoE（TWAICOE）顧問委員；大型院級合作執行力

**製程/封裝應用點（詳述）**

- **節點 / 段別**：N3/N2 後段 AOI（Automated Optical Inspection）+ 中段 inline 外觀量測；重點在「跨製程 / 跨機台 Domain Adaptation」，即舊節點標記資料 → 新節點無標記資料的知識遷移
- **痛點對應**：
  - **AOI 跨節點訓練資料稀缺**：每推一代新製程（N5→N3→N2），缺陷外觀形態改變，舊標記資料直接用在新節點模型精度驟降；重標記成本動輒數百萬 + 數月時程 → 詹寶珠 ACC-GAN / A-ReSEUnet 系列的 Domain Adaptation 可將舊節點標記映射至新節點，大幅減少重標記工時
  - **GAN 合成缺陷資料增強**：後段 AOI 中，某類稀有缺陷（如微橋、空洞）正樣本極少，模型召回率低；GAN 生成合成缺陷圖像補足少量正樣本，呼應其 ACC-GAN 系列核心方法
  - **跨機台泛化**：同廠不同品牌 AOI 機台（KLA、Lasertec、Camtek）影像風格差異導致模型需重訓；DA 方法可降低跨機台 retraining 成本
  - **能力限制 PoC 必要性**：詹寶珠無半導體 domain 先例（醫療 DL 為主），方法論可遷移但 fab 製程語境需 TSMC AOI 工程師引導；必須先做 PoC 驗證方法在實際 fab 資料上的精度，再決定是否轉入量產 SOP
- **可導入時程（TRL）**：**TRL 4-5 / 6-12 個月 PoC** — 核心 DA 演算法已有學術驗證（ACC-GAN, A-ReSEUnet 2024），但半導體製程資料適配性未測；PoC 階段用 TSMC 去識別化 AOI 圖像驗收後視精度決定是否進入 TRL 6-7（量產導入試驗）
- **配合 fab 部門**：後段 AOI 工程（Defect Inspection Eng.）為主對口；製程整合（PIE）提供節點規格 + 標記資料；與 B35 陳以錚、B39 連震杰、B42 黃乾怡（AOI 群）協作，可共用資料標記 pipeline 降低前置成本（cross-ref: B35/B39/B42）
- **預期成效**：
  - 跨節點 AOI 重標記工時降低 40-60%（PoC 目標）
  - 新製程首次建模 recall rate ≥ 85%（vs 現行冷啟動 60-70%）
  - GAN 合成稀有缺陷讓少樣本模型 F1 提升 ≥ 0.1
  - 跨機台 domain gap 縮小至精度差距 ≤ 5%

**合作紀錄 × 與外部公司狀況**
- 無半導體廠綁定（零 domain 先例）；過往合作以醫療 DL 為主
- **無公開可見外部綁定**；醫療 DL 背景，無半導體廠經歷

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — AOI 跨節點 Domain Adaptation PoC**：以 ACC-GAN / A-ReSEUnet 為核心，將 N5 AOI 標記資料映射至 N3/N2 節點，驗證跨節點精度保留率；PoC 資料由 TSMC 提供去識別化後段 wafer 影像
  - **主題目 B — GAN 稀有缺陷合成增強**：針對後段 AOI 少樣本缺陷類別（微橋、空洞、顆粒），以 ACC-GAN 生成合成正樣本補足訓練集，提升召回率
  - **延伸題目 C — 跨機台泛化模型**：延伸 DA 框架處理 KLA vs Camtek 機台影像風格差異，探索 style transfer-based 統一特徵空間（可與 B39 連震杰 AOI 群協作，cross-ref: B39）
  - **延伸題目 D — 醫療 ↔ 半導體遷移基準測試**：建立跨域 DA 方法論 benchmark（醫療組織切片 vs fab wafer 影像），作為方法論論文 + TSMC 內部白皮書雙用途
- **制度與簽約**
  - **架構**：第 1 年 PoC 合約（獨立短期）；PoC 達標後轉 3 年 JDP；PoC 失利則僅交付方法論白皮書，無繼續義務
  - **預算建議區間**：PoC 年 NT$ 600-900 萬（推估區間，非承諾數字，依 NCKU 院級短期技術合作對標）；JDP 轉入後年 NT$ 1,500-2,500 萬（含學生獎助、GPU 資源、標記工具授權）
  - **簽約對象**：NCKU 電機系（院級支援）+ 詹寶珠 PI（個人委案）；PoC IP 歸 TSMC 所有，論文共著由 PI 協商
  - **學生通道**：NCKU-TSMC 既有招募通道；PoC 期可安排 1-2 名碩士生駐廠標記資料（降低前期成本）
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年（PoC）**：跨節點 DA 模型在 TSMC 去識別化資料上 recall ≥ 80%；GAN 合成缺陷通過 TSMC AOI 工程師視覺驗收（30 人次盲測 F1 ≥ 0.75）；至少 1 篇聯名 IEEE 期刊投出
  - **第 2 年（JDP 初期）**：DA pipeline 導入 N3 AOI 試驗機台；跨機台精度差距 ≤ 5%；聯名論文 1 篇發表
  - **第 3 年（JDP 深化）**：N2 節點冷啟動建模時間從 6 個月壓縮至 2 個月；與 AOI 群（B35/B39/B42）形成資料標記共池機制
  - **Exit criteria**：PoC 結束時 recall < 70% 且 PI 無明確改進路線，終止 JDP 轉換，僅保留方法論白皮書交付
- **執行對口與啟動條件**
  - **主對口**：後段 AOI 工程（Defect Inspection Eng.）
  - **次對口**：PIE 製程整合（資料提供）+ 品質工程（QE）+ AOI 群 B35/B39/B42 PI 協調
  - **啟動條件**：TSMC 去識別化 AOI 資料集準備（500 張以上 / 節點）+ NDA 簽署 + PoC 合約 Q2 啟動；建議詹寶珠先訪廠一次（由台灣 AI CoE 引薦通道）
- **風險與緩解**
  - **競業 / IP**：詹寶珠無半導體廠綁定，無競業風險；IP 框架建議 PoC 期 TSMC 持有全部 fab 應用 IP，學術方法論留 PI 發表
  - **學生流向**：院長卸任後 Lab 規模可能縮小，建議每年確認學生數量；若縮減則補入 B35/B39 AOI 群聯合指導機制
  - **學界 vs 量產 SOP 落差**：詹寶珠無 fab 實戰經歷，DA 模型在量產資料噪音、機台漂移下可能退化；PoC 期必須用真實量產資料（非 benchmark）驗收，避免學術精度虛高
  - **能力限制**：無半導體 domain 先例，跨域遷移是否 work 需 PoC 實驗驗證；WebSearch 亦無法查到詹寶珠與半導體廠公開合作記錄，此限制已明確揭示
- **連結**：[NCKU 電機系](https://www.ee.ncku.edu.tw/en/teacher/index2.php?teacher_id=78) ｜ [Google Scholar](https://scholar.google.com.tw/citations?user=RqfodmYAAAAJ) ｜ [TWAICOE](https://www.twaicoe.org/pau-choo-chung) ｜ [IIPP Mentor](https://iipp.tw/mentor/34) ｜ 代表論文：ACC-GAN 2024 / A-ReSEUnet 2024（Knowledge-Based Systems）

---

### S10. 謝昱銘（Yu-Ming Hsieh）｜總分 **8.3**（S 級）｜第一波

| 校系職級 | NCKU 半導體封測學位學程（PSPT）助理教授 ｜ 助理教授 ｜ PhD: NCKU IMIS（鄭芳田門下）|
|---|---|
| 學術指標 | h-11；452 引用（Scopus）；IEEE RA-L/TASE 一作多篇（2019-2024）|
| Lab | 推估 5-10 人（助理教授新銳階段）|
| **5 維度評分** | 研究 9 ｜ fab 9 ｜ Lab 7 ｜ 接洽 9 ｜ 長期 9 ｜ IEEE 一作 6 篇 + 直接命中 fab + 鄭芳田接班人 |

**核心專長 × 近 3 年代表實績**
- CNN-AVM（Virtual Metrology via CNN）/ Concept Drift VM 概念漂移處理 / Golden Path KSA（Key Step Analysis）/ Transfer Learning for fab
- 2021-2024 IEEE RA-L / TASE 一作 6 篇（鄭芳田共同通訊）；論文題目精準命中 fab 痛點（VM drift, CP 時序, KSA root cause）；IYM 系統第一順位接班人（鄭芳田師承繼承）
- IEEE RA-L / TASE 一作 6 篇；US11921474B2 美國專利

**製程/封裝應用點（詳述）**

- **節點 / 段別**：N3/N2/A16 前段製程 VM（Virtual Metrology）/ SPC 統計製程管制 / CP（Critical Parameter）時序管理；涵蓋薄膜沉積（CVD）、蝕刻（Etch）、CMP 多站段
- **痛點對應**：
  - **VM Concept Drift**：製程機台老化、PM（預防性維護）後參數偏移導致 VM 模型精度漸降；謝昱銘的 Concept Drift VM 框架（TASE 2022-2024）可即時偵測 drift 並自適應更新模型，避免 VM 誤判累積至實際量測站才被發現
  - **CP 多變量時序**：Advanced node 的 Critical Parameter 之間存在跨站時序相關（前站 CP → 後站 yield impact）；謝昱銘的多變量時序分析方法可建立跨站 CP 預測模型，提前 2-3 站預警 yield risk
  - **KSA Root Cause 定位**：當 OOC（Out-of-Control）訊號觸發時，傳統 SPC 僅能告警，無法定位 key step；謝昱銘的 Golden Path KSA 分析（一作論文）可用 ML 自動縮窄 root cause 至 key process step，壓縮工程師排查時間
  - **Transfer Learning 跨機台部署**：同一製程步驟的不同機台（tool-to-tool variation），原本需各自訓練模型；Transfer Learning 框架可從 master tool 遷移至 slave tool，節省標記資料 + retraining 時間（呼應其 IEEE RA-L 2024 TL-VM 論文）
- **可導入時程（TRL）**：**TRL 6-7 / 立即至 6 個月** — 謝昱銘的 VM / KSA 系列已在 NCKU iMRC 與鄭芳田（A24）既有 IYM 系統環境下驗證（TRL 5-6）；透過鄭芳田接班通道，可快速接入 TSMC IYM 現有平台，達 TRL 7 試產驗證
- **配合 fab 部門**：製程技術（Process Integration / PE）+ 製造技術（TSMC AMEM）為主對口；VM/SPC 系統維護部門（TSMC iMRC 對口）為次對口；與 S07 銀慶剛（高維 SPC 方法論）/ A19 / A24 / A16 / B37 / B45（SPC 群）形成資料 + 方法論共池（cross-ref: S07/A24）
- **預期成效**：
  - VM MAPE（Mean Absolute Percentage Error）相較靜態模型降低 20-30%（Concept Drift 修正效益）
  - CP OOC 後 root cause 定位時間從平均 2-4 小時壓縮至 < 30 分鐘（KSA 自動化）
  - 跨機台 VM 模型重訓成本降低 50-60%（Transfer Learning 框架）
  - IYM 系統覆蓋站數在現有基礎上擴展 30%（謝昱銘接班後新製程段涵蓋）

**合作紀錄 × 與外部公司狀況**
- 透過 iMRC 與 TSMC 既有關係（鄭芳田師承弱繼承）；尚無獨立廠商合作（年資短）
- **無公開可見外部綁定**；透過鄭芳田教授弱繼承與 TSMC 長期關係

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — VM Concept Drift 自適應框架**：將謝昱銘 TASE 2022-2024 系列的 Concept Drift VM 模型導入 TSMC N3/N2 CVD/Etch 站段，建立 IYM 系統內的自適應更新機制
  - **主題目 B — KSA Root Cause 自動定位**：延伸 Golden Path KSA 分析至 TSMC 多站 SPC 警報系統，建立 OOC 後 ML 自動 root cause ranking 模組
  - **延伸題目 C — Cross-tool Transfer Learning VM**：建立跨機台 VM 遷移框架（master→slave tool），涵蓋 Etch / CMP 等 tool-to-tool variation 嚴重段（可與 A24 鄭芳田 IYM 平台串聯，cross-ref: A24）
  - **延伸題目 D — CP 跨站多變量時序預警**：以 CP 時序模型提前 2-3 站預警 yield risk，整合至 TSMC 現有 e-Diagnostics 或 FDC 系統
- **制度與簽約**
  - **架構**：「師徒包」— 鄭芳田（A24）顧問費作框架背書 + 謝昱銘為執行 PI；可單立謝昱銘委案或掛靠 NCKU iMRC 機構；建議雙軌（短期確保知識傳承延續性）
  - **預算建議區間**：謝昱銘執行 PI 年 NT$ 800-1,500 萬；鄭芳田顧問 NT$ 100-200 萬/年（推估區間，非承諾數字，依 NCKU iMRC 既有 VM 合作量級對標）
  - **簽約對象**：NCKU AIS2M 學位學程（機構）+ 謝昱銘（個人 PI 委案）；IP 依 iMRC 既有歸屬框架（US11921474B2 先例已有）
  - **學生通道**：NCKU-TSMC 既有招募通道；博士生可申請 TSMC 台積獎學金 + 廠內實習
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：VM Concept Drift 框架在 TSMC N3 CVD 站段 shadow mode 測試；MAPE vs 靜態 baseline 降幅 ≥ 10%；與 TSMC 工程師聯名 IEEE RA-L / TASE 投稿 1 篇
  - **第 2 年**：框架升至 advisory mode（工程師輔助決策）；KSA root cause 模組通過 A/B 測試（工程師採納率 ≥ 70%）；專利申請 1 件
  - **第 3 年**：VM+KSA 系統接入 IYM 正式平台；覆蓋站數 +30%；跨機台 TL 框架完成 3 個機台組的驗收
  - **Exit criteria**：第 1 年末 MAPE 降幅 < 5% 且無改進路線，終止主題目 A；若師徒包鄭芳田無法持續顧問，需評估謝昱銘獨立執行能力再決定是否續約
- **執行對口與啟動條件**
  - **主對口**：TSMC AMEM（先進製造設備技術）/ iMRC 系統對口工程師
  - **次對口**：製程整合（PE）/ SPC 系統 owner + A24 鄭芳田顧問框架協調
  - **啟動條件**：iMRC 既有合作 MOU 延伸確認 + 鄭芳田（A24）顧問同意書 + Q1 三方 kick-off（謝昱銘 / 鄭芳田 / TSMC AMEM）
- **風險與緩解**
  - **競業 / IP**：謝昱銘無獨立大廠綁定；US11921474B2 專利在 NCKU/鄭芳田體系，需確認 sub-license 條款不影響 TSMC 使用
  - **學生流向**：助理教授新銳，Lab 規模 5-10 人，學生數量有限；師徒包模式可共用鄭芳田 Lab 學生彌補人力
  - **學界 vs 量產 SOP 落差**：謝昱銘與 iMRC 接觸密切，落差相對小；但年資短（助理教授），獨立執行大型 fab 計畫能力尚待評估，師徒包模式為關鍵緩解機制
  - **能力限制**：WebSearch 無法驗證謝昱銘獨立主持的廠內合作紀錄（目前記錄均為鄭芳田共同通訊）；建議 kick-off 前確認其獨立洽談能力
- **連結**：[NCKU researchoutput](https://researchoutput.ncku.edu.tw/en/persons/yu-ming-hsieh) ｜ [ORCID](https://orcid.org/0000-0002-3037-0104) ｜ [USPTO US11921474B2](https://patents.google.com/patent/US11921474) ｜ [IEEE RA-L CNN-AVM](https://researchoutput.ncku.edu.tw/zh/publications/convolutional-neural-networks-for-automatic-virtual-metrology) ｜ 代表論文：IEEE RA-L / TASE 2021-2024 系列（VM / Concept Drift / KSA）

---

### S11. 楊哲化（Che-Hua Yang）｜總分 **8.1**（S 級）｜第一波

| 校系職級 | NTUT 製造科技研究所 教授（兼任機械工程系）｜ 教授 ｜ PhD: Johns Hopkins University 機械 |
|---|---|
| 學術指標 | h-25 / 2,215 引用；論文 128 期刊 + 31 會議 |
| Lab | LUT Lab 4 間研究室；推估 10-15 人 |
| **5 維度評分** | 研究 8 ｜ fab 9 ｜ Lab 8 ｜ 接洽 9 ｜ 長期 8 ｜ h-25 + 20+ 年軌跡 + NDT 工業應用級 + 3D 封裝檢測剛需 |

**核心專長 × 近 3 年代表實績**
- 雷射超音波（Laser Ultrasonic）/ 導波工程（Guided Wave）/ 壓電技術（Piezoelectric）/ 3D 封裝內部隱裂非破壞檢測（NDT）
- T-SAFT 2023（Time-Domain Synthetic Aperture Focusing Technique）雷射超音波 subsurface defects imaging；2024 導波分析論文；h-25 / 2,215 引用累計；4 間專屬研究室（LUT Lab 規模完整）
- LUT Lab 4 間研究室規模；128 期刊 + 31 會議論文累積

**製程/封裝應用點（詳述）**

- **節點 / 段別**：後段封裝（Advanced Packaging）— CoWoS / SoIC / InFO 3D 積層封裝；重點段別為「封裝後內部檢測（Post-bond inspection）」與「封裝過程中 inline NDT」；節點無關（N3/N2 皆適用，瓶頸在封裝結構複雜度而非前段節點）
- **痛點對應**：
  - **CoWoS / SoIC 內部隱裂不可見**：3D 封裝 bump / micro-bump / TSV 區域在 X-ray 或傳統光學 AOI 下難以偵測 subsurface crack（特別是 Cu-Cu bonding 界面）；楊哲化的雷射超音波 T-SAFT（Time-Domain SAFT）可非接觸式穿透封裝體做 subsurface defect imaging，填補 X-ray / C-SAM 的盲區
  - **封裝 inline 速度瓶頸**：現行 C-SAM（超音波掃描顯微鏡）需接觸式探頭 + 耦合介質，inline 速度慢（30-60 min/wafer）；雷射超音波為非接觸式，潛力提升至 5-10 min/wafer（需 PoC 確認）
  - **異質整合新材料**：CoWoS 採用 underfill、PCB-level die-to-die interconnect 的界面層在不同材料間聲速差異大，傳統 NDT 難以校準；楊哲化導波工程（Guided Wave）方法可對多材料層界面做頻率掃描，自動辨識異常反射
  - **良率預測前置**：隱裂往往在溫度循環老化測試後才顯現（HTOL / TCT）；若能在封裝剛完成時做 NDT，可前置篩選高風險單元，避免老化測試後報廢的時程浪費（與 S12 江國寧 FEA 疲勞預測形成互補，cross-ref: S12）
- **可導入時程（TRL）**：**TRL 5-6 / 6-12 個月 PoC** — T-SAFT 系統已在 NTUT LUT Lab 學術驗證（128 期刊論文 + 工業 NDT 應用），能源 / 航太 NDT TRL 8-9；半導體封裝適配性（thin die / underfill / micro-bump 尺寸）需 PoC；預計 6-12 個月驗收後可升至 TRL 7
- **配合 fab 部門**：先進封裝工程（CoWoS / InFO 封裝 PIE）為主對口；製造品質（MQ）/ 良率提升中心（YEC）為次對口；與 S06/S08/S12/S13（封裝群）協作共用封裝樣品測試資源（cross-ref: S12 江國寧疲勞壽命 FEA + S13 宋振銘 bonding 改質）
- **預期成效**：
  - CoWoS / SoIC 封裝後內部缺陷檢出率提升至 ≥ 90%（vs 現行 C-SAM 70-75%）
  - Inline NDT 速度提升：接觸式 30-60 min → 非接觸式目標 10-15 min / wafer（PoC 驗收）
  - 封裝良率提升 0.5-1%（提前篩除隱裂高風險批次）
  - 形成「NDT 隱裂偵測 × FEA 疲勞壽命預測」聯合封裝質量保證平台（與 S12 串接）

**合作紀錄 × 與外部公司狀況**
- 無已知半導體廠合作（待查 NSTC 技轉庫）；過往以能源 / 航太 NDT 應用為主
- **無公開可見外部綁定**；無獨家顧問、無 Chair、無 Director 職

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — CoWoS / SoIC 雷射超音波隱裂 PoC**：以 T-SAFT 系統對 TSMC 提供的 CoWoS 封裝樣品（含已知隱裂 / 正常組）做 subsurface defect imaging，驗收檢出率 ≥ 90%
  - **主題目 B — 非接觸式 Inline NDT 速度優化**：研究雷射超音波掃描速度提升方案（多點陣列 / 並行掃描 / AI 輔助圖像重建），目標達 PoC inline 量產 throughput 需求
  - **延伸題目 C — 多材料界面導波校準**：開發針對 CoWoS underfill + RDL + micro-bump 多層材料的導波頻率校準方法，擴展適用材料範圍（可與 S13 宋振銘 Cu-Cu bonding 材料改質協作，cross-ref: S13）
  - **延伸題目 D — NDT 隱裂早篩 × FEA 壽命預測聯合平台**：將 NDT 檢出的初期隱裂形態輸入 S12 江國寧的 FEA 疲勞模型，預測剩餘壽命（cross-ref: S12）
- **制度與簽約**
  - **架構**：第 1 年 PoC 合約（3-6 個月）；PoC 達標後轉 3-5 年技術合作 JDP；封裝樣品由 TSMC 提供，設備由楊哲化 LUT Lab 出
  - **預算建議區間**：PoC 年 NT$ 500-800 萬（推估區間，非承諾數字，依 NTUT NDT 產學合作規模對標）；JDP 轉入後年 NT$ 2,000-3,000 萬（含設備升級 + 學生獎助 + 系統整合）
  - **簽約對象**：NTUT 製造科技研究所（機構）+ 楊哲化 PI（個人委案）；NDT 系統技術 IP 歸屬依雙方貢獻比協商，建議 TSMC 持有封裝應用 IP、PI 保留學術發表權
  - **學生通道**：NTUT 碩博士生可申請 TSMC 封裝廠實習；LUT Lab 4 間研究室學生資源充足
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年（PoC）**：T-SAFT 系統在 CoWoS 樣品上 subsurface crack 檢出率 ≥ 85%（盲測，與 C-SAM baseline 對比）；非接觸掃描速度達 < 20 min/wafer
  - **第 2 年（JDP 初期）**：inline 試驗機台整合；檢出率 ≥ 90%；掃描速度 < 15 min/wafer；至少 1 篇聯名 IEEE CPMT / JEP 論文
  - **第 3 年（JDP 深化）**：多材料導波校準方法完成 3 種材料組合驗收；NDT × FEA 聯合平台 PoC（與 S12）；良率提升效益量化報告
  - **Exit criteria**：PoC 結束時檢出率 < 75% 且無明確技術改進方向，終止 JDP 轉換；速度 > 30 min/wafer 且無改進路線，亦終止
- **執行對口與啟動條件**
  - **主對口**：先進封裝工程（CoWoS / SoIC PIE）
  - **次對口**：製造品質 MQ / 良率提升中心 YEC + S12 江國寧協調（封裝群）
  - **啟動條件**：CoWoS 封裝樣品（已知缺陷 / 正常組各 ≥ 20 片）準備 + NDA 簽署 + LUT Lab 訪廠確認機台尺寸適配性（NTUT → TSMC 封裝廠）
- **風險與緩解**
  - **競業 / IP**：楊哲化無半導體廠競業綁定；NDT 方法論為公開學術，IP 風險主要在系統化 SOP 專利，建議 PoC 期即申請聯名專利保護
  - **學生流向**：NTUT 學生轉業界比例高，LUT Lab 不缺來源；但封裝 NDT 技術積累慢，建議指定 2-3 名博士生為核心長期培養
  - **學界 vs 量產 SOP 落差**：楊哲化的 NDT 應用以能源 / 航太為主，半導體封裝的 die 薄度（< 100 µm）和 underfill 材質與傳統工業 NDT 差異顯著；需 PoC 期工程師陪同校準，不可跳過
  - **能力限制**：無半導體廠合作先例（NSTC 技轉庫待查），半導體封裝 NDT 適配性為主要未知數；PoC 是必要前置，WebSearch 亦無法確認楊哲化現有量產驗證記錄
- **連結**：[NTUT 機械](https://me1.ntut.edu.tw/p/405-1062-84647,c13043.php?Lang=zh-tw) ｜ [Elsevier Pure](https://ntut.elsevierpure.com/zh/persons/che-hua-yang) ｜ [ResearchGate](https://www.researchgate.net/profile/Che-Hua-Yang) ｜ [學術資源網](https://ar.ntut.edu.tw/professor/%E6%A5%8A%E5%93%B2%E5%8C%96/1405) ｜ 代表論文：T-SAFT 雷射超音波 subsurface defect imaging 2023

---

### S12. 江國寧（Kuo-Ning Chiang）｜總分 **8.1**（S 級）｜第二波

| 校系職級 | NTHU PME 動力機械工程學系 清華講座 ｜ 清華講座教授（NTHU Chair Professor）｜ PhD: Georgia Institute of Technology 機械工程 1989 |
|---|---|
| 學術指標 | iMAPS Fellow（2019）；ASME EPPD Excellence；350+ 論文、43 國際專利；NSTC Merit Research Fellow 2023 |
| Lab | CSML 實驗室 + APRC 中心級資源 |
| **5 維度評分** | 研究 9 ｜ fab 9 ｜ Lab 9 ｜ 接洽 10 ｜ 長期 7 ｜ iMAPS Fellow + ASME 獎 + AI×封裝方法論第一人 + 完全自由 PI |

**核心專長 × 近 3 年代表實績**
- AI × FEA（Finite Element Analysis）/ 封裝疲勞壽命 ML 預測 / WLP（Wafer Level Package）ML 預測 / CoWoS 翹曲 / HBM 疲勞預測
- ASME EPPD Excellence in Mechanics Award 2021；iMAPS Fellow；Scientific Reports 2022 3D IC DL；Materials 2024 solder joint fatigue ML；350+ 論文 + 43 國際專利累積
- iMAPS Fellow（2019）；ASME EPPD Excellence；NSTC Merit Research Fellow 2023

**製程/封裝應用點（詳述）**

- **節點 / 段別**：後段封裝（Advanced Packaging）— CoWoS-S / CoWoS-R / SoIC / HBM 堆疊封裝；重點段別為「封裝可靠度驗證（Reliability）」與「封裝結構設計優化（Package Design）」；節點無關，適用 N5 至 N2（瓶頸在封裝複雜度）
- **痛點對應**：
  - **CoWoS 翹曲（Warpage）預測**：CoWoS-R / CoWoS-S 在大面積 substrate 上因材料 CTE 不匹配，翹曲量超標導致 die bonding 失敗；傳統 FEA 全模型模擬需 24-72 hr / case，無法支援大量設計迭代；江國寧的 ML 代理模型（FEA surrogate）可在 < 1 min 內預測翹曲量，加速 10-100 倍設計迭代
  - **HBM 疲勞壽命不足**：HBM stack 在溫度循環下 micro-bump solder joint 疲勞裂紋擴展，壽命不達規格（≥ 1000 cycles TCT）；江國寧的 AI-FEA 疲勞壽命預測模型可在設計階段即評估不同 bump pitch / underfill 方案的壽命，減少反覆實物測試成本
  - **WLP 製程窗口（Process Window）縮窄**：Wafer Level Package 的 RDL（Redistribution Layer）設計在 A16 節點以下 pitch 縮小，製程窗口收窄；ML 模型可輔助工程師快速評估 RDL 設計對翹曲 / 熱阻的影響
  - **設計 ↔ 製造 SOP 橋接**：封裝設計部門（Package Design）與封裝製程工程師（PIE）之間的 FEA 模型設定常不一致（材料參數 / BC 設定差異），導致設計端 simulation 結果與量產不符；江國寧作為 AI × FEA 方法論第一人，具備建立統一封裝模擬 SOP 的能力
- **可導入時程（TRL）**：**TRL 6-7 / 立即至 6 個月** — 江國寧的 ML 代理模型已有 Scientific Reports 2022、Materials 2024 等多篇 peer-reviewed 驗證（學術 TRL 5-6）；CSML 中心具備 FEA 工具鏈，快速接入 TSMC 材料參數即可啟動 TRL 7 試驗；完全自由 PI 無綁定問題，立即可簽約
- **配合 fab 部門**：封裝整合工程（Package Integration Eng. / PIE CoWoS）為主對口；封裝可靠度部門（Package Reliability）/ 封裝設計部門為次對口；與 S06/S08/S11/S13（封裝群）協作（S11 NDT 檢測 + S13 bonding 材料改質 + S12 FEA 壽命預測，形成完整封裝可靠度三角，cross-ref: S11/S13）
- **預期成效**：
  - CoWoS 翹曲預測迭代速度從 24-72 hr / case → < 1 min（ML 代理模型，100x 加速）
  - HBM 疲勞壽命評估從實物測試（3-6 個月）縮短至設計階段預測（1-2 週）
  - 封裝可靠度設計迭代次數在 TCT 前減少 30-50%（提前淘汰不合規設計方案）
  - 建立 TSMC × NTHU CSML 統一封裝 FEA SOP，消除設計 ↔ PIE 模擬不一致問題

**合作紀錄 × 與外部公司狀況**
- 無 TSMC JDP（**完全自由 PI**）；ASME / iMAPS 頂會體系
- **完全無任何外部綁定** — first mover 窗口

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — CoWoS 翹曲 ML 代理模型**：以 NTHU CSML 的 FEA surrogate 框架，導入 TSMC CoWoS-S / CoWoS-R 材料參數，建立翹曲量快速預測模型；目標支援 Package Design 部門的設計迭代加速
  - **主題目 B — HBM micro-bump 疲勞壽命 AI 預測**：開發 TCT 疲勞模型（AI-FEA 聯合），針對不同 bump pitch / underfill 配方預測壽命，支援 HBM 封裝規格選定
  - **延伸題目 C — WLP / InFO RDL 製程窗口 ML 評估**：延伸 ML 模型至 WLP / InFO RDL 設計，評估細 pitch 下翹曲 / 熱阻 trade-off（可與封裝群 S06/S08 協作，cross-ref: S06/S08）
  - **延伸題目 D — NDT 隱裂 × FEA 壽命聯合平台**：整合 S11 楊哲化 NDT 檢出的隱裂形態輸入 FEA 疲勞模型，預測剩餘壽命（cross-ref: S11）
- **制度與簽約**
  - **架構**：NTHU CSML 中心級 Joint Lab + 冠名年度獎（「TSMC Advanced Packaging AI Award」）；5 年期中長程；建議首年直接 Joint Lab，無需 PoC 過渡（TRL 已夠高）
  - **預算建議區間**：年 NT$ 3,000-5,000 萬（推估區間，非承諾數字，依 NTHU 中心級 Joint Lab 及 CSML 規模對標）；含 CSML 設備（FEA license / GPU cluster）+ 學生獎助 + 冠名獎
  - **簽約對象**：NTHU PME / CSML 中心（機構）+ 江國寧 PI（個人委案）；IP 依 NTHU 技轉辦歸屬框架，TSMC 持有封裝應用 IP，學術方法論 PI 保留
  - **學生通道**：CSML 中型以上 Lab；博士生可申請 TSMC 台積獎學金 + 封裝廠實習；冠名年度獎可作業界招募槓桿
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：CoWoS-S 翹曲 ML 代理模型建立，在 TSMC 提供的 20 個設計 case 上預測誤差 ≤ 10%；HBM 疲勞模型完成初步 baseline 訓練；至少 1 篇聯名 IEEE CPMT 期刊投出
  - **第 2 年**：代理模型導入 Package Design 部門 design-in-loop；翹曲預測加速驗收（design iteration cycle ≤ 1 week from 4 weeks）；HBM 模型達 3-sigma 壽命預測準確度
  - **第 3 年**：CoWoS-R 延伸；WLP/InFO 模型涵蓋；NDT × FEA 聯合平台 PoC 完成（與 S11）；NTHU CSML 冠名年度獎首屆頒發
  - **Exit criteria**：第 1 年末翹曲預測誤差 > 20%（vs 全模型 FEA 驗證），且 PI 無改進路線，降回題目規模；HBM 模型若無法涵蓋主要 underfill 材料組合，縮窄至已驗證材料範圍
- **執行對口與啟動條件**
  - **主對口**：封裝整合工程 PIE（CoWoS）
  - **次對口**：封裝可靠度部門 + 封裝設計部門 + S11/S13 封裝群協調
  - **啟動條件**：TSMC 提供 CoWoS 材料參數（CTE / modulus / 幾何尺寸，NDA 下）+ Joint Lab MOU 簽署 + Q1 kick-off（PME / CSML / 封裝 PIE）
- **風險與緩解**
  - **競業 / IP**：完全無外部綁定（first mover 窗口）；43 國際專利已建立歸屬框架，IP 談判有先例可循，風險低
  - **學生流向**：NTHU PME 學生台積電 / ASE 為主要出口，流向高度一致；冠名年度獎可進一步強化 TSMC 品牌吸引力
  - **學界 vs 量產 SOP 落差**：江國寧的 FEA 設定（材料參數 / BC）以學術標準建立，與 TSMC 量產用參數庫可能有差距；建議第 1 年 co-calibration 階段由 TSMC PIE 提供量產材料參數修正模型
  - **能力限制**：江國寧年齡（1989 PhD，資深教授），長期接班人（Lab 主力博士生的繼承性）需確認；建議合約中明訂 key personnel 條款（若主持 PI 不能持續，計畫暫停協商）
- **連結**：[NTHU PME 英文頁](https://pme.site.nthu.edu.tw/p/406-1308-73988,r4027.php?Lang=en) ｜ [NSTC Merit Fellow 公告](https://eng-en.site.nthu.edu.tw/p/406-1060-260930,r3410.php?Lang=en) ｜ [ResearchGate](https://www.researchgate.net/scientific-contributions/2113062702_Kuo-Ning_Chiang) ｜ 代表論文：Scientific Reports 2022 3D IC DL ｜ Materials 2024 solder joint fatigue ML

---

### S13. 宋振銘（Jenn-Ming Song）｜總分 **8.0**（S 級）｜第二波

| 校系職級 | NCHU 材料系 + 研發長（Dean of R&D）｜ 教授 / 研發長 ｜ PhD: 待核實 |
|---|---|
| 學術指標 | h-31；3,090 引用（Google Scholar）；JMRT/JJAP 2025 多篇 |
| Lab | 中型 + 跨校（彰師大）|
| **5 維度評分** | 研究 8 ｜ fab 9 ｜ Lab 8 ｜ 接洽 9 ｜ 長期 8 ｜ 2025 未來科技獎 + TRL 4-5 量測/感測 + 研發長制度對接 |

**核心專長 × 近 3 年代表實績**
- Cu-Cu Bonding 銅銅直接接合（SoIC 核心）/ 表面改質 光誘導接合前處理 / 電化學感測 / AI 預測平台 跨彰師大合作
- 2025/04 VUV/HCOOH Al-to-Al ultrasonic bonding（呼應 Hybrid Bonding 路線）；2025 未來科技獎 [待核實官方公告]；i-ONE 儀器創新獎；JMRT / JJAP 2025 多篇；光誘導表面改質專利；PCB 學生優秀論文金獎 2025
- 2025 未來科技獎；i-ONE 儀器創新獎；Materials Chemistry and Physics 期刊 Editorial Board

**製程/封裝應用點（詳述）**

- **節點 / 段別**：後段封裝（Advanced Packaging）— SoIC / CoWoS Hybrid Bonding；重點段別為「Cu-Cu 直接接合（Hybrid Bonding / Copper-Copper Direct Bonding）」+ 「接合前表面改質（Pre-bond Surface Treatment）」；節點趨勢：A16 以下 SoIC 需求急增，Cu-Cu bonding 為關鍵製程卡點
- **痛點對應**：
  - **Cu-Cu Bonding 界面氧化控制**：Cu 表面在空氣中快速氧化（Cu₂O 數 nm 即可阻礙接合），接合強度 variability 大；宋振銘的光誘導表面改質（VUV/HCOOH 處理）可在接合前去除氧化層並活化 Cu 表面，提升接合強度一致性（2025/04 論文已驗證 Al-Al ultrasonic bonding，路線呼應 Cu-Cu Hybrid Bonding）
  - **接合強度線上感測缺口**：現行 SoIC bonding 製程缺乏即時接合強度感測，只能靠事後拉力測試（destructive）或 X-ray 非破壞性推估；宋振銘的電化學感測平台可設計為 inline 非破壞性接合品質監測，填補量產 SPC 盲區
  - **AI 預測平台跨參數空間優化**：Cu-Cu bonding 參數（溫度 / 壓力 / 時間 / 表面粗糙度 / 氧化層厚度）組合空間大，傳統 DOE 試驗成本高；宋振銘跨彰師大的 AI 預測平台可建立 bonding 參數 ↔ 接合強度的代理模型，加速最佳參數搜索
  - **新材料路線適配（Al-to-Cu 過渡）**：2025/04 論文的 Al-Al ultrasonic bonding 方法論可向 Cu-Cu hybrid bonding 遷移，特別是在 SoIC 使用 Al redistribution layer 的過渡設計方案上
- **可導入時程（TRL）**：**TRL 4-5 / 6-12 個月 PoC** — 光誘導表面改質在 Al-Al bonding 已驗證（TRL 5），Cu-Cu 版本需 PoC；AI 預測平台在彰師大合作環境已有雛形（TRL 4）；2025 未來科技獎評定技術就緒度顯示 TRL 4-5 可信
- **配合 fab 部門**：SoIC 封裝製程工程（SoIC PIE）/ Hybrid Bonding 製程開發為主對口；封裝可靠度部門（接合強度測試規格）/ 品質工程（QE inline SPC）為次對口；與 S11 楊哲化（NDT 隱裂）/ S12 江國寧（FEA 壽命預測）組成封裝可靠度三角協作（cross-ref: S11/S12）
- **預期成效**：
  - Cu-Cu bonding 界面 shear strength variability（Cpk）從 < 1.0 改善至 ≥ 1.33（表面改質效益）
  - Inline 非破壞性接合品質感測誤報率 ≤ 5%（電化學感測 + AI 模型）
  - Bonding 參數 DOE 次數減少 30-50%（AI 代理模型替代全面 DOE）
  - 2025 未來科技獎技術導入 TSMC SoIC 試驗線，形成聯名 IP

**合作紀錄 × 與外部公司狀況**
- CCNRIA 聯盟；跨彰師大 AI 協作
- **無公開可見外部綁定**；研發長身份便於制度對接

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — Cu-Cu Hybrid Bonding 光誘導表面改質 PoC**：將 VUV/HCOOH 光誘導改質方法從 Al-Al 遷移至 Cu-Cu 系統，在 TSMC SoIC 試驗線材料樣品上驗收接合強度 Cpk 改善
  - **主題目 B — Inline 接合品質電化學感測**：開發適用 SoIC bonding 製程的非破壞性 inline 感測模組，建立接合強度即時 SPC 回饋機制
  - **延伸題目 C — AI 接合參數優化平台**：整合彰師大跨校合作的 AI 預測平台，針對 Cu-Cu bonding 多變量參數空間建立代理模型，加速 DOE 收斂（可與 S12 江國寧 FEA 代理模型方法論串聯，cross-ref: S12）
  - **延伸題目 D — 未來科技獎技術孵化**：將 2025 未來科技獎技術（光誘導接合改質）進一步 scale-up，目標聯名申請台灣 / 美國專利（NCHU × TSMC）
- **制度與簽約**
  - **架構**：第 1 年 PoC（材料樣品由 TSMC 提供）；PoC 達標後轉 3 年 JDP；NCHU 研發長身份便於機構層級制度對接
  - **預算建議區間**：PoC 年 NT$ 800-1,200 萬（推估區間，非承諾數字，依 NCHU 院校級材料科技合作對標）；JDP 轉入後年 NT$ 1,500-2,500 萬（含實驗設備、學生獎助、跨彰師大協作費）
  - **簽約對象**：NCHU 材料系（機構，宋振銘為研發長，制度對接順暢）+ 宋振銘 PI（個人委案）；IP 協商建議 TSMC 持有 fab 應用 IP，學術方法論 PI 保留
  - **學生通道**：NCHU + 彰師大聯合 Lab 學生；NCHU 材料系碩博士生為主力；可申請 TSMC 封裝廠實習
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年（PoC）**：Cu-Cu bonding 表面改質後 shear strength 均值提升 ≥ 20%（vs 未改質組）；接合強度 Cpk ≥ 1.0；至少 1 篇 IEEE CPMT / JMRT 聯名論文投出
  - **第 2 年（JDP 初期）**：Inline 感測模組 prototype 完成；誤報率 ≤ 5%（在 50 批樣品測試）；AI 參數優化平台 DOE 次數降幅 ≥ 30%
  - **第 3 年（JDP 深化）**：技術導入 SoIC 試驗線；聯名專利申請 ≥ 2 件；跨彰師大 AI 平台整合完成
  - **Exit criteria**：PoC 結束時 shear strength 提升 < 10%，且無明確材料方案替代，終止 JDP；若 inline 感測誤報率 > 20%，先暫停主題目 B，集中資源在主題目 A + C
- **執行對口與啟動條件**
  - **主對口**：SoIC PIE / Hybrid Bonding 製程開發部門
  - **次對口**：封裝可靠度部門 + QE inline SPC + 封裝群（S11/S12）協調
  - **啟動條件**：TSMC SoIC Cu 樣品提供（標準 bumped wafer ≥ 50 片）+ NDA 簽署 + 宋振銘訪廠一次（TSMC 中科 / 竹科封裝廠）確認試驗機台規格
- **風險與緩解**
  - **競業 / IP**：CCNRIA 聯盟合作，需確認聯盟成員中是否有 TSMC 競業方（如 ASE）；研發長身份對跨機構 IP 管理有一定把握度
  - **學生流向**：NCHU 材料系學生以台積電 / 日月光封裝廠為主要出口，流向高度匹配；彰師大協作學生需確認 NDA 擴及條款
  - **學界 vs 量產 SOP 落差**：光誘導改質方法在學術環境以批次處理為主，TSMC inline 量產需連續式腔體整合；建議 PoC 期即評估腔體設計可行性（可委託設備商 PoC 同步）
  - **能力限制**：Cu-Cu hybrid bonding 先例為 Al-Al 論文，跨材料系統的方法遷移有效性需 PoC 驗證；WebSearch 無法確認宋振銘現有 Cu-Cu bonding 直接量產合作記錄
- **連結**：[NCHU 材料系](https://www.mse.nchu.edu.tw/en/members/teacher/Jenn-Ming-Song-69623319) ｜ [Google Scholar](https://scholar.google.com/citations?user=LNiBlZwAAAAJ) ｜ [ResearchGate](https://www.researchgate.net/profile/Jenn-Ming-Song) ｜ [VUV/HCOOH 論文](https://www.researchgate.net/publication/390351765) ｜ 代表論文：JMRT / JJAP 2025 系列 ｜ 2025 未來科技獎

---

### S14. 李家岩（Chia-Yen Lee）｜總分 **8.0**（S 級）｜第二波

| 校系職級 | NTU 資管系 + 管院副院長 + EiMBA Director ｜ 教授 / 副院長 / EiMBA Director ｜ PhD: Texas A&M University 工業與系統工程 2012 |
|---|---|
| 學術指標 | h-27；1,934 引用（Google Scholar）；IEEE TASM AE |
| Lab | PoLab 12-18 人；GitHub 開源 93+ star |
| **5 維度評分** | 研究 9 ｜ fab 9 ｜ Lab 9 ｜ 接洽 8 ｜ 長期 8 ｜ IEEE TASM AE + 2024 CIIE Best + 多業態實戰 |

**核心專長 × 近 3 年代表實績**
- DRL / MARL 深度強化學習 / 多智能體 / 製造 OR 作業研究排程 / 預測性維護 / 《製造數據科學》作者
- MARL chiller IJPE 2025；BMB-LIME 42 引用；IEEE Transactions on Automation Science and Management AE；2024 CIIE Best Paper；GitHub 開源 93+ star
- IEEE TASM AE；2024 CIIE Best Paper；NSTC 傑出研究獎

**製程/封裝應用點（詳述）**

- **節點 / 段別**：前段製程整合（Process Integration）/ 製造作業管理（Fab Operations）/ 設施工程（Facilities Engineering）；應用橫跨 N3/N2/A16 節點（排程 / 能源管理與節點無強相關）；重點在「Fab 內 OR 排程問題」與「公用系統（Chiller / Air）能源 AI」
- **痛點對應**：
  - **Reticle / 光罩排程最佳化**：fab 內的 reticle（photomask）是高價值、數量有限的資源；N2 / A16 多層 EUV reticle 的排程不當（reticle shuttle 等待、機台 queue 不均）會直接延長 WIP makespan；李家岩的 DRL 排程方法（PoLab 系列）可將 reticle 排程問題建模為 MDP，用 MARL 協同多 WS 機台決策
  - **Chiller 系統能源最佳化**：TSMC 每座 fab 的 chiller 系統耗電量極大（占 fab 總用電約 20-30%）；李家岩的 MARL chiller IJPE 2025 一作已在商用 chiller 驗證；直接遷移 TSMC 多機組 chiller 可估算 8-15% 節電效益
  - **異常偵測（Anomaly Detection）**：前段製程機台異常訊號（FDC OOC 早期微弱訊號）需 PoLab 的 anomaly detection 方法；現行規則式 FDC 對緩變型異常（漸進老化）敏感度不足，ML 方法可提前 2-5 天預警
  - **預測性維護（Predictive Maintenance）**：台積電部分已有 PM 系統，但李家岩 PoLab 方法（含 DRL 主動 PM 排程）可進一步讓 PM 排程動態化，根據機台狀態預測最佳換件時機，降低 unplanned downtime
- **可導入時程（TRL）**：**TRL 6-7 / 立即至 6 個月** — 李家岩的 DRL / MARL 方法已在日月光、台達、友達等業界環境有實戰紀錄（TRL 6）；chiller MARL 已發表 IJPE 2025，有商用 chiller 驗證先例；TSMC 環境更複雜但方法論成熟，6 個月可達 TRL 7；PoLab GitHub 開源 93+ star 顯示社群驗證度
- **配合 fab 部門**：製造部（Fab Operations / MFG）/ 設備工程（Equipment Eng.）為主對口；設施工程（Facilities / 能源）/ FDC 系統 owner 為次對口；與 SPC 群（S07/S10/A19/A24/A16/B37/B45）的 FDC / 異常偵測段有協作空間（cross-ref: S10/A24）
- **預期成效**：
  - Reticle 排程 makespan 降低 10-20%（DRL vs 現行啟發式規則）
  - Chiller 系統能耗降低 8-15%（MARL，依 IJPE 2025 對標）
  - 機台異常 ML 早期預警提前量 ≥ 2 天（vs 規則式 FDC 即時觸發）
  - PM unplanned downtime 降低 15-25%（DRL 主動排程 PM）

**合作紀錄 × 與外部公司狀況**
- 台積電（碩士後工作經歷）；日月光 / 台達 / 友達 / 華邦；Profet AI 顧問
- Profet AI 顧問（非獨家）；多家合作顯示開放度；**無獨家排他綁定**

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — Reticle DRL 排程最佳化**：以 PoLab DRL 框架對 TSMC fab 的 reticle 排程問題建模（N2/A16 多層 EUV reticle shuttle），目標降低 makespan 10-20%
  - **主題目 B — 多機組 Chiller MARL 能源最佳化**：將 IJPE 2025 MARL chiller 方法直接移植 TSMC 設施工程，針對多機組 chiller 組合最佳化，目標節電 8-15%
  - **延伸題目 C — 機台異常 DL 早期預警**：以 PoLab anomaly detection 方法補強 TSMC FDC 規則式系統，針對緩變型異常（漸進老化）建立 ML 早期預警層（可與 S10 謝昱銘 KSA 串聯，cross-ref: S10）
  - **延伸題目 D — 預測性維護 DRL 主動排程**：開發 DRL 主動 PM 排程模型，使 PM 時機動態化；結合 EiMBA 業師網絡拓展實務知識（Profet AI 顧問經驗可引進）
- **制度與簽約**
  - **架構**：JDP + EiMBA 業師雙軌（EiMBA 業師槓桿降低個人行政負擔）；3-5 年中程，前 2 年聚焦主題目 A + B，後期延伸 C + D
  - **預算建議區間**：年 NT$ 1,500-2,500 萬（推估區間，非承諾數字，依 NTU 資管 JDP 規模及多業態合作對標）；含 PoLab 學生獎助 + 計算資源（DRL 訓練需 GPU）+ EiMBA 業師費用分攤
  - **簽約對象**：NTU 資管系（機構）+ 李家岩 PI（個人委案）；Profet AI 顧問合作非獨家，需確認無利益衝突條款
  - **學生通道**：PoLab 12-18 人，PhD / 碩士均有；GitHub 開源 93+ star 顯示學生具備開源工程能力；可安排廠內 shadow mode 測試期駐廠
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：Reticle 排程 DRL 模型在 TSMC 模擬環境（digital twin / 歷史資料）makespan 降幅 ≥ 8%；Chiller MARL 在 TSMC 試驗機組節電 ≥ 5%（shadow mode）；聯名 IEEE TASM 論文投出 1 篇
  - **第 2 年**：Reticle 排程升至 advisory mode（工程師確認採納率 ≥ 70%）；Chiller MARL 正式上線（≥ 3 機組）；異常偵測模型達早期預警 ≥ 2 天
  - **第 3 年**：DRL 排程系統覆蓋 ≥ 1 條完整 fab reticle 流程；PM DRL 排程完成 PoC；PoLab 學生 1-2 人轉入 TSMC 數位製造部門
  - **Exit criteria**：第 1 年 reticle makespan 降幅 < 3%，降轉 advisory-only 模式，重評主題目 A 主軸；chiller 節電 < 2%，降至延伸題目處理
- **執行對口與啟動條件**
  - **主對口**：Fab Operations（製造部）/ 設施工程（Facilities）
  - **次對口**：FDC 系統 owner + EiMBA 業師協調 + Profet AI 顧問接口（非 TSMC 直接，作技術佐證）
  - **啟動條件**：TSMC 歷史 reticle 排程資料（去識別化）+ chiller 能耗資料提供（NDA）+ 李家岩行政排期確認（副院長 / EiMBA Director 職務繁重，需確認執行 PI 時間配置）
- **風險與緩解**
  - **競業 / IP**：Profet AI 顧問非獨家，但需確認 Profet AI 與 TSMC 無直接競業條款（Profet AI 客戶含 fab 廠）；日月光 / 台達 / 友達合作應不衝突，但建議以書面確認無排他條款
  - **學生流向**：PoLab 學生以 NTU 資管背景，製造業 + AI 複合背景符合 TSMC 數位製造需求；流向匹配度高
  - **學界 vs 量產 SOP 落差**：李家岩的業界合作（台積電、日月光、台達）顯示落差處理能力強；DRL 訓練 reward 設計與量產 KPI 的 alignment 需前 1-2 個月密集 workshop 定義
  - **能力限制**：副院長 / EiMBA Director 行政負擔大，執行 PI 時間有限；建議合約明訂每週投入時數（建議 ≥ 1/3 FTE）或指定資深博士生作為 co-PI；WebSearch 無法驗證 TSMC 台積電工作期間的具體貢獻（僅知為台積電工作歷史）
- **連結**：[NTU 資管](https://management.ntu.edu.tw/IM/faculty/teacher/sn/388) ｜ [PoLab Bio](http://polab.im.ntu.edu.tw/Bio.html) ｜ [Google Scholar](https://scholar.google.com/citations?user=M_DB0CQAAAAJ) ｜ [NSTC 傑出研究獎](https://web.nstc.gov.tw/cen/oaa/award_110e/website/ChiaYen-Lee.html) ｜ 代表論文：MARL Chiller IJPE 2025 ｜ BMB-LIME（42 引用）

---

### S15. 鄭桂忠（Kea-Tiong Samuel Tang）｜總分 **8.0**（S 級）｜第二波

| 校系職級 | NTHU EE ｜ 教授 ｜ PhD: Caltech 電機 1998 MS / 2001 PhD |
|---|---|
| 學術指標 | IEEE Fellow；h-49；9,210 引用（Google Scholar）；ISSCC 2024 ReRAM CIM 一作 |
| Lab | NBME Lab 中大型 |
| **5 維度評分** | 研究 9 ｜ fab 9 ｜ Lab 9 ｜ 接洽 6 ｜ 長期 8 ｜ IEEE Fellow + ISSCC 頂會 + tape-out 能力 |

**核心專長 × 近 3 年代表實績**
- Neuromorphic Computing / CIM（Compute-in-Memory）/ ReRAM（Resistive RAM）/ TinyML 邊緣 AI 晶片
- IEEE Fellow；第 21 屆國家新創獎；CES 2026 神經形態晶片展示（突破馮·紐曼架構）；ISSCC 2024 22nm 16Mb Floating-Point ReRAM CIM Macro 一作；ISSCC TPC 任期 2021-2024；Nature / Science 2024-2025 共著
- IEEE CASS VP-Regional Activities and Membership（2022-2025）；ITRI 電子與光電系統研究所 生醫暨工業 IC 技術組 技術長（2017-）；台達飛雁特聘 2022

**製程/封裝應用點（詳述）**

- **節點 / 段別**：N5/N3/N2/A16 前段晶圓製造（CIM macro 設計 + tape-out）+ 後端 AI 推論晶片應用；重點段別為「CIM（Compute-in-Memory）巨集電路設計 × ReRAM 嵌入式記憶體製程整合」；與 TSMC 標準邏輯製程（N2 / A16）的 backend-of-line 記憶體整合段直接相關
- **痛點對應**：
  - **AI 推論功耗瓶頸**：傳統馮·紐曼架構在 AI 推論時 memory-compute 間資料搬移耗能佔總功耗 40-60%（memory wall）；鄭桂忠的 CIM macro 將乘法累加（MAC）運算直接在 ReRAM cell 內完成，消除資料搬移，ISSCC 2024 22nm 16Mb CIM macro 已驗證
  - **ReRAM 製程良率**：ReRAM 的 set/reset 特性一致性（cell-to-cell variation）影響 CIM 精度，在 22nm 節點量產化仍有挑戰；鄭桂忠 Lab（NBME Lab）有完整 tape-out 能力，可在 TSMC 工程 wafer 環境反覆驗證 ReRAM array 良率
  - **TinyML 邊緣推論硬體**：TSMC 客戶（IoT / 車用 / 穿戴裝置）有 TinyML 晶片需求；鄭桂忠 CES 2026 Neuromorphic 晶片展示（突破馮·紐曼架構）顯示 TinyML edge AI 硬體已達展示就緒，是 TSMC 差異化服務的潛在賣點（Multi-Project Wafer + Design Advisory）
  - **CIM IP Block 標準化**：TSMC 現有 eDRAM / SRAM IP 庫，缺乏 ReRAM-based CIM IP 標準化 block；若與鄭桂忠共同開發可授權的 CIM macro IP，可直接納入 TSMC 客戶設計套件（PDK），創造平台收益
- **可導入時程（TRL）**：**TRL 7-8 / 立即** — ISSCC 2024 22nm 16Mb CIM macro 為 tape-out 驗證（TRL 7-8）；TSMC-NTHU JDP 既有框架下，直接延伸至 A16 節點無需新立 MOU；CES 2026 展示顯示系統整合層（TRL 8）已達；進入 TSMC 量產線僅需 DRC rule 對齊 + IP sign-off（TRL 9）
- **配合 fab 部門**：前段邏輯製程整合（Logic PIE / 記憶體整合 BTOL）為主對口；設計技術合作（DTC Design Technology Co-optimization）/ PDK 部門為次對口；與 CIM 群（S03 馬誠佑 / S05 胡璧合 / A26 張孟凡）形成 CIM 技術棧分工（cross-ref: S03/S05/A26：架構層 × 電路層 × 製程整合層）
- **預期成效**：
  - CIM macro AI 推論能效提升 10-100x（vs 傳統 SRAM-based MAC，依 ISSCC 2024 數據外推）
  - ReRAM CIM macro 在 TSMC A16 製程工程 wafer 上良率達 ≥ 85% cell-pass rate（第 2 年 KPI）
  - CIM IP block 納入 TSMC PDK 設計套件，服務 ≥ 3 個 fabless 客戶 tape-out（第 3 年目標）
  - TinyML 晶片樣品通過 TSMC JEDEC / AEC-Q100 可靠度初篩（車用市場入口）

**合作紀錄 × 與外部公司狀況**
- TSMC-NTHU JDP 教授；ITRI 技術長（2017-）；台達飛雁特聘 2022
- TSMC-NTHU JDP（經費依賴非機構忠誠）；ITRI 技術長非 TSMC 競業；與張孟凡（A26 內部 Director）職能不同層級，綁定程度低 1-2 級

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — ReRAM CIM macro A16 節點延伸 tape-out**：在 TSMC-NTHU JDP 既有框架下，將 ISSCC 2024 22nm CIM macro 延伸至 A16（1.4nm）節點，目標良率 ≥ 85%、能效持平或提升
  - **主題目 B — CIM IP Block 標準化 × PDK 整合**：與 TSMC DTC / PDK 部門共同開發可授權 ReRAM-based CIM IP block，規格對齊主流 fabless AI 晶片客戶需求
  - **延伸題目 C — TinyML Neuromorphic 晶片系統整合**：以 CES 2026 展示晶片為基礎，進行車用 / IoT 場景系統整合（可與 S03 馬誠佑、S05 胡璧合 CIM 群協作，cross-ref: S03/S05）
  - **延伸題目 D — CIM × SRAM 混合架構設計方法論**：探索 ReRAM CIM 與 TSMC 標準 SRAM 的混合記憶體層次（hybrid memory hierarchy），為客戶提供彈性 IP 選配方案（可與 A26 張孟凡內部 CIM 協作，cross-ref: A26）
- **制度與簽約**
  - **架構**：深化既有 TSMC-NTHU JDP；建議升級為「NTHU CIM 聯合研究中心」冠名；5 年期續約（現有 JDP 基礎上）；tape-out 費用由雙方各出一部份（學術 MPW 優惠 + TSMC 工程 wafer）
  - **預算建議區間**：年 NT$ 3,000-5,000 萬（推估區間，非承諾數字，依 TSMC-NTHU JDP 既有量級 + tape-out 工程 wafer 成本對標）；含 NBME Lab 學生獎助 + 設計工具 license（Cadence / Synopsys）+ tape-out 費用分攤
  - **簽約對象**：NTHU EE 系（機構）+ 鄭桂忠 PI（個人委案）；IP 依 TSMC-NTHU JDP 既有歸屬框架（已有 IP 分配先例）
  - **學生通道**：NBME Lab 中大型；ISSCC 一作學生是優質招募標的；博士生可申請 TSMC 台積獎學金 + 前段設計實習
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：A16 節點 CIM macro 完成 DRC clean 設計（tapeout-ready）；TSMC 工程 wafer shuttle 申請送出；ISSCC 2025 / VLSI 2025 聯名論文投稿 1 篇
  - **第 2 年**：A16 tape-out 完成；CIM macro cell-pass rate ≥ 85%；CIM IP block spec 完成初稿（對齊 PDK 格式）
  - **第 3 年**：CIM IP block 納入 TSMC PDK 客戶試用；≥ 3 個 fabless 客戶 design-in；TinyML 晶片 AEC-Q100 初篩通過
  - **Exit criteria**：第 2 年 tape-out 後 cell-pass rate < 70%，需 re-spin（第 3 年預算轉為 re-spin）；若 IP block 無 fabless 客戶採用，縮回 IP 標準化子議題
- **執行對口與啟動條件**
  - **主對口**：Logic PIE（記憶體整合段）/ DTC Design Technology Co-optimization
  - **次對口**：PDK 部門 + CIM 群（S03 馬誠佑 / A26 張孟凡 內部協調）+ ITRI 技術長接口（非競業，資源借用）
  - **啟動條件**：既有 JDP 續約文件確認 + A16 工程 wafer shuttle 時程排定 + kick-off（NTHU EE / NBME Lab / TSMC Logic PIE）；建議 Q1 啟動避免 A16 資源窗口競爭
- **風險與緩解**
  - **競業 / IP**：TSMC-NTHU JDP 既有框架下 IP 歸屬有先例，風險可控；**關鍵風險在台達飛雁特聘（2022）**：台達在工業用 AI 晶片 / 邊緣 AI 有布局，若台達客製 IC 需求與 TSMC PDK IP block 有衝突需事先澄清；建議合約中加入台達相關揭露條款（台達是否已有 TSMC 客戶設計合作關係）
  - **學生流向**：NBME Lab 學生以 TSMC / 台積電 / 聯發科為主要出口，流向高度匹配；ISSCC 一作資歷的學生市場競爭激烈，需確保 TSMC 招募窗口優先
  - **學界 vs 量產 SOP 落差**：鄭桂忠有 ISSCC tape-out 實戰 + JDP 經驗，SOP 落差相對最小；**ITRI 技術長（2017-）**身份可能涉及 ITRI 與廠商的技術服務合約，需確認無利益衝突（ITRI 技術組業務與 TSMC ReRAM 製程整合若有重疊需事先聲明）
  - **能力限制**：接洽度評分 6（最低分項）反映 TSMC-JDP + ITRI + 台達三方綁定後的接洽複雜度；WebSearch 無法完整查明台達飛雁特聘的具體合作範疇 / 排他性條款，建議洽談前請 NTHU 技轉辦確認；ITRI 技術長為 2017 年至今長期職位，是否涉及當前 TSMC 同類業務需主動查詢
- **連結**：[NBME Lab](https://nbme.ee.nthu.edu.tw/advisor.html) ｜ [NTHU EE 國家新創獎](https://dee.site.nthu.edu.tw/p/406-1175-291610,r3748.php?Lang=en) ｜ [IEEE CASS](https://ieee-cas.org/contact/kea-tiong-samuel-tang) ｜ [Google Scholar](https://scholar.google.com/citations?user=DiSis28AAAAJ) ｜ [Digitimes CES 2026](https://www.digitimes.com/news/a20260108PD220/taiwan-ces-chips-mems-efficiency.html) ｜ 代表論文：ISSCC 2024 22nm 16Mb Floating-Point ReRAM CIM Macro

---

### A16. 張國浩（Kuo-Hao Chang）｜總分 **7.8**（A 級）｜觀察（條件釐清後可遞補第二波）

| 校系職級 | NTHU IEEM 特聘教授 ｜ 特聘教授 ｜ PhD: Purdue 工業工程 |
|---|---|
| 學術指標 | IEEE T-SM Best Paper |
| Lab | NTHU IEEM Lab 中型 |
| **5 維度評分** | 研究 8 ｜ fab 8 ｜ Lab 8 ｜ 接洽 7 ｜ 長期 8 ｜ T-SM Best Paper + 產線最佳化 + Powerchip 2 年案 |

**核心專長 × 近 3 年代表實績**
- Simulation Optimization 模擬最佳化 / Operations Research 作業研究 / RL for Manufacturing 製造 RL / 產能規劃與 APC 調度
- IEEE Transactions on Semiconductor Manufacturing Best Paper；TSMC / UMC / VisEra 顧問實績；IJPR 2025-10「Optimal maintenance policy with degradation-shock dependence and a reliability constraint using simulation optimisation」共同作者含 TSMC 工程師 Yan-Shuo Chen（首度公開的 TSMC 聯名論文）；隨機模擬在晶圓廠應用
- IEEE T-SM Best Paper；TSMC 公開聯名論文 IJPR 2025-10

**製程/封裝應用點（詳述）**

- **節點 / 段別**：N3 / N2 / A16 前段 + 中段；APC 自適應製程控制、設備健康預測維護（PHM）、產能規劃與排程最佳化、CVD / CMP 良率提升
- **痛點對應**：
  - **CVD 設備退化震動耦合導致 APC 失準**：多設備同步退化時，傳統 APC 無法區分製程偏移與設備退化訊號；張教授 2025 IJPR TSMC 聯名論文「degradation-shock dependence」直接命中此痛點，可將維護觸發點從時間基礎轉為狀態基礎，降低非計畫停機率
  - **N2 / A16 產能規劃不確定性爆增**：EUV 曝光層增加使 WIP 波動更劇烈；Simulation Optimization + RL 可在短回路時間內找出 robust 排程策略，降低 bottleneck layer cycle time
  - **力晶 CVD APC 案已驗證可遷移性**：連續兩年實廠落地（Powerchip）的 CVD APC 案代表方法論已具備可重複性；可做 TSMC N3 / N2 CVD chamber 快速 pilot
  - **多目標維護政策最佳化（設備壽命 × 利用率 × 良率三角）**：N2 以下設備更換成本倍增，需更精準的預測維護決策窗口
- **可導入時程（TRL）**：**TRL 6-7 / 6-9 個月啟動 PoC**；CVD APC 方法論已有工廠驗證，遷移至 TSMC 環境主要為資料接口與機台校正工作，非方法論從零建立
- **配合 fab 部門**：主對口 **SEM（設備工程）+ CIM**；次對口 **ME（製造工程）/ 產能規劃部**
- **預期成效**：
  - CVD chamber 非計畫停機率降低 ≥ 15%（基於 IJPR 2025 論文模型推估）
  - N2 bottleneck layer cycle time 變異係數（CV）降低 ≥ 10%
  - APC 模型重訓週期從月縮短至週
  - 每年聯名論文 ≥ 1 篇（目標 IEEE T-SM 或 IJPR）

**合作紀錄 × 與外部公司狀況**
- TSMC 公開聯名論文 IJPR 2025-10（首度確認直接合作）；TSMC / UMC / VisEra 顧問；力晶 Powerchip 連 2 年 CVD APC 案
- TSMC 聯名論文（2025-10，IJPR）；Powerchip 連 2 年案（時間排擠）；Micron Chair 傳聞**待核實**

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — 設備退化—震動耦合下的動態 APC 調控框架**：以 IJPR 2025 TSMC 聯名論文為基礎，擴展至 EUV 層多腔體退化聯合建模；cross-ref S05 簡禎富（NSTC RAISE SPC 群）與 S06 蔡銘宏（製程穩定度群），形成「設備健康 → 製程穩定 → APC 閉環」三角合作叢集
  - **主題目 B — Simulation-RL 混合排程於 N2 / A16 產能規劃**：針對 EUV 層導入後的 WIP 不確定性，建立快速模擬-強化學習混合框架，輸出 robust 排程建議
  - **延伸題目 C — 跨廠 CVD 預測維護知識轉移**：將 Powerchip 兩年實廠資料做遷移學習基礎，建立 TSMC CVD 快速 onboarding 機制（需 NDA 保護 Powerchip 資料）
- **制度與簽約**
  - **架構**：NSTC RAISE 產學聯盟（主框架）+ 個別 PoC 技轉授權（CVD APC 方法論）；若 Micron Chair 傳聞屬實，需先確認排他條款後再談 Chair Endowment
  - **預算建議區間**：年 NT$ 1,500-2,500 萬（含博士生 2 名薪資、設備模擬授權、出差驗證費）；3 年滾動（推估區間，非承諾數字，依 NTHU IEEM 既有產學量級對標）
  - **簽約對象**：NTHU 研究發展處 + 張國浩個人 PI；IP 框架建議共同申請、TSMC 取得優先商業授權
  - **學生通道**：NTHU IEEM → TSMC IE / CIM 招募管道；建議設立暑期實習 quota 2 名以觀察學生落地能力
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：完成 CVD APC 動態退化模型 PoC（TSMC 廠端資料接口建立）；投稿 1 篇 IEEE T-SM 或 IJPR；博士生 1 名完成 6 個月駐廠
  - **第 2 年**：N2 bottleneck 排程模型上線測試；非計畫停機降低指標可量測（基線對比）；產出 2 篇聯名論文
  - **第 3 年**：至少 1 個模型移交 CIM 團隊維運；技轉授權金談判啟動；累積論文 ≥ 3 篇
  - **Exit criteria**：第 2 年末 CVD 非計畫停機改善 ＜ 5%（未達門檻）或連續 12 個月無可用資料交付，則暫緩續約；論文產出低於每年 1 篇達 2 年則降規模
- **執行對口與啟動條件**
  - **主對口**：SEM 設備工程處 + CIM 部門
  - **次對口**：製程整合 ME / 產能規劃部
  - **啟動條件**：廠端資料使用合約簽署；NDA 覆蓋 Powerchip 既有合作資料邊界；kick-off 會議含 SEM 主管與 PI 共同確認 PoC 設備選擇
- **風險與緩解**
  - **競業 / IP**：Micron Chair 傳聞**待核實**——若屬實，Micron 可能要求 RAM / DRAM 相關排程成果優先授權；建議 MOU 前以 warm intro 確認；Powerchip 兩年合作已結束但 IP 歸屬需確認，避免 TSMC PoC 複用 Powerchip proprietary 配方
  - **學術深度 vs 量產 SOP 落差**：Simulation Optimization 模型假設（泊松到達率、指數服務時間）在 N2 超複雜路徑下可能失準；緩解：第一年 PoC 限縮在單一 CVD 模組，不做全廠推演
  - **學生流向**：NTHU IEEM 博士生競爭激烈（TSMC / 台積系供應商 / 新加坡 IME 均在搶）；建議設立明確的 in-lab TSMC co-branding 計畫提高吸力
  - **能力限制**：WebSearch 無法驗證 Micron Chair 是否已正式簽約 / Powerchip 合約 IP 條款細節；建議透過 NTHU 研發長或張教授直接問卷核實後再談架構
- **連結**：[NTHU IEEM](https://ieem.site.nthu.edu.tw/p/406-1310-111510,r5910.php?Lang=en) ｜ [個人 Lab](https://chang.ie.nthu.edu.tw/) ｜ [IJPR 2025 TSMC 聯名](https://www.tandfonline.com/doi/full/10.1080/00207543.2025.2566975) ｜ [Google Scholar](https://scholar.google.com/citations?user=ZfWgbacAAAAJ)

---

### A17. 蔡佩璇（Pei-Hsuan Tsai）｜總分 **7.7**（A 級）｜第二波

| 校系職級 | NCKU CSIE 教授 + IMIS 兼任 ｜ 教授（正教授）｜ PhD: NTHU 資訊工程 2010 |
|---|---|
| 學術指標 | IEEE IoT J 2025；Applied Intelligence 2024；ICCPS 2026 |
| Lab | CPS Lab（1 博 + 12 碩）|
| **5 維度評分** | 研究 8 ｜ fab 7 ｜ Lab 7 ｜ 接洽 9 ｜ 長期 8 ｜ Fulbright + IEEE IoT J + 畢業生進 TSMC |

**核心專長 × 近 3 年代表實績**
- Digital Twin（DT）/ Cyber-Physical Systems（CPS）/ SOP 視覺驗證 / 多模態感測融合
- 2024-2025 Fulbright Senior Scholar（Pittsburgh）；IEEE IoT Journal 2025 Multi-Objective DT；Applied Intelligence 2024；畢業生進 TSMC 有紀錄
- Fulbright Senior Scholar 2024-2025；IEEE IoT J 2025；ICCPS 2026

**製程/封裝應用點（詳述）**

- **節點 / 段別**：N3 / N2 中段 + 封裝（CoWoS / SoIC）；Digital Twin 製程即時監控、SOP 視覺驗證自動化、CPS 多感測融合異常偵測、HBM 封裝 DT 建模
- **痛點對應**：
  - **SOP 視覺驗證人工瓶頸**：N2 以下製程 SOP 複雜度倍增，目視驗證仍依賴人工比對；蔡教授的多模態感測融合 + DT 視覺驗證框架可自動比對操作影像與 SOP 標準態，顯著降低人為遺漏率
  - **CoWoS / SoIC 封裝製程 DT 缺失**：先進封裝段尚無即時數位孿生模型，導致良率異常診斷慢；IEEE IoT Journal 2025 多目標 DT 框架可直接遷移至 HBM 堆疊製程監控
  - **CPS 跨廠機台狀態一致性驗證**：不同 fab site 相同機台因環境差異導致製程飄移，CPS 多感測融合可建立跨廠一致性基線，加速 ramp-up
  - **Fulbright 停駐 Pittsburgh 國際 co-branding 價值**：2024-2025 訪問美國先進製造廠商，可作為 TSMC 美國 fab（Arizona）封裝 DT 國際協作潛在對接點
- **可導入時程（TRL）**：**TRL 5-6 / 9-12 個月啟動 PoC**；DT 框架已有期刊發表但封裝段應用需客製化感測整合，預計一年內可出 PoC 結果
- **配合 fab 部門**：主對口 **CIM / 製程整合**；次對口 **先進封裝 CoWoS 製造工程 / 品保 QA**
- **預期成效**：
  - SOP 視覺驗證人工比對工時降低 ≥ 30%
  - CoWoS 製程異常偵測平均反應時間（MTTD）縮短 ≥ 20%
  - 跨 fab site 機台一致性指標（CPK 對比）差異縮小 ≥ 15%
  - 每年聯名論文 ≥ 1 篇（目標 IEEE T-Industrial Informatics 或 IEEE IoT Journal）

**合作紀錄 × 與外部公司狀況**
- NCKU 內部（無半導體廠綁定）；醫療 / 災防 DT 應用為主
- **無公開可見外部綁定**；Fulbright 2024-2025 期間部分時間在美，需注意時程

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — CoWoS / SoIC 封裝製程多目標數位孿生建模**：以 IEEE IoT Journal 2025 框架為基礎，針對 HBM 堆疊與 CoWoS RDL 製程建立即時 DT；可 cross-ref S08 蔡明哲（封裝 AI 群）形成 DT 資料源 + 模型雙層合作
  - **主題目 B — 多模態感測融合 SOP 自動視覺驗證系統**：部署於 N2 製程操作稽核環節，輸出「操作偏差即時警示」；ICCPS 2026 方法論為基礎
  - **延伸題目 C — 跨廠區 CPS 機台一致性基線建立**：與 fab 海外 site（Arizona / 日本熊本）協作，建立跨廠 CPS 環境差異校正框架（Fulbright 國際連結可用）
- **制度與簽約**
  - **架構**：NSTC 一般產學合作（主框架）+ 可評估 ICCPS / IEEE IoT 聯合投稿合著協議；未來可升級為 Chair Endowment 若先進封裝 DT 成效顯著
  - **預算建議區間**：年 NT$ 1,500-2,000 萬（含碩博士生 2-3 名、感測器硬體整合費、出差 Pittsburgh / Arizona 協作費）；3 年滾動（推估區間，非承諾數字，依 NCKU CSIE 既有產學量級對標）
  - **簽約對象**：NCKU 研究發展處 + 蔡佩璇個人 PI；IP 框架建議 TSMC 取得封裝 DT 模型商業授權，學術方法論論文授權保留 PI
  - **學生通道**：NCKU CSIE + IMIS → TSMC 先進封裝 / CIM 招募管道；建議設 TSMC-NCKU 聯合指導名額 1-2 名
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：完成 CoWoS 製程 DT PoC（感測資料接口 + 單一製程段建模）；投稿 1 篇 IEEE T-Industrial Informatics 或 IoT Journal；SOP 視覺驗證原型 demo
  - **第 2 年**：DT 覆蓋 CoWoS 主要製程段（≥ 3 段）；SOP 視覺驗證系統上線測試（量產前驗證環境）；異常偵測 F1 ≥ 0.85
  - **第 3 年**：DT 模型移交 CIM 維運；跨廠 CPS 基線原型；累積論文 ≥ 3 篇；畢業生 ≥ 1 名進入 TSMC 封裝部門
  - **Exit criteria**：第 2 年末 DT 模型 MTTD 改善 ＜ 10% 或感測資料品質不足（缺失率 ＞ 30%）達 6 個月以上，則暫緩；論文產出低於每年 1 篇達 2 年則降規模
- **執行對口與啟動條件**
  - **主對口**：CoWoS 製造工程部 + CIM
  - **次對口**：品保 QA / 製程整合 ME
  - **啟動條件**：感測資料取用合約（含封裝廠端 OPC / MES 介面定義）；kick-off 含 PI + 封裝 ME 主管共同確認 PoC 範圍；Fulbright 返台後（預計 2025 下半）為最佳啟動窗口
- **風險與緩解**
  - **競業 / IP**：目前無已知外部競業綁定；Fulbright 停駐期間是否簽署美國廠商 NDA 需確認，避免知識移轉受限
  - **學術深度 vs 量產 SOP 落差**：ICCPS 2026 論文方法論尚未 camera-ready，封裝段特定 SOP 規格需 TSMC 廠端工程師配合定義；緩解：第一年 PoC 鎖定 1 條 CoWoS 產線、1 個 SOP 步驟
  - **學生流向**：NCKU CSIE 畢業生去 TSMC 有紀錄（已知），但也有強烈 IC 設計公司（聯發科 / 瑞昱）吸力；建議以封裝 AI 差異化定位強化 TSMC offer 吸引力
  - **能力限制**：WebSearch 無法驗證 Fulbright 訪察期間是否與美國廠商簽署保密或排他協議；建議以 warm intro 請蔡教授本人說明國際合作邊界
- **連結**：[NCKU CSIE 個人頁](https://www.csie.ncku.edu.tw/en/members/42) ｜ [NCKU researchoutput](https://researchoutput.ncku.edu.tw/zh/persons/pei-hsuan-tsai/) ｜ [CPS Lab](https://cps.imis.ncku.edu.tw/) ｜ [Fulbright 文章](https://journal.fulbright.org.tw/author/pei-hsuan-tsai/)

---

### A18. 林嘉文（Chia-Wen Lin）｜總分 **7.5**（A 級）｜觀察

| 校系職級 | NTHU EE 特聘 + AI 中心副主任 ｜ 特聘教授 ｜ PhD: NTHU 電機 2000 |
|---|---|
| 學術指標 | IEEE Fellow 2018；h-70；17,453 引用 |
| Lab | AI 中心級資源 |
| **5 維度評分** | 研究 9 ｜ fab 8 ｜ Lab 8 ｜ 接洽 7 ｜ 長期 7 ｜ IEEE Fellow + h-69 + 中心級 + 副主任 |

**核心專長 × 近 3 年代表實績**
- Vision Transformer / 光刻 EDA 光罩 hotspot 預測 / Mamba SSM 狀態空間模型 / 跨領域 AI 方法論
- IEEE Fellow 2018（multimedia coding and editing）；h-70 / 17,453 引用累計；清大 AI 中心副主任；Mamba / ViT 在光刻上的應用
- IEEE Fellow 2018；清大 AI 中心副主任

**製程/封裝應用點（詳述）**

- **節點 / 段別**：N3 / N2 / A16 前段；光刻 OPC / ILT 光罩 hotspot 預測、Defect Inspection AI、ViT / Mamba SSM 用於 EUV 製程偏移偵測、跨領域 AI 方法論移植（Multimedia → Semiconductor）
- **痛點對應**：
  - **EUV 光罩 hotspot 預測準確率瓶頸**：N2 / A16 EUV 層 ILT 運算量爆增，傳統 DNN 在 long-range context 上表現受限；林教授將 Mamba SSM 狀態空間模型應用於光刻 hotspot 預測可補足 ViT 計算成本過高的缺口，與 cross-ref A20 郭鴻飛（OPC / 光刻 EDA）、S04 Marek Strojwas（EDA 方法論）形成叢集
  - **缺陷影像分類的長尾分布問題**：N2 以下缺陷類別極度不均衡，傳統 CNN 在 rare defect 上 F1 極低；ViT 的 global attention 在低樣本稀有缺陷上表現明顯優於 CNN，林教授 h-70 的方法論庫可快速遷移
  - **Mamba SSM 計算效率優勢**：相較 ViT，Mamba 在長序列（如 wafer map 全面掃描）上計算量呈線性而非二次方成長，在 N2 晶圓 overlay 連續偵測場景具實用價值
  - **AI 中心副主任跨域整合能量**：可協助 TSMC 快速媒合清大內部其他 AI 團隊（如材料 AI / 化工 AI），形成 TSMC-NTHU AI 生態圈
- **可導入時程（TRL）**：**TRL 6-7 / 6-9 個月啟動 PoC**；ViT / Mamba 光刻應用已有論文發表，方法論成熟度高，遷移至 TSMC EDA 環境主要為資料格式與 OPC 工具 API 整合工作
- **配合 fab 部門**：主對口 **EDA / 光罩技術部（Mask Tech）**；次對口 **Defect Engineering / YE（良率工程）**
- **預期成效**：
  - EUV hotspot 預測 F1 ≥ 0.90（vs 現行 DNN baseline）
  - Mamba SSM vs ViT 計算時間降低 ≥ 40%（長序列 wafer map 場景）
  - Rare defect 類別 F1 ≥ 0.80（10 倍以下樣本量情境）
  - 每年聯名論文 ≥ 1 篇（目標 IEEE T-CAD 或 IEEE T-SM）

**合作紀錄 × 與外部公司狀況**
- 清大 AI 中心副主任（無外部綁定）；方法論研究為主
- **無公開可見外部綁定**

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — Mamba SSM 於 EUV 光刻 hotspot 預測與 ILT 加速**：以林教授現有 Mamba / ViT 光刻論文為基礎，針對 N2 / A16 EUV 光罩設計規則建立 hotspot 偵測模型；強烈建議 cross-ref A20 郭鴻飛（OPC EDA 工具端）與 S04 Marek Strojwas（方法論設計端），形成「AI 模型 + EDA 工具 + 方法論」三角
  - **主題目 B — Rare Defect 長尾分類：ViT + 資料增強聯合框架**：針對 N2 以下缺陷影像不均衡問題，建立 ViT + synthetic augmentation 聯合訓練框架；方法論可移植自 multimedia editing 的 few-shot 技術
  - **延伸題目 C — NTHU AI 中心媒合平台建立**：以林教授 AI 中心副主任身分，建立 TSMC-NTHU AI 雙邊議題媒合機制（每半年一次 workshop），非直接研究合作但具長期生態圈價值
- **制度與簽約**
  - **架構**：NSTC RAISE 產學聯盟（主框架，因 h-70 等級具備資格）+ 光刻 AI 方法論技轉授權；延伸題目 C 可另以 MOU 形式簽約
  - **預算建議區間**：年 NT$ 1,000-1,500 萬（含博士生 2-3 名、GPU 算力補助、EDA 工具授權費分攤）；3 年滾動（推估區間，非承諾數字，依 NTHU EE 特聘級教授既有產學量級對標；h-70 IEEE Fellow 通常可談較高量級）
  - **簽約對象**：NTHU 研究發展處 + 林嘉文個人 PI + 清大 AI 中心（延伸題目 C）；IP 框架建議 TSMC 取得半導體應用商業授權，multimedia 原始方法論 IP 保留 PI
  - **學生通道**：NTHU EE + AI 中心跨域生 → TSMC EDA / YE 招募管道；建議設 TSMC AI 獎學金名額強化清大優先錄取率
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：完成 Mamba SSM 光刻 hotspot 模型 PoC（N2 測試資料集）；投稿 1 篇 IEEE T-CAD 或 T-SM；rare defect 資料集建立（與 YE 合作標注）
  - **第 2 年**：Mamba hotspot 模型上線 EDA 測試環境；F1 達標（≥ 0.90）；rare defect F1 ≥ 0.80；論文 2 篇；NTHU-TSMC AI workshop 第一場
  - **第 3 年**：至少 1 個模型整合進 TSMC EDA 工具鏈；累積論文 ≥ 4 篇（h-70 PI 預期產出）；AI 中心媒合引入 ≥ 2 個新 NTHU PI 進入 TSMC 合作池
  - **Exit criteria**：第 2 年末 Mamba hotspot F1 ＜ 0.85 且未提出改進方案；或 EDA 工具 API 整合受阻超過 18 個月無進展，則降規模；論文低於每年 1 篇達 2 年則重新評估
- **執行對口與啟動條件**
  - **主對口**：EDA 部門 / 光罩技術部（Mask Tech）
  - **次對口**：良率工程 YE / Defect Engineering
  - **啟動條件**：EDA 工具 API 使用授權（含 OPC 工具資料格式規範）；NDA 覆蓋 N2 光罩設計規則資料；kick-off 含 PI + EDA 主管共同確認 Mamba 整合切入點
- **風險與緩解**
  - **競業 / IP**：IEEE Fellow 等級學者通常有多國際合作（Samsung LSI / Intel Foundry 可能有方法論共享協議）；建議 MOU 前確認是否有排他性 IP 條款涵蓋光刻 AI；清大 AI 中心若有其他企業贊助，需確認利益衝突邊界
  - **學術深度 vs 量產 SOP 落差**：Mamba 在 EDA 工具鏈整合的工程複雜度（API / 資料格式 / 版本管理）遠高於純論文場景；緩解：第一年鎖定離線模型驗證，不做即時嵌入
  - **學生流向**：NTHU EE AI 方向博士生被 Google DeepMind / Meta AI / 台灣 IC 設計公司高薪搶奪；建議以「EDA × AI 稀缺定位 + TSMC co-branding」做差異化
  - **能力限制**：WebSearch 無法確認林教授是否已與 Samsung / Intel Foundry 簽署光刻 AI 排他合作協議；建議透過清大 AI 中心行政端 warm intro 詢問
- **連結**：[個人網頁](https://www.ee.nthu.edu.tw/cwlin/) ｜ [Google Scholar](https://scholar.google.com/citations?user=fXN3dl0AAAAJ) ｜ [NTHU AI 中心](https://ai.site.nthu.edu.tw/p/404-1206-131034.php) ｜ [IEEE Signal Processing Society](https://signalprocessingsociety.org/our-story/chia-wen-lin) ｜ [IEEE Xplore](https://ieeexplore.ieee.org/author/37278408000)

---

### A19. 范書愷（Shu-Kai S. Fan）｜總分 **7.5**（A 級）｜第二波

| 校系職級 | NTUT 工業工程與管理系 特聘教授 + 管理學院院長 ｜ 特聘教授 / Dean of School of Management ｜ PhD: University of Texas at Arlington 工業工程 1996/12 |
|---|---|
| 學術指標 | Engineering Optimization 首位亞洲主編 |
| Lab | 院長級資源 |
| **5 維度評分** | 研究 8 ｜ fab 8 ｜ Lab 7 ｜ 接洽 8 ｜ 長期 7 ｜ Eng Opt 主編 + VM 已落地 + 院長級 |

**核心專長 × 近 3 年代表實績**
- SPC × ML 統計製程管制結合機器學習 / Virtual Metrology（VM）/ 工業統計 / 多變量製程最佳化
- CIE 2022 VM 論文已落地半導體大廠；Engineering Optimization 首位亞洲主編；多家半導體大廠落地合作（未具名）；NTUT 管院院長級資源
- Engineering Optimization 首位亞洲主編；NTUT 管院院長

**製程/封裝應用點（詳述）**

- **節點 / 段別**：N3 / N2 中段 + 前段；SPC × ML 製程統計監控、Virtual Metrology（VM）晶圓量測替代、多變量製程最佳化、良率工程統計方法論
- **痛點對應**：
  - **N2 製程參數維度爆增導致傳統 SPC 失效**：N2 以下量測參數維度超過數千，傳統單變量 SPC 控制圖無法偵測多維相關性偏移；范教授的 SPC × ML 多變量框架可在高維空間建立 adaptive control limits，cross-ref S05 簡禎富（SPC 方法論）、S06 蔡銘宏（製程穩定度）、A23 李淑敏（ML 良率模型）形成 SPC + ML + 良率三角叢集
  - **Virtual Metrology 量測替代降低在線量測成本**：N2 以下每片晶圓全量測不可行，VM 以製程設備參數（EES）預測量測值可降低 in-line 量測頻次 30-50%；CIE 2022 VM 論文已有半導體大廠落地案例
  - **多變量製程最佳化（DOE × ML 融合）**：N3 / N2 新製程開發期 DOE 實驗成本極高（EUV 曝光費用），ML 輔助 DOE 設計可顯著降低實驗次數並找出全局最優製程窗口
  - **Engineering Optimization 主編跨領域方法論整合**：首位亞洲主編身分使其具備快速掌握最新最佳化方法論並移植至半導體場景的系統優勢
- **可導入時程（TRL）**：**TRL 6-8 / 6-9 個月啟動 PoC**；VM 方法論已有半導體大廠落地驗證（CIE 2022），SPC × ML 框架成熟度高，遷移至 TSMC 主要為資料管道整合工作
- **配合 fab 部門**：主對口 **良率工程 YE / SPC 製程管制**；次對口 **量測工程 ME / CIM**
- **預期成效**：
  - VM 準確度（RMSE vs 在線量測值）達 ≤ 3% 誤差
  - 在線量測頻次降低 ≥ 30%（VM 替代部分量測點）
  - 多變量 SPC 異常偵測準確率 F1 ≥ 0.88（vs 傳統 SPC）
  - 每年聯名論文 ≥ 1 篇（目標 IEEE T-SM 或 Engineering Optimization）

**合作紀錄 × 與外部公司狀況**
- 多家半導體大廠落地合作（未具名）
- **無公開可見外部綁定**；院長身份便於制度對接

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — N2 / N3 多變量 SPC × ML 自適應監控框架**：以范教授工業統計方法論為核心，針對 N2 製程高維參數空間建立 adaptive multivariate control limits；cross-ref S05 簡禎富（NSTC RAISE SPC 聯盟）、S06 蔡銘宏（統計製程穩定）、A23 李淑敏（ML 良率模型）形成四人 SPC-ML-良率叢集，分工明確且互補
  - **主題目 B — Virtual Metrology 2.0：EES 驅動多步製程量測替代**：以 CIE 2022 落地論文為基礎，擴展至 EUV 多層製程的跨步驟 VM（不只單步預測），建立跨製程段 VM 鏈
  - **延伸題目 C — DOE × ML 融合：N2 新製程窗口最小實驗次數探索**：以 Engineering Optimization 主編視角整合最新 Bayesian Optimization + DOE 文獻，針對 EUV 曝光成本最小化設計實驗路徑
- **制度與簽約**
  - **架構**：NSTC 一般產學合作（主框架）+ VM 技轉授權（已有落地案例，技轉框架相對清晰）；若 SPC-ML 叢集合作成形，可考慮 NSTC RAISE 聯盟升級
  - **預算建議區間**：年 NT$ 1,000-1,500 萬（含博士生 2 名薪資、統計軟體授權、半導體資料處理算力）；3 年滾動（推估區間，非承諾數字，依 NTUT 工管系特聘級教授既有產學量級對標）
  - **簽約對象**：NTUT 研究發展處 + 范書愷個人 PI；IP 框架建議 TSMC 取得 VM 模型商業授權、SPC × ML 方法論論文授權保留 PI；技轉授權金依 CIE 2022 落地案例量級評估
  - **學生通道**：NTUT 工管系 → TSMC 製程統計 / 良率工程招募管道；管院院長身分代表有對外產學橋接能量，可建立 NTUT-TSMC 雙軌管道（工管 + 工程雙系所）
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：完成 N2 多變量 SPC 模型 PoC（選定 1 條製程線、3-5 個關鍵參數群）；VM 資料管道建立（EES 接口定義）；投稿 1 篇 IEEE T-SM 或 Engineering Optimization；S05 / S06 / A23 叢集 kick-off 協調會議
  - **第 2 年**：多變量 SPC F1 達標（≥ 0.88）；VM RMSE ≤ 3% 目標可量測；在線量測頻次降低 ≥ 20%（第一階段）；論文 2 篇；叢集聯名論文 ≥ 1 篇
  - **第 3 年**：VM 2.0 跨步驟模型上線測試；SPC × ML 模型移交 YE 維運；在線量測頻次降低達 30% 目標；累積論文 ≥ 3 篇；技轉授權金談判啟動
  - **Exit criteria**：第 2 年末 VM RMSE ＞ 5% 且未提出改進方案，或資料管道長期不穩定（資料缺失率 ＞ 25% 超過 9 個月）則暫緩；論文低於每年 1 篇達 2 年則降規模；叢集協作若 S05 / S06 先行退出，則重新評估范教授獨立合作規模
- **執行對口與啟動條件**
  - **主對口**：良率工程 YE / SPC 製程管制部門
  - **次對口**：量測工程 ME / CIM 部門
  - **啟動條件**：EES 資料取用合約（含 N2 製程設備參數清單）；NDA 覆蓋「多家半導體大廠落地合作」既有成果的 IP 邊界；kick-off 含 PI + YE 主管 + 量測工程主管三方確認 VM 切入點
- **風險與緩解**
  - **競業 / IP**：「多家半導體大廠落地合作（未具名）」是主要風險點——若其中包含 Samsung Foundry / 英特爾晶圓代工，VM 方法論可能有排他條款；建議 MOU 前要求 PI 揭露現有合作廠商名單（至少確認無直接 TSMC 競爭者）
  - **學術深度 vs 量產 SOP 落差**：工業統計方法論在 NTUT 工管系環境通常以模擬資料驗證，真實 EES 資料的噪聲水準、缺失率與 fab 側的期待差距需第一年 PoC 期間仔細對齊；緩解：指派 TSMC YE 駐點工程師協助資料清洗規格定義
  - **學生流向**：NTUT 工管系博士生數量較 NTHU / NCKU 少，供應量有限；管院院長身分可加速校內跨系招募（如電機系雙修統計方向），但需事先確認 TSMC 對「非工管系背景統計博士生」的接受度
  - **能力限制**：WebSearch 無法驗證「多家半導體大廠」具體廠商名單及合約 IP 排他條款；建議以 warm intro 請范教授本人揭露現有合作邊界，確認無競業衝突後再推進
- **連結**：[NTUT IEM 個人頁](https://iem.ntut.edu.tw/p/405-1081-131668,c11887.php?Lang=en) ｜ [NTUT 主編公告](https://www-en.ntut.edu.tw/p/404-1006-103796.php?Lang=en) ｜ [ResearchGate](https://www.researchgate.net/profile/Shu-Kai-Fan) ｜ [Elsevier Pure](https://ntut.elsevierpure.com/en/persons/shu-kai-fan) ｜ [IEEE Xplore](https://ieeexplore.ieee.org/author/37596641800)

---

### A20. 郭鴻飛（Hung-Fei Kuo）｜總分 **7.5**（A 級）｜第二波

| 校系職級 | NTUST 自動化所 教授（前所長 + 副院長 + 高階製造研發中心主任）｜ 教授（雙行政）｜ PhD: Georgia Institute of Technology 電機暨電腦工程 2004 |
|---|---|
| 學術指標 | NTUST 高階製造 |
| Lab | NTUST 學生流向清晰（TSMC/南亞科/應材）|
| **5 維度評分** | 研究 7 ｜ fab 8 ｜ Lab 7 ｜ 接洽 8 ｜ 長期 7 ｜ Georgia Tech 博士 + Mask AI 補位 + 學生流向清 |

**核心專長 × 近 3 年代表實績**
- Mask Optimization 光罩最佳化 / 光罩演算 / 對準誤差量測 / OPC 補強方法 / 先進製造控制
- Georgia Tech 電機博士 + 美系訓練；學生流向 TSMC / 南亞科 / 應材（公開背書）；前所長 + 副院長 + 高階製造中心主任（雙行政）
- 前所長 + 副院長 + 高階製造研發中心主任（三項行政實績）

**製程/封裝應用點（詳述）**

- **節點 / 段別**：N2（2nm）/ A16（1.4nm）/ A14（1.2nm）EUV 光刻段；前段微影（Litho）中的光罩製造（Mask Fabrication）+ 對準量測（Overlay Metrology）+ OPC 補強；重心在光罩演算法與先進製造控制（APC）端的 AI 補強層
- **痛點對應**：
  - **EUV Overlay 誤差累積**：N2 進入多層 EUV 後，對準誤差（Overlay Error）在層間累積效應下偏差放大；郭鴻飛長期研究 Overlay Metrology 與對準誤差量測，可提供 sampling 策略最佳化 + 補償模型，減少多層 EUV 因對準漂移造成的良率損失
  - **OPC 殘差修正不足**：傳統 model-based OPC 在 N2 / A16 corner case 殘差仍有 1-3nm 級漂移；郭鴻飛的 Mask Optimization 演算法（OPC 補強方法）可作 post-OPC 殘差校正層，與 S01 王俊明 ML hotspot 偵測並聯形成雙保險（cross-ref：S01 王俊明 / S04 Marek Strojwas）
  - **APC 製程漂移回應慢**：N2 高精度製程中，APC（Advanced Process Control）在設備老化 / 環境擾動下的回應週期若過長，會導致批次漂移；郭鴻飛的先進製造控制研究可縮短 feedback loop，提升批次間一致性
  - **NTUST 學生 → TSMC 通道未制度化**：現有學生流向 TSMC / 南亞科 / 應材為非正式通道；制度化合作後可將招募通道顯化，降低每年招募摩擦成本
- **可導入時程（TRL）**：**TRL 5-7 / 6-12 個月啟動 PoC**；Overlay 量測補償屬成熟研究方向（TRL 6-7），可 6 個月內接入 TSMC shadow mode 測試；OPC 殘差補強（TRL 5-6）需 N2 dummy mask 資料配合，估 6-12 個月完成 PoC → 第 2 年進入量產輔助層
- **配合 fab 部門**：光罩部（Mask Operation）+ Overlay / 量測部（Metrology）為主對口；微影製程整合（Litho PIE）+ APC 系統 owner 為次對口；Mask 群（S01 王俊明 / S04 Marek Strojwas）為跨組整合點（cross-ref）
- **預期成效**：
  - N2 EUV Overlay 誤差補償後批次間 3-sigma 縮減 ≥ 10%
  - OPC 殘差校正後 tape-out 前 critical layer CD 偏差降幅 ≥ 0.5nm（N2 baseline 對標）
  - APC feedback loop 回應週期縮短 ≥ 15%（設備老化漂移情境）
  - 每年 NTUST 學生進入 TSMC 招募通道人數 ≥ 3 人（制度化後）
  - 每年聯名論文 ≥ 1 篇（SPIE Advanced Lithography / IEEE T-SM）

**合作紀錄 × 與外部公司狀況**
- 無具體業界合作紀錄（公開端）
- **無公開可見外部綁定**；副院長 + 所長雙行政負擔重

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — N2 EUV Overlay 誤差補償模型**：以郭鴻飛對準誤差量測研究為基礎，建立 N2 多層 EUV Overlay sampling 最佳化 + 補償模型，目標縮減批次間 Overlay 3-sigma ≥ 10%；可與 Litho PIE 現有 APC 框架整合
  - **主題目 B — OPC 殘差 AI 補強層**：以 Mask Optimization 演算法對接 N2 / A16 OPC 後端，建立 post-OPC 殘差快速校正工具；與 S01 王俊明 ML hotspot 預測串聯形成 Mask PoC 雙軌（cross-ref：S01 王俊明 / S04 Marek Strojwas EUV mask 驗證體系）
  - **延伸題目 C — APC 製程控制 ML 補強**：以先進製造控制研究結合 fab 設備老化感測資料，建立 APC 自適應補償模組；可擴展至 NTUST 高階製造研發中心為後續合作平台
- **制度與簽約**
  - **架構**：NTUST 一般產學合作合約（掛自動化所 + 高階製造研發中心）+ PI 個人委案雙軌；可後接 NSTC 產學合創（RAISE）計畫為公共槓桿
  - **預算建議區間**：年 NT$ 800-1,200 萬（含學生獎助 + 量測設備 license + 教師研究費 + dummy mask 試片費用）；3 年滾動（推估區間，非承諾數字，依 NTUST 產學既有量級對標）
  - **簽約對象**：NTUST 研發處（機構）+ 郭鴻飛 PI（個人委案）雙軌；IP 依 NTUST 標準歸屬框架，TSMC 取得量產使用授權
  - **學生通道**：NTUST → TSMC / 應材定向實習通道（現有非正式通道制度化）；合約內加碼 1-2 名研究生獎助名額
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：Overlay 補償模型在 N2 dummy wafer shadow mode 測試；batch-to-batch 3-sigma 改善 ≥ 5%；OPC 殘差校正工具完成 N2 benchmark cell PoC；聯名 SPIE / IEEE T-SM 投稿 ≥ 1 篇
  - **第 2 年**：Overlay 補償模型升至 advisory mode（正式量產輔助）；OPC 殘差工具進入 Litho PIE 測試環境；APC 補強模組完成 pilot run 驗證；NTUST 學生通道制度化，第 1 批招募 ≥ 2 人
  - **第 3 年**：Overlay 補償接入 N2 量產 APC 系統；OPC 殘差工具移交 Mask Operation 維運；延伸至 A16 節點；NTUST 高階製造研發中心成為 TSMC 長期合作節點
  - **Exit criteria**：第 1 年 Overlay 3-sigma 改善 ＜ 3% 即重新評估補償模型主軸；OPC PoC 未通過 N2 benchmark 則暫緩主題目 B；兩項均未達標則終止轉顧問諮詢模式
- **執行對口與啟動條件**
  - **主對口**：Mask Operation + Overlay Metrology 部門
  - **次對口**：Litho PIE + APC 系統 owner
  - **啟動條件**：NTUST 產學合約確認（Q3-Q4）+ N2 dummy mask 資料授權（NDA）+ kick-off 三方（郭鴻飛 / Mask Operation / Litho PIE）
- **風險與緩解**
  - **競業 / IP**：郭鴻飛無公開外部競業綁定；IP 依 NTUST 標準框架，風險低
  - **學術深度 vs 量產 SOP 落差**：Mask Optimization 研究以理論演算法為主，落入 TSMC 量產 OPC flow 需 Litho PIE 工程師共同定義邊界條件；建議初期安排 3-6 個月 embedded engineer 橋接
  - **行政負擔**：郭鴻飛現兼所長 + 副院長 + 中心主任三職，啟動時程須配合行政週期；建議 Q3 以前完成 MOU，避免學年初行政壅塞
  - **學生流向**：現有學生流向 TSMC / 南亞科 / 應材為非正式通道，制度化後流向風險低；南亞科 / 應材為互補而非競業
  - **能力限制**：WebSearch 無法驗證郭鴻飛與 TSMC 現有直接合作細節（公開資料缺乏廠內合作記錄）；建議由 TSMC Mask Operation 或 Litho PIE 主管做內部 warm intro 後啟動洽談
- **連結**：[NTUST GSAC 個人頁](https://gsac-r.ntust.edu.tw/p/404-1020-76568.php?Lang=en) ｜ [NTUST GSAC 首頁](https://www.gsac.ntust.edu.tw/index.php?Lang=en) ｜ 代表研究方向：Mask Optimization / Overlay Metrology / OPC 補強 / 先進製造控制（APC）

---

### A21. 高宏宇（Hung-Yu Kao）｜總分 **7.3**（A 級）｜第二波（2026 站穩可啟動）

| 校系職級 | NTHU 資訊系統與應用研究所（ISA）+ 兼資訊工程系（CS）｜ 正教授（Full Professor，2024/8 從 NCKU 維持等級轉校）｜ PhD: NTU 電機工程 2003 |
|---|---|
| 學術指標 | h-31 / 引用 5,106（GS）/ i10-73；ACL 2025 main；EMNLP 2023 Findings |
| Lab | IKMLab @ NTHU ISA |
| **5 維度評分** | 研究 8 ｜ fab 7 ｜ Lab 7 ｜ 接洽 9 ｜ 長期 8 ｜ ACL/EMNLP 頂會 + 跨 domain 方法論 + 正教授盛年 |

**核心專長 × 近 3 年代表實績**
- Retrieval Domain Adaptation / RAG（Retrieval-Augmented Generation）/ Hallucination Detection / 中文 NLP
- ACL 2025 main；EMNLP 2023 Findings "Breaking Boundaries in Retrieval Systems"；TAICA 跨校 NLP 課程 400 人；2024/8 NCKU 正教授 11 年 → NTHU 正教授（母校）
- ACL 2025 main；EMNLP 2023 Findings；NTHU CS 1994 首屆畢業

**製程/封裝應用點（詳述）**

- **節點 / 段別**：跨節點（N3 / N2 / A16）製程與封裝段；應用場域為 TSMC 內部知識管理系統 / 工程師工作輔助層（CIM / MES 介面、製程文件檢索、設備 SOP 知識庫、良率分析報告生成）；技術層次在 NLP / RAG / Domain Adaptation，非直接製程設備干預
- **痛點對應**：
  - **製程文件跨域幻覺率高**：TSMC 工程師使用通用 LLM 查詢製程規格 / 材料屬性 / 設備參數時，模型在 semiconductor-specific domain 的幻覺率（hallucination）居高不下，錯誤引用風險大；高宏宇 EMNLP 2023「Breaking Boundaries in Retrieval Systems」直接命中 Retrieval Domain Adaptation 痛點，可建立半導體域 RAG 基礎架構降低幻覺
  - **跨廠區 SOP 文件檢索效率低**：竹科 / 南科 / 高雄多廠區的設備 SOP、製程參數文件分散，工程師跨廠查詢耗時；域適應 RAG 可建立統一檢索層，自動對齊各廠文件格式差異
  - **中文工程文件 NLP 弱化**：TSMC 大量中英混合的製程日誌、ECN（Engineering Change Notice）、DR（Defect Review）報告缺乏結構化解析工具；高宏宇中文 NLP 研究可補強此弱點，提高日誌自動分類與摘要精度
  - **新進工程師知識傳承斷鏈**：資深工程師退休後製程 know-how 難以系統化傳承；RAG-based 知識圖譜可將隱性知識顯式化，降低知識衰退風險
- **可導入時程（TRL）**：**TRL 4-6 / 9-15 個月啟動 PoC**；RAG 框架已有 ACL / EMNLP 頂會驗證（學術基礎紮實，TRL 5-6），需接入 TSMC 內部文件語料庫（保密協議後）進行域適應微調；高宏宇 2024/8 剛轉 NTHU 立腳，2025 下半年 Lab 重建完成後啟動最佳
- **配合 fab 部門**：CIM / MES 系統 owner（製程知識管理）為主對口；設備工程（Equipment Engineering）知識庫 owner / 良率工程（Yield Engineering）文件管理為次對口；可與 NLP 群（cross-ref：A30 馬席彬 — 若有 RAG / 知識圖譜方向）協作形成 NLP 群方法論共池
- **預期成效**：
  - RAG 半導體域問答幻覺率相較通用 LLM baseline 降低 ≥ 40%（domain-specific benchmark）
  - 製程文件跨廠檢索響應時間縮短 ≥ 50%（多廠區統一檢索層）
  - 中文工程日誌自動分類 F1 ≥ 0.85（對比人工標注 baseline）
  - 每年聯名論文 ≥ 1 篇（ACL / EMNLP / NAACL）
  - 2026-2027 第一批博士生畢業後可導入 TSMC 研究職通道

**合作紀錄 × 與外部公司狀況**
- 無綁定；NTHU 資工 1994 首屆畢業
- **無公開可見外部綁定**；Lab 重建中，第一批博生 2026-2027 畢業

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — 半導體製程域 RAG 知識庫**：以 EMNLP 2023 Retrieval Domain Adaptation 方法論為基礎，建立 TSMC 製程文件域適應 RAG 系統；目標幻覺率降低 ≥ 40%，覆蓋設備 SOP / 製程規格 / ECN 三類文件（cross-ref：A30 馬席彬若有 RAG 群可串方法論）
  - **主題目 B — 中英混合工程日誌 NLP 結構化解析**：以高宏宇中文 NLP 研究為基礎，建立 CIM / MES 系統的日誌自動分類 + 摘要 + 異常標記流水線；直接接入 TSMC 現有 MES 架構
  - **延伸題目 C — 跨廠區知識圖譜 + 工程師問答助理**：整合主題目 A / B 成果，建立 TSMC 多廠區工程知識圖譜；提供工程師自然語言查詢介面（LLM + RAG + KG 三層架構）
- **制度與簽約**
  - **架構**：NTHU IKMLab 一般產學合作（掛 ISA 研究所）+ NSTC RAISE 產學合創計畫並軌（高宏宇正教授資格可主導 NSTC）；建議 2025 下半年啟動 PoC，2026 上半年正式簽約
  - **預算建議區間**：年 NT$ 1,000-1,500 萬（含學生獎助 + GPU 算力 + 教師研究費 + 文件語料授權處理費）；3 年滾動（推估區間，非承諾數字，依 NTHU ISA 同規模產學計畫對標）
  - **簽約對象**：NTHU 研究發展處（機構）+ 高宏宇 PI（個人委案）雙軌；語料 IP 歸屬需特別約定（TSMC 製程文件屬 TSMC IP，高宏宇 Lab 僅取得研究授權，衍生模型 IP 依比例分配）
  - **學生通道**：IKMLab 第一批博士生預計 2026-2027 畢業，可規劃 TSMC 研究職定向推薦；NTHU TAICA 跨校 NLP 課程（400 人規模）可作 TSMC 廣泛招募觸及點
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：半導體域 RAG PoC 在 TSMC shadow 文件集上幻覺率降低 ≥ 20%（相對 baseline）；中文日誌分類 F1 ≥ 0.80 in internal benchmark；ACL / EMNLP 聯名投稿 ≥ 1 篇
  - **第 2 年**：RAG 系統升至 pilot mode（特定廠區試用）；日誌 NLP 流水線接入 CIM / MES 測試環境；跨廠區知識圖譜 prototype 完成；IKMLab 第一批博士生進入 TSMC 實習通道
  - **第 3 年**：RAG 知識庫覆蓋竹科 / 南科雙廠區；工程師問答助理完成 1 個部門正式上線；幻覺率降低達 ≥ 40% 量產 benchmark；模型移交 CIM / MES 系統 owner 維運
  - **Exit criteria**：第 1 年幻覺率降低 ＜ 10% 即重新評估 domain adaptation 策略；日誌分類 F1 ＜ 0.70 則暫緩主題目 B；兩項均未達標且第 2 年無改善趨勢則終止，轉為方法論顧問合作
- **執行對口與啟動條件**
  - **主對口**：CIM / MES 系統 owner（製程知識管理部門）
  - **次對口**：設備工程（Equipment Engineering）知識庫 owner；良率工程（Yield Engineering）文件管理
  - **啟動條件**：文件語料授權 NDA 簽署（含中英混合 SOP / ECN 樣本）+ NTHU IKMLab 第二學期 Lab 重建確認（2025/02）+ 三方 kick-off（高宏宇 / CIM owner / TSMC 資訊長辦公室）
- **風險與緩解**
  - **競業 / IP**：高宏宇無公開外部競業綁定；語料 IP 需特別約定（TSMC 文件不得用於外部公開訓練），建議合約明訂模型訓練僅限 TSMC 內部 private corpus
  - **Lab 重建期風險**：2024/8 剛轉 NTHU，Lab 成員尚在招募中，第一批博士生 2026-2027 才畢業；建議初期以方法論 PoC（PI + RA 2-3 人小組）啟動，不依賴大 Lab 規模
  - **學術深度 vs 量產 SOP 落差**：高宏宇強項在 NLP 方法論，半導體製程域知識需 TSMC 工程師協同標注；建議安排 domain expert annotator pool（TSMC 內部工程師兼職）彌補落差
  - **學生流向**：IKMLab 方向偏 NLP / AI，競爭者為 Google / Meta / 科技大廠 NLP 組；建議以研究職 offer + NLP-in-semiconductor 差異化定位吸引優秀博士生
  - **能力限制**：WebSearch 無法驗證高宏宇轉 NTHU 後的 Lab 實際運作規模與現有學生人數；建議洽談前請 NTHU ISA 所辦確認現況
- **連結**：[NTHU ISA 公告](https://isa.site.nthu.edu.tw/p/406-1182-272217,r4919.php?Lang=en) ｜ [IKMLab](https://ikmlab.cs.nthu.edu.tw/advisor.html) ｜ [Google Scholar](https://scholar.google.com/citations?user=X5Is2lAAAAAJ&hl=en) ｜ [ORCID](https://orcid.org/0000-0002-8890-8544) ｜ [NCKU 原教師頁](https://www.csie.ncku.edu.tw/zh-hant/members/28)

---

### A22. 張耀文（Yao-Wen Chang）｜總分 **7.3**（A 級，觀察名單）｜觀察（2027 獨董卸任後升 S）

| 校系職級 | NTU 電機系 / 電子所 EDA Lab BL-406 ｜ 特聘教授（Distinguished Professor）；EECS 院長 2018-2024 卸任 ｜ PhD: University of Texas at Austin Dept. of Computer Sciences 1996 |
|---|---|
| 學術指標 | h-58 / 引用 12,544；IEEE Fellow 2013（VLSI 實體設計）；ACM Fellow 2020（算法 EDA）|
| Lab | EDA Lab BL-406；2023 年發表 8 篇創個人紀錄；NTUplace4 = Synopsys MaxPlace 核心引擎 |
| **5 維度評分** | 研究 10 ｜ fab 9 ｜ Lab 9 ｜ 接洽 1 ｜ 長期 7 ｜ IEEE+ACM Fellow + EDA 世界級 + 競業獨董（MediaTek） |

**核心專長 × 近 3 年代表實績**
- EDA（Electronic Design Automation）/ Placement 佈局演算法 / Routing 繞線演算法 / DFM（Design for Manufacturing）
- 2024 IEEE CAD Contest @ ICCAD 多位元 Flip-Flop 功耗時序優化冠軍；2023 IEEE CAD Contest 3D Placement with Macros 冠軍；DAC / ICCAD 一作 30 年穩定產出（DAC 全球累積 95 篇排名第一）；IEEE Fellow 2013 + ACM Fellow 2020；NTU EDA 研究中心前主任
- IEEE Fellow 2013；ACM Fellow 2020；NTU EECS 院長 2018-2024

**製程/封裝應用點（詳述）**

> ⚠️ **狀態提示**：張耀文現任 MediaTek 獨立董事（2024/05 — 2027/05），任期內暫不啟動合作。以下應用點分析為 2027 卸任後立即啟動之預備文件，供主管 2027 年前預先評估。

- **節點 / 段別**：N2（2nm）/ A16（1.4nm）/ A14（1.2nm）前段設計段；EDA 全流程（Physical Design）— Placement 佈局演算法 / Routing 繞線演算法 / 3D-IC 佈局 / DFM 後段；以及 CoWoS / SoIC 3D 封裝層的 Chiplet 佈局自動化
- **痛點對應**：
  - **N2 / A16 全晶片 Placement runtime 爆炸**：N2 進入 multi-patterning + sub-7nm pitch 後，商用 P&R 工具（Synopsys IC Compiler / Cadence Innovus）全晶片 runtime 動輒 3-6 週；張耀文 NTUplace4 引擎（已授權給 Synopsys MaxPlace）是目前學術界最接近量產等級的 placement 核心，DAC 全球累積 95 篇第一的方法論深度可直接切入 N2 P&R bottleneck
  - **3D-IC Macro 佈局無自動化工具**：2023 IEEE CAD Contest 冠軍題目即為「3D Placement with Macros」，直接對應 CoWoS / SoIC chiplet 在 3D 堆疊時的 Macro 定位與 TSV 間距最佳化痛點；現有商用工具尚無成熟 3D Macro placement solution
  - **多位元 Flip-Flop 功耗時序聯合優化**：2024 IEEE CAD Contest 冠軍題目（多位元 Flip-Flop 功耗時序優化）命中 N2 / A16 標準元件庫設計最佳化痛點；可降低先進節點 clock tree 功耗 5-10%（估）
  - **DFM hotspot 修補工具缺口**：N2 DFM 規則 2,000+ 條後，rule-based DRC 修補效率下降；張耀文 EDA 方法論可提供 placement-aware DFM hotspot 預防層（與 S02 江蕙如 / A23 李淑敏 EDA 群串題，cross-ref）
- **可導入時程（TRL）**：**TRL 7-9 / 2027 卸任後 3-6 個月啟動 PoC**；NTUplace4 已有量產授權先例（Synopsys MaxPlace），屬高 TRL 成熟技術；3D Placement 為 TRL 6-7（CAD Contest 驗證），需接入 TSMC 真實 CoWoS 設計包做 PoC；獨董任期內完全封存，2027/05 卸任後立即可啟動
- **配合 fab 部門**：設計實現（Design Enablement / DE）+ EDA 工具規格 owner 為主對口；CoWoS / 3D-IC 封裝整合（Advanced Packaging）為次對口；聯合 EDA 群（S02 江蕙如 / A23 李淑敏 / A25 李建模）形成 N2 Physical Design 完整覆蓋（cross-ref）
- **預期成效**：
  - N2 全晶片 Placement runtime 降幅 ≥ 25%（NTUplace4 方法論延伸，相較商用工具 baseline）
  - 3D Macro Placement in CoWoS 自動化覆蓋率達 ≥ 80%（現況幾乎全人工）
  - 多位元 FF 優化後 clock tree 功耗降幅 ≥ 5%（A16 標準元件庫試算）
  - DFM hotspot 漏補率改善 ≥ 20%（與 S02 江蕙如串聯情境）
  - 每年聯名論文 ≥ 2 篇（DAC / ICCAD，對應張耀文 30 年穩定產出量）

**合作紀錄 × 與外部公司狀況**
- 長期與 TSMC 合作（pre-獨董時期）；Synopsys / Cadence 工具合作；MediaTek 獨立董事（2024/05-）
- **MediaTek 獨立董事**（2024/05- 就任，任期 3 年至 2027）— 競業 IC 設計公司，法務 IP 邊界複雜

**建議合作方式 × 公開連結**

> ⚠️ **凍結合作 / 2027 卸任後立即升 S 級啟動**
>
> MediaTek 獨立董事任期：2024/05 — 2027/05（3 年任期）。任期內與 TSMC 啟動正式合作案涉及競業敏感（MediaTek 為 TSMC 主要客戶且屬 IC 設計公司，獨董負有保密與迴避義務），法務建議封存。2027/05 卸任後無冷卻期法律限制（一般董事需 1 年冷卻，獨立董事依公司章程），建議卸任當季即啟動洽談。

- **題目（2027/05 後啟動）**
  - **主題目 A — N2 / A16 全晶片 Placement 加速**：以 NTUplace4 方法論延伸開發 N2 AI-enhanced placement engine，接續 2024 IEEE CAD Contest 多位元 FF 優化成果；與 S02 江蕙如 GNN P&R 串聯，形成 NTU EDA 雙 PI 聯合題（cross-ref：S02 江蕙如 / A25 李建模）
  - **主題目 B — CoWoS / SoIC 3D Macro Placement 自動化**：接續 2023 IEEE CAD Contest 3D Placement with Macros 冠軍技術，開發 TSMC CoWoS / SoIC 3D 堆疊的 Macro 自動佈局工具；此題為 Advanced Packaging 當前最缺工具鏈的空白地帶
  - **延伸題目 C — DFM-aware Placement 前置防護層**：將 placement 階段的 DFM hotspot 風險評估前移，與 S02 江蕙如 Transformer DFM + A23 李淑敏 Defect Pattern 串成 Design → Defect end-to-end 防護鏈（cross-ref：S02 / A23 / A25 EDA 群）
- **制度與簽約（2027/05 後）**
  - **架構**：NTU EDA Lab BL-406 直屬委案（JDP）+ NSTC RAISE 旗艦產學計畫並軌；建議以 S 級規格啟動（Chair Endowment 或等值框架），體現 IEEE+ACM 雙 Fellow 等級
  - **預算建議區間**：年 NT$ 3,000-5,000 萬（含 PhD Scholarship × 5 名 + GPU cluster + 工具 license + 教師研究費 + tape-out 試片）；3+2 年滾動（推估區間，非承諾數字，依 NTU EE 同規模旗艦 JDP 對標，如台大-台積 N2 旗艦合作規模）
  - **簽約對象**：NTU 研發處（NTU OTT）+ 張耀文 PI（個人委案）雙軌；IP 依 NTU OTT 標準協議，NTUplace4 延伸衍生物 IP 歸屬需個案談判（現有 MaxPlace 授權先例可參考）
  - **學生通道**：NTU EDA Lab 博士生品質最高（DAC / ICCAD 一作為常態）；建議 PhD Scholarship × 3-5 名 + TSMC 研究職定向推薦；EECS 院長（2018-2024）人脈可加速學生招募
- **KPI（2027/05 後第 1-3 年）**
  - **2027/05 後第 1 年**：N2 placement engine PoC 完成；CoWoS Macro Placement 工具在 1 個 CoWoS 設計包上驗證覆蓋率 ≥ 60%；NTU EDA Lab 聯名 DAC / ICCAD 論文 ≥ 2 篇；PhD Scholarship 首批 3 名到位
  - **2027/05 後第 2 年**：N2 placement runtime 降幅 ≥ 20%（對比商用工具量產 benchmark）；3D Macro Placement 工具升至 pilot 版（特定 CoWoS 設計流程試用）；DFM-aware placement 前置防護層完成 S02 串聯 PoC
  - **2027/05 後第 3 年**：N2 / A16 placement engine 移交 Design Enablement 整合；3D Macro 工具接入 Advanced Packaging 正式流程；A14 節點延伸啟動；NTU EDA Lab 博士生轉任 TSMC 研究職 ≥ 3 人
  - **Exit criteria**：第 1 年 CoWoS 覆蓋率 ＜ 40% 且 placement runtime 降幅 ＜ 10% 同時發生，則重新評估方法論路徑；任一主題目連續 2 年 KPI 未達 60% 則降為延伸題目，縮減預算
- **執行對口與啟動條件**
  - **主對口**：Design Enablement（DE）/ EDA 工具規格 owner
  - **次對口**：Advanced Packaging（CoWoS / SoIC）整合部門；Litho PIE（DFM context 提供方）
  - **啟動條件**：2027/05 獨董任期確認屆滿 + 法務清廉查核（競業迴避確認）+ 當季洽談 kick-off + NTU OTT 合約起草 + CoWoS 設計包 NDA 授權
- **風險與緩解**
  - **競業 / IP（核心風險）**：MediaTek 獨立董事任期 2027/05 前，任何正式合作均有競業疑慮（MediaTek 是 TSMC 重要客戶，獨董負保密義務）；**任期內嚴禁啟動任何正式協議**，包含非正式口頭意向書（LOI）；法務建議封存並在 2027/04 提前內部預熱（僅內部評估，無對外接觸）
  - **NTUplace4 / MaxPlace IP 邊界**：NTUplace4 延伸衍生物與 Synopsys MaxPlace 現有授權邊界需由 NTU OTT + TSMC 法務 + Synopsys 三方確認，避免侵權；建議合約起草前先做 Freedom-to-Operate（FTO）分析
  - **學術深度 vs 量產 SOP 落差**：張耀文方法論深度極高但量產 SOP 對接需 DE 工程師密集協作；NTUplace4 有 Synopsys 商業化先例，落差相對可控
  - **學生流向**：NTU EDA Lab 博士生競爭者為 Synopsys / Cadence / Google EDA 研究組；建議以 TSMC 研究職（Research Scientist）+ 薪資競爭力 + 台灣在地優勢應對
  - **能力限制**：WebSearch 無法驗證 MediaTek 獨董合約的具體保密條款範圍及 TSMC 法務對此案的內部評估結論；建議正式洽談前由 TSMC 法務部門做競業合規評估，並請 MediaTek / NTU 三方法律確認無利益衝突
- **連結**：[NTU EE 傳記頁](https://www.ee.ntu.edu.tw/bio1.php?id=69) ｜ [個人首頁](https://cc.ee.ntu.edu.tw/~ywchang/) ｜ [Google Scholar](https://scholar.google.com/citations?user=qKJ_7jAAAAAJ&hl=en) ｜ [IEEE CEDA 頁面](https://ieee-ceda.org/contact/yao-wen-chang) ｜ [ACM 數字圖書館](https://dl.acm.org/profile/81408595786)

---

### A23. 李淑敏（Katherine Shu-Min Li）｜總分 **7.3**（A 級）｜第二波

| 校系職級 | NSYSU 資工系 教授（2015 升等）+ 積體電路設計研究所（IICD）兼聘 ｜ 教授 ｜ PhD: NCTU 電子工程研究所（年份待核實，約 2000s 初）；BS Rutgers 資工 |
|---|---|
| 學術指標 | IEEE Senior Member 2014（非 Fellow）；2016 IEEE Education Society VanValkenburg Award |
| Lab | EDA&T Lab（電子設計自動化與測試實驗室）|
| **5 維度評分** | 研究 8 ｜ fab 8 ｜ Lab 7 ｜ 接洽 7 ｜ 長期 8 ｜ EDA 旗手 + 南台灣對口 + 工具合作（Synopsys/Cadence 弱綁定） |

**核心專長 × 近 3 年代表實績**
- AI-EDA / HDL Automation 硬體描述語言自動化 / DfT（Design for Testability）/ 南台灣 EDA 對口
- IEEE TCAD 2024 "Reinforcement Learning Double DQN for Chip-Level Synthesis of Paper-Based Digital Microfluidic Biochips"；IEEE TSM 2022 "Wafer Defect Pattern Labeling and Recognition Using Semi-supervised Learning"；IEEE TSM 2022 "TestDNA-E: Wafer Defect Signature for Pattern Recognition by Ensemble Learning"；南台灣 EDA 對口（TSMC 高雄 2nm 周邊）
- IEEE Senior Member 2014；2016 IEEE Education Society VanValkenburg Award

**製程/封裝應用點（詳述）**

- **節點 / 段別**：N2（2nm）/ A16（1.4nm）前段設計段；EDA 流程 + DfT（Design for Testability）/ HDL 自動化；以及 Microfluidic Biochip 端的生物晶片設計自動化（BDA）；重心在南台灣（高雄、台南）TSMC 2nm fab 周邊的 EDA 人才與工具供應
- **痛點對應**：
  - **HDL 自動化 RTL-to-GDS 落差**：N2 先進節點中 RTL 至 GDS 過程規則爆炸（設計規則 2,000+），人工 HDL 編修錯誤率高；李淑敏 DQN-based HDL 自動合成可作 RTL-level sanity check，降低人工介入錯誤率
  - **Wafer Defect Pattern 識別不足**：IEEE TSM 2022 兩篇一作直接命中 Wafer Defect 識別痛點（Semi-supervised + Ensemble Learning），可補強現有 YM（Yield Management）系統中 pattern 辨識弱區
  - **南台灣 EDA 人才缺口**：TSMC 高雄 2nm fab 擴建期間，南部在地 EDA 師資與訓練管道稀缺；NSYSU EDA&T Lab 是南台灣最具規模的 EDA 學術據點，具地緣與生態優勢
  - **Biochip 跨界整合**：IEEE TCAD 2024 RL DQN for Microfluidic Biochip 一作，可延伸至 TSMC 醫療 / 生技晶片客戶合作場景（非核心量產題，但具差異化定位）
- **可導入時程（TRL）**：**TRL 5-6 / 6-12 個月啟動 PoC**；Wafer Defect Pattern 系列已有 IEEE TSM 頂會驗證，需接入 TSMC 南科 YM 系統實際資料集做 benchmark；HDL 自動合成處於學術驗證階段（TRL 4-5），需 6-12 個月 PoC 橋接
- **配合 fab 部門**：南科良率管理（YM）/ 缺陷偵測（Defect Inspection）部門為主對口；設計實現（Design Enablement）/ EDA 規則 owner 為次對口；NSYSU SAT 中心（若與 S01 串題）為跨組整合點
- **預期成效**：
  - Wafer Defect Pattern 識別 F1 分數相較現有 rule-based 系統提升 ≥ 15%（Semi-supervised + Ensemble 合用）
  - HDL 自動化 RTL 修訂週期縮短 ≥ 20%（DQN proxy 篩選效益）
  - 南台灣在地碩博士生進入 TSMC 南科 / 高雄 fab 比例提升（教師地緣優勢）
  - 每年聯名論文 ≥ 1 篇（IEEE TSM / TCAD）

**合作紀錄 × 與外部公司狀況**
- Synopsys / Cadence 弱綁定（工具合作，非人事）
- Synopsys / Cadence 為工具層面合作，**非人事綁定**，不影響 TSMC 合作

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — Wafer Defect Pattern ML 強化**：接續 IEEE TSM 2022 Semi-supervised + Ensemble 系列，導入 TSMC 南科 YM 系統，建立 defect pattern 自動分類 + 異常告警強化模組；與 EDA 群（S02 江蕙如 / A22 張耀文 / A25 李建模）形成 Design ↔ Defect end-to-end 閉環
  - **主題目 B — HDL 自動合成 DQN 代理**：以 IEEE TCAD 2024 RL DQN 方法論延伸至 TSMC N2 設計規則 context，建立 HDL 自動修訂 + DRC pre-check 前置工具；縮短 tape-out 前 RTL 手改循環（cross-ref：A25 李建模 DFT 串接可能）
  - **延伸題目 C — 南台灣 EDA 人才管道建設**：建立 NSYSU EDA&T Lab → TSMC 高雄 / 南科 定向實習通道；配合 SAT 中心擴增南部 EDA 訓練容量（若與 S01 王俊明 SAT 通道合并）
- **制度與簽約**
  - **架構**：NSYSU 一般產學合約（IICD 機構掛單）+ PI 個人委案雙軌；無需新立 MOU（NSYSU 已有產學合作框架）
  - **預算建議區間**：年 NT$ 1,000-1,500 萬（含學生獎助 + EDA 工具 license + 教師研究費）；3 年滾動（推估區間，非承諾數字，依 NSYSU 產學既有量級對標）
  - **簽約對象**：NSYSU IICD（機構）+ 李淑敏（個人 PI）；IP 依 NSYSU 標準歸屬框架
  - **學生通道**：NSYSU → 南科 / 高雄 fab 地緣招募通道；可配合台積獎學金申請
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：Wafer Defect Pattern 模型在 TSMC 南科 shadow mode 測試；F1 提升 ≥ 10%；HDL DQN 代理完成 N2 benchmark cell PoC；聯名 IEEE TSM 或 TCAD 投稿 1 篇
  - **第 2 年**：Defect Pattern 系統升至 advisory mode；HDL 代理工具完成 1 條 N2 tape-out 輔助驗證；南部學生進入 TSMC 通道人數 ≥ 3 人
  - **第 3 年**：Defect Pattern 模組接入南科 YM 正式平台；HDL 自動化工具完成 1 個量產品系驗收；延伸 Biochip 題目視醫療晶片客戶需求啟動 PoC
  - **Exit criteria**：第 1 年 Defect F1 提升 < 5%，終止主題目 A 調整方向；HDL PoC 未通過 benchmark 則暫緩主題目 B
- **執行對口與啟動條件**
  - **主對口**：南科 YM 部門 / Defect Inspection 工程師
  - **次對口**：Design Enablement / EDA 規則 owner；NSYSU SAT 中心（S01 協同窗口）
  - **啟動條件**：NSYSU 產學合約確認 + Q1 kick-off（李淑敏 / YM 部門 / IICD）+ 學生暑期實習名額 alignment
- **風險與緩解**
  - **競業 / IP**：Synopsys / Cadence 為工具合作（非人事綁定），不構成競業；IP 依 NSYSU 標準框架，風險低
  - **學術深度 vs 量產 SOP 落差**：李淑敏 IEEE TSM 論文已有量產導向（Wafer 資料集），落差相對小；HDL 自動化部分需 TSMC 工程師共同定義規則邊界
  - **學生流向**：NSYSU 南台灣地緣優勢，學生以南科 / 高雄 fab 為主要 target，流向風險低
  - **能力限制**：WebSearch 無法驗證李淑敏與 TSMC 現有直接合作紀錄（公開資料缺乏廠內合作細節）；建議洽談前先由 TSMC 南科 EDA 窗口做內部 warm intro
- **連結**：[NSYSU CSE 教師頁](https://cse.nsysu.edu.tw/p/412-1205-19760.php?Lang=en) ｜ [NSYSU IICD 教師頁](https://iicd.nsysu.edu.tw/p/404-1355-321795.php?Lang=en) ｜ [EDA&T Lab](https://edat.cse.nsysu.edu.tw/main.html) ｜ 代表論文：IEEE TCAD 2024 DQN Microfluidic Biochip / IEEE TSM 2022 Wafer Defect Pattern Semi-supervised + TestDNA-E

---

### A24. 鄭芳田（Fan-Tien Cheng）｜總分 **7.3**（A 級，戰略顧問定位）｜觀察（師徒包搭配 S10 謝昱銘）

| 校系職級 | NCKU IMIS 名譽教授 + iMRC 執行長（CEO 掛名，蕭弘昌實質執行）｜ 名譽教授（2024/01/31 退休，非 2023）｜ PhD: Ohio State University 電機工程 1989（非機械）|
|---|---|
| 學術指標 | h-41 / 引用 6,074；IEEE Life Fellow（2008 → 2021 升 Life Fellow）|
| Lab | iMRC（2018 設立）；63 件技轉 / NT$2.7 億授權金 |
| **5 維度評分** | 研究 9 ｜ fab 10 ｜ Lab 6 ｜ 接洽 8 ｜ 長期 2 ｜ IYM 系統發明 + 63 件技轉 + 顧問職 + 72 歲已退休 |

**核心專長 × 近 3 年代表實績**
- AVM（Automatic Virtual Metrology）系統發明人 / IYM（Intelligent Yield Management）系統創始者 / 系統架構 + IP 繼承諮詢
- US12354122B2 共同發明人；累計 63 件技術移轉 / NT$2.7 億授權金；TSMC 終生合作夥伴（1998-）；2024/01/31 退休，現任 iMRC 執行長；2024 經濟部國家產業創新獎：產學貢獻獎；2024 國家發明創作獎：發明類銀牌；教科書《Industry 4.1: Intelligent Manufacturing with Zero Defects》英文版 2021 / 中文版 2023
- IEEE Life Fellow；2024 經濟部國家產業創新獎：產學貢獻獎；2024 國家發明創作獎：發明類銀牌

**製程/封裝應用點（詳述）**

- **節點 / 段別**：全節點（N3/N2/A16 及以後）；製程管控層（AVM / IYM 架構層）；定位為方法論顧問而非執行 PI — 提供 IYM 系統架構設計、IP 使用邊界釐清、接班路徑諮詢，不主導大規模廠內實驗
- **痛點對應**：
  - **IYM 系統 IP 邊界模糊**：63 件技轉 + NT$2.7 億授權金背後有複雜 IP 歸屬層次；N2/A16 導入新製程段時需確認既有 IYM IP 是否自動覆蓋或需補簽協議；鄭芳田本人是 IP 最高解釋權人
  - **AVM / VM 接班知識落差**：AVM 系統架構深度仍在創始人腦中（隱性知識），S10 謝昱銘為第一接班人，但需系統性師承機制；顧問框架可結構化知識移轉
  - **SPC 群方法論整合**：IYM 系統橫跨 VM / SPC / YM 三層，與 SPC 群（S07/S10/A19/A16/B37/B45）協作時需架構層協調人，鄭芳田是唯一能從整體框架角度協調的人選
  - **新製程段 IYM 延伸設計**：A16/A14 等後進節點的 AVM 模組設計需顧問指引（現有 iMRC TRL 尚未延伸至 A16 以後）
- **可導入時程（TRL）**：**顧問即啟動**（不需 PoC）— 顧問性質；合約 Q1 可生效，每季 4-8 次諮詢（in-person 或遠端）；知識移轉至 S10 謝昱銘的執行 PI 框架，再進入 TRL 6-7 驗證
- **配合 fab 部門**：TSMC AMEM（先進製造設備技術）/ iMRC 系統對口為主對口；VM / SPC 系統架構 owner 為次對口；SPC 群各 PI 為跨組協調點（cross-ref：S07/S10/A19）
- **預期成效**（顧問框架，以定性指標為主）：
  - IYM IP 邊界釐清文件完成，N2/A16 新製程段適用範圍確認（第 1 年）
  - 謝昱銘（S10）接班路徑正式確立（師徒包架構落地）
  - SPC 群方法論整合指引文件 ≥ 2 份（AVM 架構層 × 各群 PI 執行層對接）
  - 顧問期間協助鑑別並規避至少 1 個 IYM IP 潛在衝突場景

**合作紀錄 × 與外部公司狀況**
- TSMC 終生合作夥伴（自 1998 起）；多家半導體廠技轉 63 件
- 72 歲已退休；iMRC 執行長為制度性顧問職，**非競業綁定**

**建議合作方式 × 公開連結**

- **題目**
  - **主顧問職能 A — IYM 架構諮詢 + IP 邊界釐清**：以 TSMC 戰略顧問身份，就 N2/A16 及後進節點的 IYM / AVM 系統延伸提供架構設計諮詢；釐清 63 件技轉 IP 在新製程段的適用邊界，避免 TSMC 工程師在 iMRC 合作中踩 IP 灰色地帶
  - **主顧問職能 B — 師徒包框架設計與監督**：監督 S10 謝昱銘執行 PI 計畫；每季提供方法論回饋（VM 模型架構 / KSA 方法論 / SPC 群協作）；確保接班知識移轉完整
  - **延伸顧問職能 C — SPC 群跨 PI 方法論整合**：在 SPC 群（S07/S10/A19/A16/B37/B45）多 PI 合作體系中擔任方法論仲裁人，協調不同 PI 產出在 IYM 系統層的相容性（cross-ref：S07/S10/A19）
- **制度與簽約**
  - **架構**：獨立戰略顧問合約（個人合約，非機構合約）；與 S10 謝昱銘「師徒包」雙軌並行（謝昱銘執行 PI 合約另立）
  - **預算建議區間**：顧問年費 NT$ 100-200 萬（每年 8-12 次深度諮詢）× 5 年期；搭配 S10 謝昱銘執行 PI 年 NT$ 800-1,500 萬（推估區間，非承諾數字，依 NCKU iMRC 既有顧問費量級對標）
  - **簽約對象**：鄭芳田個人（名義上可掛靠 iMRC，但顧問費直接給付個人）
  - **時間投入**：每月 2-4 小時 in-person 或視訊；退休後時間彈性，但不宜要求廠內長時間駐點
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：IYM IP 邊界白皮書完成；師徒包框架正式確立（合約 + kick-off 會議）；協助謝昱銘 VM Concept Drift 框架完成 TSMC shadow mode 驗證設計
  - **第 2 年**：謝昱銘執行 PI 通過第 1 年 KPI（MAPE 降幅 ≥ 10%）；IYM 延伸至 1 個新製程段方案提交
  - **第 3-5 年**：知識移轉完整度評估（謝昱銘可獨立主持 SPC 群協調）；顧問費可視移轉完成度調降
  - **Exit criteria**：鄭芳田因健康 / 個人因素無法達每季 2 次諮詢，師徒包需提前評估謝昱銘獨立能力；顧問費支出 > NT$ 1,200 萬 / 年但無明確 IP 釐清產出則重評
- **執行對口與啟動條件**
  - **主對口**：TSMC AMEM 系統負責人 / iMRC 對口窗口
  - **次對口**：VM/SPC 系統 owner；謝昱銘（S10）執行 PI 協調
  - **啟動條件**：鄭芳田個人顧問意願確認（建議由 TSMC 高管直接接觸）+ iMRC 既有 MOU 確認延伸 + 師徒包 Q1 三方 kick-off
- **風險與緩解**
  - **退休後時間有限**：2024/01/31 已退休，iMRC 執行長為掛名職；實際可投入諮詢時間有限（每月 2-4 小時較為合理）；避免要求大量廠內實驗指導
  - **健康風險**：72 歲，長期顧問合約需有接班安排（謝昱銘接班機制本身即為緩解方案）
  - **競業 / IP**：iMRC 執行長為顧問性質，非競業綁定；63 件技轉有既有授權框架，IP 釐清本身是合作目標而非障礙
  - **能力限制**：WebSearch 無法確認鄭芳田退休後的諮詢投入意願；建議由 TSMC 高管層級（VP 以上）直接致意，提高接受機率
- **連結**：[NCKU CSIE 師資頁](https://www.csie.ncku.edu.tw/zh-hant/members/14) ｜ [NCKU Research Output](https://researchoutput.ncku.edu.tw/zh/persons/fan-tien-cheng/) ｜ [iMRC 官網](https://imrc.ncku.edu.tw/) ｜ [Google Scholar](https://scholar.google.com/citations?user=m9IzwP8AAAAJ&hl=en) ｜ [NSTC 學術研究獎項頁](https://web.nstc.gov.tw/cen/oaa/award_111/website/Fan-Tien-Cheng.html) ｜ 代表：US12354122B2 共同發明人 / 教科書 Industry 4.1（2021 英文版）

---

### A25. 李建模（Chien-Mo James Li）｜總分 **7.2**（A 級）｜第二波

| 校系職級 | NTU 電機系 / GIEE 電子所（EDA 群組）｜ 副教授（Associate Professor，系統分類；個人頁稱 Prof.）｜ PhD: Stanford University ECE 2002（MS Stanford 1997；BS NTU 1993）|
|---|---|
| 學術指標 | NTU EE Test 領域旗手；非 IEEE Fellow |
| Lab | LaDS 聯合 Lab（與黃俊良、黃鐘揚共設，VLSI Testing 研究重鎮）|
| **5 維度評分** | 研究 7 ｜ fab 8 ｜ Lab 7 ｜ 接洽 7 ｜ 長期 8 ｜ Test 領域穩定 + Vmin 落地 + MediaTek 非獨家 + 2nm Test 剛需 |

**核心專長 × 近 3 年代表實績**
- 2nm / 先進封裝 DFT（Design for Test）/ Test / Diagnosis / Yield 診斷 / AI-EDA for Testing
- VTS 2025 "ML-based Adaptive Wafer Sort"、"Multi-core Vmin Prediction"；ASP-DAC 2025 "Efficient ML-Based Transient Thermal Prediction for 3D-ICs"；ITC 2025 "Debugging Abnormally High Vmin"；ITC 2024 "qFD: Coherent and Depolarizing Fault Diagnosis for Quantum Processors"；IEEE TCAD 2023 "Small Sampling Overhead Error Mitigation for Quantum Circuits"
- LaDS 聯合 Lab 共主持；Stanford ECE PhD 2002

**製程/封裝應用點（詳述）**

- **節點 / 段別**：N2（2nm）/ A16（1.4nm）先進節點 + CoWoS / SoIC 先進封裝；重心在 DFT（Design for Testability）/ Test / Diagnosis / Yield 診斷；封裝後測試（Package-level Test）+ 量子電路錯誤緩解（擴展方向）
- **痛點對應**：
  - **N2 DFT Coverage 爆炸**：N2 gate count 激增，傳統 DFT scan chain 覆蓋率測量成本線性上升；李建模 VTS 2025 "ML-based Adaptive Wafer Sort" 可在 sort 階段動態調整測試序列，降低 ATE 時間 ≥ 20%，同時維持缺陷逃逸率
  - **Vmin 異常高 Debug 成本**：VTS 2025 "Debugging Abnormally High Vmin" 直接對應 N2 時序 signoff 中 Vmin outlier 的 root cause 定位問題；可與 TSMC YM 系統整合，自動縮窄 Vmin 異常至製程段 + 機台 + recipe 層級
  - **3D-IC / CoWoS 熱分析盲區**：ASP-DAC 2025 "Efficient ML-Based Transient Thermal Prediction for 3D-ICs" 直接命中 CoWoS stack 的熱點預測痛點；hotspot 定位準確率提升可減少 TSMC CoWoS 可靠度測試失敗率
  - **量子電路 Fault Diagnosis 前沿**：ITC 2024 "qFD: Coherent and Depolarizing Fault Diagnosis for Quantum Processors" — 早期佈局量子計算 IC 測試方法論；TSMC 已為 IQM 等量子客戶提供製程，測試診斷方法論具前瞻價值
- **可導入時程（TRL）**：**TRL 6-7 / 即時至 12 個月**；ML Wafer Sort + Vmin Debugging 方法論已有 VTS 2025 頂會驗證，接入 TSMC N2 ATE benchmark 後估 6-12 個月完成 PoC；3D-IC 熱預測需 CoWoS 堆疊結構資料，TRL 5-6，估 12-18 個月 PoC
- **配合 fab 部門**：測試部門（Sort / Final Test）+ ATE 工程（Automated Test Equipment）為主對口；YM / 缺陷工程（Defect Engineering）為次對口；CoWoS 封裝整合（Advanced Packaging PIE）為 3D-IC 熱預測對口
- **預期成效**：
  - N2 Wafer Sort ATE 時間縮短 ≥ 15%（ML-based Adaptive Sort）
  - Vmin 異常 root cause 定位時間從 2-4 hr 壓縮至 < 1 hr（ML diagnosis）
  - CoWoS hotspot 預測誤差 ≤ 5°C（ML transient thermal model）
  - 每年聯名論文 ≥ 1 篇（IEEE TCAD / VTS / ITC）

**合作紀錄 × 與外部公司狀況**
- MediaTek Vmin 合作（非獨家）
- MediaTek Vmin 合作為**非獨家**專案合作，與 TSMC Test 不衝突

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — N2 ML-based Adaptive Wafer Sort**：接續 VTS 2025 一作，導入 TSMC N2 ATE 流程，建立動態測試序列優化引擎；目標縮短 Sort 時間同時不提升缺陷逃逸率
  - **主題目 B — Vmin Abnormality ML Root Cause**：延伸 VTS 2025 "Debugging Abnormally High Vmin" 至 TSMC N2 YM 系統，建立自動 Vmin root cause ranking 模組；與 SPC 群（S07/S10/A19）可串接資料層（cross-ref：S10 謝昱銘 KSA 模組）
  - **延伸題目 C — CoWoS 3D-IC 熱點 ML 預測**：以 ASP-DAC 2025 ML transient thermal model 接入 TSMC CoWoS 堆疊實際量測資料，建立熱分布早期預警工具；與封裝群（S06/S08/S11/A27）形成 EDA ↔ 封裝可靠度閉環（cross-ref：A27 水野潤）
  - **延伸題目 D — Multi-core Vmin Prediction（跨核心統計）**：VTS 2025 "Multi-core Vmin Prediction" 接入 N2 multi-core SoC，建立跨核心 Vmin 相關性模型，輔助 power / timing signoff
- **制度與簽約**
  - **架構**：NTU 產學共同主持（LaDS Lab 機構）+ 李建模個人 PI 委案；MediaTek Vmin 合作為非獨家，不影響簽約
  - **預算建議區間**：年 NT$ 1,500-2,500 萬（含 ATE benchmark 費用 + 學生獎助 + 設備 + 教師研究費）；3 年滾動（推估區間，非承諾數字，依 NTU EE 產學既有量級對標）
  - **簽約對象**：NTU LaDS Lab（機構）+ 李建模（個人 PI）；IP 依 NTU 標準歸屬框架
  - **學生通道**：NTU EE → TSMC 既有招募通道；LaDS Lab 博碩生具 Stanford PhD 指導血統，質量穩定
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：ML Adaptive Sort 在 TSMC N2 shadow mode 測試；ATE 時間縮短 ≥ 8%；Vmin root cause 模組完成設計 + 內部 A/B 測試；聯名 VTS 或 TCAD 投稿 1 篇
  - **第 2 年**：Sort 優化升至 advisory mode（ATE 工程師採納率 ≥ 60%）；Vmin 模組通過 N2 production 抽測 50 lot 驗收；CoWoS 熱預測 PoC 啟動
  - **第 3 年**：Adaptive Sort 接入 N2 正式 ATE SOP；CoWoS 熱預測完成 1 個封裝規格驗收；Multi-core Vmin 模型延伸至 A16
  - **Exit criteria**：第 1 年 Sort 縮短 < 5% 且無改進路線，暫緩主題目 A；Vmin 模組 root cause 準確率 < 60% 則重新評估方法論
- **執行對口與啟動條件**
  - **主對口**：TSMC Sort 工程 / ATE 部門
  - **次對口**：YM / Defect Engineering；CoWoS PIE（先進封裝整合）
  - **啟動條件**：NTU 產學合約確認 + N2 ATE benchmark 資料集授權（保密協議）+ Q1 kick-off（李建模 / Sort 工程 / LaDS Lab）
- **風險與緩解**
  - **競業 / IP**：MediaTek Vmin 合作非獨家，合作內容為 Vmin prediction 方法論（非 MediaTek IC 設計機密）；TSMC Test 題目與 MediaTek 產品線無直接交疊，風險低
  - **副教授職級限制**：李建模為副教授（非正教授），部分機構要求正教授掛名；建議以 LaDS Lab 聯合 PI（黃俊良 / 黃鐘揚）為掛名機構 PI，李建模為執行 PI 雙軌處理
  - **學生流向**：NTU EE 學生以大廠（TSMC / MediaTek / Qualcomm）為主要目標，流向風險低
  - **能力限制**：WebSearch 無法核實 LaDS Lab 現有廠內合作具體規模；MediaTek 合作細節為非公開，TSMC 洽談前建議請 NTU 窗口提供現有合作概況
- **連結**：[NTU EE 教師頁](https://www.ee.ntu.edu.tw/bio1.php?teacher_id=943007) ｜ [個人首頁](http://cc.ee.ntu.edu.tw/~cmli/) ｜ [LaDS Lab 首頁](https://lads.ee.ntu.edu.tw/) ｜ [VTS 2025 論文記錄](https://tttc-vts.org/public_html/new/2025/program-3/index.html) ｜ 代表論文：VTS 2025 ML Adaptive Wafer Sort / ASP-DAC 2025 3D-IC Thermal / ITC 2024 qFD

---

### A26. 張孟凡（Meng-Fan Chang）｜總分 **7.2**（A 級，內部名單）｜不啟動（內部資源協調）

| 校系職級 | NTHU 電機 特聘教授 + TSMC Director of Corporate Research（2025 升 Senior Fellow，兼任）｜ 特聘教授（TSMC Director / Senior Fellow）｜ PhD: NCTU（交大）電機工程（MS Penn State；年份未公開）|
|---|---|
| 學術指標 | h-79 / 引用 21,849；IEEE Fellow Class of 2026（低功耗 SRAM 與 CIM）；2025 Chenming Hu Award |
| Lab | Memory Design Lab + TSMC 內部資源 |
| **5 維度評分** | 研究 10 ｜ fab 10 ｜ Lab 9 ｜ 接洽 0 ｜ 長期 8 ｜ CIM 世界頂級 + TSMC 內部 + TSMC Senior Fellow |

**核心專長 × 近 3 年代表實績**
- CIM — Compute-in-Memory 架構 / ReRAM / STT-MRAM 技術 / Neuromorphic AI 晶片 / TSMC CR 戰略題目
- IEEE Fellow Class of 2026（低功耗 SRAM 設計與 Compute-in-Memory）；2025 升任 TSMC Senior Fellow（高於 Director）；ISSCC 2025 三篇錄取（16nm Gain-Cell CIM 188.4TOPS/W；22nm STT-MRAM Heterogeneous CIM 104.5TOPS/W；STEP 8K-60fps Resolution-Enhancement NN Processor）；2025 Chenming Hu Award（台灣半導體創新貢獻獎）；Nature Communications 2024 memristor-based ANN 硬體實作（478 引）
- IEEE Fellow Class of 2026；TSMC Senior Fellow（2025-）；2025 Chenming Hu Award

**製程/封裝應用點（詳述）**

> ⚠️ **分類：不啟動（內部資源協調）** — 張孟凡自 2025 年升任 TSMC Senior Fellow（高於 Director），已為 TSMC 內部戰略資產。以下應用點描述的是 TSMC 內部利用其價值的方式，**不適用外部 JDP 或產學合作框架**。

- **節點 / 段別**：N2（2nm）/ N3（3nm）/ A16（1.4nm）前段邏輯 + 記憶體整合；CIM 架構層（Compute-in-Memory）/ ReRAM / STT-MRAM；Neuromorphic AI 晶片製程整合
- **內部協調價值點**：
  - **CIM 技術棧跨 cluster 知識橋接**：CIM 群（S03 馬誠佑 / S05 胡璧合）為外部合作 PI，張孟凡為 TSMC 內部 CIM 戰略架構人；三人形成「架構層（張孟凡內部）× 電路層（S05 胡璧合）× 製程整合層（S03 馬誠佑）」分工；跨 cluster 知識整合由張孟凡協調（cross-ref：S03/S05）
  - **NTHU 研究生聯合指導**：張孟凡仍為 NTHU EE 特聘教授，可以學校身份聯合指導碩博士生，配合 TSMC 內部題目設計研究方向，學生畢業後直通 TSMC CR（不走 JDP 通道）
  - **ReRAM / STT-MRAM 內部製程整合**：ISSCC 2025 三篇錄取（22nm STT-MRAM CIM 104.5 TOPS/W 等）為 TSMC 量產路徑鋪墊；內部 CR（Corporate Research）直接承接
  - **Neuromorphic 競爭情報**：Nature Communications 2024 memristor ANN（478 引）為學界指標論文，張孟凡可協助 TSMC CR 追蹤 Neuromorphic 競爭態勢（不需對外合作）
- **可導入時程（TRL）**：**即時（內部）** — 張孟凡現為 TSMC Senior Fellow，所有技術協調透過 TSMC 內部機制執行，不需外部 TRL 評估
- **配合 fab 部門**：TSMC Corporate Research（CR）為主通道；NTHU 聯合指導為學生供應通道；CIM 群外部 PI（S03/S05）的研究方向對齊由張孟凡在 CR 層協調

**合作紀錄 × 與外部公司狀況**
- 歷年 TSMC 合作；2025 升 Senior Fellow 後內部資產地位更牢固
- **TSMC Senior Fellow（2025-）** — 已為 TSMC 內部戰略資產，外部合作通道更受限

**建議合作方式 × 公開連結**

> ⚠️ **不對外合作；以下為 TSMC 內部協調機制描述，非外部 JDP 框架。**

- **內部協調職能**
  - **職能 A — CIM 群外部 PI 研究方向對齊**：由張孟凡作為 TSMC CR 代表，定期（每季）與 S03 馬誠佑 / S05 胡璧合進行研究方向 alignment 會議，確保外部合作題目與 TSMC N2/A16 CIM 路線圖一致；外部 PI 不知悉張孟凡 Senior Fellow 身份的具體職責
  - **職能 B — NTHU 學生聯合指導通道**：以 NTHU EE 特聘教授身份，每年聯合指導 2-4 名碩博士生，研究方向設計配合 TSMC CR CIM / STT-MRAM 題目；學生畢業後優先錄用至 TSMC CR / Design 部門
  - **職能 C — 跨 cluster 知識庫建立**：主導 CIM / ReRAM / Neuromorphic 技術白皮書撰寫（內部），作為 TSMC N2 以後節點的 CIM 路線圖基礎文件
- **制度**：
  - **框架**：TSMC 內部 Corporate Research 預算；NTHU 聯合指導走學校正常教師職責，不另立對外合約
  - **預算**：由 TSMC CR 部門編列，不適用外部合作預算估算框架
  - **TSMC 員工身份聲明**：張孟凡為 TSMC Senior Fellow，任何以其個人名義對外的合作洽談須經 TSMC 法務 + HR 同意，且極可能被限制（不建議嘗試）
- **KPI（內部，由 CR 部門評估）**
  - CIM 群外部 PI alignment 會議每季 ≥ 1 次，方向偏差在季度內修正
  - NTHU 聯合指導學生 ≥ 2 名 / 年，畢業後 TSMC 錄用率 ≥ 80%
  - CIM 技術白皮書 ≥ 1 份 / 年（TSMC 內部機密文件）
  - **Exit criteria**：不適用（張孟凡為 TSMC 正職員工，關係不以「終止合作」方式結束）
- **執行對口**：
  - **主通道**：TSMC CR 部門主管
  - **次通道**：NTHU EE 系所行政（聯合指導公文）；CIM 群外部 PI（S03/S05）計畫管理窗口
- **風險聲明**：
  - **TSMC 員工不適用對外 JDP 框架**：任何第三方（包括競業公司研究人員）嘗試繞過 TSMC HR / 法務直接接觸張孟凡洽談合作，可能引發 TSMC 內部合規問題；**請勿啟動對外接觸**
  - **能力限制**：WebSearch 無法驗證 TSMC Senior Fellow 內部職責細節；所有內部協調機制描述基於公開資訊推估，實際執行以 TSMC 內部 SOP 為準
- **連結**：[NTHU EE 個人頁](https://www.ee.nthu.edu.tw/~mfchang/) ｜ [Google Scholar](https://scholar.google.com/citations?user=7rcOEiIAAAAJ&hl=zh-TW) ｜ [IEEE Xplore Author](https://ieeexplore.ieee.org/author/37420875800) ｜ [DBLP](https://dblp.org/pid/89/6934.html) ｜ 代表：ISSCC 2025 三篇 / Nature Communications 2024 memristor ANN / 2025 Chenming Hu Award

---

### A27. 水野潤（Jun Mizuno）｜總分 **7.2**（A 級）｜觀察（NCKU 三方合作 NCKU × NARLabs TSRI；Tokyo Tech 正式連結待核實）

| 校系職級 | NCKU 智慧與永續製造學位學程（PSSM）正職教授 + Waseda RISE 上級研究員 ｜ NCKU 正職教授（雙重身份；Waseda 為兼任研究職）｜ PhD: Tohoku University 工學博士（年份待核實）|
|---|---|
| 學術指標 | h-27 / 引用 2,671（Scopus）；296 件研究產出（134 期刊 + 137 研討會）|
| Lab | Mizuno Lab @ NCKU 約 9 人（1 博 + 4 碩 + 2 大學部）+ Waseda 體系協作 |
| **5 維度評分** | 研究 9 ｜ fab 9 ｜ Lab 8 ｜ 接洽 7 ｜ 長期 6 ｜ Waseda 資深 + NCKU 正職 + 日本量產經驗 |

**核心專長 × 近 3 年代表實績**
- 異質整合封裝 / 3D TSV（Through-Silicon Via）/ 原子層沉積（ALD）/ ALD-FeFET 鐵電記憶體 / 日系封裝製程
- 2025 Cu/Polyimide Hybrid Bonding Reliability Study；2025 Microfluidic Cooling for ASIC Packages；2026 Electric-Current-Induced Grain Reorientation in Ni-Stabilized Compounds；ICEP 2024 異質整合；NCKU × NARLabs TSRI 半導體異質整合合作（2025）
- Waseda RISE 上級研究員；NCKU PSSM 正職教授；296 件研究產出

**製程/封裝應用點（詳述）**

- **節點 / 段別**：先進封裝（Advanced Packaging）— CoWoS / SoIC / 3DIC 等；異質整合（Heterogeneous Integration）/ 3D TSV 互連 / Hybrid Bonding / Microfluidic Cooling；ALD 製程（薄膜沉積）+ ALD-FeFET 鐵電記憶體（延伸方向）
- **痛點對應**：
  - **Hybrid Bonding 可靠度驗證缺口**：2025 年一作 "Cu/Polyimide Hybrid Bonding Reliability Study" 直接命中 CoWoS-L / SoIC Hybrid Bonding 的銅柱 + 介電層界面可靠度問題；N2 Chiplet + CoWoS 堆疊時 bonding 界面受熱應力循環影響，可靠度模型缺乏高精度預測
  - **3D 封裝散熱瓶頸**：2025 年一作 "Microfluidic Cooling for ASIC Packages" 直接對應 CoWoS AI 加速器封裝的散熱密度問題（HBM + ASIC 堆疊熱流密度 > 1 kW/cm²）；微流道冷卻為下一代 AI 封裝的散熱路線之一
  - **Ni 化合物晶粒重定向**：2026 年一作 "Electric-Current-Induced Grain Reorientation in Ni-Stabilized Compounds" 探討封裝互連材料在電流應力下的晶粒演化，對 TSV + UBM 材料長期可靠度有直接貢獻
  - **日本量產製程知識**：Waseda RISE 上級研究員身份連結日本封裝生態（Renesas / Sony / Ibiden 等）；TSMC CoWoS 日本客戶（Sony CIS / Renesas 等）的封裝界面規範對齊有潛在協調價值
- **可導入時程（TRL）**：**TRL 6-7 / 即時至 12 個月**；Hybrid Bonding 可靠度 + Microfluidic Cooling 均已有 2025 發表成果（TRL 5-6），接入 TSMC CoWoS 實際結構後估 6-12 個月 PoC；NCKU 正職身份使合約可依一般 NCKU 產學框架立即啟動
- **配合 fab 部門**：先進封裝整合（Advanced Packaging PIE）/ CoWoS 製程整合為主對口；封裝可靠度工程（Reliability Eng.）/ 散熱管理（Thermal Mgt.）為次對口；Waseda / NCKU × NARLabs TSRI 合作框架為跨機構整合點（cross-ref：S06/S08/S11/S12/S13）
- **預期成效**：
  - Hybrid Bonding 界面可靠度預測模型誤差 ≤ 5%（相較實測 MTTF）
  - 微流道冷卻設計可將 CoWoS AI 封裝熱阻降低 ≥ 20%（PoC 驗證）
  - Ni 互連晶粒演化模型完成 TSV 直徑 10μm / 20μm 兩規格驗證
  - NCKU × NARLabs TSRI × Waseda 三方聯名論文 ≥ 1 篇 / 年

**合作紀錄 × 與外部公司狀況**
- Waseda 日本產學體系；NCKU 三方半導體異質整合合作
- **NCKU 正職教授**（先前誤記為 Waseda 客座），可接洽度由日籍限制大幅放寬至一般 NCKU PI 模式

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — CoWoS Hybrid Bonding 可靠度預測模型**：接續 2025 Cu/Polyimide Hybrid Bonding Reliability 一作，建立 TSMC CoWoS-L / SoIC 規格的 bonding 界面可靠度預測模型（熱循環 + 電流應力耦合）；與封裝群（S06/S08/S11/S12/S13）形成封裝可靠度共同研究體系
  - **主題目 B — AI 封裝 Microfluidic Cooling 設計優化**：延伸 2025 Microfluidic Cooling for ASIC Packages 一作至 TSMC CoWoS AI 加速器封裝規格，建立散熱密度 > 1 kW/cm² 場景的微流道設計方法論 + 製程規範
  - **延伸題目 C — NCKU × NARLabs TSRI 三方封裝異質整合平台**：以水野潤為 NCKU 側 PI，整合 NARLabs TSRI 設備資源，建立台南 / 南科在地的先進封裝異質整合驗證平台；可洽 Waseda RISE 為日本技術顧問方（三方框架）
  - **延伸題目 D — ALD-FeFET 薄膜整合**：探索 ALD FeFET 在先進封裝基板或 3D 堆疊中的嵌入式記憶體應用（長期方向，TRL 3-4）
- **制度與簽約**
  - **架構**：NCKU 一般產學合約（PSSM 學程機構）+ 水野潤個人 PI；NCKU 正職教授身份使合約等同一般台灣 PI，無日籍特殊限制；Waseda RISE 為研究協作方，非合約主體
  - **預算建議區間**：年 NT$ 1,200-2,000 萬（含可靠度測試設備使用 + 學生獎助 + Microfluidic 原型製作 + 教師研究費）；3 年滾動（推估區間，非承諾數字，依 NCKU 產學封裝合作量級對標）
  - **簽約對象**：NCKU AIS2M / PSSM（機構）+ 水野潤（個人 PI）；IP 依 NCKU 標準歸屬框架
  - **學生通道**：NCKU → 南科封裝部門招募通道；Waseda 日本學生交換（日本封裝技術視角輸入）
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：Hybrid Bonding 可靠度模型在 TSMC CoWoS dummy test vehicle 完成 shadow validation；熱循環 1,000 次預測誤差 ≤ 10%；Microfluidic PoC 設計完成並送 NARLabs TSRI 製作
  - **第 2 年**：可靠度模型精度提升至 ≤ 5%（實測 2,000 cycle 驗收）；Microfluidic 散熱降幅 ≥ 15%（PoC 量測）；聯名論文 ≥ 1 篇（IEEE ECTC / JAP）
  - **第 3 年**：可靠度模型接入 TSMC CoWoS 封裝設計 sign-off checklist；Microfluidic 設計規範提交先進封裝 PIE；三方平台（NCKU × TSRI × Waseda）完成正式合作備忘錄
  - **Exit criteria**：第 1 年可靠度預測誤差 > 20%（表示模型架構不適用），暫緩主題目 A 重新評估方法；Microfluidic PoC 散熱降幅 < 5% 則轉為延伸題目觀察
- **執行對口與啟動條件**
  - **主對口**：TSMC Advanced Packaging PIE / CoWoS 整合工程
  - **次對口**：封裝可靠度工程 / 散熱管理；NARLabs TSRI 設備窗口
  - **啟動條件**：NCKU 產學合約確認 + CoWoS test vehicle 設計資料授權 + Q1 三方 kick-off（水野潤 / 封裝 PIE / NCKU PSSM）；Waseda RISE 三方備忘可在第 2 年推進
- **風險與緩解**
  - **雙重身份行政複雜度**：NCKU 正職 + Waseda 上級研究員可能有行政時間衝突；建議合約明確規定每年在 NCKU 的研究投入時間（建議 ≥ 6 個月 / 年在台）
  - **Tokyo Tech 連結待核實**：Tokyo Tech 正式連結未確認，建議啟動前由 NCKU 窗口確認合作備忘錄狀態，避免三方框架預期落差
  - **競業 / IP**：Waseda 體系無 TSMC 競業綁定；NARLabs TSRI 為台灣公共研究機構，IP 歸屬需在合約中明確（建議 TSMC 委託研究優先取 JDA 模式）
  - **能力限制**：WebSearch 無法確認 TSMC 是否已透過 CoWoS 封裝部門直接接觸水野潤；建議由封裝群（S06/S11 等）共同 PI 的 TSMC 窗口作 warm intro
- **連結**：[NCKU PSSM 成員頁](https://ais2m.ncku.edu.tw/?action=department&cn=member_list&dpid=5) ｜ [Mizuno Lab @ NCKU](https://sites.google.com/gs.ncku.edu.tw/mizunolabncku/home) ｜ [NCKU Research Output](https://researchoutput.ncku.edu.tw/en/persons/jun-mizuno) ｜ [Researchmap（日）](https://researchmap.jp/read0205512) ｜ [ResearchGate](https://www.researchgate.net/profile/Jun-Mizuno) ｜ 代表論文：2025 Cu/Polyimide Hybrid Bonding Reliability / 2025 Microfluidic Cooling for ASIC Packages / ICEP 2024 異質整合

---

### A28. 吳添立（Tian-Li Wu）｜總分 **7.2**（A 級，升等後 +0.3）｜觀察（需資訊牆）

| 校系職級 | NYCU 電子所（IEE）/ 電子工程系（DEE）正教授（2026/02 升等）+ AI 學程兼聘 ｜ 正教授（2026/02 升等）；2025/10 IEEE Senior Member ｜ PhD: KU Leuven（比利時）電機工程 2016（imec 為工作經歷 2011-2017，非學位）|
|---|---|
| 學術指標 | h-28 / 引用 3,077（Google Scholar；since 2021: h=25, 引用 1,969）|
| Lab | WLab（NYCU-Keysight WISER 中心 2026 創辦）；200+ 期刊/會議論文 |
| **5 維度評分** | 研究 9 ｜ fab 8 ｜ Lab 7 ｜ 接洽 4 ｜ 長期 7 ｜ 多獎項 + 升正教授 + MediaTek Junior Chair（獨家 7 年） |

**核心專長 × 近 3 年代表實績**
- GaN / SiC / Ga₂O₃ 功率半導體可靠度 / 功率 IC 設計 / FeFET（副專長）/ 先進節點可靠度分析
- 2026/02 升等正教授（Full Professor）；2025/10 升 IEEE Senior Member；2025 NYCU ECE Teaching Award；2023 NSTC 吳大猷紀念獎（Ta-You Wu Memorial Award）；2023 NSTC Excellent Young Scholars Project；2023 CIEE Outstanding Young Electrical Engineer；2022 EDMA Outstanding Young Engineer Award；imec Leuven 6 年海外訓練（2011-2017）；ITRI Distinguished Research Fellow（since 2023）；TSRI Joint Researcher（since 2025）；MediaTek Junior Chair 7 年
- 2023 NSTC 吳大猷紀念獎；2023 NSTC Excellent Young Scholars Project；2025 NYCU ECE Teaching Award

**製程/封裝應用點（詳述）**

- **節點 / 段別**：功率半導體製程段 — GaN-on-Si / SiC / Ga₂O₃ MOSFET；電源管理 IC（PMIC）可靠度；先進節點（N16 / N7 FinFET）FeFET 副專長；重心在 GaN / SiC 功率元件可靠度分析，而非 IC 設計產品線
- **痛點對應**：
  - **GaN HEMT 熱載子降解機制**：GaN-on-Si HEMT 在高壓 / 高電流應力下的熱載子注入 + 電流崩潰（Current Collapse）是量產可靠度的核心未解題；吳添立 imec 訓練背景 + NYCU WLab 6 年 GaN 可靠度研究為台灣最強組合之一
  - **SiC MOSFET 介面態退化**：SiC/SiO₂ 界面態密度 Dit 問題直接影響閘極氧化層壽命，高溫操作下 NBTI / PBTI 退化加速；吳添立 KU Leuven / imec 訓練切入此核心痛點
  - **GaN 功率可靠度 JEDEC 標準對接**：車載 / 工業 GaN 需通過 JEDEC JESD47 等壽命測試；TSMC 若擴大 GaN 服務（如 TSMC GaN PDK 客戶），可靠度方法論認證缺口需填補
  - **TSRI Joint Researcher 通道（2025 起）**：吳添立已與 NARLabs TSRI 建立 Joint Researcher 身份（2025），可作為 TSMC × NARLabs 功率半導體可靠度共同研究的橋接通道
- **可導入時程（TRL）**：**TRL 6-7 / 6-18 個月（需資訊牆先行）**；GaN / SiC 可靠度方法論已有 NYCU WLab 6 年系統驗證（TRL 5-6）；需先完成法務資訊牆審查（MediaTek Junior Chair 7 年獨家），估 3-6 個月法務先行，之後 6-12 個月 PoC
- **配合 fab 部門**：功率半導體部門（Power Semiconductor）/ GaN PDK 工程為主對口；可靠度工程（Reliability Eng.）/ 元件物理（Device Physics）為次對口；NARLabs TSRI Joint Researcher 窗口為跨機構整合點
- **預期成效**：
  - GaN HEMT 熱載子退化模型精度 ≤ 10% MTTF 預測誤差（相較 JEDEC 測試資料）
  - SiC MOSFET 閘極氧化層壽命預測模型建立，覆蓋 150°C / 175°C 兩個操作溫度點
  - 可靠度方法論白皮書完成，支援 TSMC GaN PDK 客戶認證需求
  - TSRI × NYCU 聯名論文 ≥ 1 篇 / 年（IEEE TED / EDL / IRPS）

**合作紀錄 × 與外部公司狀況**
- MediaTek Junior Chair Professor（2017-，獨家 7 年）
- **MediaTek Junior Chair（2017-，獨家 7 年）** — 為競業 IC 設計公司之冠名講座，需法務先檢排他條款

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — GaN HEMT 電流崩潰 + 熱載子可靠度模型**：以 NYCU WLab GaN 可靠度方法論接入 TSMC GaN-on-Si PDK 規格，建立 current collapse + hot carrier injection 退化預測模型；支援 TSMC GaN PDK 客戶可靠度認證需求
  - **主題目 B — SiC MOSFET 閘極介面態可靠度**：延伸 KU Leuven / imec 訓練的 SiC/SiO₂ 界面態 Dit 分析至 TSMC 或其合作方 SiC 晶圓規格，建立 NBTI/PBTI 退化加速模型
  - **延伸題目 C — FeFET 可靠度副專長整合**：探索 N16 / N7 FeFET 在 PMIC embedded memory 應用中的可靠度需求（吳添立副專長；長期方向，TRL 4-5，資訊牆釐清後再評估）
  - ⚠️ **排除範疇**：MediaTek 現有產品線相關之 IC 設計、功率 IC 電路設計（IC design team 的產品機密）；合作限縮於 **器件可靠度物理 / GaN-SiC 製程段**，不涉及 MediaTek 任何電路設計細節
- **制度與簽約**
  - **架構**：需法務先行（資訊牆協議）+ NYCU 產學合約（WLab 機構）+ 吳添立個人 PI；資訊牆協議須明確劃定合作範疇（GaN / SiC 可靠度）與排除範疇（MediaTek IC 設計線）
  - **預算建議區間**：年 NT$ 1,200-2,000 萬（含可靠度測試設備 / JEDEC 加速老化測試 + 學生獎助 + 教師研究費）；3 年滾動（推估區間，非承諾數字，依 NYCU 功率半導體產學量級對標）
  - **簽約對象**：NYCU WLab（機構）+ 吳添立（個人 PI）；資訊牆協議附加於主合約
  - **學生通道**：NYCU IEE → TSMC 功率半導體部門招募；imec 訓練背景使學生具國際可靠度測試能力
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：法務資訊牆協議完成 + 合作範疇確認文件；GaN HEMT 退化模型在 TSMC GaN-on-Si 標準 test structure 完成 shadow validation；IEEE IRPS 或 TED 投稿 1 篇
  - **第 2 年**：GaN 退化模型 MTTF 預測誤差 ≤ 15%（JEDEC 加速測試驗收）；SiC 閘極氧化層壽命模型完成 2 個溫度點驗收；聯名論文 ≥ 1 篇
  - **第 3 年**：可靠度方法論白皮書提交 TSMC GaN PDK 部門；模型接入 TSMC 可靠度 sign-off checklist（至少 1 個製程規格）；升等正教授（2026/02 已完成）後學術話語權提升，可洽 JEDEC 委員會合作
  - **Exit criteria**：若法務資訊牆協議 6 個月內無法達成，暫緩啟動；GaN 退化模型 MTTF 預測誤差 > 30% 持續 2 季，重新評估方法論
- **執行對口與啟動條件**
  - **主對口**：TSMC 功率半導體部門 / GaN PDK 工程窗口
  - **次對口**：可靠度工程（Reliability Eng.）/ 元件物理（Device Physics）；法務（Legal）— 資訊牆協議起草
  - **啟動條件**：法務資訊牆審查完成 + NYCU 合約確認 + GaN test structure 授權 + Q1 三方 kick-off（吳添立 / 功率半導體部門 / 法務）
- **風險與緩解**
  - **MediaTek Junior Chair 獨家 7 年（嚴重綁定）**：MediaTek Junior Chair（2017-）排他條款可能涵蓋「功率半導體技術諮詢」範疇；法務先行是必要前置，未完成前不得啟動任何技術討論
  - **合作範疇劃定難度**：GaN 功率元件可靠度 vs MediaTek 內部功率 IC 設計的邊界在實務中可能模糊；建議合約明列正面清單（允許的題目）而非僅負面排除清單
  - **升等後行政負擔**：2026/02 剛升等正教授，可能面臨新任期行政壓力；建議合約設計彈性（每月 1-2 次深度 meeting，不要求廠內長時間駐點）
  - **能力限制**：WebSearch 無法確認 MediaTek Junior Chair 排他條款具體文字；法務審查需取得協議全文，不能依公開資訊推估
- **連結**：[NYCU IEE 教師頁](https://iee.nycu.edu.tw/en/teacher/p1.php?num=225&page=1) ｜ [NYCU Academic Hub](https://scholar.nycu.edu.tw/en/persons/tian-li-wu/) ｜ [Google Scholar](https://scholar.google.be/citations?user=9WV7g6QAAAAJ&hl=en) ｜ [WLab 個人頁](https://tianliwu.wixsite.com/nycuwlab/about-me?lang=en) ｜ [LinkedIn](https://tw.linkedin.com/in/tian-li-wu-ba803349) ｜ 代表：2025 NYCU ECE Teaching Award / 2023 NSTC 吳大猷紀念獎 / imec Leuven 6 年訓練（2011-2017）

---

### A29. 郭浩中（Hao-Chung Kuo）｜總分 **7.2**（A 級，HHRI 競業判定後可定案）｜第三波（HHRI 法務先檢）

| 校系職級 | NYCU 光電工程學系 / 光電系統研究所 + 鴻海研究院（HHRI）半導體研究中心主任 ｜ Distinguished Professor（特聘教授，since 2013）+ HHRI 半導體中心主任 ｜ PhD: University of Illinois at Urbana-Champaign ECE 1999（BS NTU 1992；MS Rutgers 1995）|
|---|---|
| 學術指標 | h-85 / 引用 34,160（GS）；五料 Fellow（IEEE 2015 / Optica 2011 / SPIE 2012 / IET 2012 / IAAM 2021）；NSTC 傑出獎 2020；Research.com TW EE Leader 2022-2025 |
| Lab | AI-Enabled Silicon Nanophotonic Lab（AESNL）+ HHRI 半導體中心 |
| **5 維度評分** | 研究 9 ｜ fab 7 ｜ Lab 8 ｜ 接洽 5 ｜ 長期 7 ｜ 四料 Fellow + 多獎 + HHRI 競業待法務 |

**核心專長 × 近 3 年代表實績**
- Micro-LED 晶片設計（全球頂尖）/ 化合物半導體（GaN / InP / Ga₂O₃）/ ALD 製程 / 第四代半導體 Ga₂O₃ MOSFET / 光電元件 + 量子亂數產生器（QRNG）
- IEEE / OSA / SPIE / IET 四料 Fellow；2025 Research.com Electronics & Electrical Engineering in Taiwan Leader Award（連 4 年 2022-2025）；2025 HHRI × NYCU × RPI 合作 InGaN Micro-LED 陣列高速量子亂數產生器（QRNG）；2026 Adv. Electron. Mater. 增強模式 β-Ga₂O₃ MOSFET（NYCU × HHRI）；2025 PubMed「Current Landscape of Micro-LED Display Industrialization」；NSTC 傑出研究獎 2020
- 五料 Fellow（IEEE/OSA/SPIE/IET/IAAM）；NSTC 傑出研究獎 2020；Research.com TW EE Leader 連 4 年

**製程/封裝應用點（詳述）**

- **節點 / 段別**：化合物半導體製程 — GaN / InP / Ga₂O₃；Micro-LED 晶片設計；ALD 薄膜沉積；化合物半導體器件整合（非 Si 主線製程，屬 TSMC 特殊製程 / SPC 業務）；QRNG（量子亂數產生器）為前沿方向
- **痛點對應**：
  - **Micro-LED 轉移良率**：TSMC 承接 Apple / Sony 等 Micro-LED 客戶訂單面臨大面積轉移良率問題；郭浩中 2025 HHRI × NYCU × RPI InGaN Micro-LED 陣列 QRNG 論文顯示高密度 Micro-LED 陣列製程能力；可協助 TSMC SPC 業務 Micro-LED 製程整合方法論
  - **Ga₂O₃ MOSFET 增強模式突破**：2026 年 Adv. Electron. Mater. 一作增強模式 β-Ga₂O₃ MOSFET（NYCU × HHRI）直接命中 WBG（Wide-Bandgap）功率元件下一代方向；TSMC 若布局 Ga₂O₃ 製程服務，郭浩中為台灣首選技術顧問
  - **ALD 製程整合**：Picosun（ALD 設備商，已被 Applied Materials 收購）2019-2022 合作背景，使郭浩中具 ALD 製程在化合物半導體上的應用實作經驗；TSMC ALD 製程擴展至化合物半導體段時有銜接價值
  - **QRNG 量子安全前沿**：2025 InGaN Micro-LED QRNG（高速量子亂數產生器）為量子安全 IC 應用前沿；TSMC 可藉此布局量子通信晶片製程服務（長期方向）
- **可導入時程（TRL）**：**TRL 5-6 / 法務先行後 12-18 個月**；Ga₂O₃ / Micro-LED 方法論已有 2025-2026 發表成果，TRL 4-5；需先完成 HHRI 競業法務審查（3-6 個月），再啟動 PoC 設計；設定為第三波
- **配合 fab 部門**：特殊製程部門（SPC — Specialty Process Competence）/ 化合物半導體工程為主對口；ALD 製程工程 / 可靠度工程為次對口；TSMC 歐洲先進製程部門（若有 Ga₂O₃ 規劃）為潛在跨組整合點
- **預期成效**：
  - Ga₂O₃ 增強模式 MOSFET 製程整合：建立 TSMC 化合物半導體製程評估報告（技術可行性 PoC）
  - Micro-LED 陣列製程規範文件 ≥ 1 份（轉移良率改善方向）
  - ALD 在 Ga₂O₃ / GaN 介電層上的製程窗口報告
  - QRNG 製程可行性評估報告（前沿布局參考）

**合作紀錄 × 與外部公司狀況**
- Picosun 3 年技術合作（2019-2022 結束；Picosun 後被 Applied Materials 收購）；鴻海研究院（HHRI）半導體研究中心主任（現任）
- **HHRI 半導體研究中心主任** — 鴻海在半導體封裝/3D IC 有佈局；TSMC 啟動前需法務確認 HHRI 是否構成競業關係；Picosun 合作已於 2022 結束（後被 Applied Materials 收購）

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — Ga₂O₃ MOSFET 製程整合可行性 PoC**：以 2026 年 Adv. Electron. Mater. 增強模式 β-Ga₂O₃ MOSFET 方法論，評估 TSMC 化合物半導體製程平台上的 Ga₂O₃ MOSFET 整合可行性；目標建立 TSMC Ga₂O₃ 製程服務技術白皮書
  - **主題目 B — Micro-LED 製程整合方法論**：以郭浩中 Micro-LED 全球頂尖研究能量，協助 TSMC SPC 業務 Micro-LED 客戶（Apple / Sony）的製程整合方法論升級；範疇限制：製程側（不涉及 HHRI 在封裝 / 3D IC 的主力研究）
  - **延伸題目 C — InGaN Micro-LED QRNG 製程評估**：評估 TSMC 製程平台製作高密度 InGaN Micro-LED 陣列的可行性，作為量子安全晶片製程服務的前沿布局參考
  - ⚠️ **排除範疇**：HHRI 主力研究方向（封裝 / 3D IC）；鴻海半導體供應鏈相關題目；避免任何與鴻海 × TSMC 客戶關係交疊的研究範疇
- **制度與簽約**
  - **架構**：**法務先行（第三波）** — 需完成 (1) HHRI 半導體中心主任職責競業判定；(2) Picosun→應材 收購延伸條款確認；(3) 資訊牆協議；完成後再立 NYCU 產學合約（AESNL Lab 機構）+ 郭浩中個人 PI
  - **預算建議區間**：年 NT$ 1,500-2,500 萬（含化合物半導體製程實驗 + ALD 製程費用 + 學生獎助 + 教師研究費）；3 年滾動（推估區間，非承諾數字，依 NYCU 化合物半導體產學量級對標）；第三波啟動，預算編列在 HHRI 法務完成後才可確認
  - **簽約對象**：NYCU AESNL Lab（機構）+ 郭浩中（個人 PI）；IP 依 NYCU 標準框架（HHRI 共同研究 IP 需在法務階段釐清）
  - **學生通道**：NYCU 光電 → TSMC SPC 業務化合物半導體部門；HHRI × NYCU 學生不跨入 TSMC 合作範疇（資訊牆隔離）
- **KPI（年度滾動 + Exit criteria）**
  - **法務階段（啟動前）**：HHRI 競業判定完成 + Picosun 條款確認 + 資訊牆協議草案；目標在第三波前 Q 完成
  - **第 1 年**：Ga₂O₃ MOSFET PoC 製程設計完成；Micro-LED 製程方法論白皮書初稿提交;NYCU × TSMC 聯名論文投稿 1 篇（IEEE Photon. Technol. Lett. 或 Adv. Electron. Mater.）
  - **第 2 年**：Ga₂O₃ PoC 完成 1 個製程規格實作驗證；Micro-LED 製程改善方法論接入 TSMC SPC 業務 1 個客戶專案
  - **第 3 年**：Ga₂O₃ 製程技術白皮書正式提交 SPC 業務規劃部門；QRNG 製程可行性報告完成
  - **Exit criteria**：HHRI 競業法務判定為「構成競業」，則停止啟動；Ga₂O₃ PoC 第 1 年無法達到增強模式閾值電壓穩定性，暫緩主題目 A
- **執行對口與啟動條件**
  - **主對口**：TSMC 特殊製程部門（SPC）/ 化合物半導體工程
  - **次對口**：法務（Legal）— HHRI 競業審查 + 資訊牆；ALD 製程工程
  - **啟動條件**：**HHRI 競業法務先行完成**（必要前置）+ NYCU 合約確認 + Q kick-off（郭浩中 / SPC 部門 / 法務）
- **風險與緩解**
  - **HHRI 競業風險（高）**：鴻海 HHRI 半導體中心有 3D IC / 先進封裝布局，與 TSMC 在封裝業務上有潛在利益衝突；且鴻海為 TSMC 大客戶，雙方關係敏感；法務審查為強制前置，不得繞過
  - **Picosun → 應材 收購延伸**：2022 年 Picosun 被 Applied Materials 收購，原 Picosun 合作條款是否有延伸義務或競業限制需確認（Applied Materials 為 TSMC 重要設備供應商，條款複雜度高）
  - **HHRI + NYCU 雙重身份資訊隔離**：郭浩中同時是 NYCU 教授 + HHRI 中心主任，資訊牆協議需明確區隔哪些研究成果屬 NYCU 學術（可對外合作）vs HHRI 委任（需 HHRI 同意）
  - **能力限制**：WebSearch 無法確認 HHRI 半導體中心的具體研究項目與鴻海核心業務的重疊範圍；法務審查需取得 HHRI 組織職能文件，不能依公開資訊推估
- **連結**：[NYCU 光電教師頁](https://dop.nycu.edu.tw/en/people_ii.html?tID=49) ｜ [HHRI 個人頁](https://www.hh-ri.com/hhri/people/郭浩中/) ｜ [HHRI × NYCU QRNG 新聞](https://www.cna.com.tw/postwrite/eng/429121) ｜ [Ga₂O₃ MOSFET 新聞](https://www.nycu.edu.tw/nycu/en/app/news/view?module=headnews&serno=466f83de-2f81-4c17-aff6-ccc3dac5cd3a) ｜ [Google Scholar（郭浩中）](https://scholar.google.com/citations?user=JcIbGsYAAAAJ) ｜ 代表：2026 增強模式 β-Ga₂O₃ MOSFET（Adv. Electron. Mater.）/ 2025 InGaN Micro-LED QRNG / IEEE/OSA/SPIE/IET 四料 Fellow

---

### A30. 陳柏宏（Po-Hung Chen）｜總分 **6.9**（A 級）｜第三波

| 校系職級 | NYCU 電子研究所所長（Director, Institute of Electronics，自 2021）｜ 教授 兼 電子所所長 ｜ PhD: 東京大學 電機工程 2012（MS NCTU 電子所 2007）|
|---|---|
| 學術指標 | h-22 / 引用 1,864（Scopus）；IEEE Senior Member；VLSIC TPC since 2020；A-SSCC TPC since 2016 |
| Lab | Green Power Electronics Lab 約 16 人（5 博 + 10 碩 + 1 助理）|
| **5 維度評分** | 研究 7 ｜ fab 7 ｜ Lab 7 ｜ 接洽 9 ｜ 長期 8 ｜ 東大博士 + 原型 IC + 無綁定 + 中生代 |

**核心專長 × 近 3 年代表實績**
- 電源管理 IC（PMIC）/ 無線電力傳輸（WPT）/ LDO / DC-DC Converter / 系統 IC 優化
- IEEE JSSC 2024 "A Quad-Mode Structure-Reconfigurable Regulating Rectifier"；IEEE TCAS-I 2025 "A Reconfigurable Wireless Power Receiver With Shared-Inductor Buck-Boost Converter"；ISPSD 2025「LLC Resonant Converter Controller with Burst Mode Control and Soft-Start Function」；IPEMC-ECCE Asia 2025 Best Paper Award「Current Measurement of GaN HEMTs Without Insertion Impedance」；NYCU 電子所所長（Director, Institute of Electronics，2021-）
- IPEMC-ECCE Asia 2025 Best Paper Award；NYCU 電子所所長；VLSIC TPC since 2020

**製程/封裝應用點（詳述）**

- **節點 / 段別**：N3/N2 I/O 電源域 + CoWoS AI 封裝電源管理；PMIC IC 設計（製程節點：N16 / N7 / N5）；無線電力傳輸（WPT）/ 諧振式轉換器（LLC Resonant Converter）/ AI Server PSU 電源架構
- **痛點對應**：
  - **CoWoS AI 封裝 PDN（Power Delivery Network）壓降**：N2 Chiplet + HBM 在 CoWoS 封裝下的 PDN 設計面臨 IR-drop 驗證複雜度劇增；陳柏宏 IEEE JSSC 2024 Quad-Mode Regulating Rectifier + TCAS-I 2025 Reconfigurable Buck-Boost 可提供動態電壓調節架構參考，降低 CoWoS PDN IR-drop
  - **AI Server PSU 效率瓶頸**：AI Server（H100 / A100 / GB200 等）PSU 效率要求 > 97%（80 PLUS Titanium），LLC Resonant Converter 配合 Burst Mode Control 在輕載下效率崩潰；陳柏宏 ISPSD 2025 "LLC Resonant Converter Controller with Burst Mode Control and Soft-Start" 直接對應輕載效率優化
  - **GaN HEMT 電流量測精度**：IPEMC-ECCE Asia 2025 Best Paper "Current Measurement of GaN HEMTs Without Insertion Impedance" — 零插入阻抗量測方法解決 GaN 開關機高頻電流量測精度問題，對 TSMC GaN PDK 功率級驗證有直接工具價值
  - **AI Server 無線充電 / 電力傳輸整合**：WPT 在 AI 資料中心的機架間電力分配（無接觸連接器替代）是新興方向；陳柏宏 TCAS-I 2025 Shared-Inductor Buck-Boost 可作 WPT + DC-DC 整合的電路架構基礎
- **可導入時程（TRL）**：**TRL 6-7 / 即時至 12 個月**；LLC Resonant + Regulating Rectifier 均有 JSSC / TCAS-I 頂會發表（TRL 6），接入 TSMC N2 CoWoS PDN benchmark 後估 6-12 個月 PoC；GaN 電流量測工具為 TRL 7（已有 IPEMC 驗證），可即時提供 TSMC GaN 部門參考
- **配合 fab 部門**：TSMC IP 部門（PMIC IP / Analog IP）/ I/O 電源規格 owner 為主對口；CoWoS 封裝整合（Advanced Packaging PIE / PDN 設計）/ GaN PDK 工程為次對口；AI Server 業務（Cloud 客戶 — NVIDIA / AMD / Google）的 TSMC 客戶成功工程為延伸對口
- **預期成效**：
  - CoWoS PDN IR-drop 改善 ≥ 10 mV（以 Regulating Rectifier 動態調節架構介入）
  - AI Server PSU 輕載效率（< 20% 負載）提升 ≥ 2%（Burst Mode LLC 優化）
  - GaN HEMT 電流量測精度誤差 ≤ 2%（無插入阻抗方法）
  - NYCU × TSMC 聯名論文 ≥ 1 篇 / 年（IEEE JSSC / TCAS-I / ISPSD）

**合作紀錄 × 與外部公司狀況**
- 無綁定（學術主導）
- **無公開可見外部綁定**；AI Server 電源研究與下游應用（CoWoS HBM 電源、AI 加速器 PMIC）高度相關，TSMC 客戶端潛在共同價值

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — CoWoS AI 封裝 PDN 動態電壓調節 IC**：以 JSSC 2024 Quad-Mode Regulating Rectifier 架構為基礎，設計適用 TSMC N16 / N7 製程的 PDN 調節器 IP，目標將 CoWoS stack 的 IR-drop 峰值壓低 ≥ 10 mV；可與 Advanced Packaging PIE 串接驗證
  - **主題目 B — AI Server PSU LLC Resonant 效率優化**：接續 ISPSD 2025 LLC + Burst Mode 成果，以 TSMC N7 製程設計高效率 LLC 控制器 IC（原型 tape-out）；目標輕載效率達業界水準，支援 AI Server 整機 PSU 認證
  - **延伸題目 C — GaN HEMT 電流量測工具標準化**：將 IPEMC-ECCE Asia 2025 Best Paper 量測方法轉為 TSMC GaN PDK 客戶可用的標準化量測建議書，降低 GaN 功率模組客戶驗證門檻
  - **延伸題目 D — AI Server WPT 機架電力整合**：以 TCAS-I 2025 Shared-Inductor Buck-Boost 為電路模組，探索資料中心機架無線電力傳輸替代傳統連接器的可行性（長期方向，TRL 3-4）
- **制度與簽約**
  - **架構**：NYCU 產學共同主持（Green Power Electronics Lab 機構）+ 陳柏宏個人 PI；所長行政檔期需在合約中明確研究時間保障（建議每週 ≥ 10 小時研究投入）
  - **預算建議區間**：年 NT$ 800-1,500 萬（含 N16/N7 原型 tape-out 預算 + 學生獎助 + 設備 + 教師研究費）；2-3 年滾動（推估區間，非承諾數字，依 NYCU 電子所產學 PMIC 量級對標）
  - **簽約對象**：NYCU Green Power Electronics Lab（機構）+ 陳柏宏（個人 PI）；IP 依 NYCU 標準框架；原型 tape-out IP 歸屬在合約中明確
  - **學生通道**：NYCU IEE（陳柏宏兼所長）→ TSMC IP 部門 / AI Server 電源設計招募；所長身份有助於整合 IEE 全所學生資源
- **KPI（年度滾動 + Exit criteria）**
  - **第 1 年**：PDN Regulating Rectifier 電路設計完成 + 模擬驗證（TSMC N16 PDK）；LLC 控制器 IC 完成 layout 設計；GaN 量測標準化建議書草案完成；IEEE JSSC / TCAS-I 投稿 1 篇
  - **第 2 年**：PDN Regulating Rectifier 完成 N16 tape-out + 實測；IR-drop 改善 ≥ 10 mV 驗收；LLC 控制器 IC 完成 N7 tape-out；IPEMC GaN 量測建議書正式提交 GaN PDK 部門
  - **第 3 年**：PDN 調節器 IP 進入 TSMC CoWoS IP 庫候選評估；LLC 控制器 IC 完成效率量測（輕載 ≥ 2% 提升）；AI Server WPT PoC 設計提案完成
  - **Exit criteria**：第 2 年 tape-out 後 IR-drop 改善 < 5 mV，重新評估電路架構；LLC 控制器輕載效率改善 < 1%，暫緩主題目 B
- **執行對口與啟動條件**
  - **主對口**：TSMC IP 部門（Analog / Power IP）/ I/O 電源規格 owner
  - **次對口**：CoWoS PDN 設計工程；GaN PDK 工程；AI Server 客戶成功工程
  - **啟動條件**：NYCU 產學合約確認 + N16 PDK 授權（保密協議）+ Q1 kick-off（陳柏宏 / IP 部門 / Green Power Lab）；所長行政檔期確認（可能需等學期間安排）
- **風險與緩解**
  - **所長行政負擔（中等風險）**：陳柏宏自 2021 擔任 NYCU 電子所所長，行政事務佔用研究時間；建議合約明確每週研究時間最低投入，並指定學生 TA 協助 PM
  - **AI Server PSU 為新方向**：陳柏宏 AI Server PSU 方向相對新穎（2025 起發表），與 PMIC 主軸串接的成熟度尚待評估；建議以 PMIC + PDN 為主線，AI Server PSU 為第 2 年延伸
  - **Tape-out 預算風險**：N16 / N7 原型 tape-out 費用高（單次 NT$ 300-500 萬 est.）；預算估算需納入失敗重跑風險 buffer
  - **能力限制**：WebSearch 無法確認陳柏宏現有廠內合作紀錄；無綁定狀態增加接洽彈性，但也意味著無既有 TSMC 窗口；建議透過 VLSIC TPC 人脈網絡（陳柏宏 since 2020）建立初始連接
- **連結**：[NYCU 電子所教師頁](https://iee.nycu.edu.tw/en/teacher/p1.php?num=144&page=1) ｜ [NYCU Academic Hub](https://scholar.nycu.edu.tw/en/persons/po-hung-chen/) ｜ [Green Power Electronics Lab](https://hakko0921.wixsite.com/wpmu) ｜ [Lab Biography](https://hakko0921.wixsite.com/wpmu/biography?lang=zh) ｜ [Lab Publication](https://hakko0921.wixsite.com/wpmu/publication) ｜ 代表論文：IEEE JSSC 2024 Quad-Mode Regulating Rectifier / TCAS-I 2025 Shared-Inductor Buck-Boost / IPEMC-ECCE Asia 2025 Best Paper（GaN HEMTs 電流量測）

---

### B31. 蔡銘峰（Ming-Feng Tsai）｜總分 **7.0**（B 級）｜第三波

| 校系職級 | NCCU 資訊科學系 + Academia Sinica CITI 合聘（2020/06-）｜ 正教授（Professor，2025/08 升等）；2017-2025 副教授；2011-2017 助理教授 ｜ PhD: NTU CSIE 2009（指導教授：Hsin-Hsi Chen）|
|---|---|
| 學術指標 | h-23 / 引用 5,393 / i10-40；最高引論文 ICML 2007 Listwise（3,005 引）|
| Lab | CLIP Lab（http://clip.csie.org/）|
| **5 維度評分** | 研究 8 ｜ fab 6 ｜ Lab 7 ｜ 接洽 9 ｜ 長期 6 ｜ SIGIR 頂會 + 方法論原型 + 無綁定 |

**核心專長 × 近 3 年代表實績**
- Learning-to-Rank / RAG（Retrieval-Augmented Generation）/ 對話 IR / 中文檢索
- SIGIR 2025 Dynamic Margin-based Contrastive Learning for IR；TREC iKAT 2025 "Enhancing Personalized Conversational Search via Query Reformulation and Rank Fusion"；WSDM Cup 2016 Entity Ranking 冠軍；2025/08 升正教授；AS CITI 兼任副研究員（since 2020/06）；MSRA 2006 Best Intern
- 2025/08 升正教授；WSDM Cup 2016 Entity Ranking 冠軍；MSRA 2006 Best Intern

**合作紀錄 × 與外部公司狀況**
- 無綁定
- **無公開可見外部綁定**

**製程/封裝應用點（詳述）**

- **節點 / 段別**：製程知識庫整合；適用 N5/N3 以降複雜製程文件管理
- **痛點對應**：
  - **工程師查文件耗時**：多版本製程文件手動查找、BKM 知識碎片化
  - **跨部門知識轉移低效**：YE/RD 新進工程師 onboarding 慢，知識孤島難打通
- **可導入時程（TRL）**：**TRL 3-5 / 12-18 個月**；RAG PoC 框架已成熟，需工廠語料適配與資安隔離
- **配合 fab 部門**：IT/FIT（知識平台主導）；YE/PE 提供製程文件語料
- **預期成效**：
  - 工程師查文件時間減少 40%
  - YE FAQ 覆蓋率 ≥ 80%
  - 每年聯名論文 ≥ 1 篇

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — 製程知識 RAG 系統**：以 N5/N3 製程文件語料建立工程師自然語言查詢 BKM 與故障排查知識平台
  - **主題目 B — LtR 優化檢索排序**：利用 Learning-to-Rank 優化文件相關性排序，結合工程師回饋迭代改善
- **制度與簽約**：技術合作合約（NCCU CSIE）；年度預算 500-800 萬（推估區間，非承諾數字，依 NCCU 既有量級對標）；學生通道：碩博生 RA 駐場 + TSMC IT 實習
- **KPI + Exit criteria**：第 1 年 RAG MRR ≥ 0.65 / 文件覆蓋 ≥ 500 份；第 3 年工程師主動使用率 ≥ 30%；Exit：MRR < 0.5 且連續 2 季無改善
- **執行對口**：主 IT/FIT / 次 YE 製程部門
- **風險**：製程文件機密等級高（IP 隔離需先行）；學生離職帶走 fine-tuned 模型需合約約束
- **能力限制**：WebSearch 無法驗證 NCCU-TSMC 既有非公開合作協議
- **連結**：[NCCU CS 個人頁](https://www.cs.nccu.edu.tw/~mftsai/about.html) ｜ [NCCU CS 系師資列表](https://www.cs.nccu.edu.tw/csnccu/web/team/team.jsp?lang=en) ｜ [Google Scholar](https://scholar.google.com/citations?user=ZLkFlS0AAAAJ&hl=zh-CN) ｜ [CLIP Lab](http://clip.csie.org/wiki/pages/B5H3f2N2/MingFeng_Tsai.html) ｜ [研究頁](https://www.cs.nccu.edu.tw/~mftsai/research.html)

---

### B32. 黃瀚萱（Hen-Hsen Huang）｜總分 **6.9**（B 級）｜第三波

| 校系職級 | Academia Sinica 資訊科學研究所（IIS）｜ 副研究員（Associate Research Fellow，2024 升等）；2021-2024 助研究員；前 NCCU CS 助理教授 2019-2021 ｜ PhD: NTU CSIE ~2013-2014（ACLCLP 2014 Doctoral Dissertation Honorable Mention 推算；MS NCTU ~2008）|
|---|---|
| 學術指標 | h-25 / 引用 2,209 / i10-70；CAG 論文 82 引（2025）|
| Lab | AS IIS 副研究員（前語言與知識科技實驗室）|
| **5 維度評分** | 研究 7 ｜ fab 6 ｜ Lab 7 ｜ 接洽 9 ｜ 長期 6 ｜ WWW 2025 + 方法論 + AS 獨立 |

**核心專長 × 近 3 年代表實績**
- CAG（Cache-Augmented Generation）— WWW 2025 範式提出者 / RAG 配套範式 / LLM Evaluation
- WWW 2025 "Don't Do RAG: When Cache-Augmented Generation is All You Need"（82 引用）；"Unveiling selection biases: order/token sensitivity in LLMs"（2024，57 引）；SIGIR 2023 General Co-Chair；ROCLING 2024 General Co-Chair；2024 副研究員升等
- 2024 AS 副研究員升等；SIGIR 2023 General Co-Chair；ROCLING 2024 General Co-Chair

**合作紀錄 × 與外部公司狀況**
- 無綁定
- **無公開可見外部綁定**

**製程/封裝應用點（詳述）**

- **節點 / 段別**：製程知識靜態快取管理；適用 N3/A16 工程師規範文件
- **痛點對應**：
  - **RAG 計算成本高**：製程規範文件更新頻率低但查詢量大，向量化成本持續累積
  - **長文件語義切片難**：百頁製程手冊在 RAG 中切片後語境碎裂，CAG 提供完整上下文優勢
- **可導入時程（TRL）**：**TRL 3-5 / 12-15 個月**；CAG 框架已有學術驗證，需工廠語料適配
- **配合 fab 部門**：IT/FIT（與 B31 蔡銘峰配套部署）；PE 提供靜態規範語料
- **預期成效**：
  - 重複查詢延遲降低 60%（CAG vs RAG）
  - 快取命中率 ≥ 70%
  - 每年聯名論文 ≥ 1 篇

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — CAG 製程手冊快取系統**：以 CAG 範式建立 TSMC 製程規範靜態快取知識庫，提升高重複查詢響應效率
  - **主題目 B — RAG/CAG 混合部署評估**：在真實製程文件場景比較 RAG 與 CAG 效能，形成混合部署建議
- **制度與簽約**：技術合作合約（Academia Sinica IIS；走 AS 合作協議）；年度預算 400-700 萬（推估區間，非承諾數字，依 AS IIS 既有量級對標）；學生通道：AS 博後 + 碩士生 RA 合聘
- **KPI + Exit criteria**：第 1 年 CAG 快取命中率 ≥ 70% / 延遲改善 ≥ 50%；第 3 年製程手冊覆蓋率 ≥ 80%；Exit：快取命中率 < 50% 且連續 3 個月無改善
- **執行對口**：主 IT/FIT / 次 PE 製程工程部門
- **風險**：AS 合作合約週期較長（需提前 3-4 個月啟動）；製程文件更新頻繁時 CAG 快取需頻繁重建
- **能力限制**：WebSearch 無法驗證 AS IIS-TSMC 非公開合作協議
- **連結**：[AS IIS 個人頁](https://homepage.iis.sinica.edu.tw/pages/hhhuang/index_zh.html) ｜ [AS IIS Vita](https://homepage.iis.sinica.edu.tw/pages/hhhuang/vita_en.html) ｜ [Google Scholar](https://scholar.google.com/citations?user=ro65EMcAAAAA&hl=en) ｜ [AS IIS Research Fellows](https://www.iis.sinica.edu.tw/en/page/People/ResearchFellows.html) ｜ [NCCU CS 舊個人頁](https://www.cs.nccu.edu.tw/~hhhuang/)

---

### B33. 游濟華（Chi-Hua Yu）｜總分 **6.9**（B 級）｜第二波

| 校系職級 | NCKU 工程科學系（半導體學院合聘待核實）｜ 副教授（Associate Professor）｜ PhD: NTU 土木工程 2013（BEng 中原大學 2008；MIT postdoc 後跨域到 AI+材料）|
|---|---|
| 學術指標 | h-22 / 引用 2,339；62 件研究產出 |
| Lab | LAiMM Lab（Laboratory for AI and Multiscale Modeling）|
| **5 維度評分** | 研究 7 ｜ fab 7 ｜ Lab 6 ｜ 接洽 9 ｜ 長期 6 ｜ h-22 + 軸向前瞻 + 跨域背景 |

**核心專長 × 近 3 年代表實績**
- AI 多尺度模擬 / 新材料預測（材料資訊學）/ DFT + ML 混合方法
- 2025 Materials and Design "AI-Driven Woven Composite Optimization via Deep+RL"；2025 microfluidic thermal control AI；2025/12 Results in Engineering "AI-driven bandsaw machining"；2026 IJGO "Spontaneous preterm birth AI prediction"；h-22 / 引用 2,339；跨域背景 NTU 土木 → MIT postdoc → AI+材料
- 跨域背景：NTU 土木 → MIT postdoc → AI+材料；62 件研究產出

**合作紀錄 × 與外部公司狀況**
- 無綁定
- **無公開可見外部綁定**

**製程/封裝應用點（詳述）**

- **節點 / 段別**：先進介電材料開發；適用 N3/A16 High-k/Metal Gate（HKMG）堆疊
- **痛點對應**：
  - **DFT 模擬耗時**：SiO2/HfO2 替代材料的 first-principles 計算試誤成本高，新材料候選篩選週期長
  - **全參數空間最佳化難**：介電常數與漏電流 trade-off 難以在高維參數空間快速收斂
- **可導入時程（TRL）**：**TRL 3-5 / 18-24 個月**；AI 多尺度模擬需 fab 真實量測數據驗證校準
- **配合 fab 部門**：MSE 材料科學部門 / PTD 製程整合；提供 CVD 沉積條件與電性量測資料
- **預期成效**：
  - 新材料候選篩選週期縮短 30-40%
  - SiO2/HfO2 工藝參數預測誤差 ≤ 5%
  - 每年聯名論文 ≥ 1 篇

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — 先進介電材料 AI 篩選**：以 DFT+ML 混合方法預測 High-k 材料電性，加速 N3/A16 HKMG 候選篩選
  - **主題目 B — AI 驅動工藝參數最佳化**：利用 RL 方法自動探索 SiO2/HfO2 沉積參數，最大化介電常數並抑制漏電流
- **制度與簽約**：技術合作合約（NCKU 工程科學系）；年度預算 600-1000 萬（推估區間，非承諾數字，依 NCKU 既有量級對標）；學生通道：碩博生 RA + TSMC MSE 實習
- **KPI + Exit criteria**：第 1 年材料預測準確率 ≥ 90% / fab 驗證樣品 ≥ 10 批；第 3 年主動提供工藝建議 ≥ 5 項；Exit：預測誤差 > 15% 且連續 3 個月無改善
- **執行對口**：主 MSE 材料部門 / 次 PTD 製程整合
- **風險**：材料特性數據高度機密（資安隔離需先行）；跨域背景（土木→材料）對 fab 製程流程的認知存在差距
- **能力限制**：WebSearch 無法驗證 NCKU-TSMC 非公開材料合作協議
- **連結**：[LAiMM Lab](https://www.laimm.net/) ｜ [NCKU ResearchOutput](https://researchoutput.ncku.edu.tw/zh/persons/chi-hua-yu) ｜ [LinkedIn](https://www.linkedin.com/in/chi-hua-yu-a7a86377) ｜ [ResearchGate](https://www.researchgate.net/profile/Chi-Hua-Yu)

---

### B34. 羅裕龍（Yu-Lung Lo）｜總分 **6.9**（B 級，行政升級 +0.1）｜第二波

| 校系職級 | NCKU 機械工程學系 + 儀器發展中心主任（since 2010）+ 工學院副院長兼任 ｜ 成大講座教授（Chair Professor / Eminent Scholar Professor，特聘教授 since 2006 後升等）｜ PhD: University of Maryland, College Park 機械工程 1995（MS UMD 1992）|
|---|---|
| 學術指標 | h-46 / 引用 6,918（since 2021: h=27, 引用 2,718）；SEM Fellow / CSME Fellow；亞洲實驗力學會主席 |
| Lab | MOEMS Lab（Micro-Opto-Electro-Mechanical Systems）+ 儀器中心 |
| **5 維度評分** | 研究 8 ｜ fab 5 ｜ Lab 7 ｜ 接洽 9 ｜ 長期 7 ｜ h-46 + 無半導體 PoC + 中型 + 無綁定 |

**核心專長 × 近 3 年代表實績**
- 高深寬比結構關鍵尺寸預測 / 光學精密量測（理論強）/ 干涉量測
- 特聘教授 + 儀器發展中心主任 + 國科會儀器中心主任；2025/04 Journal of Materials Processing Technology；2026/01 Journal of Materials Research and Technology；2026/06 Optics and Lasers in Engineering（光學精密量測）；h-46 累積；Google Scholar 6,300+ 引用
- SEM Fellow；CSME Fellow；亞洲實驗力學會主席

**合作紀錄 × 與外部公司狀況**
- 無綁定
- **無公開可見外部綁定**

**製程/封裝應用點（詳述）**

- **節點 / 段別**：GAA 奈米片結構光學量測；適用 N2/A16 以降高深寬比元件
- **痛點對應**：
  - **CD 量測破壞性高**：GAA 奈米片高深寬比下傳統 SEM 截面量測耗時且破壞性，無法全批次監控
  - **原位量測空缺**：製程線寬監控需非破壞性方案，現有光學方法對 GAA 精度不足
- **可導入時程（TRL）**：**TRL 2-4 / 24-30 個月**；理論基礎完整，半導體 PoC 橋接尚未完成，需先期驗證
- **配合 fab 部門**：Metrology 量測部門（主）；Equipment 設備工程（次）；提供 GAA 測試片與量測基準
- **預期成效**：
  - GAA CD 非破壞量測 throughput 提升 2-3x
  - 量測精度達 ±0.5nm 級
  - 每年聯名論文 ≥ 1 篇

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — GAA 干涉光學 CD 量測 PoC**：以光學干涉量測技術建立 N2/A16 GAA 結構非破壞性 CD 預測模型
  - **主題目 B — AI 輔助量測模型校正**：結合 ML 方法消除干涉量測系統誤差，提升高深寬比結構準確率
- **制度與簽約**：技術合作合約（NCKU 機械工程系）；年度預算 500-800 萬（推估區間，非承諾數字，依 NCKU 既有量級對標）；學生通道：博士生 RA + TSMC Metrology 實習
- **KPI + Exit criteria**：第 1 年半導體 PoC 完成 / 量測精度 ≤ ±0.5nm；第 3 年 throughput 較 SEM 提升 ≥ 2x；Exit：精度 > ±2nm 且連續 3 個月無改善
- **執行對口**：主 Metrology 量測部門 / 次 Equipment 設備工程
- **風險**：fab 5 分偏低，需先完成半導體 PoC 橋接才進 JDP；院長行政職影響研究投入時間
- **能力限制**：WebSearch 無法驗證 NCKU-TSMC 量測技術非公開合作
- **連結**：[NCKU ME 教師頁](https://me.ncku.edu.tw/content_teacher_detail.php?teacher_rkey=92FXQZG3V4) ｜ [NCKU ResearchOutput](https://researchoutput.ncku.edu.tw/en/persons/yu-lung-lo) ｜ [Google Scholar](https://scholar.google.com/citations?user=Li7MD7YAAAAJ&hl=en) ｜ [ResearchGate](https://www.researchgate.net/profile/Yu-Lung-Lo-2) ｜ [SPIE](https://spie.org/profile/Yu-Lung.Lo-12555)

---

### B35. 陳以錚（Yi-Cheng Chen）｜總分 **6.6**（B 級）｜第二波

| 校系職級 | NCU 資訊管理學系 教授 + 系主任 ｜ 教授（Professor）+ 系主任（Chair）｜ PhD: NCTU（今 NYCU）資訊工程 2012 |
|---|---|
| 學術指標 | h-22 / 引用 1,728 / i10（Scopus h=18, 1,208）|
| Lab | ADML Lab |
| **5 維度評分** | 研究 7 ｜ fab 6 ｜ Lab 6 ｜ 接洽 8 ｜ 長期 6 ｜ IEEE TETC + 方法論應用 + 系主任 |

**核心專長 × 近 3 年代表實績**
- 智慧製造 / Industry 4.0 決策 / 缺陷預測 / 虛擬強化學習
- IEEE TETC 2025 "Virtual Reinforcement Learning for Defect Prediction in Smart Manufacturing"（Vol. 13, No. 3, pp. 990-1002）；IEEE TKDE 2026 sequential basket recommendation；IEEE TCSS 2024 transformer-based recommendation；ACM TOIT 2024 cross-domain recommendation；系主任級制度對接
- IEEE TETC 2025；NCU 資管系主任

**合作紀錄 × 與外部公司狀況**
- 無綁定
- **無公開可見外部綁定**

**製程/封裝應用點（詳述）**

- **節點 / 段別**：製程缺陷 Virtual RL 預測；適用任一節點量產線（缺陷模式跨節點通用）
- **痛點對應**：
  - **缺陷標記數據不足**：fab 缺陷數據有限且標記成本高，真實數據訓練樣本稀缺
  - **模型泛化性差**：換線或新製程時需重訓練，缺乏即時回饋迴路
- **可導入時程（TRL）**：**TRL 4-6 / 12-18 個月**；Virtual RL 框架已在 TETC 論文驗證，需 fab 真實製程數據適配
- **配合 fab 部門**：YE 良率工程（主）；Equipment 設備工程（次）；提供缺陷標記數據與設備感測資料
- **預期成效**：
  - 缺陷預測 F1-score ≥ 0.85
  - 虛擬 RL 訓練效率較純真實數據提升 30%
  - 每年聯名論文 ≥ 1 篇

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — fab 缺陷 Virtual RL 預測**：以 Virtual RL 框架在模擬環境預訓練缺陷預測模型，遷移至 TSMC 量產線
  - **主題目 B — Industry 4.0 良率決策優化**：利用 RL 策略自動決策製程調整方向，縮短缺陷追因時間
- **制度與簽約**：技術合作合約（NCU 資訊管理系）；年度預算 500-800 萬（推估區間，非承諾數字，依 NCU 既有量級對標）；學生通道：碩博生 RA + TSMC YE 實習
- **KPI + Exit criteria**：第 1 年 PoC 缺陷預測 F1 ≥ 0.85 / 數據覆蓋率 ≥ 80%；第 3 年自動決策建議採納率 ≥ 50%；Exit：F1 < 0.70 且連續 2 季無改善
- **執行對口**：主 YE 良率工程 / 次 Equipment 設備工程
- **風險**：製程缺陷數據高度機密（分類存取需先行）；系主任行政職影響研究投入時間
- **能力限制**：WebSearch 無法驗證 NCU-TSMC 非公開合作協議
- **連結**：[個人網站](https://sites.google.com/view/ycchen) ｜ [NCU Scholars](https://scholars.ncu.edu.tw/en/persons/yi-cheng-chen) ｜ [Google Scholar](https://scholar.google.com/citations?user=pxx0z6oAAAAJ&hl=zh-TW) ｜ [ADML Lab Publications](https://sites.google.com/view/ycchen/publications)

---

### B36. 蕭宏章（Hung-Chang Hsiao）｜總分 **6.6**（B 級）｜第三波

| 校系職級 | NCKU 資訊工程學系 ｜ 教授（2012 升正；2009 副；2005 助理）｜ PhD: NTHU 資訊工程 2000（1996-2000）|
|---|---|
| 學術指標 | h-17 / 引用 1,270 / i10-29 |
| Lab | 分散式系統研究實驗室（資訊系館 65A03）|
| **5 維度評分** | 研究 7 ｜ fab 7 ｜ Lab 6 ｜ 接洽 7 ｜ 長期 6 ｜ 分散系統 + FDC 單點 + 中型 |

**核心專長 × 近 3 年代表實績**
- 分散式系統 / 大數據平台 / 雲原生計算 / Apache Submarine ML / 聯邦學習（部分研究方向）/ 機台數據分散式儲存
- 2022 IEEE TASE 數位孿生容器雲製造（76 引）；2022 EuroMLSys Apache Submarine ML 平台；2023 IEEE BigData Apache Kafka 負載平衡；2026 IEEE TSC（已接受）；2018 IEEE ICTC × 聯電半導體大數據平台合作
- IEEE TSC 2026；IEEE TASE 2022；NCKU CSIE 教授 2012 升等

**合作紀錄 × 與外部公司狀況**
- 日月光、華邦、聯華電子（聯電）、工研院、資策會；2018 聯電大數據平台合作論文
- **有聯電大數據平台合作實證**（2018）；屬分散式儲存/平台層合作，非製程 AI 核心

**製程/封裝應用點（詳述）**

- **節點 / 段別**：機台數據分散式採集與儲存；適用所有節點 EDA/FDC 數據基礎設施
- **痛點對應**：
  - **集中式儲存瓶頸**：機台感測器每分鐘產生 TB 級數據，集中式架構難支撐即時 FDC 負載
  - **跨廠區隱私合規空缺**：多廠區 / 多機台數據聯邦學習缺統一平台，合規框架未建立
- **可導入時程（TRL）**：**TRL 5-7 / 6-12 個月**；有聯電大數據平台合作實證（2018），TSMC 適配路徑清晰
- **配合 fab 部門**：IT/FIT 數據基礎設施（主）；Equipment 設備工程 FDC 感測數據（次）
- **預期成效**：
  - 機台數據 ingestion throughput 提升 50%
  - 跨廠區聯邦學習 baseline 建立
  - 每年聯名論文 ≥ 1 篇

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — 機台大數據分散式平台升級**：基於 Apache Kafka/Submarine 架構建立高吞吐 TSMC 機台感測數據分散式平台
  - **主題目 B — 跨廠區聯邦學習基礎設施**：在機台數據隱私合規約束下，建立跨 fab 聯邦學習通訊框架
- **制度與簽約**：技術合作合約（NCKU 資訊工程系）；年度預算 600-1000 萬（推估區間，非承諾數字，依 NCKU 既有量級對標）；學生通道：博士生 RA + TSMC IT 實習
- **KPI + Exit criteria**：第 1 年平台 throughput ≥ 1TB/day / FDC latency ≤ 100ms；第 3 年聯邦學習跨廠 pilot ≥ 2 廠；Exit：throughput < 500GB/day 且連續 2 季無改善
- **執行對口**：主 IT/FIT 數據基礎設施 / 次 Equipment FDC 部門
- **風險**：平台層合作非製程 AI 核心，長期需求度可能降低；聯電合作經驗需確認 TSMC 技術隔離需求
- **能力限制**：WebSearch 無法驗證 NCKU-TSMC 非公開平台合作協議
- **連結**：[NCKU CSIE 教師頁](https://www.csie.ncku.edu.tw/zh-hant/members/27) ｜ [英文教師頁](https://www.csie.ncku.edu.tw/en/members/27) ｜ [Google Scholar](https://scholar.google.com/citations?user=sqw1GncAAAAJ&hl=en) ｜ [NCKU Research Output](https://researchoutput.ncku.edu.tw/en/persons/hung-chang-hsiao/) ｜ [個人 Lab](https://sites.google.com/view/hung-chang-hsiao/home) ｜ [半導體合作論文](https://researchoutput.ncku.edu.tw/en/publications/the-case-of-big-data-platform-services-for-semiconductor-wafer-fa/)

---

### B37. 許嘉裕（Chia-Yu Hsu）｜總分 **6.5**（B 級，職級從副升至教授 +0.6）｜第二波

| 校系職級 | NTHU 工業工程與工程管理學系（IEEM）｜ 正教授（Professor，歷程：NTUT 北科大副教授 → NTUST 台科大教授 → 現任 NTHU 清華 IEEM 教授）｜ PhD: NTHU 工業工程與工程管理學系（BS 成功大學統計；MS NTHU IEEM）|
|---|---|
| 學術指標 | h-24 / 引用 2,549 / i10-42 |
| Lab | NTHU IEEM Lab |
| **5 維度評分** | 研究 8 ｜ fab 7 ｜ Lab 7 ｜ 接洽 8 ｜ 長期 7 ｜ 中生代 + h-24 + SPC/FDC/Yield + 無綁定 |

**核心專長 × 近 3 年代表實績**
- 機器學習 + 半導體良率提升 / 故障偵測與診斷（FDC）/ 大數據分析 / 先進製程控制 / SPC / FDC / VM / Yield
- 2020 吳大猷先生紀念獎；中工會陳樹勛先生紀念講座；NVIDIA 訪問研究員；智慧製造中生代旗手
- 2020 吳大猷先生紀念獎；中工會陳樹勛先生紀念講座；NVIDIA 訪問研究員

**合作紀錄 × 與外部公司狀況**
- 無綁定（學術主導）
- **無公開可見外部綁定**

**製程/封裝應用點（詳述）**

- **節點 / 段別**：製程統計控制（SPC）/ 虛擬量測（VM）/ 良率提升；適用 N5/N3 量產線批次監控
- **痛點對應**：
  - **SPC 管制圖靜態**：現有 ±3σ 管制界限無法自適應製程動態波動，誤報率高
  - **FDC 特徵手動**：故障偵測特徵依賴人工定義，缺乏自動化 ML 替代方案
- **可導入時程（TRL）**：**TRL 6-8 / 6-12 個月**；SPC/FDC/VM 框架成熟，直接適配 TSMC 製程數據
- **配合 fab 部門**：YE 良率工程（主）；統計品管部門（次）；提供製程批次數據
- **預期成效**：
  - FDC 預警準確率 ≥ 90%
  - 製程變異偵測時間縮短 50%
  - 每年聯名論文 ≥ 1 篇

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — SPC/FDC 自適應系統**：以 ML 自動更新管制界限，取代靜態 ±3σ SPC，適應 N5/N3 製程動態波動
  - **主題目 B — 多變量虛擬量測 VM**：基於製程感測數據建立 VM 模型，預測晶圓電性參數，減少破壞性量測
- **制度與簽約**：產學共同主持（NTHU IEEM）；年度預算 1000-1500 萬（推估區間，非承諾數字，依 NTHU 既有量級對標）；學生通道：博士生 RA + TSMC YE 實習
- **KPI + Exit criteria**：第 1 年 FDC 準確率 ≥ 90% / VM 殘差 ≤ 5%；第 3 年自適應 SPC 覆蓋機台 ≥ 100 台；Exit：FDC < 80% 且連續 2 季無改善
- **執行對口**：主 YE 良率工程 / 次 統計品管部門
- **風險**：SPC 警報假陽性可能影響工程師信任度；NVIDIA 訪問研究員期間研究重心可能轉移
- **能力限制**：WebSearch 無法驗證 NTHU-TSMC 非公開合作協議
- **連結**：[NTHU IEEM 師資列表](https://ieem.site.nthu.edu.tw/p/403-1310-2658-1.php?Lang=zh-tw) ｜ [NTHU IEEM 個人頁](https://ieem.site.nthu.edu.tw/p/406-1310-297808,r5910.php?Lang=en) ｜ [Google Scholar](https://scholar.google.com/citations?user=I23ksWUAAAAJ&hl=en) ｜ [NTHU 得獎公告](https://ieem.site.nthu.edu.tw/p/406-1310-299817,r3168.php?Lang=zh-tw) ｜ [IEEE Xplore](https://ieeexplore.ieee.org/author/37631630400)

---

### B38. 彭文志（Wen-Chih Peng）｜總分 **6.4**（B 級，內部名單）｜不啟動

| 校系職級 | NYCU 資工 正教授 → 2025 借調 TSMC 處長（內部已確認）｜ 正教授（借調 TSMC 中）｜ PhD: NTU 電機 2001（前 NYCU 資訊學院院長 2019-2022；前 E.SUN-NCTU 金融 AI 中心主任 2021-2024/3）|
|---|---|
| 學術指標 | h-47 / 引用 8,214 / i10-142 |
| Lab | 前瞻資料庫系統實驗室（Advanced Database Systems Laboratory，EC446A）|
| **5 維度評分** | 研究 9 ｜ fab 7 ｜ Lab 7 ｜ 接洽 0 ｜ 長期 7 ｜ SIGIR 頂會 + Agentic IR 應用 + 借調 TSMC 中 |

**核心專長 × 近 3 年代表實績**
- Agentic Decomposed IR / SIGIR 主題 / Query 解構與檢索
- SIGIR 2025 "Template-Based Financial Report Generation in Agentic and Decomposed IR"；LLM4TS 時序預測（2025，ACM TIST，490 引）；2025 自監督學習綜述；2023/8-2024/1 借調工研院（前次紀錄）；2025 借調 TSMC 任處長（內部已確認）；前 NYCU 資訊學院院長 2019-2022
- 前 NYCU 資訊學院院長 2019-2022；2025 借調 TSMC 處長

**合作紀錄 × 與外部公司狀況**
- 2025 借調 TSMC（TSMC 員工身份）
- **TSMC 借調處長（2025-）** — 借調期間屬 TSMC 員工身份

**製程/封裝應用點（詳述）**（不啟動 — 借調 TSMC 中，理論定位）

- **節點 / 段別**：製程文件 Agentic IR 應用；適用工程師知識管理與決策支援
- **痛點對應**：
  - **Agentic 製程決策缺工具**：複雜製程變更決策涉及多步驟文件查詢，現有工具不支援 Agentic 推理
  - **工程師 LLM 部署空缺**：TSMC 尚缺成熟製程知識 RAG/CAG 部署框架
- **可導入時程（TRL）**：借調期間 TSMC 內部主導；**2027 返校後重評**
- **配合 fab 部門**：由 TSMC 借調處長身份內部協調
- **預期成效**：借調期間 TSMC 內部推進；返校後依研究方向重評合作可能

**建議合作方式 × 公開連結**

- **題目**
  - **不啟動（借調中）**：2025 起借調 TSMC 處長，借調期間屬 TSMC 員工身份，外部合約視為利益衝突
  - **2027 返校後重評**：依返校後研究方向評估 Agentic IR / 製程知識管理 PoC
- **制度與簽約**：借調期間不啟動；返校後評估技術合作合約（NYCU CS）
- **KPI + Exit criteria**：借調期間由 TSMC 內部評定；返校後訂定
- **執行對口**：借調期間 TSMC 內部負責；返校後重新對接
- **風險**：借調期間接洽可能違反 TSMC 內規；返校時間及研究方向不確定
- **能力限制**：WebSearch 無法驗證借調細節與確切返校時間表
- **連結**：[NYCU 系教師頁](https://www.cs.nycu.edu.tw/members/detail/wcpeng) ｜ [個人網站](https://sites.google.com/site/wcpeng/) ｜ [Google Scholar](https://scholar.google.com/citations?user=T5Rs-ngAAAAJ&hl=zh-TW) ｜ [NYCU Academic Hub](https://scholar.nycu.edu.tw/en/persons/wen-chih-peng) ｜ [SIGIR 2025 論文](https://dl.acm.org/doi/10.1145/3726302.3730253)

---

### B39. 連震杰（Jenn-Jier James Lien）｜總分 **6.4**（B 級）｜第三波

| 校系職級 | NCKU 資工系 教授 + 電資學院副院長 + 多媒體博士學程主任 + AI 機器人學程主任 ｜ 教授 / 電資學院副院長 ｜ PhD: University of Pittsburgh 電機工程 1998（BS 中原大學生醫工程 1989；MS 華盛頓大學 St. Louis 電機 1993）|
|---|---|
| 學術指標 | h-20 / 引用 3,051（GS）/ 2,969（ResearchGate）/ i10-35 |
| Lab | 機器人實驗室（資訊系館新大樓 9F）；南科 20 分鐘 |
| **5 維度評分** | 研究 6 ｜ fab 6 ｜ Lab 7 ｜ 接洽 8 ｜ 長期 6 ｜ h-20 + 原型級 AOI + 中型 + 無綁定 |

**核心專長 × 近 3 年代表實績**
- CNN / YOLO 缺陷分類 / 3D 結構光量測 / CUDA 嵌入式 / 南科地緣優勢
- NCKU 電機資訊學院副院長 + AI 機器人學程主任；2025 Taiwan AI Academy 夏季論壇 keynote「打造台灣 AI 機器人新國力」；Measurement journal 2025/06 新論文（量測領域）；Sensors 多篇 2023（品質評估 / 幾何量測 / 缺陷偵測）；2022 Intel + Qisda 合作（IEEE Systems Journal）
- 2025 Taiwan AI Academy 夏季論壇 keynote；NCKU 電資學院副院長；AI 機器人學程主任

**合作紀錄 × 與外部公司狀況**
- Intel / Qisda 2022 合作
- **無獨家綁定**；Intel / Qisda 為歷史合作

**製程/封裝應用點（詳述）**

- **節點 / 段別**：3D 結構光 AOI 缺陷檢測；適用 CoWoS / SoIC 封裝後段 + 南科廠區地緣優勢
- **痛點對應**：
  - **封裝 3D 翹曲偵測空缺**：CoWoS/SoIC 接合缺陷 2D AOI 難以偵測 3D 翹曲，需光學 3D 量測方案
  - **南科在地合作未充分利用**：NCKU 機器人實驗室距南科廠區 20 分鐘，地緣優勢未轉化為快速迭代
- **可導入時程（TRL）**：**TRL 4-6 / 12-18 個月**；3D 結構光 AOI 原型具備，需封裝測試片適配
- **配合 fab 部門**：AP 先進封裝（主）；Metrology 量測部門（次）；南科廠區協調
- **預期成效**：
  - CoWoS 接合缺陷 3D 檢出率 ≥ 95%
  - 南科學生轉任 TSMC 通道建立
  - 每年聯名論文 ≥ 1 篇

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — CoWoS/SoIC 3D 結構光 AOI**：建立封裝後段 3D 翹曲 / 接合缺陷非接觸式光學檢測系統
  - **主題目 B — 嵌入式 CUDA 即時缺陷分類**：結合 YOLO 模型實現 CUDA 嵌入式即時推論，縮短檢測週期
- **制度與簽約**：技術合作合約（NCKU CSIE）；年度預算 400-600 萬（推估區間，非承諾數字，依 NCKU 既有量級對標）；學生通道：碩博生 RA 駐廠 + 南科 TSMC 就地實習
- **KPI + Exit criteria**：第 1 年 PoC 缺陷檢出率 ≥ 95% / 推論速度 ≤ 100ms；第 3 年南科廠區部署 ≥ 1 條線；Exit：檢出率 < 85% 且連續 2 季無改善
- **執行對口**：主 AP 先進封裝 / 次 Metrology 量測部門
- **風險**：3D 結構光系統對振動敏感，fab 環境需額外防震設計；Intel/Qisda 歷史合作需確認無技術隔離
- **能力限制**：WebSearch 無法驗證 NCKU-TSMC 南科廠區非公開合作
- **連結**：[NCKU CSIE 教師頁](https://www.csie.ncku.edu.tw/zh-hant/members/25) ｜ [電資學院副院長](https://eecs.ncku.edu.tw/p/412-1020-24885.php?Lang=zh-tw) ｜ [Google Scholar](https://scholar.google.com/citations?user=C6Ic16IAAAAJ) ｜ [NCKU Research Output](https://researchoutput.ncku.edu.tw/zh/persons/james-jenn-jier-lien/) ｜ [AI 機器人學程](https://aim.ncku.edu.tw/p/426-1179-13.php?Lang=en) ｜ [2025 AI Academy](https://workshop202506.aiacademy.tw/jenn-jier-james-lien/)

---

### B40. 劉禹辰（Yu-Chen Liu）｜總分 **6.4**（B 級）｜第二波

| 校系職級 | NCKU 機械工程系（半導體學院合聘待核實）｜ 助理教授（Assistant Professor）｜ PhD: NCKU 材料科學與工程 2019（本土 PhD）|
|---|---|
| 學術指標 | h-16-17（GS / NCKU 一致）/ 引用 690-739 / i10-21 |
| Lab | LIU LAB 20 人（博生 3 + 碩生 12 + 學士生 5）|
| **5 維度評分** | 研究 6 ｜ fab 6 ｜ Lab 5 ｜ 接洽 9 ｜ 長期 7 ｜ 新銳 + 命中 3D IC + 無綁定 |

**核心專長 × 近 3 年代表實績**
- ML 材料熱力學 / 電遷移（Electromigration）/ 焊接可靠性 / 3D IC 封裝 EM
- Materials Characterization 2025/10（Vol. 228, 115384）Ag/Cu 合金 effective charge ML 建模；Annual Review of Materials Research 2025/07（高影響力年度綜述）；Liu Lab NCKU 新銳；封裝 EM 命中 3D IC；機器學習 + 材料熱力學結合
- Annual Review of Materials Research 2025/07；Materials Characterization 2025/10；LIU LAB 20 人

**合作紀錄 × 與外部公司狀況**
- 無綁定
- **無公開可見外部綁定**

**製程/封裝應用點（詳述）**

- **節點 / 段別**：3D IC 電遷移（EM）可靠性預測；適用 CoWoS / SoIC 封裝銅錫焊點
- **痛點對應**：
  - **EM 失效難預測**：3D IC 堆疊 TSV / Bump 在高電流密度下電遷移失效機制難以事先建模
  - **新材料建模慢**：Ag/Cu 合金等新型焊接材料 EM 有效電荷參數缺乏 ML 快速建模方法
- **可導入時程（TRL）**：**TRL 4-6 / 12-18 個月**；ML 材料熱力學框架已在 Materials Characterization 論文驗證，需 fab 封裝真實數據適配
- **配合 fab 部門**：AP 先進封裝（主）；Package Reliability 可靠性部門（次）；提供 CoWoS 焊點測試數據
- **預期成效**：
  - 3D IC EM 壽命預測誤差 ≤ 10%
  - 新焊接材料候選篩選週期縮短 30%
  - 每年聯名論文 ≥ 1 篇

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — 3D IC EM ML 可靠性預測**：以 ML 建立 CoWoS/SoIC 銅錫焊點 EM 有效電荷參數模型，預測高電流密度失效
  - **主題目 B — 封裝散熱材料可靠性 PoC**：結合熱力學模擬與 ML，評估新型封裝散熱材料的長期可靠性
- **制度與簽約**：技術合作合約（NCKU 機械系）；年度預算 500-800 萬（推估區間，非承諾數字，依 NCKU 既有量級對標）；學生通道：碩博生 RA + TSMC Package Reliability 實習
- **KPI + Exit criteria**：第 1 年 EM 模型誤差 ≤ 10% / fab 驗證樣品 ≥ 5 批；第 3 年主動提供封裝材料選材建議 ≥ 3 項；Exit：誤差 > 20% 且連續 3 個月無改善
- **執行對口**：主 AP 先進封裝 / 次 Package Reliability 可靠性部門
- **風險**：助理教授（新銳）研究穩定性較低；Lab 20 人規模承擔大型專案人力有限
- **能力限制**：WebSearch 無法驗證 NCKU-TSMC 封裝可靠性非公開合作
- **連結**：[LIU LAB](https://sites.google.com/gs.ncku.edu.tw/liumaterials/home) ｜ [LIU LAB Members](https://sites.google.com/gs.ncku.edu.tw/liumaterials/members) ｜ [NCKU ME 教師頁](https://en.me.ncku.edu.tw/content_teacher_detail.php?teacher_rkey=VMOZBD9OE1) ｜ [Google Scholar](https://scholar.google.com/citations?user=gZv6IkwAAAAJ&hl=zh-TW) ｜ [NCKU Research Output](https://researchoutput.ncku.edu.tw/en/persons/yu-chen-liu)

---

### B41. 林勇志（Yeong-Jyh Lin）｜總分 **6.3**（B 級）｜觀察（法務先檢）

| 校系職級 | NSYSU 半導體及重點科技研究學院（SAT）— 先進半導體封測研究所 + 創新半導體製造研究所雙合聘（2024/8 起；前 TSMC 13 年）｜ 副教授級專業技術人員（實務職非學術職）｜ PhD: NCKU 機械工程研究所（年份待核實）|
|---|---|
| 學術指標 | TSMC 多件專利；2021 TSMC 第 9 屆金牌保密獎銀獎 |
| Lab | NSYSU SAT 先進封測所 LA7004（無獨立 Lab）|
| **5 維度評分** | 研究 7 ｜ fab 9 ｜ Lab 7 ｜ 接洽 1 ｜ 長期 7 ｜ 業界資深 + 量產訓練 + 商秘綁定 |

**核心專長 × 近 3 年代表實績**
- 3D 晶圓接合 / 異質整合封裝 / TSV 製程（TSMC 經驗）
- TSMC 2010-2023（特殊模組處經理 → 技術副理 → 主任工程師）；2021 TSMC 第 9 屆金牌保密獎銀獎；技術專長：Hybrid Bond / CoWoS / InFO / SoIC 晶圓級異質整合 + FEA 模擬 + CIS 製程；2024/08 雙所合聘 NSYSU SAT
- 2021 TSMC 第 9 屆金牌保密獎銀獎；TSMC 多件專利

**合作紀錄 × 與外部公司狀況**
- 前 TSMC 13 年資深工程師（商秘綁定）
- **前 TSMC 13 年 + 商秘獎綁定** — 法務先檢 IP 邊界

**製程/封裝應用點（詳述）**（觀察中 — 法務先行確認 IP 邊界）

- **節點 / 段別**：3D 晶圓接合 / 異質整合封裝；Hybrid Bond / CoWoS / InFO / SoIC 相關（**法務先核可範疇**）
- **痛點對應**：
  - **實務知識稀缺**：前 TSMC 13 年 SoIC/CoWoS 工程師，具備外部學術界難以複製的實務深度
  - **商秘邊界不清**：技術知識與商業機密邊界須法務事前確認，否則合作存在 IP 風險
- **可導入時程（TRL）**：**視法務結論**；技術成熟度高（TRL 8-9），啟動條件為法務核可
- **配合 fab 部門**：AP 先進封裝（技術對口）；法務部門（必要前置，確認 IP 邊界）
- **預期成效**：視法務核可範疇決定；S06/S08/S12/S11 已覆蓋同類題目，戰略補充性較低

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — 3D 晶圓接合 IP 邊界確認（法務先行）**：由法務界定前 TSMC 13 年商秘範圍，確認可教授的技術邊界
  - **主題目 B — 異質整合封裝教學顧問**：法務核可後，以 NSYSU SAT 顧問身份提供封裝製程教育訓練
- **制度與簽約**：法務確認後決定（目前觀察中）；若啟動：短期顧問合約為主，年費 100-200 萬；S06/S08/S12/S11 已覆蓋同類題目，戰略優先度不高
- **KPI + Exit criteria**：法務核可後訂定；若核可範疇過窄（僅基礎教學），不啟動正式 PI 合作
- **執行對口**：主 法務部門（IP 邊界審查）/ 次 AP 先進封裝（技術對口）
- **風險**：2021 金牌保密獎銀獎顯示曾接觸高機密性技術，IP 洩露風險高；接洽評分 1 分，須法務主導
- **能力限制**：WebSearch 無法驗證前 TSMC 商秘協議範疇；法務審查需線下執行
- **連結**：[NSYSU SAT 教師頁（英）](https://sat.nsysu.edu.tw/p/405-1325-336409,c25172.php?Lang=en) ｜ [NSYSU SAT 教師頁（中，含學經歷）](https://sat.nsysu.edu.tw/p/405-1325-334976,c25997.php?Lang=zh-tw) ｜ [榮譽獎項頁](https://sat.nsysu.edu.tw/p/404-1325-339788.php?Lang=zh-tw)

---

### B42. 黃乾怡（Chien-Yi Huang）｜總分 **6.2**（B 級）｜第三波

| 校系職級 | NTUT 工業工程與管理系 教授 + 系主任 ｜ 教授 / 系主任 ｜ PhD: SUNY Binghamton 工業工程 1996（MS 1993）|
|---|---|
| 學術指標 | h-21 / 引用 1,503 / i10-41（過去 5 年 h-16）|
| Lab | Advanced Process Technology and Quality Lab（宏裕大樓 632 室）+ 品管實踐訓練教室（534 室）|
| **5 維度評分** | 研究 6 ｜ fab 5 ｜ Lab 7 ｜ 接洽 8 ｜ 長期 6 ｜ h-21 + 後段 PCB + 系主任 + 無綁定 |

**核心專長 × 近 3 年代表實績**
- PCB Gold Finger AOI 缺陷 / 陶瓷基板 AOI / SMT / PCB 後段品質
- 2022 陶瓷基板 DL 缺陷檢測（33 引）；2022 5G 數位孿生（30 引）；2024 Smart TOPSIS 神經網絡供應商選擇（117 引）；2022 金屬製品業精實製造（74 引）；h-21 / 引用 1,503
- NTUT IEM 系主任；SUNY Binghamton PhD 1996

**合作紀錄 × 與外部公司狀況**
- 無綁定
- **無公開可見外部綁定**

**製程/封裝應用點（詳述）**

- **節點 / 段別**：PCB / 陶瓷基板後段 AOI 缺陷檢測；適用 CoWoS / SoIC 供應鏈端封裝基板品質控管
- **痛點對應**：
  - **Gold Finger 漏檢率高**：PCB Gold Finger / 陶瓷基板表面缺陷人工目視漏檢，DL 自動化需求急
  - **供應鏈品質追溯空缺**：CoWoS 基板供應鏈缺陷追溯鏈尚未數位化，良率問題難溯源
- **可導入時程（TRL）**：**TRL 5-7 / 6-12 個月**；陶瓷基板 DL 缺陷論文（33 引）已驗證，可快速適配
- **配合 fab 部門**：AP 先進封裝供應鏈管理部門（主）；供應商品質管理（次）
- **預期成效**：
  - Gold Finger / 陶瓷基板缺陷漏檢率降低 80%
  - 供應鏈缺陷追溯自動化率 ≥ 90%
  - 每年聯名論文 ≥ 1 篇

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — CoWoS 基板 DL AOI 缺陷檢測**：以深度學習建立 Gold Finger / 陶瓷基板表面缺陷自動化辨識系統
  - **主題目 B — 供應鏈端品質數位追溯**：結合 Smart TOPSIS 多準則決策，建立基板供應商品質評估與追溯框架
- **制度與簽約**：技術合作合約（NTUT 工業工程系）；年度預算 400-700 萬（推估區間，非承諾數字，依 NTUT 既有量級對標）；學生通道：碩博生 RA + TSMC 供應鏈品管實習
- **KPI + Exit criteria**：第 1 年漏檢率 ≤ 5% / 缺陷分類準確率 ≥ 95%；第 3 年供應商品質追溯覆蓋率 ≥ 80%；Exit：準確率 < 85% 且連續 2 季無改善
- **執行對口**：主 AP 供應鏈品管 / 次 供應商管理部門
- **風險**：PCB/陶瓷基板屬後段供應鏈，非 TSMC 核心製程 AI，預算優先度偏低；系主任行政職影響研究投入時間
- **能力限制**：WebSearch 無法驗證 NTUT-TSMC 供應鏈非公開合作
- **連結**：[系主任頁](https://iem.ntut.edu.tw/p/405-1081-65525,c11955.php?Lang=en) ｜ [教師頁](https://iem.ntut.edu.tw/p/405-1081-131700,c17321.php?Lang=en) ｜ [Google Scholar](https://scholar.google.com/citations?user=N_1GIA0AAAAJ&hl=en) ｜ [Binghamton SSIE Alumni（PhD 1996 確認）](https://www.binghamton.edu/ssie/graduate/faculty-alumni.html) ｜ [Lab 網站](https://sites.google.com/mail.ntut.edu.tw/ntut632)

---

### B43. 楊素芬（Su-Fen Yang）｜總分 **6.2**（B 級）｜第三波

| 校系職級 | NCCU 統計學系 ｜ 特聘教授（Distinguished Professor）｜ PhD: University of California, Riverside 統計學（年份待核實，約 1990s 中期）|
|---|---|
| 學術指標 | h-22 / 引用 2,015 / i10-53（近 5 年 h-12，引用 782）；多份期刊 Associate Editor |
| Lab | NCCU 統計系所架構（無獨立 Lab）|
| **5 維度評分** | 研究 7 ｜ fab 5 ｜ Lab 6 ｜ 接洽 8 ｜ 長期 6 ｜ 150+ 論文 + 純統計 + 標準局委員 |

**核心專長 × 近 3 年代表實績**
- AEWMA 控制圖 / CUSUM 非參數 / Bayesian EWMA / Gamma / Birnbaum-Saunders 分布
- 2025 Scientific Reports AEWMA 控制圖（Gamma 分佈）；2025（接受）多項式分佈 EWMA 控制圖；2024 Quality and Reliability Engineering International Birnbaum-Saunders 控制圖；2023 Computers & Industrial Engineering 多變量 EWMA 比率監控；經濟部標準局品管委員；中華品質學會委員
- 經濟部標準局品管委員；中華品質學會委員；多份期刊 Associate Editor

**合作紀錄 × 與外部公司狀況**
- 經濟部標準局品管委員（中性）
- **無獨家綁定**；標準局委員為政府諮詢職

**製程/封裝應用點（詳述）**

- **節點 / 段別**：進階統計製程控制（SPC）方法論；適用所有節點量產線批次數據監控
- **痛點對應**：
  - **分布假設錯誤**：製程數據多呈 Gamma / Birnbaum-Saunders 非常態分布，現有 EWMA 假設常態導致誤報
  - **多變量監控不足**：現有 Hotelling T² 對異常值敏感，缺乏非參數多變量 CUSUM 方法
- **可導入時程（TRL）**：**TRL 5-7 / 6-12 個月**；AEWMA / 非參數 CUSUM 方法論已有頂刊驗證，可移植
- **配合 fab 部門**：統計品管部門（主）；YE 良率工程（次）；提供批次數據
- **預期成效**：
  - 非常態製程誤報率降低 40%
  - 多變量 EWMA 比率監控覆蓋機台 ≥ 50 台
  - 每年聯名論文 ≥ 1 篇

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — 非常態製程 SPC 方法論移植**：以 AEWMA / Gamma 控制圖取代現有常態假設管制圖，降低誤報率
  - **主題目 B — 多變量 EWMA 比率監控**：部署多變量 EWMA 比率控制圖，監控批次間良率變異
- **制度與簽約**：委託研究 / 短期顧問合約（NCCU 統計系）；年度預算 200-400 萬（推估區間，非承諾數字，依 NCCU 既有量級對標）；學生通道：碩生 RA 協助數據分析
- **KPI + Exit criteria**：第 1 年 AEWMA 誤報率 ≤ 5% / 適配機台 ≥ 20 台；第 3 年多變量監控覆蓋 ≥ 50 台；Exit：誤報率 > 10% 且連續 2 季無改善
- **執行對口**：主 統計品管部門 / 次 YE 良率工程
- **風險**：純統計方法論需較長推廣期；標準局委員職可能分散研究時間
- **能力限制**：WebSearch 無法驗證 NCCU-TSMC 非公開方法論顧問協議
- **連結**：[NCCU 統計系教師頁](https://stat.nccu.edu.tw/zh_tw/members/楊-素芬-88908104) ｜ [NCCU 統計系英文](https://stat.nccu.edu.tw/en/members/members1/SU-FEN-YANG-88908104) ｜ [Google Scholar](https://scholar.google.com/citations?user=rOz5ZhYAAAAJ&hl=en) ｜ [AEIC 簡介頁（特聘教授確認）](https://mip.keoaeic.org/aeic-members/37.html) ｜ [NCCU 商學院](https://commerce.nccu.edu.tw/en/faculty_link/faculty_directory_bydept/SU-FEN-YANG-31144682)

---

### B44. 林錦德（Chin-Te Lin）｜總分 **6.15**（B 級）｜第三波

| 校系職級 | NCU 機械工程學系 助理教授（前工研院智慧機械中心副主任 2017-2019，含 ITRI Elite 殊榮）｜ 助理教授 ｜ PhD: NTU 機械工程（年份約 2012）|
|---|---|
| 學術指標 | h-6 / 引用 187（NCU Scholars）|
| Lab | E2-218 IoT-enabled Manufacturing Lab |
| **5 維度評分** | 研究 5 ｜ fab 5 ｜ Lab 6 ｜ 接洽 9 ｜ 長期 6 ｜ 新銳 + 室內定位 + 無綁定 |

**核心專長 × 近 3 年代表實績**
- AI 智慧決策 / 可見光定位（VLP）/ AMR 室內定位 / LSTM 時序定位
- 2025 IEEE Sensors Journal "VLP + Kolmogorov-Arnold Network (KAN) 精度強化"；2025 Scientific Reports「區塊鏈 Shop Floor 控制系統」；2024 IEEE Access「智慧製造 DDS」；2024 Materials Science and Engineering A「選擇性雷射熔融 TiN」；2016 RD100 Award 合作（前工研院）；產學合作：透明牙套業 / 迅得機械 / 宏致電子
- 2016 RD100 Award；前工研院智慧機械中心副主任 ITRI Elite

**合作紀錄 × 與外部公司狀況**
- 無綁定
- **無公開可見外部綁定**

**製程/封裝應用點（詳述）**

- **節點 / 段別**：fab AMHS 自動搬運系統室內精準定位；適用前段 / 後段 fab 廠區物料搬運
- **痛點對應**：
  - **AMHS AMR 定位精度不足**：fab 無塵室 WiFi 訊號弱，現有定位精度 ±1m+，影響搬運路徑規劃
  - **RFID 粗糙定位**：現有 RFID 系統精度不足釐米級，VLP 可見光定位提供量級提升
- **可導入時程（TRL）**：**TRL 3-5 / 12-18 個月**；KAN 增強 VLP（IEEE Sensors 2025）已驗證，需 fab 光源環境適配
- **配合 fab 部門**：AMHS 搬運系統部門（主）；設施工程部門（次）；提供廠區光源佈局
- **預期成效**：
  - AMR 室內定位精度 ≤ 5cm（vs 現有 ±1m）
  - AMHS 搬運效率提升 20%
  - 每年聯名論文 ≥ 1 篇

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — fab 無塵室 VLP 高精度定位**：以可見光定位（VLP）+ KAN 建立 fab 廠區 AMR 釐米級室內定位系統
  - **主題目 B — AMHS AMR 自主導航 PoC**：整合 VLP 定位與 LSTM 時序預測，提升 AMR 搬運路徑效率
- **制度與簽約**：技術合作合約（NCU 機械系）；年度預算 400-600 萬（推估區間，非承諾數字，依 NCU 既有量級對標）；學生通道：碩博生 RA + TSMC AMHS 實習
- **KPI + Exit criteria**：第 1 年 PoC 定位精度 ≤ 5cm / fab 光源適配完成；第 3 年 AMHS 效率提升 ≥ 20%；Exit：精度 > 30cm 且連續 3 個月無改善
- **執行對口**：主 AMHS 搬運系統部門 / 次 設施工程部門
- **風險**：fab 無塵室光源頻率可能干擾 VLP 精度（需先期環境測試）；助理教授 h-6 研究成熟度相對有限
- **能力限制**：WebSearch 無法驗證 NCU-TSMC AMHS 非公開合作
- **連結**：[NCU 機械系教師頁](https://www.me.ncku.edu.tw/en/portfolio-item/%E6%9E%97%E9%8C%A6%E5%BE%B7/) ｜ [NCU iTeacher 履歷平台](https://cis.ncu.edu.tw/iTeacher/home/0x548fc79e95899388ef6675c6d14ffaac) ｜ [NCU Scholars](https://scholars.ncu.edu.tw/zh/persons/chin-te-lin) ｜ [LinkedIn](https://www.linkedin.com/in/chin-te-lin-5b41b52b/)

---

### B45. 藍俊宏（Jakey Blue）｜總分 **6.1**（B 級）｜第三波

| 校系職級 | NTU 工業工程學研究所 副教授 + 數學統計碩士學程、機械系兼任 ｜ 副教授（2022/8/1 升等）｜ PhD: NTU 機械工程 2010（**非法國 Mines Saint-Étienne**；法國為 Postdoc 2011-2013 + Maître de Conférences 助理教授 2013-2018 工作職位）|
|---|---|
| 學術指標 | h-13 / 引用 632（過去 5 年 h-? 引用 343）/ i10-16 |
| Lab | LAKE Lab（Laboratory of Analytics on Knowledge Engineering）|
| **5 維度評分** | 研究 6 ｜ fab 5 ｜ Lab 6 ｜ 接洽 8 ｜ 長期 7 ｜ h-13 + 原型 APC + 新副教授 |

**核心專長 × 近 3 年代表實績**
- Physics-Informed APC / HMM 設備劣化 / XAI Manufacturing / R2R Control
- 2010-2011 TSMC Principal Engineer；2011-2013 Mines Saint-Étienne Postdoc → 2013-2018 Maître de Conférences（法國工作）；2020 ESWA / IEEE TASE 代表作；2024 ISSM HMM Equipment State；研究領域：Data analytics, APC, Time series, XAI, 半導體製造
- 2022/8/1 升副教授；前 TSMC Principal Engineer（1 年短期）；Mines-NTU 2022 法合作

**合作紀錄 × 與外部公司狀況**
- 前 TSMC Principal Engineer（1 年短期）；Mines-NTU 2022 法合作
- TSMC 1 年短期經歷為歷史；**無現役競業綁定**

**製程/封裝應用點（詳述）**

- **節點 / 段別**：先進製程控制（APC）/ 設備健康預測；適用 N5/N3 蝕刻 / CMP 製程
- **痛點對應**：
  - **R2R 線性模型不足**：現有 R2R Control 基於線性模型，對非線性製程漂移適應慢
  - **設備劣化閾值手動**：設備狀態監控依賴人工設定，HMM 可提供自動狀態轉換建模
- **可導入時程（TRL）**：**TRL 4-6 / 12-18 個月**；ESWA / IEEE TASE 代表作已驗證方法論，需 TSMC 製程數據適配
- **配合 fab 部門**：PE 製程工程（R2R APC 主）；Equipment 設備工程（HMM 健康次）
- **預期成效**：
  - R2R Control 收斂時間縮短 30%
  - 設備劣化提前預警準確率 ≥ 85%
  - 每年聯名論文 ≥ 1 篇

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — Physics-Informed R2R Control**：以 Physics-Informed APC 取代純數據驅動 R2R 控制，提升 N5/N3 非線性製程穩定性
  - **主題目 B — HMM 設備狀態健康監控**：建立 HMM 設備劣化狀態模型，自動偵測 Chamber / CMP 狀態轉換
- **制度與簽約**：技術合作合約（NTU IE）；年度預算 400-600 萬（推估區間，非承諾數字，依 NTU 既有量級對標）；學生通道：碩博生 RA + TSMC PE 實習
- **KPI + Exit criteria**：第 1 年 R2R 收斂時間縮短 ≥ 30% / HMM 狀態偵測準確率 ≥ 85%；第 3 年 APC 覆蓋機台 ≥ 50 台；Exit：收斂改善 < 10% 且連續 2 季無進展
- **執行對口**：主 PE 製程工程 / 次 Equipment 設備工程
- **風險**：前 TSMC Principal Engineer 1 年短期，需確認無競業條款；2022 剛升副教授，Lab 規模較小
- **能力限制**：WebSearch 無法驗證 NTU-TSMC APC 非公開合作
- **連結**：[NTU IE 升等公告](https://ie.ntu.edu.tw/english/News_Content_n_48014_s_118237.html) ｜ [個人學術網站](https://jakeyblue.github.io/) ｜ [Google Scholar](https://scholar.google.com/citations?user=WFvE0xIAAAAJ&hl=en) ｜ [NTU 技術交易網](https://mip.ord.ntu.edu.tw/expert1.asp?ser=2472)

---

### B46. 蔡坤諭（Kuen-Yu Tsai）｜總分 **6.1**（B 級）｜第三波

| 校系職級 | NTU 電機工程學系 副教授 + 電子所（GIEE）兼聘（since 2008）+ TSMC-NTU Research Center 兼聘（since 2013）｜ 副教授（2005 助理 → 後升副教授）｜ PhD: Stanford University, Aeronautics and Astronautics（航太），2002（副修 EE）|
|---|---|
| 學術指標 | h-12 / 引用 505 / i10-20；前 Intel 193nm 微影製程工程師（2002-2005）|
| Lab | 三實驗室：NDFSL（奈米設計與製造系統）/ PBPPIL（粒子束精密圖案化）/ HPSSL（高性能伺服系統）|
| **5 維度評分** | 研究 7 ｜ fab 6 ｜ Lab 6 ｜ 接洽 7 ｜ 長期 5 ｜ Stanford 博士 + EUV/DFM + 副教授 13 年未升 |

**核心專長 × 近 3 年代表實績**
- EUV 微影 + DFM / e-beam direct-write / TSMC-NTU Center 長期合作
- 2002 Stanford 航太 PhD（副修 EE）；Intel 高級製程工程師（2002-2005，193nm 微影）；TSMC-NTU Center 兼聘 13 年（since 2013）；研究：奈米微影、EUV、DFM、OPC、多電子束微影、控制
- TSMC-NTU Center 兼聘 13 年；前 Intel 193nm 微影製程工程師

**合作紀錄 × 與外部公司狀況**
- TSMC-NTU Center 13 年
- TSMC-NTU Center 為既有合作；**無其他綁定**

**製程/封裝應用點（詳述）**

- **節點 / 段別**：EUV 微影 DFM / OPC / e-beam 多電子束；適用 N3/N2/A16 微影段
- **痛點對應**：
  - **EUV 隨機缺陷激增**：sub-3nm 節點 EUV 隨機缺陷（Stochastic Defects）急增，DFM 規則優化需求高
  - **OPC 計算量龐大**：多電子束 OPC 補償計算量大，缺乏 ML 加速框架
- **可導入時程（TRL）**：**TRL 5-7 / 6-12 個月**；TSMC-NTU Center 13 年合作，既有框架直接延伸
- **配合 fab 部門**：Lithography 微影整合部門（主）；OPC/RET 工程部門（次）
- **預期成效**：
  - EUV 隨機缺陷降低 20%
  - OPC 計算時間縮短 30%（ML 加速）
  - 每年聯名論文 ≥ 1 篇

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — EUV DFM 隨機缺陷 ML 優化**：以 ML 建立 EUV 隨機缺陷預測模型，協助 N2/A16 DFM 設計規則優化
  - **主題目 B — e-beam 多電子束 OPC 加速**：利用 ML 加速多電子束 OPC 補償計算，縮短 mask 製備週期
- **制度與簽約**：既有 TSMC-NTU Center 框架延伸；Center 內預算（推估 500-1000 萬，非承諾數字，依 Center 既有量級對標）；學生通道：NTU EE 博士生 + TSMC Lithography 實習
- **KPI + Exit criteria**：第 1 年 EUV 缺陷預測準確率 ≥ 85% / OPC 計算加速 ≥ 30%；第 3 年 DFM 規則建議採納 ≥ 3 條；Exit：準確率 < 75% 且連續 2 季無改善
- **執行對口**：主 Lithography 微影部門 / 次 OPC/RET 工程
- **風險**：副教授 13 年未升（h-12 偏低），長期研究穩定性存疑；Center 合作需遵循 TSMC-NTU 規則
- **能力限制**：WebSearch 無法驗證 TSMC-NTU Center 合作具體技術範疇
- **連結**：[NTU EE 個人頁](https://www.ee.ntu.edu.tw/profile1.php?teacher_id=901160) ｜ [Biography（含 PhD）](http://www.ee.ntu.edu.tw/bio1.php?id=674) ｜ [Google Scholar](https://scholar.google.com/citations?user=U2qcl4wAAAAJ&hl=en) ｜ [GIEE EDA 教師列表](https://giee.ntu.edu.tw/en/eda_faculty.php) ｜ [NTU Scholars](https://scholars.lib.ntu.edu.tw/entities/person/3dfdfd8e-e9c8-465d-acbc-952cf547943b)

---

### B47. 李宏毅（Hung-Yi Lee）｜總分 **6.1**（B 級，半導體無直接交集 / 工程師效率軸跨域方法論候補）｜不啟動（保留橋接）

| 校系職級 | NTU 電機系 + 兼任資工系 ｜ 正教授（Professor，2023 升等）；2019-2023 副教授；2014-2019 助理教授 ｜ PhD: NTU 通訊工程研究所 2012（本碩博均 NTU）；AS CITI 博後 2012-2013；MIT CSAIL 訪問科學家 2013-2014 |
|---|---|
| 學術指標 | h-62 / 引用 17,964 / i10-266（since 2021: 引用 16,066）|
| Lab | Speech Processing and ML Lab（NTU EE 博理館 R508）|
| **5 維度評分** | 研究 10 ｜ fab 1 ｜ Lab 8 ｜ 接洽 7 ｜ 長期 7 ｜ 語音教父 + 零半導體 + 大型 Lab + 無業界綁定 |

**核心專長 × 近 3 年代表實績**
- 語音辨識 / 合成 / NLP / 自監督學習 / LALM（Large Audio-Language Model）/ LLM-as-Evaluator / AI 通識教育
- SUPERB benchmark（2021，1,312 引）；Can LLMs Replace Human Evaluators（2023，1,092 引）；Self-supervised speech review（2022，625 引）；2023 升正教授（Full Professor）；YouTube 機器學習課程超 400 萬次觀看；已確認非 Appier 共同創辦人（前次已修正）
- 2023 升正教授；YouTube 機器學習課程超 400 萬次觀看

**合作紀錄 × 與外部公司狀況**
- 無公開可見業界綁定
- **無公開可見業界綁定**；研究主軸為語音 / 語言基礎模型，與半導體 fab 應用距離遠（任何題目均需 6-12 月方法論橋接 PoC）

**製程/封裝應用點（詳述）**（不啟動主軸 — 保留橋接；無半導體直接 fab 應用，工程師效率軸候補）

- **節點 / 段別**：工程師效率軸跨域方法論；適用文件審查 / 語音 / 聲學異常偵測（非直接製程段）
- **痛點對應**：
  - **SOP/FMEA 文件審查人工成本高**：LLM-as-Evaluator 可自動化 ECN / FMEA 文件一致性審查
  - **fab 聲學異常偵測 label 稀缺**：Self-Supervised 方法論可降低設備聲學異常偵測的標記需求
- **可導入時程（TRL）**：橋接成本 3-12 個月（依題目，見下表）；**fab 1 分，任何題目均需跨域橋接期**
- **配合 fab 部門**：IT/FIT（LLM-as-Evaluator）；Equipment 設備工程（聲學異常）；人才發展部門（AI 素養課）
- **預期成效**：依優先 PoC 題目而定；首選題目（①）橋接成本最低，3-6 月可見成果

**建議合作方式 × 公開連結**

> **v4.3 雙 check 後追加（v4.4 維持）**：定位為**工程師效率軸方法論候補（非主軸 PI）**。5 題依橋接成本 / 對應目的優先排序：

| 優先 | 對應目的軸 | 跨域題目 | 橋接成本 |
|---|---|---|---|
| 1（首選 PoC）| 工程師效率 / 法遵 | LLM-as-Evaluator 自動審查 SOP / ECN / FMEA 文件 | 低（3-6 月）|
| 2 | 工程師效率 | 無塵室 hands-free 語音操作 / SOP 查詢 | 中（6-12 月）|
| 3 | 工程師效率 | 交班報告自動轉寫 + 結構化摘要 | 中（6-12 月）|
| 4 | 良率（橋接）| 自監督學習 × 設備聲學異常偵測（Pump/CMP）| 高（12 月+）|
| 5 | 人才漏斗 | TSMC AI 素養課 / 新進工程師 reskilling 共同設計 | 低（單次合約）|

- **制度與簽約**：目前不主動接觸；若工程師效率軸 S/A 級 PI 飽和或缺 LLM-as-Evaluator 專長，可作候補；首選 PoC 3-6 月、法遵 / 變更管理流程對接（不承諾金額，單次 PoC 議）
- **KPI + Exit criteria**：①LLM 與工程師 agreement rate（Cohen's κ）≥ 0.75；④聲學異常偵測 AUC ≥ 0.90；Exit：任一 PoC 指標連續 2 季未達 50% 改善
- **執行對口**：主 IT/FIT / 次依題目（Equipment / 人才發展）
- **風險**：fab 1 分，任何題目均需 6-12 月橋接期；YouTube 教學知名度不等於半導體 fab 合作意願
- **能力限制**：WebSearch 無法驗證 NTU-TSMC 非公開合作意向
- **連結**：[個人網站](https://speech.ee.ntu.edu.tw/~tlkagk/) ｜ [個人網站（hylee）](https://speech.ee.ntu.edu.tw/~hylee/index.php) ｜ [Google Scholar](https://scholar.google.com/citations?user=DxLO11IAAAAJ&hl=en) ｜ [ResearchGate](https://www.researchgate.net/profile/Hung-Yi-Lee-2) ｜ [YouTube 教學頻道](https://www.youtube.com/@HungyiLeeNTU)

---

### B48. 吳凱強（Kai-Chiang Wu）｜總分 **6.0**（B 級，升等後 +0.3）｜第二波

| 校系職級 | NYCU 資訊工程學系 + CS 研究所 ｜ 正教授 + CS 研究所所長（2025/8/1 起）｜ PhD: Carnegie Mellon University ECE 2011（CMU 能源感知運算組 RA 2006-2011；Intel CAD 軟體工程師 2011-2013；2013 加入 NCTU 助理教授）|
|---|---|
| 學術指標 | h-16 / 引用 973 / i10-29（GS）；2018 TSIA 新秀研究獎；2011 CMU Liang Ji-Dian Fellowship；ICCD 2008 Best Paper |
| Lab | GREAT Lab 約 14 人（1 postdoc + PhD + 約 13 碩士）|
| **5 維度評分** | 研究 8 ｜ fab 5 ｜ Lab 6 ｜ 接洽 5 ｜ 長期 6 ｜ CMU + ICML 2025 + EDA+LLM 跨界 + Neuchips |

**核心專長 × 近 3 年代表實績**
- LLM 量化 / FPGA AI 加速 / DfT（Design for Test）/ Hardware Trojan 偵測 / EDA + LLM 跨界 / SSM（State Space Model）量化
- 2024-2025 升正教授（NYCU CS）；ICLR 2025 Palu（KV-Cache 低秩壓縮）；ICLR 2025 Quamba（SSM 量化）；ICML 2025 Quamba2（PMLR 267:10411-10427，Robust SSM 量化）；ICCAD 2025 CAD Contest Problem A 共同命題人；FPGA 2025 稀疏張量
- 2018 TSIA 新秀研究獎；2011 CMU Liang Ji-Dian Fellowship；ICCD 2008 Best Paper

**合作紀錄 × 與外部公司狀況**
- Neuchips 創鑫智慧技術顧問（待核實排他性）
- **Neuchips 顧問**（排他性待核實）

**製程/封裝應用點（詳述）**

- **節點 / 段別**：AI 晶片硬體安全 DfT 驗證 / LLM 量化設計；適用 N5/N3 AI SoC 設計驗證段
- **痛點對應**：
  - **Hardware Trojan 偵測難自動化**：AI 晶片 Trojan 插入點多，現有 DfT 設計難以全覆蓋
  - **AI 推論功耗偏高**：TSMC 量產 AI 晶片（CoWoS）需要量化加速方案降低 package 功耗
- **可導入時程（TRL）**：**TRL 4-6 / 12-18 個月**；ICLR 2025 Palu / Quamba / Quamba2 方法論成熟，EDA+LLM 跨界新穎
- **配合 fab 部門**：DfT 設計驗證部門（主）；DTCO 設計技術共優化（次）
- **預期成效**：
  - Hardware Trojan 偵測率 ≥ 95%
  - LLM KV-Cache 壓縮率 ≥ 40%（Palu 方法論）
  - 每年聯名論文 ≥ 1 篇

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — AI 晶片 Hardware Trojan 自動偵測**：以 LLM+EDA 整合建立 N5/N3 AI SoC Hardware Trojan 自動化偵測系統
  - **主題目 B — LLM 量化加速器設計 PoC**：利用 SSM 量化（Quamba2）方法論設計低功耗 AI 推論加速器 RTL
- **制度與簽約**：技術合作合約（NYCU CS）；年度預算 600-1000 萬（推估區間，非承諾數字，依 NYCU 既有量級對標）；學生通道：博士生 RA + TSMC DfT 實習；**Neuchips 顧問排他性需先確認**
- **KPI + Exit criteria**：第 1 年 Trojan 偵測率 ≥ 90% / 量化 benchmark 完成；第 3 年 DfT 覆蓋率提升 ≥ 20%；Exit：Trojan 偵測率 < 80% 且連續 2 季無改善
- **執行對口**：主 DfT 設計驗證 / 次 DTCO 設計技術共優化
- **風險**：Neuchips 顧問排他性未確認，可能限制合作範疇；CS 所長行政職（2025/8/1 起）影響研究時間
- **能力限制**：WebSearch 無法驗證 Neuchips 顧問排他性協議；NYCU-TSMC 非公開合作
- **連結**：[NYCU CS 個人頁](https://www.cs.nycu.edu.tw/members/detail/kcw?locale=en) ｜ [個人學術頁](https://people.cs.nycu.edu.tw/~kcw/) ｜ [Google Scholar](https://scholar.google.com/citations?user=TrWPWaIAAAAJ&hl=en) ｜ [NYCU Academic Hub](https://scholar.nycu.edu.tw/en/persons/kai-chiang-wu/) ｜ [所長任命公告](https://www.cs.nycu.edu.tw/announcements/detail/12859?locale=en)

---

### B49. 杜長慶（Chang-Ching Tu）｜總分 **5.75**（B 級）｜第三波

| 校系職級 | NYCU 半導體學院（International College of Semiconductor Technology, ICST）（2026/02 從 NCU 電機轉入）｜ 副教授（Associate Professor）｜ PhD: University of Washington, Seattle 電機工程 2011（指導：Prof. Lih Y. Lin）|
|---|---|
| 學術指標 | h-17 / 引用 1,157 / i10-29（since 2021 引用 839）|
| Lab | NYCU ICST Lab（從 NCU 轉入）；上海交大密西根學院兼任 Research Group |
| **5 維度評分** | 研究 6 ｜ fab 4 ｜ Lab 6 ｜ 接洽 8 ｜ 長期 5 ｜ 939 引用 + 硬體（邊界）+ 無綁定 |

**核心專長 × 近 3 年代表實績**
- 矽量子點（SiQD）能源/生醫應用 / 功率電子（SiC、GaN、電動車）/ β-Ga2O3 FET / SiC CMP 技術
- 2024 Nature Reviews Electrical Engineering：電動車功率電子工業展望；2022 LSC Performance Reporting 共識聲明（145 引）；2022 β-Ga2O3 FETs SOTA review（100 引）；2022 SiC CMP technologies review（86 引）；2026/02 從 NCU EE 轉入 NYCU ICST
- Nature Reviews Electrical Engineering 2024；2026/02 從 NCU EE 轉入 NYCU ICST

**合作紀錄 × 與外部公司狀況**
- Foxconn 合作背景
- **無獨家綁定**；Foxconn 為歷史合作

**製程/封裝應用點（詳述）**（邊界應用 — 非 TSMC 核心製程 AI）

- **節點 / 段別**：資料中心電源供應（PSU）GaN 功率元件；**廠房設施軸，非 fab 製程主軸**
- **痛點對應**：
  - **廠房 PUE 偏高**：TSMC 資料中心廠房供電效率受制於傳統 Si PSU，GaN 方案可提升整體 PUE
  - **β-Ga2O3 功率元件研究空白**：TSMC 尚未規模量產 GaN 邏輯製程，相關合作機會有限
- **可導入時程（TRL）**：**TRL 3-5 / 18-24 個月**；廠房設施應用路徑有限（fab 4 分），需先確認 TSMC GaN 策略方向
- **配合 fab 部門**：設施工程（廠房 PSU）；新業務開發（GaN Foundry 探索）
- **預期成效**：廠房 PUE 評估報告 1 份；β-Ga2O3 特性評估報告 1 份（視策略方向）

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — GaN 資料中心 PSU 能效顧問**：評估 GaN 元件在 TSMC 廠房 PSU 中的應用可行性，協助設施工程降低 PUE
  - **主題目 B — β-Ga2O3 製程特性評估（探索）**：提供 β-Ga2O3 FET 技術建議，探索 TSMC GaN Foundry 可能性
- **制度與簽約**：短期顧問合約（NYCU ICST）；單次專案為主，年費 100-200 萬（推估區間，非承諾數字）；製程 AI 主軸之外的邊界合作
- **KPI + Exit criteria**：第 1 年 GaN PSU 可行性評估報告 1 份；Exit：若 TSMC GaN Foundry 策略不啟動則不續約
- **執行對口**：主 設施工程部門 / 次 新業務開發
- **風險**：fab 4 分低，功率電子與 TSMC 核心製程關聯度有限；2026/02 剛轉入 NYCU，適應期影響
- **能力限制**：WebSearch 無法驗證 Foxconn 歷史合作技術詳情；NYCU-TSMC 功率元件非公開合作
- **連結**：[個人網站（NYCU ICST）](https://staff.ee.ncu.edu.tw/changching.tu/public_html/) ｜ [Google Scholar](https://scholar.google.com/citations?hl=en&user=I5Niz7YAAAAJ) ｜ [ResearchGate](https://www.researchgate.net/profile/Chang-Ching-Tu-2) ｜ [Nature 矽量子點論文](https://www.nature.com/articles/s42005-024-01806-3)

---

### B50. 陳朝鈞（Chao-Chun Chen）｜總分 **5.55**（B 級，核實後上修）｜第三波

| 校系職級 | NCKU 資訊工程學系 / 製造資訊與系統研究所（CSIE / IMIS）｜ 教授（since 2011/08）｜ PhD: NCKU 資訊工程學系 2004（指導：Chiang Lee）|
|---|---|
| 學術指標 | h-16 / 引用 870（NCKU researchoutput）|
| Lab | NCKU.IMIS.CIoT Lab（智慧計算物聯網實驗室）|
| **5 維度評分** | 研究 6 ｜ fab 5 ｜ Lab 6 ｜ 接洽 8 ｜ 長期 5 ｜ h-16 跨域 + 工業製造可遷移 + CIoT Lab |

**核心專長 × 近 3 年代表實績**
- 智慧計算 / IoT / Edge Computing / 分散式 ML 演算法 / CNN 虛擬量測 / 跨域應用
- 2025 IEEE Robotics and Automation Letters（生理治療視頻匹配 / CNN 虛擬量測 / 小型物體測距）；2025 Computing 期刊：分散式 C4.5 演算法；IEEE CASE 2017 最佳應用論文獎；IEEE ICRA 2018 最佳論文入圍
- IEEE CASE 2017 最佳應用論文獎；IEEE ICRA 2018 最佳論文入圍

**合作紀錄 × 與外部公司狀況**
- 無公開外部綁定
- **無公開可見外部綁定**；研究橫跨農業科技、醫療影像、工業製造（VM）

**製程/封裝應用點（詳述）**

- **節點 / 段別**：CNN 虛擬量測（VM）/ Edge IoT 感測；適用任一節點量產線批次量測替代
- **痛點對應**：
  - **破壞性量測成本高**：fab 量測需破壞晶圓，VM 系統以感測數據預測電性可降低成本
  - **IoT 邊緣設備算力受限**：fab 大量 IoT 感測器需輕量化分散式 ML，Cloud-only 方案延遲高
- **可導入時程（TRL）**：**TRL 4-6 / 12-18 個月**；CNN VM 方法論已在 IEEE Robotics 論文驗證，需 fab 批次數據適配
- **配合 fab 部門**：YE 良率工程（VM 主）；IT/FIT IoT Edge 部署（次）
- **預期成效**：
  - CNN VM 預測殘差 ≤ 5%
  - IoT 邊緣部署機台 ≥ 50 台
  - 每年聯名論文 ≥ 1 篇

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — 批次 CNN 虛擬量測系統**：以 CNN 端到端學習預測晶圓批次電性參數，減少破壞性量測頻率
  - **主題目 B — 分散式 IoT 製程監控**：部署輕量化分散式 ML 演算法於 fab IoT 邊緣設備，實現即時監控
- **制度與簽約**：技術合作合約（NCKU CSIE/IMIS）；年度預算 400-700 萬（推估區間，非承諾數字，依 NCKU 既有量級對標）；學生通道：碩博生 RA + TSMC YE 實習
- **KPI + Exit criteria**：第 1 年 CNN VM 預測誤差 ≤ 5% / IoT 部署機台 ≥ 20 台；第 3 年 VM 替代量測比例 ≥ 30%；Exit：誤差 > 10% 且連續 3 個月無改善
- **執行對口**：主 YE 良率工程 / 次 IT/FIT IoT 部門
- **風險**：跨域背景（農業、醫療、工業）帶來泛化能力但半導體專注度偏低；h-16 研究量能中等
- **能力限制**：WebSearch 無法驗證 NCKU-TSMC IoT 非公開合作
- **連結**：[NCKU 研究輸出資料庫](https://researchoutput.ncku.edu.tw/zh/persons/chao-chun-chen/) ｜ [CIoT Lab 指導教授頁](https://ciot.imis.ncku.edu.tw/?page_id=35) ｜ [NCKU IMIS 師資頁](https://www.csie.ncku.edu.tw/zh-hant/members/imis) ｜ [CIoT Lab 首頁](https://ciot.imis.ncku.edu.tw/)

---

### B51. 曾釋鋒（Shih-Feng Tseng）｜總分 **5.5**（B 級）｜第三波（設備合作軌）

| 校系職級 | NTUT 製造科技研究所 + 兼機械工程系 ｜ 教授 + 機械工程系主任 ｜ PhD: NCTU 機械工程（年份待核實）|
|---|---|
| 學術指標 | h-22（Scopus）/ 引用 1,310（Pure）；141 篇 / 1,686 引（ResearchGate）；2019-2020 NSTC 研究獎 |
| Lab | 光製造與檢測實驗室（Light Manufacture & Inspection Lab，綜合科技大樓 707-1 / B13-5）|
| **5 維度評分** | 研究 6 ｜ fab 5 ｜ Lab 6 ｜ 接洽 7 ｜ 長期 5 ｜ h-22 / 141 篇 + 設備合作軌 + 系主任 + 無綁定 |

**核心專長 × 近 3 年代表實績**
- 雷射加工 / 表面處理 / 雷射誘導石墨烯感測器 / MXene/ZnO 氣體感測器 / 濕度感測器 / Stealth dicing / TGV / TSV 雷射加工
- 雷射誘導石墨烯感測器論文系列；MXene/ZnO 氣體感測器；濕度感測器；2019-2020 NSTC 研究獎；h-22 / 141 篇論文累計
- 2019-2020 NSTC 研究獎；NTUT 機械系主任

**合作紀錄 × 與外部公司狀況**
- 無綁定
- **無公開可見外部綁定**

**製程/封裝應用點（詳述）**（設備合作軌 — 獨立於製程 AI 主軸）

- **節點 / 段別**：TGV / TSV 雷射加工 / Stealth Dicing；適用 CoWoS / 3D IC 封裝介面製程
- **痛點對應**：
  - **TGV/TSV 加工精度要求升**：3D IC 高密度接線中 TGV/TSV 雷射加工參數優化依賴試誤，成本高
  - **Stealth Dicing 缺陷難線上偵測**：雷射加工微裂縫 / 剝層缺陷缺乏即時線上監控手段
- **可導入時程（TRL）**：**TRL 5-7 / 12-18 個月**；h-22 / 141 篇積累，設備合作框架成熟
- **配合 fab 部門**：AP 先進封裝製程設備部門（主）；TSV 製程工程（次）；**設備合作軌（非製程 AI 主軸）**
- **預期成效**：
  - TGV/TSV 雷射加工精度提升 20%
  - Stealth Dicing 微裂縫線上偵測率 ≥ 90%
  - 每年聯名論文 ≥ 1 篇

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — TGV/TSV 雷射加工參數優化（設備合作）**：建立 CoWoS/3D IC TGV/TSV 雷射加工製程參數優化方法
  - **主題目 B — Stealth Dicing 缺陷線上監控**：建立雷射加工即時缺陷偵測系統，提升晶圓切割良率
- **制度與簽約**：設備合作合約（NTUT 製造科技所）；年度預算 600-1000 萬（推估區間，非承諾數字，依 NTUT 既有量級對標）；學生通道：碩博生 RA + TSMC 封裝設備部門實習；**注意：設備合作軌，獨立於製程 AI 主軸預算**
- **KPI + Exit criteria**：第 1 年加工精度提升 ≥ 20% / PoC 完成；第 3 年生產線部署 ≥ 1 條；Exit：精度改善 < 10% 且連續 2 季無進展
- **執行對口**：主 AP 封裝製程設備部門 / 次 TSV 製程工程
- **風險**：設備合作軌與 AI 主軸分屬不同預算來源，需雙軌協調；系主任行政職影響研究投入
- **能力限制**：WebSearch 無法驗證 NTUT-TSMC 設備合作非公開協議
- **連結**：[NTUT 製造科技所教師頁](https://imt.ntut.edu.tw/p/405-1065-87844,c382.php?Lang=zh-tw) ｜ [NTUT 機械系教師頁](https://me1.ntut.edu.tw/p/405-1062-87760,c2760.php?Lang=en) ｜ [Elsevier Pure 學術資料庫](https://ntut.elsevierpure.com/en/persons/shih-feng-tseng/) ｜ [光製造與檢測實驗室](https://academic.ntut.edu.tw/5157/) ｜ [北科大學術資源網](https://academic.ntut.edu.tw/1781/1556/2159/)

---

### B52. 王蒞君（Li-Chun Wang）｜總分 **5.4**（B 級，研究主軸 6G/UAV 非半導體製造 -1.1）｜觀察（精省合作 / 制度合作 > 直接技術合作）

| 校系職級 | NYCU 電機工程研究所（IECE）終身講座 + 電機資訊學院院長（Dean，2023/02 起）｜ 終身講座教授（Lifetime Chair Professor）+ 電機學院院長 ｜ PhD: Georgia Institute of Technology 電機工程 1996（前 AT&T Labs Research Senior Technical Staff 1996-2000）|
|---|---|
| 學術指標 | h-54 / 引用 10,729；IEEE Fellow 2011（cellular architecture & radio resource management）；NSTC 傑出研究獎 ×2（2012/2017）；2023 有庠科技獎；2025 潘文淵基金會傑出研究獎 |
| Lab | Intelligent Communication and Computing Lab（11 博生 + 22-25 碩 + 1 博後）；163 期刊 + 200+ 會議 + 26 美國專利 |
| **5 維度評分** | 研究 8 ｜ fab 2 ｜ Lab 7 ｜ 接洽 9 ｜ 長期 4 ｜ IEEE Fellow + 通訊頂級 + 無 fab/封裝直接連結 + 院長行政重 |

**核心專長 × 近 3 年代表實績**
- AI for 6G 無線通訊（55%，RIS Reconfigurable Intelligent Surface、AI-based radio resource management、波形與頻譜）/ UAV 通訊網路（20%，UAV relay、UAV-RIS 整合、無人機 3D 部署）/ Satellite-Terrestrial 整合網路（8%，LEO 衛星路由）/ IoT / WSN / Energy Harvesting（8%，Backscatter、SWIPT）/ AI for Smart City（ISAC）/ Health 4.0（9%，新興，交叉路口預警、BCI、fNIRS）；明確不涉：AOI 檢測 / 晶圓缺陷分類 / EDA / 封裝測試
- IEEE TWC 2023 "Energy Harvesting RIS for UAV Based on Robust DRL"（93 引）；IEEE Wireless Communications 2023 "IRS-Enhanced UAV Communications"（35 引）；IEEE IoT-J 2022 "DRL-Based Drone Base Station Deployment"（52 引）；IEEE TVT 2022 "Adaptive Fair Deployment in Multi-UAV Networks"（19 引）；IEEE TCCN 2022 "Data-Driven Spectrum Partition for URLLC and eMBB"（16 引）；IEEE TWC 2025 "Energy Efficiency for IoT With RIS: Self-Supervised RL"；2025 潘文淵基金會傑出研究獎
- IEEE Fellow 2011；NSTC 傑出研究獎 ×2（2012/2017）；2023 有庠科技獎；2025 潘文淵基金會傑出研究獎

**合作紀錄 × 與外部公司狀況**
- 無綁定（完全自由 PI）；前 AT&T Labs Research 1996-2000
- **無公開可見外部綁定**；完全自由 PI；NYCU 電資學院院長行政負擔重

**製程/封裝應用點（詳述）**（觀察 — 精省合作；研究主軸 6G/UAV 非半導體製造）

- **節點 / 段別**：TSMC 廠區 5G 私網 / ISAC 智慧工廠；**廠區網路基礎設施，非核心製程 AI**
- **痛點對應**：
  - **廠區無線網路覆蓋不足**：fab 廠區內部 5G 私網 NR-U 佈建尚無成熟學術合作框架
  - **人員 / 物流定位粗糙**：ISAC 整合感知通訊可提供廠區人員定位與物流追蹤，優於現有 RFID
- **可導入時程（TRL）**：**TRL 3-5 / 12-18 個月**；6G/ISAC 方法論成熟，fab 場域驗證需先行
- **配合 fab 部門**：設施工程（廠區網路）；IT/FIT IoT 感知平台；注意：與 TSMC 核心 fab/封裝/EDA 無直接連結
- **預期成效**：廠區 5G 私網覆蓋規劃報告 1 份；ISAC 智慧工廠 pilot 方案 1 份；學術合作框架簽署

**建議合作方式 × 公開連結**

- **題目**
  - **主題目 A — TSMC 廠區 5G 私網部署顧問**：評估 TSMC fab 廠區 NR-U 5G 私網覆蓋方案，提供部署建議
  - **主題目 B — ISAC 智慧工廠人員定位**：以整合感知通訊（ISAC）建立廠區人員定位 / 物流追蹤 pilot
- **制度與簽約**：5G 私網顧問年費 100-200 萬 × 3 年；制度合作框架另議（院長身分有 NYCU 整體合作戰略意義）；不建議方向：AI for 製程異常偵測、AOI、EDA 加速、CoWoS 封裝（研究主軸無交集）
- **KPI + Exit criteria**：5G 私網覆蓋規劃報告 1 份 / ISAC pilot 完成；Exit：若廠區網路策略轉向不續約
- **執行對口**：主 設施工程廠區網路 / 次 IT/FIT IoT 平台
- **風險**：研究主軸（6G/UAV）與 fab 核心業務無直接連結，長期合作深度受限；電資學院院長行政重，研究投入時間有限
- **能力限制**：WebSearch 無法驗證 NYCU-TSMC 5G 私網非公開合作意向
- **連結**：[NYCU IECE 教師頁](https://iece.dee.nycu.edu.tw/teachers.php?pa=getItem&teacher_id=133&locale=en) ｜ [個人 Lab](https://wang.web.nycu.edu.tw/) ｜ [NYCU Academic Hub](https://scholar.nycu.edu.tw/en/persons/li-chun-wang) ｜ [DBLP](https://dblp.org/pid/w/LiChunWang.html) ｜ [ORCID](https://orcid.org/0000-0002-7883-6217) ｜ [NYCU 電資學院院長公告](https://ece.nycu.edu.tw/department/index.aspx?Parser=40,4,242,260)

---

### B53. 陳正剛（Argon Chen）｜總分 **4.5**（B 級）｜不啟動

| 校系職級 | NTU 工業工程學研究所（2009 後轉生醫）｜ 教授 ｜ PhD: Rutgers University 工業工程（年份待核實）|
|---|---|
| 學術指標 | h-22 / 引用 1,813 / i10-41；最高引論文 "Optimal levels of process parameters"（258 引，1993）|
| Lab | NTU 工工 Lab 僅 3 人；辦公室 國慶館 111 室 |
| **5 維度評分** | 研究 6 ｜ fab 3 ｜ Lab 4 ｜ 接洽 7 ｜ 長期 4 ｜ h-22 歷史 + 已轉生醫 + 僅 3 人 |

**核心專長 × 近 3 年代表實績**
- SPC / APC（2009 前權威）/ 超音波 / OSA（2009 後轉向）/ 睡眠呼吸中止研究（生醫）
- h-22 全期（歷史累計）；Lab 僅 3 人；自 2009 轉生醫為主軸；Jakey Blue（B45）之師
- 半導體 SPC 代表作距今 10+ 年

**合作紀錄 × 與外部公司狀況**
- 半導體 SPC 代表作距今 10+ 年
- **無公開可見外部綁定**；已脫離半導體 10+ 年

**製程/封裝應用點（詳述）**（不啟動 — 主軸已轉生醫 10+ 年；理論定位）

- **節點 / 段別**：SPC / APC 統計方法論（2009 前歷史積累）；現研究主軸為生醫，不啟動獨立 PI 合作
- **痛點對應**：SPC/APC 歷史方法論權威（最高引 "Optimal levels of process parameters" 258 引），可作 Tier 2 會診
- **可導入時程（TRL）**：N/A（研究主軸已轉生醫 10+ 年；Lab 僅 3 人）；透過 B45 Jakey Blue 橋接
- **配合 fab 部門**：透過 B45 Jakey Blue 橋接 YE / 統計品管部門
- **預期成效**：會診型，無量化 KPI；依 Jakey Blue 案需求按次橋接

**建議合作方式 × 公開連結**

> **v4.3 雙 check 後修訂（v4.4 維持）**：定位為**Tier 2 方法論會診顧問**（非獨立委案 PI），透過 Jakey Blue 案需求橋接。

- **題目**
  - **Tier 2 會診 — SPC/APC 方法論橋接**：依 B45 Jakey Blue 案需求，提供 SPC/APC 方法論歷史觀點會診
  - **不獨立委案**：Lab 僅 3 人 + 主軸已轉生醫，不作為獨立 PI
- **制度與簽約**：會診型顧問，按次計費或併入 B45 Jakey Blue 案；不獨立簽約
- **KPI + Exit criteria**：—（會診型，無量化 KPI）
- **執行對口**：透過 B45 Jakey Blue 橋接
- **風險**：研究主軸已轉生醫，SPC 方法論距今 10+ 年，技術現貨性存疑
- **能力限制**：WebSearch 無法驗證研究主軸轉向後的方法論持續更新狀況
- **連結**：[NTU IE 教師頁](https://ie.ntu.edu.tw/News_Photo_Content_n_44392_sms_48541_s_51387.html) ｜ [Google Scholar](https://scholar.google.com/citations?user=IahSBeQAAAAJ&hl=en)

---

### B54. 謝旻甫（Min-Fu Hsieh）｜總分 **4.4**（B 級）｜不啟動

| 校系職級 | NCKU 電機工程學系 特聘教授（since 2022）+ 電動馬達技術研究中心研究教授（since 2015）｜ Distinguished Professor；前 NCKU 研發副校長 2023-2025 ｜ PhD: University of Liverpool（英國）機械工程 2000（MS Liverpool 1996；BS NCKU 機械 1991）|
|---|---|
| 學術指標 | h-36 / 引用 4,240 / i10-90；2025 IET Fellow；IEEE Senior Member（Magnetics / IA / PE）|
| Lab | 電機與驅動系統實驗室（Electrical Machines and Drive Systems Lab）約 30 人 |
| **5 維度評分** | 研究 5 ｜ fab 3 ｜ Lab 5 ｜ 接洽 6 ｜ 長期 5 ｜ 廠務非核心 + 廠務應用 + 中型 + 台達電歷史 |

**核心專長 × 近 3 年代表實績**
- 馬達驅動 AI 參數優化 / 廠務風機預測維護
- 2025 IET Fellow；IEEE Magnetics Society Distinguished Lecturer（2025-2026）；Stanford / Scopus Top 2% Scientists（2022-2024）；2022 李國鼎金質獎；2024 國科會傑出研究獎；2024 中工會傑出工程教授獎；Delta Electronics Chair Professor 2019-2024；IEEE Intermag Editor-in-Chief（2020/2021/2023/2025）
- 2025 IET Fellow；2022 李國鼎金質獎；2024 國科會傑出研究獎；Stanford / Scopus Top 2% Scientists 連 3 年

**合作紀錄 × 與外部公司狀況**
- 台達電特聘歷史；中鋼 / 國太中心合作
- 台達電特聘歷史（時間優先度被佔用）；廠務研究非 fab 核心

**製程/封裝應用點（詳述）**（不啟動製程 AI 主軸 — 屬廠務設施軸；轉介 Fab 設施部門）

- **節點 / 段別**：廠務風機 / 馬達驅動預測維護；適用 TSMC 廠房 chiller / 風扇驅動設施（非 fab 製程段）
- **痛點對應**：
  - **廠務設備劣化難預測**：馬達電流訊號 → 軸承劣化 ML 預測缺乏系統化實施
  - **廠務節能潛力未充分開發**：chiller 調度節能與 S14 李家岩 MARL 軸有題目競合
- **可導入時程（TRL）**：**TRL 6-8 / 6-12 個月**；廠務應用技術成熟，台達電 Chair 2019-2024 已結束，時間檔期釋放
- **配合 fab 部門**：轉介 Fab 設施部門；本盤點（製程 AI 軸）不啟動
- **預期成效**：轉介後參考 — 馬達/風機預測維護準確率提升；廠務年度節能 %

**建議合作方式 × 公開連結**

> **v4.3 雙 check 後修訂（v4.4 維持）**：屬**Fab 設施軸（廠務）**而非製程 AI 軸，本盤點不啟動但建議轉介。

- **題目**
  - **廠務轉介 — 風機/馬達預測維護**：廠務風機/馬達電流訊號 → 軸承劣化 ML 預測（轉介 Fab 設施部門）
  - **廠務節能顧問（chiller 調度）**：注意與 S14 李家岩 MARL chiller 軸有題目競合，需協調
- **制度與簽約**：轉介 Fab 設施部門：年度設施合作專案制；本盤點（製程 AI 軸）不啟動；台達電 Chair 2019-2024 已結束
- **KPI + Exit criteria**：（轉介後參考）馬達/風機預測維護準確率、故障預警提前時數、廠務年度節能 %
- **執行對口**：Fab 設施部門（轉介）；非本盤點製程 AI 執行對口
- **風險**：chiller 題目與 S14 李家岩競合，需確認題目分工；廠務研究非 fab 核心，長期 TSMC 重視度不確定
- **能力限制**：WebSearch 無法驗證 NCKU-TSMC 廠務非公開合作協議
- **連結**：[NCKU EE 師資頁（含 IET Fellow 確認）](https://www.ee.ncku.edu.tw/teacher/index2.php?teacher_id=163) ｜ [NCKU Research Output](https://researchoutput.ncku.edu.tw/en/persons/min-fu-hsieh/) ｜ [Google Scholar](https://scholar.google.com/citations?user=VkHJZYQAAAAJ&hl=zh-TW) ｜ [ORCID](https://orcid.org/0000-0002-5514-3397) ｜ [ResearchGate](https://www.researchgate.net/profile/Min-Fu-Hsieh)

---

### B55. 洪英超（Ying-Chao Hung）｜總分 **4.2**（B 級）｜不啟動

| 校系職級 | NTU 工業工程學研究所（2022/8 從 NCCU 統計系轉入；前 NCCU 統計系主任 + 統計諮詢中心主任）｜ 教授（NTU IE，since 2022/08）｜ PhD: University of Michigan 統計學 1995（BS NTU 數學；MS NCCU 統計研究所）|
|---|---|
| 學術指標 | 42 篇論文 / 引用 370（ResearchGate）|
| Lab | NTU IE Ying-Chao Hung Lab |
| **5 維度評分** | 研究 5 ｜ fab 2 ｜ Lab 5 ｜ 接洽 7 ｜ 長期 5 ｜ 方法論漂移 + 無直接應用 + 中型 + 偏離 |

**核心專長 × 近 3 年代表實績**
- SVR Profile Monitoring（2012 前）/ Granger Causality / EV 充電最佳化（近年轉向）
- 2022/8 從 NCCU 統計系正式轉入 NTU IE；2018 Microsoft 訪問學者；2024「Granger Causality Tests Based on Reduced Variable Information」（統計頂刊）；2025 IEEE Trans. on Intelligent Transportation Systems：EV 充電站選址路由最佳化；多次訪問學者：U Florida、MSR、日本統計數理研究所、新加坡大學；主軸轉為「EV 充電 + 統計方法論」雙軸（半導體軌偏離）
- 2018 Microsoft 訪問學者；前 NCCU 統計系主任 + 統計諮詢中心主任

**合作紀錄 × 與外部公司狀況**
- 無綁定
- **無公開可見外部綁定**

**製程/封裝應用點（詳述）**（不啟動 — 研究主軸已轉 EV 充電；單次諮詢顧問定位）

- **節點 / 段別**：多變量 SPC 根因分析（Granger Causality）；研究主軸已偏離，不啟動獨立 PI
- **痛點對應**：Granger Causality 方法論可橋接 fab 多變量 SPC 根因分析；SVR Profile Monitoring（2012 前）為方法論底子
- **可導入時程（TRL）**：N/A（研究主軸已轉 EV 充電 + 統計方法論雙軸，半導體軌偏離）；單次諮詢顧問，不委案
- **配合 fab 部門**：統計品管部門（單次諮詢）；不啟動正式合作
- **預期成效**：會診型，無量化 KPI；Granger 因果方法論問題按次計費

**建議合作方式 × 公開連結**

> **v4.3 雙 check 後修訂（v4.4 維持）**：定位為**Granger 因果統計單次諮詢顧問**（非主動委案 PI）。

- **題目**
  - **單次諮詢 — Granger Causality SPC 橋接**：SPC 多變量因果鏈方法論會診，按次計費
  - **不主動委案**：研究主軸已轉「EV 充電 + 統計方法論」雙軸（半導體軌偏離）
- **制度與簽約**：單次諮詢顧問，按次計費；不作為獨立 PI 委案
- **KPI + Exit criteria**：—（會診型，無量化 KPI）
- **執行對口**：統計品管部門（單次諮詢）
- **風險**：研究主軸已轉，半導體方法論知識可能不再更新；2022/8 剛轉入 NTU IE，適應期影響
- **能力限制**：WebSearch 無法驗證研究主軸轉向後的方法論持續更新狀況
- **連結**：[NTU IE 教師頁](https://ie.ntu.edu.tw/News_Photo_Content_n_44392_s_214735.html) ｜ [NTU 工學院公告（確認加入）](https://www.eng.ntu.edu.tw/iet/News_Content_n_182589_s_234981.html) ｜ [NTU IE 歡迎新進教師公告](https://ie.ntu.edu.tw/News_Content_n_44395_s_109275.html) ｜ [ResearchGate](https://www.researchgate.net/profile/Ying-Chao-Hung)

---

### C56. 林清安（Ching-An Lin）｜總分 **4.0**（C 級）｜不啟動（候補位）

| 校系職級 | NTUST 機械工程系 ｜ 教授 |
|---|---|
| 學術指標 | 論文透明度低，近年發表難以公開核實 |
| **5 維度評分** | 研究 4 ｜ fab 5 ｜ Lab 5 ｜ 接洽 7 ｜ 長期 3 ｜ 論文透明度低 + 方向偏 + 候補位 |

**核心專長 × 近 3 年代表實績**
- 機械視覺 / 機械手臂（潛在 fab AMHS / 封裝視覺定位接點）
- 論文透明度低，近年發表難以公開核實；曾出現在候選名單但未入選

**合作紀錄 × 與外部公司狀況**
- **無公開可見外部綁定**

**製程/封裝應用點（詳述）**（不啟動 — 候補位；論文證據不足）

- **節點 / 段別**：fab AMHS / 後段封裝機械視覺定位（理論接點）
- **痛點對應**：機械視覺 / 機械手臂與 fab AMHS / 封裝視覺定位有間接接點，但近年論文證據不足以評估技術深度
- **可導入時程（TRL）**：N/A（不啟動）；候補條件：AMHS / 封裝視覺軸 S/A 級 PI 飽和或缺人時重評
- **預期成效**：不啟動，無量化目標

**建議合作方式 × 公開連結**

- **題目**：不啟動（候補位）；不主動接觸
- **制度與簽約**：不啟動；候補重評條件見上
- **KPI + Exit criteria**：—（不啟動）
- **執行對口**：—
- **風險**：論文透明度低，技術能力難客觀評估；不投入資源
- **能力限制**：WebSearch 無法充分核實近年論文發表與技術深度
- **連結**：[NTUST 機械系教師頁（待補）]

---

### C57. 柏林（Berlin Chen）｜總分 **3.8**（C 級）｜不啟動（候補位）

| 校系職級 | NTNU 資訊工程學系 ｜ 教授 |
|---|---|
| 學術指標 | 台灣普通話 ASR 領域知名；BERT reranking 方法論 |
| **5 維度評分** | 研究 7 ｜ fab 1 ｜ Lab 6 ｜ 接洽 8 ｜ 長期 4 ｜ ASR 專項 + 零半導體 + 與 B47 李宏毅競合 |

**核心專長 × 近 3 年代表實績**
- Mandarin ASR / BERT reranking / 語音辨識後處理 / 台灣普通話語音模型
- ASR 專家（非 LLM）；與半導體 fab 應用需 6-12 月橋接；與 B47 李宏毅 LALM 路徑存在題目競合

**合作紀錄 × 與外部公司狀況**
- **無公開可見外部綁定**

**製程/封裝應用點（詳述）**（不啟動 — 候補位；與 B47 李宏毅競合）

- **節點 / 段別**：工程師語音指令 / 製程文件語音檢索（理論接點）
- **痛點對應**：台灣普通話 ASR → 製程文件檢索 / 工程師語音指令（理論橋接路徑）；但與 B47 李宏毅 LALM 路徑優先
- **可導入時程（TRL）**：TRL 2-4 / 需 6-12 月橋接；候補條件：B47 李宏毅路徑卡關或 LALM 覆蓋不足時
- **預期成效**：不啟動，無量化目標

**建議合作方式 × 公開連結**

- **題目**：不啟動（候補位）；ASR 專項 PoC 為 B47 李宏毅 LALM 路徑的次選備案
- **制度與簽約**：不啟動；候補重評條件：B47 路徑卡關再考慮
- **KPI + Exit criteria**：—（不啟動）
- **執行對口**：—
- **風險**：與 B47 李宏毅題目競合；ASR 專項非 LLM，橋接成本比 B47 高
- **能力限制**：WebSearch 無法驗證 NTNU-TSMC 非公開合作意向
- **連結**：[NTNU CSIE 教師頁（待補）]

---

### C58. 王振興（Jeen-Shing Wang）｜總分 **3.0**（C 級）｜不啟動（另案軸）

| 校系職級 | NCKU 電機工程學系 ｜ 教授 |
|---|---|
| 學術指標 | Neuro-fuzzy / AIoT / 生醫訊號處理 |
| **5 維度評分** | 研究 5 ｜ fab 2 ｜ Lab 5 ｜ 接洽 7 ｜ 長期 3 ｜ 半導體契合僅 5% + 主軸生醫 + 另案軸 |

**核心專長 × 近 3 年代表實績**
- Neuro-fuzzy 系統 / AIoT 邊緣推論 / 生醫訊號（主軸）
- 半導體 fab 製程直接接點低（研究主軸為生醫訊號，製程契合 ≤ 5%）

**合作紀錄 × 與外部公司狀況**
- **無公開可見外部綁定**

**製程/封裝應用點（詳述）**（不啟動 — 另案軸；fab 製程契合度低）

- **節點 / 段別**：AIoT 邊緣推論（理論接點）；若 TSMC 員工穿戴監測需求另起則重評
- **痛點對應**：AIoT / Neuro-fuzzy 邊緣推論方法論可橋接廠區 IoT，但 fab 直接製程接點極低
- **可導入時程（TRL）**：N/A（不啟動）；重評條件：TSMC 員工穿戴監測 / 邊緣 AIoT 專案另起
- **預期成效**：不啟動，無量化目標

**建議合作方式 × 公開連結**

- **題目**：不啟動（另案軸）；fab 製程契合度低，不主動接觸
- **制度與簽約**：不啟動；重評條件：員工穿戴監測 / 邊緣 AIoT 另起需求
- **KPI + Exit criteria**：—（不啟動）
- **執行對口**：—
- **風險**：研究主軸生醫，製程 AI 適配需大幅轉型
- **能力限制**：WebSearch 無法核實 NCKU-TSMC 非公開接觸記錄
- **連結**：[NCKU EE 教師頁（待補）]

---

### C59. 楊佳玲（Chia-Lin Yang）｜總分 **3.0**（C 級，借調期降級）｜不啟動（借調政務次長）

| 校系職級 | NTU 資訊工程學系（2026/02 起借調政務次長 1-2 年）｜ 正教授（Professor）｜ IEEE Fellow 2026 |
|---|---|
| 學術指標 | CIM 架構 / NAS / Memristor；2024 NSTC 傑出研究獎；IEEE Fellow 2026 |
| **5 維度評分** | 研究 9 ｜ fab 5 ｜ Lab 7 ｜ 接洽 0 ｜ 長期 5 ｜ IEEE Fellow + 借調政務次長 → 接洽 0 |

**核心專長 × 近 3 年代表實績**
- CIM（Compute-In-Memory）架構 / NAS（Neural Architecture Search）/ Memristor 非揮發記憶體
- IEEE Fellow 2026；2024 NSTC 傑出研究獎；2026/02 借調政務次長（借調期 1-2 年）

**合作紀錄 × 與外部公司狀況**
- **借調政務次長（2026/02 起）** — 借調期間屬公務員身份，外部產學合約不啟動

**製程/封裝應用點（詳述）**（不啟動 — 借調政務次長中；2027 返校後重評）

- **節點 / 段別**：CIM 架構 / Memristor；適用 TSMC 先進記憶體整合製程（理論接點）
- **痛點對應**：CIM 降低 AI 推論記憶體頻寬瓶頸，Memristor 製程整合與 TSMC N3/A16 有技術接點
- **可導入時程（TRL）**：TRL 5-7；借調期間不啟動；**2027 返校後重評**
- **預期成效**：借調期間不啟動；返校後依研究方向重評合作可能

**建議合作方式 × 公開連結**

- **題目**：不啟動（借調中）；2027 返校後重評 CIM / Memristor 製程整合合作
- **制度與簽約**：借調期間不啟動（公務員身份，外部合約視為利益衝突）；返校後重評
- **KPI + Exit criteria**：借調期間不適用；返校後訂定
- **執行對口**：—（借調期間）
- **風險**：借調時間可能延長；返校後研究方向是否維持 CIM/Memristor 主軸不確定
- **能力限制**：WebSearch 無法驗證借調確切返校時間表
- **連結**：[NTU CSIE 教師頁（待補）]

---

### C60. 鄭少為（Shao-Wei Peng）｜總分 **2.9**（C 級）｜不啟動（理論配套）

| 校系職級 | NTHU 統計學研究所 ｜ 副教授（17 年未升等）｜ PhD: 統計（年份待核實）|
|---|---|
| 學術指標 | Gaussian Process / DoE；近 5 年無頂期刊發表 |
| **5 維度評分** | 研究 4 ｜ fab 4 ｜ Lab 3 ｜ 接洽 7 ｜ 長期 3 ｜ GP/DoE 方法論 + 近 5 年產出薄弱 + 17 年未升等 |

**核心專長 × 近 3 年代表實績**
- Gaussian Process / DoE（實驗設計）/ 高維統計方法論
- 副教授 17 年未升等；近 5 年無頂期刊發表；方法論底子具備但產出薄弱

**合作紀錄 × 與外部公司狀況**
- **無公開可見外部綁定**

**製程/封裝應用點（詳述）**（不啟動 — 理論配套；近 5 年產出薄弱）

- **節點 / 段別**：高維 DoE 實驗設計 / Gaussian Process（fab DoE 加速潛力）
- **痛點對應**：GP / DoE 可協助 fab 製程參數高維實驗加速，理論方法論有接點
- **可導入時程（TRL）**：N/A（不獨立委案）；可作他人主軸 PoC 的統計支援角色
- **預期成效**：理論配套型，無獨立量化目標

**建議合作方式 × 公開連結**

- **題目**：不啟動（理論配套）；不獨立委案 PI；可作 S/A 級 PI 主軸 PoC 的高維 DoE / GP 統計支援
- **制度與簽約**：不獨立簽約；併入他人案的統計諮詢
- **KPI + Exit criteria**：—（配套型，無量化 KPI）
- **執行對口**：依配套主案對口
- **風險**：近 5 年頂期刊發表稀缺，研究量能及時效性存疑；17 年未升等暗示 Lab 發展受限
- **能力限制**：WebSearch 無法核實近 5 年具體發表情況
- **連結**：[NTHU 統計所教師頁（待補）]

---

### C61. 李祈均（Chi-Chun Lee）｜總分 **2.6**（C 級）｜不啟動（COI 雙綁定 + 員工關懷軸）

| 校系職級 | NTHU 電機工程學系 ｜ 教授 ｜ PhD: USC 電機 2012 |
|---|---|
| 學術指標 | BIIC Lab 12-18 人；Multimodal DL / Speech Affective Computing |
| **5 維度評分** | 研究 7 ｜ fab 0 ｜ Lab 6 ｜ 接洽 5 ｜ 長期 3 ｜ 0% 半導體 + NVIDIA 副主任 + 京元電子顧問（雙 COI）|

**核心專長 × 近 3 年代表實績**
- Multimodal DL / Speech Affective Computing / 情感語音辨識 / 員工壓力偵測
- NVIDIA Taiwan 研究副主任 + 京元電子技術顧問（雙 COI 綁定）；fab 製程應用接點 0%

**合作紀錄 × 與外部公司狀況**
- NVIDIA Taiwan 副主任 + 京元電子顧問
- **雙 COI 綁定** — NVIDIA 副主任 + 京元電子（同業）顧問；須先簽資訊牆協議

**製程/封裝應用點（詳述）**（不啟動 — COI 雙綁定；fab 製程接點 0%）

- **節點 / 段別**：員工情感 / 壓力偵測（員工關懷軸，非 fab 製程）；0% 半導體 fab 直接接點
- **痛點對應**：Speech Affective → TSMC 工程師壓力 / 疲勞偵測（員工關懷軸），但非製程 AI 主軸
- **可導入時程（TRL）**：N/A（不啟動）；COI 雙綁定需法務先行確認資訊牆；員工關懷軸不在本盤點主軸
- **預期成效**：不啟動，無量化目標

**建議合作方式 × 公開連結**

- **題目**：不啟動（COI 雙綁定 + 員工關懷軸）；fab 應用接點僅員工狀態偵測，優先度低
- **制度與簽約**：不啟動；若員工關懷軸另起需求：COI 先簽資訊牆協議（NVIDIA + 京元電子雙方）
- **KPI + Exit criteria**：—（不啟動）
- **執行對口**：—
- **風險**：NVIDIA 副主任 + 京元電子（同業）顧問雙重 COI，資訊牆設置複雜；員工關懷軸非製程 AI 主軸
- **能力限制**：WebSearch 無法核實 NVIDIA 副主任排他性協議範疇
- **連結**：[NTHU EE 教師頁（待補）] ｜ [BIIC Lab（待補）]

---
