# 教授盤點 — 林錦德 (Lin Chin-Te)

## 基本資料

| 項目 | 內容 |
|---|---|
| **姓名** | 林錦德 (Lin Chin-Te) |
| **機構** | 國立中央大學 (NCU) — 機械工程學系 |
| **職級** | 助理教授 (Assistant Professor) |
| **聯繫信箱** | chintelin@ncu.edu.tw |

---

## 核心領域

| 維度 | 內容 |
|---|---|
| **主軸研究** | 可見光定位（Visible Light Positioning, VLP）；AI 驅動智慧決策；自主移動機器人（AMR）定位技術；物聯網（IoT）驅動製造 |
| **應用場景** | 室內自主機器人定位、物流中心 AMR 導航、製造場景位置感知 |
| **相關技術** | 機器視覺、信號處理、深度學習（LSTM/CNN）、角度到達（AOA）估計、LED 光源定位 |

---

## 代表實績

### 論文與發表
- **可見光定位技術**：多篇 VLP 相關論文（IEEE、光學期刊）
  - "Real-Time Indoor Visible Light Positioning (VLP) Using LSTM-NN with PCA" (Sensors, 2024)
  - "Positioning Unit Cell Model Duplication with RCNN and Transfer Learning for VLP" (Journal of Lightwave Technology, 2024)
- **AMR 定位**："Positioning of autonomous mobile robot using multi-lateration with pattern recognition and differential evolution" (機器人學, 2025)

### 研究深度指標
- **被引用次數**：未在標準查詢中呈現（VLP 領域新銳，估計 20-50 次）
- **Google Scholar**：無標準檔案（新進教授可能尚未建檔）
- **h-index**：未可知（估計 5-10，新銳研究者）

### 教育背景
- **推測學位**：機械工程相關領域（具體未查獲）
- **國際視野**：論文發表於 IEEE、光電學會等國際頂級期刊

---

## 研究聚焦 vs 半導體契合度

### VLP + AMR 的應用潛力

#### 與 Fab 需求的相關性：
1. **AMR 應用場景**（直接契合）：
   - Fab 內自動物料搬運系統（AMHS）
   - 可見光定位提供 GPS-denied 環境下的室內定位
   - 精度需求：cm 級（實驗結果 1.8-5.9 cm）→ 符合 fab AMR 要求

2. **但存在技術風險**：
   - VLP 依賴穩定光源與反光特性
   - Fab 環境光污染、LED 老化可能影響定位精度
   - 需額外的冗餘定位系統（磁軌、QR code 等）

#### 半導體製造工藝級應用：
- **無直接論文指向** APC / VM / SPC 製程控制
- **應用層級**：主要為 **後勤/物流自動化**，非核心晶片製程

#### 估計契合度：**50-65%**（AMR 應用高契合，但非製程工藝）

---

## 合作狀況披露

### 外部綁定狀態
| 項目 | 狀態 |
|---|---|
| 獨董 / Chair | 無公開紀錄 |
| 技術顧問 | 無公開紀錄 |
| TSMC 綁定 | 無公開可見綁定 |
| 競業方 Chair | 無公開紀錄 |
| 技術移轉 | 無公開紀錄 |

**綜合評估**：無已知外部綁定；新進教授，資源完全自由。

---

## 5 維度評分

### 維度 1：研究軌跡可信度（權重 20%）
- **分數**：5/10
- **理由**：
  - 新銳教授（助理教授等級），發表歷程較短
  - 被引用數未明確（估 20-50），h-index 推估 5-10
  - VLP 領域為新興應用，論文質量難判；IEEE / 光電頂刊認可
  - 方向清晰（VLP → AMR），但未達穩定產出級別
- **判定**：介於「新銳」(3-5 分) 與「中階穩定」(5-6 分)，取中值

### 維度 2：Fab / Semi 應用落地能力（權重 25%）**【最關鍵】**
- **分數**：5/10
- **理由**：
  - **高分項**：VLP + AMR 定位 = Fab AMHS 核心應用場景；論文直指 AMR 室內定位
  - **低分項**：無製程工藝論文（APC/VM/CD/yield）；應用層級為 **物流/後勤**
  - **技術成熟度**：實驗原型級 → PoC 完成；需 6-12 月集成驗證
  - **Fab 契合度評估**：50-65% ✓（後勤可行，非核心製程）
- **結論**：介於「可遷移」(5-6) 與「方法論層次」(3-4)，取 5 分（需驗證 fab 環境適配性）

### 維度 3：Lab 深度與學生素養（權重 20%）
- **分數**：6/10
- **理由**：
  - Lab 規模：未在查詢結果找到
  - Rubric v2.0 規則：Lab 規模未找到 → 給 6（中性）
  - 新進教授通常 Lab 規模 < 10 人（估計 3-5 碩博生）
  - 論文有學生一作發表（e.g., VLP 論文），顯示正常培養通道

### 維度 4：可接洽度 / 資源未被搶佔（權重 20%）
- **分數**：9/10
- **理由**：
  - 完全自由（新進教授，無外部綁定）
  - 無 TSMC / 競業方 Chair 或顧問職
  - 資源未被搶佔；開放式國際合作環境
  - 唯一扣分：新進教授可能仍需建立研究基地，時間成本 -1 分

### 維度 5：長期合作價值（權重 15%）
- **分數**：6/10
- **理由**：
  - **年齡**：推測 30-40 歲（助理教授、研究軌跡 5-7 年）→ 上升期
  - **軌道匹配**：VLP + AMR = TSMC fab 後勤自動化戰略的潛在引擎
  - **接班人梯隊**：新進教授，暫無明確接班規劃
  - **5 年共同成果**：VLP 製程管控 PoC → 可能 2-3 年見成果
- **判定**：中等潛力；適合「觀察名單 → 試點」路線

---

## 加權總分

```
總分 = 5 × 0.20 + 5 × 0.25 + 6 × 0.20 + 9 × 0.20 + 6 × 0.15
     = 1.0 + 1.25 + 1.2 + 1.8 + 0.9
     = 6.15 → B（可觀察 / 單點合作）
```

---

## 歸類與優先級

| 項目 | 內容 |
|---|---|
| **優先級標籤** | **B** |
| **一句話歸類** | VLP/AMR 定位新銳專家，Fab 後勤自動化契合度中等（50-65%），適合 AMHS PoC 與試點合作 |
| **推薦合作方式** | 1. **AMHS 定位技術試點**（fab 內 AMR 導航驗證）<br>2. **學生交流計畫**（TSMC 實習 → 定位系統改善）<br>3. **光源環境適配研究**（fab 特殊光環境下的 VLP 穩定性） |

---

## Reference URL

1. [Real-Time Indoor VLP Using LSTM-NN with PCA (Sensors 2024)](https://www.mdpi.com/1424-8220/24/16/5424)
2. [Positioning Unit Cell Model Duplication with RCNN (Journal of Lightwave Technology 2024)](https://opg.optica.org/jlt/abstract.cfm?uri=jlt-39-20-6366)
3. [AMR Positioning using Multi-lateration (2025)](https://www.sciencedirect.com/science/article/abs/pii/S0921889025002106)
4. [NCU Department of Mechanical Engineering — Lin Chin-Te Faculty Profile](https://www.me.ncu.edu.tw/en/portfolio-item/%E6%9E%97%E9%8C%A6%E5%BE%B7/)
5. [NCU Scholars — Chin-Te Lin](https://scholars.ncu.edu.tw/en/organisations/department-of-mechanical-engineering/persons/)

---

## 特別提示

- **新銳教授風險管理**：5 年內可能跳槽海外頂校或業界；建議簽訂長期合約
- **VLP 可靠性驗證**：Fab 環境 24/7 運行 vs. 實驗室場景差異大；需完整 12 個月 PoC
- **競業方監控**：若此領域成熟，Sony / Philips 等光學公司可能挖角；需主動啟用合作

