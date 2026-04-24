# Phase 4 Profile — 黃乾怡 Chien-Yi (Jay) Huang（NTUT 工業工程與管理系 教授兼系主任）

> 訪查日期：2026-04-24

---

## 結論先行

**Tier：B+（Backup PDF 建議入榜,置於 36-50 段中段）**

- **職等核實 OK**：黃乾怡為 NTUT 工管系教授兼**系主任**(Department Chair),SUNY Stony Brook IE 博士。
- **半導體相關 deliverable 有,但偏 PCB/封裝後段**：代表作為 PCB Gold Finger 缺陷檢測 (Electronics 2024)、陶瓷基板 AOI (Applied Sciences 2022)、半導體 wafer dies wavelet 缺陷檢測（2010,稍舊）。
- **學術影響力中等**：Google Scholar 1,500 citations、h=21、i10=41,在工管系教授中屬中上,但相對 phase 1 Tier S 教授(h>40)有差距。
- **產學合作偏電子製造而非晶圓廠**：強項在 SMT、PCB、ceramic substrate、solder paste 印刷 — 對應對象是 ASE/SPIL/欣興/南電/楠梓電,而非 TSMC fab。

**對 TSMC 的價值**：間接 — 透過 TSMC 後段封裝 (CoWoS/SoIC) 供應鏈或 ASE 子公司觸及;直接 fab 切入點較弱。

---

## §1 隱形綁定檢查

| 檢查項 | 結果 |
|---|---|
| 是否已是 TSMC 顧問 / 借調 | 無公開資訊 |
| 是否陽明交大/清大聯合中心 PI | 否 |
| 是否聯電 / 力積電董事 / 顧問 | 無公開資訊 |
| 是否日月光 / 矽品 / 欣興 顧問 | **可能性高** — PCB/陶瓷基板 AOI 研究路徑與封測廠 highly aligned,但無公開頭銜 |
| 是否兼任新創 CTO/共同創辦人 | 未見公開記錄 |

**判斷**：無強綁定。但若 TSMC 想接觸,需先確認他是否已與 ASE/SPIL 等 OSAT 業者有產學案。

---

## §2 技術契合度（對 TSMC AI Top 痛點）

### 命中項目
- **PCB Gold Finger 缺陷檢測 (2024)** — Electronics 期刊,Pei-Xuan Tsai 共著,YOLO-based ML pipeline。可遷移至 TSMC 後段 substrate 檢測。
- **Ceramic Substrate AOI (2022)** — Applied Sciences,直接對應半導體封裝陶瓷基板;CoWoS interposer 檢測潛在切入點。
- **Solder Paste 印刷製程 (2011, 53 citations)** — 經典參考論文,對應 SMT / 封裝 process knowledge。
- **Lean Manufacturing 2022 (73 citations)** — 智慧製造管理層面,可延伸到 fab 工序整合。

### 弱項
- **無 fab front-end 任何研究**(EUV/litho/etch/CMP) — 純後段 + 資料分析。
- **論文質量分散**：top cited 是 2013 flow shop scheduling 算法（與半導體無關）;PCB/AOI 類論文 30-40 citations 屬 mid-tier。
- **5G Digital Twin (2022)** 一篇 — 屬探索性質,非主軸。

**契合度評分**：**1.0/2** — PCB/ceramic substrate 命中半導體後段,但無 front-end 切入點。

---

## §3 學生 Lab 規模與流向（技職體系觀察）

- 實驗室名稱：**Quality Control Practical Training Classroom** + **Advanced Process Technology and Quality Laboratory**(兩個 lab)
- 招生規模：系主任身分,可推測 lab 規模約 10-15 人(碩+博)
- **流向預測**:
  - 主流向 → 欣興、南電、健鼎、瀚宇博德等 PCB/IC 載板大廠
  - 次流向 → ASE、SPIL、力成、京元電 OSAT 廠的 quality / process engineer
  - 少數 → TSMC 後段 packaging 部門、聯發科 quality

**5 年招募潛力評分**：**1.5/2** — 對 TSMC CoWoS 封裝廠擴張(2025-2027 大規模招募)是補強來源,但碩班規模較范書愷組小。

---

## §4 5 維度評分明細

| 維度 | 分數 | 理由 |
|---|---|---|
| 1. 技術命中度 | **1.0/2** | PCB/ceramic substrate 命中後段,無 front-end |
| 2. 5 年學生招募潛力 | **1.5/2** | OSAT/PCB 載板強,fab 直接招募較弱 |
| 3. 企業共建長期 Lab 開放度 | **1.5/2** | 系主任身分行政力強,有 PCB 業界合作經驗 |
| 4. 資源未被搶佔程度 | **1.5/2** | 無強綁定,但可能已有 PCB 廠案 |
| 5. 個人黃金期剩餘 | **1.0/2** | 1995 PhD 推估,黃金期 5-7 年 |
| **合計** | **6.5/10** | **Tier B+**(進 backup 36-50 名單中段) |

---

## §5 合作優缺點 + 3 個合作題目建議

### 優點
- **CoWoS / SoIC 後段檢測切入點**：陶瓷基板 + PCB 缺陷檢測直接對應 advanced packaging 痛點;
- **系主任行政權**：可開定向班、整合系上資源;
- **Lean Manufacturing 視角**：對 fab 後段工序整合有獨特觀點;
- **PCB 載板供應鏈關係**：欣興/南電是 TSMC CoWoS 上游,可作為三方橋樑。

### 缺點
- **無 front-end fab 經驗**：難切入 N3/N2 主流 R&D 議題;
- **論文 mid-tier**：學術光環不及 phase 2 Tier S 候選;
- **lab 規模有限**：難承接大型 GPU-intensive 案;
- **可能已被 PCB 廠包走**：產學合作槽位可能已滿。

### 3 個合作題目建議

1. **「CoWoS Interposer Surface Defect AOI 2.0」**（中型,1 年）
   - 延伸 2022 ceramic substrate AOI,改打 TSMC CoWoS interposer 表面檢測;
   - 引入 Vision Transformer 取代 CNN,目標召回率 > 99.5%。

2. **「Substrate Solder Joint X-Ray ML 分類」**（小型,6-9 個月）
   - 對應 SoIC / CoWoS bump 焊點 X-ray 影像缺陷分類;
   - 黃老師 2011 solder paste 論文可作為 process knowledge 基礎。

3. **「TSMC 後段封測良率 Lean + ML 整合系統」**（戰略級,2-3 年）
   - 結合 Lean Manufacturing 與 ML defect detection,在嘉義/竹南 CoWoS fab 試點;
   - 培訓 NTUT 工管系定向班 20-30 人/年進入 TSMC packaging quality engineering。

---

## §6 Reference URL 清單

1. [Department Chair Chien-Yi Huang — NTUT IEM](https://iem.ntut.edu.tw/p/405-1081-65525,c11955.php?Lang=en)（訪 2026-04-24)
2. [Chien-Yi Huang — Google Scholar(1,500 citations,h=21)](https://scholar.google.com/citations?user=N_1GIA0AAAAJ&hl=en)(訪 2026-04-24)
3. [Chien-Yi Huang — ResearchGate](https://www.researchgate.net/profile/Chien-Yi-Huang)（訪 2026-04-24)
4. [Applying ML to PCB Gold Finger Defect Detection — Electronics 2024](https://www.mdpi.com/2079-9292/13/6/1090)（訪 2026-04-24)
5. [Applying Deep Learning to Ceramic Substrates Defect Detection — Applied Sciences 2022](https://mdpi.com/2076-3417/12/5/2269/htm)（訪 2026-04-24)
6. [黃乾怡 中文頁](https://iem.ntut.edu.tw/p/405-1081-120980,c3754.php?Lang=zh-tw)（訪 2026-04-24)

---

**Phase 4 結論**：黃乾怡是「後段封測補強牌」,對 TSMC CoWoS 戰略有間接價值。建議 Backup PDF 36-50 段中段位置,加註「CoWoS 後段 AOI / 陶瓷基板檢測」標籤。
