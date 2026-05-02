# 研究五：最終推薦與決策樹

## 5.1 速答頁（一頁版總結）

> **一句話結論**：守 70 萬最強組合是 **Toyota Yaris Cross 享樂版**；爆預算到 86 萬最佳組合是 **Honda HR-V 汽油 S+** 或 **Nissan Kicks 智行旗艦**；如能接受中古路徑則 **Toyota Corolla Cross Hybrid 2022（CPO）** 是 CP 王。

### 🎯 三條推薦路徑（依價位排序）

| 預算路徑 | 推薦車款 | 落地價 | 為什麼 |
|---|---|---|---|
| 守 70 萬 | **Toyota Yaris Cross 享樂版** | 約 75 萬 | TSS 全配 + 油耗最省 + 都會好開；犧牲 BSM/RCTA |
| 爆到 85 萬 | **Honda HR-V 汽油 S+** | 約 86 萬 | Honda Sensing + LSF 低速跟車（雪隧塞車神器） + BSM/RCTA 標配 |
| 爆到 85 萬（替代） | **Nissan Kicks 智行旗艦** | 約 84 萬 | TNCAP 五星 + 360° 環景 + RCTA + BSM 同價最強配備 |
| 中古車 70 萬 | **Toyota Corolla Cross Hybrid 2022 豪華（CPO）** | 約 70-75 萬 | 油電 + TSS 2.0 + 1-2 年原廠保固 |

### ✅ 必做的 5 件事
1. 三款都試駕（同一週內，當天就比較）；雪隧路段試「ACC + LKA」要實際開到才知差別
2. 試駕時帶捲尺，量你**坐進駕駛座後的後排腿部空間**（小休旅常被忽略）
3. 中古車路徑必加「**第三方驗車**」NT$3,000-6,000（HotCar / 車輛醫師）
4. 保險先抓乙式車體險（首購建議至少前 3 年）；報價找 2-3 家比
5. 落地時 dealer 一定會丟一堆配件包 NT$3-8 萬，**只買行車記錄器（前後雙鏡頭）+ 隔熱紙**，其他都可後市場做（便宜一半）

### ⛔️ 必避的 5 個雷
1. **不要買中資品牌**（MG ZS）：保值與停車場觀感雙輸
2. **不要為「外觀」爆預算到 90 萬以上**：26 歲女性首購、第一年新鮮感過後外觀差異感受度衰減極快
3. **不要相信車商「優惠送配件」**：羊毛出在羊身上，現金折抵永遠優於配件折抵
4. **不要在貸款時被推銷信貸搭配**：純車貸利率 3-5% vs 信貸 8-12%，差很大
5. **不要忽略「停車位先有再買車」**：竹科租屋若無含車位需先解決，否則路邊找位 5 年累積拖吊+刮傷成本可能 5 萬以上

### 📊 章節導航
- §5.2 三款 Top 推薦的詳細比較
- §5.3 決策樹（給「我到底該選哪一台」的圖示路徑）
- §5.4 試駕清單（試駕當天必檢項目）
- §5.5 議價與簽約建議
- §5.6 能力限制聲明

---

## 5.2 Top 3 詳細比較

| 維度 | 🥇 Honda HR-V 汽油 S+ | 🥈 Nissan Kicks 旗艦 | 🥉 Toyota Yaris Cross 享樂 |
|---|---|---|---|
| 售價 | 79.9 萬 | 78.5 萬 | 69.5 萬 |
| 落地價（估） | 86 萬 | 84 萬 | 75 萬 |
| 動力 | 1.5L NA / 121 hp | 1.5L NA / 115 hp | 1.5L NA / 106 hp |
| 變速箱 | CVT | CVT | CVT |
| 油耗 | 15-16 km/L | 14-15 km/L | 17 km/L |
| 主動安全 | Honda Sensing 全配 + LSF | NIM 智行 + ProPILOT 部分 | TSS（含 Stop&Go） |
| BSM 盲點 | ✓ | ✓ | ✗ |
| RCTA 後車側 | ✓ | ✓ | ✗ |
| 360° 環景 | ✗（升 Prestige） | ✓ AVM | ✗（升潮玩） |
| 氣囊 | 6 | 6 | 6 |
| TNCAP/E-NCAP | E-NCAP 4 ★ | TNCAP 5 ★ | TNCAP 4 ★ |
| 保值率 | 60-65% | 55-60% | 60-65% |
| 都會好開 | ★★★★ | ★★★★★ | ★★★★★ |
| 雪隧長途 | ★★★★★ | ★★★★ | ★★★ |

## 5.3 決策樹（visual）

<div style="page-break-before: always; height: 0;"></div>

<svg viewBox="0 0 580 540" xmlns="http://www.w3.org/2000/svg" style="display:block; margin:0 auto; max-width:100%;">
  <defs>
    <style>
      .node { fill: #f4f6fa; stroke: #1a3d7c; stroke-width: 1.5; }
      .nodeq { fill: #fff8e1; stroke: #b8860b; stroke-width: 1.5; }
      .nodea { fill: #e8f4ec; stroke: #2e7d32; stroke-width: 1.8; }
      .label { font-weight: 600; font-size: 11pt; font-family: "Noto Sans CJK TC", sans-serif; fill: #1a3d7c; }
      .qlabel { font-weight: 700; font-size: 11pt; font-family: "Noto Sans CJK TC", sans-serif; fill: #7a5a00; }
      .alabel { font-weight: 700; font-size: 11pt; font-family: "Noto Sans CJK TC", sans-serif; fill: #1b5e20; }
      .small { font-size: 9pt; font-family: "Noto Sans CJK TC", sans-serif; fill: #444; }
      .arrow { stroke: #555; stroke-width: 1.6; fill: none; }
      .ylabel { font-size: 9pt; font-family: "Noto Sans CJK TC", sans-serif; fill: #666; font-weight: 600; }
    </style>
  </defs>

  <!-- Q1 -->
  <rect class="nodeq" x="180" y="15" width="220" height="50" rx="6"/>
  <text class="qlabel" x="290" y="38" text-anchor="middle">你的硬預算上限是？</text>
  <text class="small" x="290" y="55" text-anchor="middle">（包含落地、配件、保險）</text>

  <!-- Q1 branches -->
  <path class="arrow" d="M 220 65 L 130 110" />
  <text class="ylabel" x="155" y="90">≤ 78 萬</text>
  <path class="arrow" d="M 360 65 L 450 110" />
  <text class="ylabel" x="395" y="90">可到 88 萬</text>

  <!-- Q2 left: tight budget -->
  <rect class="nodeq" x="20" y="115" width="220" height="50" rx="6"/>
  <text class="qlabel" x="130" y="138" text-anchor="middle">願意走中古車路徑嗎？</text>
  <text class="small" x="130" y="155" text-anchor="middle">（可加驗車費、品牌不限）</text>

  <!-- Q2 right: bigger budget -->
  <rect class="nodeq" x="340" y="115" width="220" height="50" rx="6"/>
  <text class="qlabel" x="450" y="138" text-anchor="middle">最重視哪一項？</text>
  <text class="small" x="450" y="155" text-anchor="middle">（安全配備 / 動力 / 保值）</text>

  <!-- Q2L branches -->
  <path class="arrow" d="M 65 165 L 50 215" />
  <text class="ylabel" x="38" y="195">是</text>
  <path class="arrow" d="M 195 165 L 215 215" />
  <text class="ylabel" x="215" y="195">否</text>

  <!-- Q2R branches: 3 options -->
  <path class="arrow" d="M 365 165 L 330 215" />
  <text class="ylabel" x="332" y="195">配備</text>
  <path class="arrow" d="M 450 165 L 450 215" />
  <text class="ylabel" x="455" y="195">動力</text>
  <path class="arrow" d="M 535 165 L 565 215" />
  <text class="ylabel" x="555" y="195">保值</text>

  <!-- Answers row 1 -->
  <rect class="nodea" x="0" y="220" width="100" height="65" rx="6"/>
  <text class="alabel" x="50" y="245" text-anchor="middle">CPO</text>
  <text class="small" x="50" y="262" text-anchor="middle">Corolla Cross</text>
  <text class="small" x="50" y="276" text-anchor="middle">Hybrid 2022</text>

  <rect class="nodea" x="120" y="220" width="180" height="65" rx="6"/>
  <text class="alabel" x="210" y="245" text-anchor="middle">Yaris Cross 享樂</text>
  <text class="small" x="210" y="262" text-anchor="middle">69.5 萬，TSS 全配</text>
  <text class="small" x="210" y="276" text-anchor="middle">嚴守 70 萬最佳解</text>

  <rect class="nodea" x="280" y="220" width="100" height="65" rx="6"/>
  <text class="alabel" x="330" y="245" text-anchor="middle">Kicks 旗艦</text>
  <text class="small" x="330" y="262" text-anchor="middle">78.5 萬</text>
  <text class="small" x="330" y="276" text-anchor="middle">TNCAP 5★</text>

  <rect class="nodea" x="395" y="220" width="100" height="65" rx="6"/>
  <text class="alabel" x="445" y="245" text-anchor="middle">HR-V S+</text>
  <text class="small" x="445" y="262" text-anchor="middle">79.9 萬</text>
  <text class="small" x="445" y="276" text-anchor="middle">LSF 雪隧神器</text>

  <rect class="nodea" x="510" y="220" width="70" height="65" rx="6"/>
  <text class="alabel" x="545" y="245" text-anchor="middle">Corolla</text>
  <text class="alabel" x="545" y="262" text-anchor="middle">Cross</text>
  <text class="small" x="545" y="278" text-anchor="middle">79.9 萬</text>

  <!-- Bottom note -->
  <rect class="node" x="40" y="320" width="500" height="60" rx="6"/>
  <text class="label" x="290" y="343" text-anchor="middle">三條路徑都需做的共同步驟</text>
  <text class="small" x="290" y="362" text-anchor="middle">①當週試駕全部候選 ②帶捲尺量後座 ③對比 2-3 家保險報價 ④只買行車記錄器+隔熱紙</text>

  <!-- Caveat box -->
  <rect class="node" x="40" y="395" width="500" height="55" rx="6" style="fill:#fff5f5; stroke:#c62828;"/>
  <text class="label" x="290" y="418" text-anchor="middle" style="fill:#c62828;">中古車路徑必做</text>
  <text class="small" x="290" y="437" text-anchor="middle">第三方驗車（HotCar / 車輛醫師）NT$3,000-6,000，這筆錢是必要支出不是奢侈品</text>

  <!-- Footer -->
  <text class="small" x="290" y="475" text-anchor="middle" style="fill:#888;">圖 1：26 歲竹科女性工程師購車決策樹（70 萬基準、可爆預算到 88 萬）</text>
</svg>

## 5.4 試駕清單（試駕當天必檢項目）

預約試駕前一天，把這份清單列印帶到展間。理想試駕路線：**展間 → 國道 1 號（測高速、ACC、LKA）→ 市區彎窄巷弄（測迴轉、視野）→ 倒車入位（測 BSM、RCTA、環景）**，全程 30-40 分鐘。

| 檢查項目 | 怎麼測 |
|---|---|
| 駕駛座姿勢 | 椅子調到底是否能踩到底煞車不彆扭；A 柱是否擋到右轉視線 |
| 後視鏡視野 | 變換車道時左後視鏡能否完整看到後車；無 BSM 的車要特別測 |
| ACC 全速域 | 在國道把車距調到中段，前車減速時是否平順煞停（Stop & Go 必試） |
| LKA 車道維持 | 故意微微飄向車道線，方向盤是否會回正；力道是否舒適 |
| AEB 模擬 | 不能真的去撞，但可問業務「上一台同型車的 AEB 警報靈敏度」 |
| BSM 盲點 | 走國道時請業務在旁車道並行，看儀表/後視鏡黃燈是否點亮 |
| 倒車環景 | 找停車格實際倒車入位，看影像清晰度與延遲 |
| 啟動關門質感 | 連續關 3 次車門聽聲音是否一致；副駕、後座門也要關 |
| 後座空間 | 駕駛座調好後，自己坐到後座，膝蓋與前椅背距離至少 2 拳 |
| 行李廂 | 後排放倒是否平整；備胎位置 |

## 5.5 議價與簽約建議

26 歲首購族常見的「貴在哪裡」：

1. **車價部分**：
   - 月底、季底業務 quota 壓力大，議價空間最佳；建議 **3 月底、6 月底、9 月底、12 月底**去談
   - 同品牌不同經銷商互相報價（北部、桃竹苗都可問），通常能再壓 1-3 萬
   - 不要被「總價包套」糊弄，要請業務把「車價、領牌費、配件、保險」**逐項拆開**列在訂單

2. **配件部分**：
   - 業務送的配件「估價單金額」通常是市場價 1.5-2 倍，**永遠選擇現金折抵**而非配件折抵
   - 真的要選配件，**只選**：行車記錄器（前後雙鏡頭，原廠 NT$8-15K，後市場 NT$5-8K 同等規格）、太陽隔熱紙（前擋 + 四面車窗 + 後擋，後市場 NT$8-15K）

3. **貸款部分**：
   - 純車貸利率：銀行通常 3-5%、原廠車貸 5-7%、車商代辦 6-8%；找你薪轉銀行談最低
   - 警惕「免頭款」搭信貸：信貸利率 8-12%，5 年下來多支出 8-15 萬
   - 推薦結構：**首付 30-40%、車貸 5 年期固定利率**，最不會被吃豆腐

4. **保險部分**：
   - 第一年強制險業務通常已含在落地，但任意險（第三人、車體險）**自己找產險公司詢價** 2-3 家（國泰、富邦、新光、明台）
   - 直接打 0800 客服詢價，比業務轉接的「合作產險」通常便宜 10-20%

## 5.6 能力限制聲明

本研究基於 2026 年 5 月台灣市場公開資料整理，**有以下限制不應視為個人化建議的替代**：

1. **未實地試駕、未驗證個人坐姿與操控感**：身高、坐姿、操控習慣是「人車匹配」的決定因素，無法靠書面分析取代
2. **未評估個人財務狀況**：本研究的 TCO 試算基於合理假設（年薪、租屋、儲蓄結構），實際情況可能差異很大；重大採購決策建議先做現金流盤點
3. **未涵蓋電動車路徑**：70 萬內的純電車（Luxgen n7 大改後價格、MG4 等）尚未進入分析；台積電員工是否能在公司充電、是否有住家充電條件，會大幅影響電車 vs 油車決策——本研究預設使用者沒有充電基礎設施
4. **中古車個案無法驗證**：中古車的「同型號不同車」差異極大，第三方驗車是必要環節
5. **非保險規劃師建議**：保險建議僅為一般原則，個人保單組合應與保險業務員/獨立顧問詳談
6. **2026 年下半至 2027 年的政策變動風險**：燃料稅綠化、關稅、貨物稅、TNCAP 新版規章（2026 啟動）都可能影響車價或評等——本研究僅反映「現在」可得資訊

**建議落地行動順序**：
1. 用本研究 §5.3 決策樹釘定 1-2 條路徑
2. 預約 Top 2-3 候選車款試駕（同一週內）
3. 試駕後若仍猶豫，找 1 位「開過這台車 ≥ 2 年」的車主詳聊（PTT、Mobile01 私訊都行）
4. 確定車款後 → 議價（多經銷商比 + 月底 quota 壓力 → 議價空間最佳）→ 簽約 → 落地
