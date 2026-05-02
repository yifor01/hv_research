# CLAUDE.md — hv-research

This file provides guidance to Claude Code when working in this project.

## 專案目的

跨領域深度研究產出基地。使用 `hv-analysis` skill（橫縱分析法）對任何主題做系統性研究並產出 PDF 研究報告；選擇性地用 `khazix-writer` skill 將研究成果改寫成公眾號長文。

**不限 AI 領域** — 產品、公司、概念、技術、人物、歷史事件、社會現象皆可。

## 研究類別分類索引（防呆表）

本專案的研究分為 4 大類，各類有專屬流程、專屬慣例、專屬資料來源。**啟動研究時請先用此表釘定類別，避免跨類混用規則或資料**：

| 類別 | 觸發場景 | 適用工作流程章節 | 適用慣例段 | 專屬資料來源 | 嚴禁引用 |
|---|---|---|---|---|---|
| **A. 一般主題研究** | 產品 / 公司 / 概念 / 技術 / 歷史事件 / 社會現象 | §新研究主題 | §慣例 A 通用 | `raw-materials/<topic>/` | — |
| **B. PI 盡職調查** | 人物盤點 / 教授 Top N / 候選人評估 | §PI 盡職調查類研究 | §慣例 A 通用 + B 盡調專用 | `templates/pi-due-diligence-framework.md` + `templates/scoring-rubric-v2.md` | ❌ 不引用 `用戶資訊/`（個案 PI 與使用者個人健康無關）<br>❌ 不套用「v1/v2/v3 審視意見書」流程（盡調 v1-v4.x 是廣度迭代不是審視重定位） |
| **C. 區域市場 / 決策等級** | 不動產 / 消費市場 / 投資標的買賣決策 | §區域市場 / 決策等級研究 | §慣例 A 通用 + D 區域市場專用 | 平台均價（樂居/591/實登）+ 在地素材 | ❌ 不引用 `用戶資訊/health.md`（買房決策與個人病史無關，除非無障礙需求等特殊情境） |
| **D. 健康 / 個人領域** | 補充品 / 飲食 / 治療 / 美容 / 個人保養決策 | §健康 / 個人領域研究 | §慣例 A 通用 + C 健康個人專用 | `用戶資訊/profile.md` + `用戶資訊/health.md` | ❌ 不套用 PI 盡調的「主管 3 問防禦 / Reference URL 必附」（個人決策不需主管圈選）<br>❌ 不套用區域市場的「Cap Rate / 三平台均價」 |

**判斷不確定時的優先順序**：先看主題本身是否屬人物盤點（B 類）；其次看 outcome 是否與使用者個人狀況綁定（D 類）；最後看素材來源（若已在 `用戶資訊/` 則必為 D 類）。同一主題可能有多種類別解讀時，與使用者澄清後再啟動。

## 目錄結構

```
hv-research/
├── reports/                    # hv-analysis / PI 盡職調查產出的 PDF
│   └── YYYY-MM-<topic>/        # 每份研究自成一個資料夾
│       ├── *.md                # Markdown 原稿（分檔 research_NN_*.md + 合併檔）
│       ├── *.pdf               # 最終 PDF（多版本時加 _vN 後綴）
│       ├── *.html              # weasyprint 中介產物（選擇性保留）
│       └── sources.md          # 引用資料來源清單
│   # 大型多版本研究（≥3 版本或 ≥30 檔）建議分層：
│   #   vX.Y-final/ + archive/{pdfs-old-versions,md-superseded}/ +
│   #   process/ + planning/ + README.md（索引）
│   # 案例：reports/2026-04-tw-univ-semi-ai-professors/
├── articles/                   # khazix-writer 產出的公眾號文章（目前未啟用）
├── raw-materials/              # 研究前蒐集的原始素材（PDF、截圖、筆記）
├── scripts/                    # PDF 生成等工具
│   └── md_to_pdf.py
├── templates/                  # 跨題目復用的方法論 template
│   ├── pi-due-diligence-framework.md
│   └── scoring-rubric-v2.md   # PI 盡職調查 5 維度評分標準
├── 用戶資訊/                    # ⚠️ 僅服務 D 類「健康/個人領域研究」；不應被 A/B/C 類研究讀取
│   ├── README.md              # 資料夾用途與維護規則
│   ├── profile.md             # 個人基本資料（年齡、性別、地區、職業、預算、決策風格）
│   └── health.md              # 健康狀況（已確診疾病 / 體質 / 飲食框架 / 補充品立場 / 檢驗指標）
├── CHANGELOG.md                # 版本紀錄（每份研究交付後追加）
└── README.md
```

## 工作流程

### 新研究主題
1. 在 `raw-materials/YYYY-MM-<topic>/` 放入已蒐集的素材（若有）
2. 執行 `hv-analysis` skill：
   ```
   幫我用橫縱分析法深度研究 <topic>，重點：...
   補充素材：raw-materials/YYYY-MM-<topic>/ 下的檔案
   ```
3. skill 會自動產出 PDF，存進 `reports/YYYY-MM-<topic>/`

### 改寫為公眾號文章（選配）
1. 執行 `khazix-writer` skill：
   ```
   把 reports/YYYY-MM-<topic>/*.md 用卡茲克風格改寫成公眾號長文。
   原型：<五選一>
   我的第一手經歷/觀察：...
   ```
2. 輸出存進 `articles/YYYY-MM-<topic>.md`

### PI 盡職調查類研究（template 驅動）

> **適用類別：B 類**（人物盤點 / 教授 Top N / 候選人評估）。本流程**不適用於** A/C/D 類；不應引用 `用戶資訊/`（個案 PI 與使用者個人健康無關）。

對人物盤點類題目（例如「台灣半導體 AI 教授 Top N」），用 `templates/pi-due-diligence-framework.md`：

1. 廣度掃描候選池（agent 產初步名單，注意 ~30% 幻覺率 → WebFetch 核實姓名系所）
2. 每位候選產 profile（5 維度評分 + 隱形綁定檢查 + 代表實績）
3. 整合排名 + 主管 3 問防禦（題目互補 / 替代候選 / 為何沒選名人）
4. 交付：主名單 PDF（Top N 兩層結構）+ 備選 PDF（分類候選池）；**必附 Reference URL**
5. 能力限制聲明：WebSearch 無法驗證企業內部借調 / 顧問私約 / 未公開合作（見 lessons.md）

PI 盡調的版本演進是**廣度迭代**（v1 候選池 → v2 補位 → v3 補強 → v4 主管反饋落地），與 C 類「審視意見書回應版」、D 類「outcome 重定位」是**不同類型**的版本流程，不要混用。

累積案例：`reports/2026-04-tw-univ-semi-ai-professors/`（TSMC Top 15 + 38 位備選）

### 區域市場 / 決策等級研究

> **適用類別：C 類**（不動產 / 消費市場 / 投資標的買賣決策）。本流程**不適用於** A/B/D 類；不應引用 `用戶資訊/health.md`（買房決策與個人病史無關，除非有無障礙需求等特殊情境）。

不動產、消費市場、投資標的等「買賣決策」類題目，除 hv-analysis 縱橫結構外,建議多一層「**審視意見書回應版**」流程:

1. v1:照 hv-analysis 標準流程產出
2. v2:用「房仲盡調 / 投資盡調」標準自審或外請審，補上:
   - 租金投報率(Cap Rate) / 持有成本 / 稅負試算
   - 風險揭露(地質 / 淹水 / 嫌惡設施 / 耐震)
   - 平台均價差異解釋(樂居/591/實登差距的結構性原因)
   - 三劇本推演去除無依據機率數字,改定性排序
3. v3:加入 SVG 示意圖降低閱讀門檻(歷時折線、對比條、決策樹、金字塔)

C 類的「審視意見書 v1/v2/v3」是**外部視角補強**（房仲 / 投資盡調），與 D 類「outcome 重定位 v1→v2」、B 類「廣度迭代 v1→v4.x」是**不同類型**的版本流程，不要混用。

累積案例:`reports/2026-04-hsinchu-east-guanpu-housing/`(關埔/光埔購屋 v1/v2/v3 + 6 張示意圖)

### 健康 / 個人領域研究（分檔結構）

> **適用類別：D 類**（補充品 / 飲食 / 治療 / 美容 / 個人保養決策）。本流程**不適用於** A/B/C 類；個人健康資料**僅在本類**使用，不應出現在 PI 盡調 / 區域市場 / 一般主題類報告中。

與使用者個人健康/情境綁定的研究（飲食、皮膚、補充品、醫美等），建議採「分檔 research → 合併報告」結構：

1. **啟動前先讀 `用戶資訊/profile.md` + `用戶資訊/health.md`**（個人 baseline 與長期 constraint 已寫好），避免框架錯位
2. **與使用者明確對齊「outcome」與「safety constraint」**——同一個動作可能對應完全不同的 outcome 框架（例如「美容/外觀」vs「疾病管理」），啟動時要先釘定，否則 v1 出來的報告可能完全沒回答到真實問題
3. `research_01_<sub-topic>.md` ~ `research_NN_<sub-topic>.md`：每章獨立深查（病史 / 比較 / 在地化）
4. 合併輸出：`<topic>_橫縱分析報告.md` + `.pdf`
5. 因素材高度個人化（年齡、地點、現有體質），素材放 `raw-materials/<topic>/`

#### v1 → v2 修訂模式（健康類研究專用）

對個人健康類研究，常見「v1 框架對 + 觀念對，但目標 framing 與用戶真實意圖不符」的情況。建議流程：

1. **v1**：照標準分檔結構產出第一版
2. **v2 起手前先做「相關專科主治視角審查」**：依主題制定多軸檢核框架（建議 6-8 軸：科學基礎 / 專科視角 / 跨領域準確性 / 個案適配 / 風險揭露 / 實務執行 / 觀念誤導 / 遺漏盲區）做加權評分
3. **與用戶確認真實 outcome 後重新框定**：若 v1 框架對齊錯位（解決了 X 但用戶真實意圖是 Y），v2 直接 reframe 而非補丁；原 condition 降為 safety constraint
4. **v2 修訂時保留 v1 章節編號穩定**，新內容以子章節 / 增補表 / 重寫段形式無縫嵌入；**版本溯源（哪些段落是 v2 新增 / 重寫 / 升級）寫進 `CHANGELOG.md`，不入報告本文**（避免讀者看 v2 報告時遇到「v1 漏寫了 X」「相對於 v1 變動」這類時空混亂的版本註解）。讀者拿到的 v2 報告應讀來是一份完整自足的文件

累積案例見 `reports/` 下各健康類資料夾；個別案例的修訂細節記在該 report 自己的 README 或 CHANGELOG 條目。

## 命名規則

- `<topic>`：英文小寫，連字號分隔（`claude-code`、`tsmc-2nm`、`ai-coding-agent`）
- 日期：ISO 8601（2026-04）
- PDF 檔名（三種常見格式）：
  - 標準：`<topic>_橫縱分析報告.pdf`（hv-analysis skill 預設）
  - 多版本：`<topic>_橫縱分析報告_vN.pdf`（v1/v2/v3 流程，如關埔購屋）
  - 自訂主題：`<自訂中文名>_v<X.Y>.pdf`（PI 盡調等大型研究，如 `TSMC_PI_彙整大表_v4.2.pdf`）

## 前置依賴

```bash
pip install weasyprint markdown --break-system-packages
```

## Claude Code 操作約束（避免 timeout / context 爆 / 工作中斷）

下列為跨類別、跨研究皆適用的硬約束，違反任何一條都可能造成 session 掛掉、報告半完成、commit 散亂。新研究啟動前先在腦中過一遍：

1. **編號任務一次只做一個，做完確認再進下一個**：todo list 同時只允許 1 個 `in_progress`；上一項未真正完成（檔案落地 / 測試通過 / 視覺驗證 OK）前，不開下一項，不平行推進。
2. **單一 tool call 不寫超過 ~150 行**：Write 一次最多 ~150 行；超過就拆成 Write 第一段（含 frontmatter + 第一節）+ Edit append 後續節，或拆多檔（分檔結構天然吻合此約束）。一次寫太多容易在尾段 timeout 或被 hook 中斷導致檔案半截。
3. **對話超過 20 個 tool call 就開新 session**：每次評估「目前 turn 數 + 預估剩餘 tool call 數」，逼近 20 即在當前停點 commit + push，請使用者開新 session 接續。長 session 的 context 衰減會讓後段判斷失準（記錯檔名 / 重複工作 / 漏校對）。
4. **grep / search 加 `--include`、`-l`、`head -N` 限制輸出量**：`rg` 或 `grep -r` 不加過濾常 dump 整個 repo；標準寫法 `rg -l "pattern" --type md`、`grep -rln "pattern" --include="*.md" reports/ | head -20`。寧可分多次精準搜，不要一次撈全部回來污染 context。
5. **真的 timeout 時，retry 用更小範圍而不是整個任務重做**：Write / Bash 失敗或超時，先排查是哪一段失敗（檔案太大？網路？工具卡住？），retry 時把 scope 切小（只寫剩下章節 / 只跑單一檔的 PDF）；不要無腦重跑整個 Write 或整批 PDF 生成，那只會再失敗一次並燒更多 token。

> 這五條是 Claude Code 自我約束，不是給研究內容的指令；報告本身的方法論在後面 §慣例 章節。

## 慣例

慣例分四層：A 全類別通用、B PI 盡調專用、C 區域市場決策專用、D 健康個人專用。**啟動研究前先確認類別，再套對應的專用慣例**；不要把專用慣例跨類套用。

### A. 全類別通用慣例

- **報告結論先行（BLUF / Bottom Line Up Front）**：每份報告必須以「速答頁」開場——一頁內含（a）一句話總結、（b）5-8 條 actionable 結論、（c）必跳過 / 必避坑清單、（d）章節導航。**速答頁放在所有歷史 / 框架 / 方法論章節之前**，讀者看完速答頁應該已能做出主要決策；後續章節是支持深度（可選讀）。沒有速答頁 = 把方法論的負擔丟給讀者。**這條跨類別通用，A/B/C/D 全適用**——B 類 PI 盡調的速答頁 = Top 5 圈選名單 + 主管 3 問速答；C 類區域市場的速答頁 = 「買 / 不買」決策 + 3 條最關鍵理由；D 類健康的速答頁 = 一句話建議行動 + 3 個必避雷
- **版本註解只入 CHANGELOG，不入報告本文**：版本溯源（「v2 新增」「相對於 v1」「v1 漏寫」「v1 → v2 變動表」）是「作者-協作者」之間的歷史，**不是「作者-讀者」之間的內容**。讀者拿到的報告應讀來是一份完整自足的單一文件，不需要背景知識「v1 寫了什麼」。所有版本註解只放在 `CHANGELOG.md` / commit messages / git history。**唯一例外**：報告 frontmatter 可有 1 行版本標註（例：「本研究 = 5月中聚焦版；全年通用版見 v1.pdf」），但不擴散到內文章節
- **每份研究獨立資料夾**，不要把多份研究的檔案混在同一層
- **素材溯源**：`sources.md` 記錄所有引用 URL + 訪問日期，方便日後驗證
- **PDF 產物連同 Markdown 原稿一併追蹤進 git**（方便遠端直接下載/分享給主管）；若單份 PDF > 50 MB 再個案討論
- **產 PDF 工具**：`scripts/md_to_pdf.py`（weasyprint + markdown），支援多 MD 合併、封面、目錄、emoji → 樣式化標記替換、**SVG 區塊保護**（抽出 → markdown 渲染 → 重插，避免 `nl2br` 破壞 shapes）
- **PDF 寬表格上限**：A4 頁寬下約 10-11 欄；超過會被切斷，改用「標籤列」或分段表
- **SVG 示意圖慣例**（純 PDF 排版規則，所有類別通用）：
  - 直接在 Markdown 內嵌 `<svg viewBox="0 0 580 XXX" ...>`（寬度 580 剛好貼合 A4 頁寬扣除 margin）
  - **圖片編號依章節先後順序排列**，不是設計順序（讀者看圖 1 在 §2 比圖 2 在 §3 自然）
  - **箭頭/對比色必須與底色反差足夠**（深藍底 + 灰色箭頭 = 看不見；改用亮黃 #f1c40f 或白色）
  - 箭頭終點需落在目標形狀 **外緣**；若進入填色區會被同色遮蔽
  - **多邊形寬度需容納最長中文字串**：頂部梯形 / 徽章若有 10+ 字的名單，頂寬 ≥ 180px；否則會被 clip
  - WeasyPrint 的 `<marker>` 渲染纖細，重要箭頭建議改用顯式 `<polygon>` 箭頭頭
  - **WeasyPrint 不支援 `font:` CSS shorthand**（只認 `font-weight + font-size + font-family` 顯式三屬性，否則粗體標題消失）
  - **內嵌 pill 寬度 ≥ 文字寬 + 12-15px buffer**：text-anchor 為 middle 時，pill 寬若小於文字寬，文字會視覺溢出 pill 邊界
  - **WeasyPrint SVG `break-inside: avoid` 支援不完整**：viewBox 高度 ≥ 280px 的 SVG 若放在頁面下半仍會被切跨頁。穩定解法：(a) 在 SVG 標題前手動加 `<div style="page-break-before: always; height: 0;"></div>` 強制圖從新頁頂部開始；(b) 同時壓縮 viewBox 高度 ≤ 280px。兩條都做才穩定
  - **右側標籤超出 SVG width 會被裁切**：寬度 580 的 SVG，從 x=360 起的長中文字串易超界；改用 `text-anchor: end` 配 x=560 從右算起
  - 個別 SVG 修正案例（包含具體像素調整 / pill 寬度 / page-break 處理）寫進 `~/vault/projects/hv-research/lessons.md`，本檔案只保留通用規則
- **能力限制聲明**：所有類別的報告交付前必有 §能力限制章節，避免過度承諾；類別專屬的能力限制（如 B 類的 WebSearch 限制 / D 類的個體差異）在各自專用慣例補充
- **跨領域學習**：研究過程中遇到的方法論心得寫進 `~/vault/projects/hv-research/lessons.md`
- **大型研究多版本清理**：研究歷經 ≥3 版本或 ≥30 檔案時，用 `git mv` 重組為 `vX-final/ + archive/{pdfs-old-versions,md-superseded}/ + process/ + planning/ + README.md` 分層；舊 PDF 搬移不刪除（保留版本對比能力）
- **CHANGELOG.md 維護**：每次研究交付（PDF push）或重大改版（如 v4.0 → v4.2），於 root `CHANGELOG.md` 追加 `## [YYYY-MM-DD]` 條目，依 Added/Changed/Fixed 分類

### B. PI 盡職調查類專用慣例（僅 B 類用，A/C/D 類不適用）

- **主管報告必附 Reference URL**：每位 PI 至少 2-3 個公開連結（學校頁 / Scholar / Lab / 獎項公告）
- **Companion PDF 結構與主 PDF 一致**：同 session 出多份 PDF（如 Top N 主名單 + 備選池）時結構對齊，降低主管閱讀成本
- **WebSearch 能力限制聲明必附**：WebSearch 無法驗證企業內部借調 / 顧問私約 / 未公開合作；交付文件需明寫此限制
- **版本流程是「廣度迭代」**（v1 候選池 → v2 補位 → v3 補強 → v4 主管反饋落地），與 C/D 類的版本流程**不同類型**
- 主管 3 問防禦結構：題目互補 / 替代候選 / 為何沒選名人

### C. 區域市場 / 決策類專用慣例（僅 C 類用，A/B/D 類不適用）

- **版本流程是「審視意見書回應版」**（v1 標準產出 → v2 房仲/投資盡調自審 → v3 SVG 補圖）
- **三劇本推演去除無依據機率**，改定性排序（避免「樂觀 50% / 中性 30% / 悲觀 20%」這種偽定量）
- **平台均價差異需解釋結構性原因**（樂居 vs 591 vs 實登成交價的口徑差異 = 物件年齡 / 是否含車位 / 是否含管理費 / 樣本選擇偏差）
- **風險揭露四軸格式**：地質（土壤液化 / 斷層）/ 淹水 / 嫌惡設施 / 耐震（建照年份對應法規版本）
- **持有成本必附**：Cap Rate（租金投報率）/ 持有稅費（地價稅 / 房屋稅）/ 維護攤提

### D. 健康 / 個人領域類專用慣例（僅 D 類用，A/B/C 類不適用）

- **啟動前必讀 `用戶資訊/profile.md` + `用戶資訊/health.md`**：個人 baseline 與長期 constraint 已寫好，省去重複交代
- **outcome 3 問對齊**（v1 啟動前必做，避免框架錯位浪費整輪研究）：
  1. 這個動作（補品 / 飲食 / 治療 / 醫美 / 保養）最終要解決什麼**可觀察 / 可量測**的問題？
  2. 如果這個 outcome 達成了但其他 100% 沒變，你滿意嗎？（澄清主次 outcome）
  3. 有哪些 condition 是 **constraint**（不能變糟）但不是 **target**（不需主動改善）？
- **版本流程是「outcome 重定位 v1→v2」**（v1 出爐後做專科視角審查 → 發現框架對齊錯位即 reframe v2 → 不在 v1 補丁），與 B/C 類版本流程**不同類型**
- **v2 修訂保留章節編號穩定**：新內容以子章節 / 增補表 / 重寫段形式無縫嵌入；**版本溯源（哪些段落是 v2 新增 / 重寫 / 升級）寫進 `CHANGELOG.md`，不入報告本文**（見 §慣例 A「版本註解只入 CHANGELOG」）。讀者拿到的 v2 報告應讀來是一份完整自足的文件，不需要先讀過 v1 才能理解
- **個體差異能力限制聲明**：報告無法校正使用者個別生理基線（荷爾蒙 / 代謝 / 過敏 / 用藥背景），必附「不取代相關專科醫師個案評估」聲明
- **個人健康資料絕對隔離**：`用戶資訊/` 內容**嚴禁**出現在 A/B/C 類交付報告中。即使使用者同期做多類別研究，個人健康 thread 與其他類別的資料來源完全分離
- **D 類交付前自查防呆**：
  - ❌ 是否誤把 B 類的「主管 3 問防禦 / Reference URL 必附 / Companion PDF 結構對齊」套用到健康類（個人決策不需主管圈選）
  - ❌ 是否誤把 C 類的「Cap Rate / 三平台均價解釋」套用到健康類（不適用）
  - ❌ 是否在報告中混入其他類別專屬的術語或案例命名做為類比（不相關）
