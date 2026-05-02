# Changelog

All notable changes to the hv-research project.

Format: `## [YYYY-MM-DD]` with Added / Changed / Fixed / Removed subsections.

## [2026-05-02] (CLAUDE.md 跨類別慣例新增：BLUF 結論先行 + 版本註解隔離)

### Changed
- `CLAUDE.md` §慣例 A 全類別通用慣例新增 2 條跨類別硬約束：
  - **報告結論先行（BLUF）**：每份報告必須以「速答頁」開場（≤1 頁，含一句話總結 + 5-8 條 actionable 結論 + 必跳過 / 必避坑清單 + 章節導航）；放在所有歷史 / 框架 / 方法論章節之前。讀者看完速答頁應該已能做出主要決策。A/B/C/D 全類別適用
  - **版本註解只入 CHANGELOG，不入報告本文**：版本溯源（「v2 新增」「相對 v1」「v1 漏寫」）只放在 CHANGELOG / commit / git history；報告本文應讀來是一份完整自足的單一文件。唯一例外：報告 frontmatter 可有 1 行版本標註，不擴散到內文
- `CLAUDE.md` §健康個人領域研究 v1→v2 修訂模式 第 4 條同步修訂：v2 新增 / 重寫 / 升級的段落溯源寫進 CHANGELOG.md 而非報告本文
- `reports/2026-05-hokkaido-attractions-restaurants/research_v2_*.md`：套用新慣例
  - v2-01 改寫頂部新增「速答頁」（一句話總結 + 7 條 actionable 結論 + 6 條避坑 + 章節導航表）
  - v2-01 ~ v2-04 全文移除版本註解（v1 漏寫 / v2 新增 / v1 → v2 變動表 / v2 不取代 v1 等）
  - 章節編號從 v2.X 改為 §1-§6 直白編號
  - PDF 重新產出（435.9 KB）

## [2026-05-02] (北海道四城景點與餐廳 v2 聚焦版 — 5月中行程・景點・螃蟹深章)

### Added
- `reports/2026-05-hokkaido-attractions-restaurants/`：v2 聚焦版交付（不取代 v1，補強）
  - `北海道四城景點與餐廳_橫縱分析報告_v2_5月中聚焦.pdf`（A4，430 KB，4 章節結構）
  - 4 份 v2 分章 markdown：
    - `research_v2_01_may_baseline.md`：v2 摘要 + 5月中氣候基線（4城均高/均低/朝晚低點）+ 日照與 Blue Hour 時點 + 5月中 vs 其他月份決策
    - `research_v2_02_attractions_in_may.md`：4 城景點 5月中實際狀態（盛景/過渡/未開三色標記）+ 5月中應該去/跳過清單
    - `research_v2_03_crab_deep_dive.md`：4 蟹種旬曆（タラバ/ズワイ/毛蟹/花咲）+ 4 城蟹店 14 家比較表 + 蟹宅配回國 3 種方案 + 6 條防雷常識
    - `research_v2_04_may_itinerary_matrix.md`：5/6/7 天 5月中專屬行程矩陣（含毛蟹體驗點+丁香祭時點）+ 6 條 5月專屬注意事項（リラ冷え/GW後房價/美瑛淡季/海膽尾段/霧/宅配時序）+ v1→v2 變動摘要表
- `sources.md` 第六區塊：v2 補充來源（5月氣候 10 條 + 札幌丁香祭 7 條 + 五稜郭櫻 10 條 + 螃蟹漁期 10 條 + 函館海膽 10 條 + 美瑛 5月 7 條 = 共 ~54 個新 URL）

### v2 核心發現（v1 漏寫的）
- **5月中是「毛蟹單蟹獨秀」窗口**：v1 三大蟹並列說法在 5月中失準——ズワイガニ 已禁漁（11/6-3/20）、タラバ流通主峰是 11-2月（5月多冷凍）、花咲蟹 7-9月才當令——只有毛蟹（鄂霍次克 / 宗谷產春期）為當令鮮貨
- **5月中 4 城特殊景觀（其他月份完全沒有）**：(1) 美瑛春之青麥田 + 殘雪十勝岳（5/15-6/10 限定）、(2) 小樽運河最藍水色窗口（雪融藻未長）、(3) 札幌丁香祭 pre-festival 週（5/14-5/19 綠意大通）
- **「リラ冷え」風險**：5月中下旬丁香盛開期常突降至 5-8°C，純春裝會凍，需內建薄羽絨/防風中層
- **失落景觀清單**：五稜郭櫻 4/27-28 已滿開、5月中已葉櫻；薰衣草 6月底才開；雪燈 / 雪祭 / 青池ライトアップ 全部結束
- **補位景觀清單**：北海道神宮 / 圓山八重櫻（5/1-5/15）、松前公園八重櫻、函館春期海膽尾段（漁期 4-6月）、大沼國定公園駒岳殘雪 + 新綠湖

### Changed
- `sources.md` 由 v1 五大區塊（札幌 / 小樽 / 函館 / 美瑛 / 跨城共通）擴充為六大區塊（新增「v2 補充來源」段）
- 此份研究歸入 D 類「v1 + v2 聚焦補強」模式（A 類旅遊但採用 outcome 重新對焦的修訂法），v1 全年通用版仍保留作為框架基礎

## [2026-05-02] (Agent 長期記憶系統 v3 ── 編排優化)

### Added
- `agent-memory-systems_橫縱分析報告_v3.pdf`（A4，594.6 KB，1681 行 markdown）
- §0 前置區三件套（讓讀者 3 分鐘內找到結論，符合上游 BLUF 慣例）：
  - **30 秒選型卡**：10 列 × 4 欄（情境 / 第一推薦 / 第二選擇 / 為什麼）+ 三個選型 gate
  - **本報告閱讀導引**：7 種角色路徑表（趕時間決策者 / 框架定位 / 設計取捨 / benchmark / 主管 / 採購 / 完整研究）
  - **新 SVG「11 個選項的抽象層級全景」**：第零層（Long Context+Cache）/ 第一層（tool-primitive）/ 第二層（service-layer）/ 第三層（概念範式）四層分類
- §1 ~ §10 各章開頭新增「**本節結論**」blockquote 3-5 行 bullet（L3 結論先行）
- frontmatter 新增 1 行 v3 版本標註（符合上游「版本註解隔離」唯一例外條款）

### Changed
- 全文 inline v1/v2 標註激進清除（共 ~24 處），對齊上游新慣例「版本註解只入 CHANGELOG，不入報告本文」：
  - 9 處章節標題（§1.3 / §2.6 / §2.7 / §2.8 / §2.9 / §3.4 / §4.3 / §7 / §9.1）
  - ~15 處內文括號（§2.4 22K→47K 對齊註、§2.11 公式註記、§7 場景速查 / 關鍵 reframe、§8 四條失敗模式、§9.1 雛形括號、§10 items 10/11/12、§11 Model Provider 標題、SVG 內 v2 文字 / comments）
- 章節敘述改為單一時間點視角，讀者不需在 v1/v2 之間時空切換
- 文首移除原「v2 重點修訂（vs v1）」6 條 bullet 列表
- 保留真實版本識別號（Mem0 v1.0.0、all-MiniLM-L6-v2、rohitg00 LLM Wiki v2 gist 等）

### Preserved
- `agent-memory-systems_橫縱分析報告_v2.pdf`（v2 PDF 保留歸檔，供版本對比）
- `agent-memory-systems_橫縱分析報告_v2.md`（v2 MD 新建為歸檔副本）

## [2026-05-02] (北海道四城景點與餐廳深度分析 v1 — A 類旅遊主題研究)

### Added
- `reports/2026-05-hokkaido-attractions-restaurants/`：A 類一般主題研究第一版交付
  - `北海道四城景點與餐廳_橫縱分析報告.pdf`（A4，472 KB，5 章節結構）
  - 5 份分章 markdown：
    - `research_01_overview_and_vertical_part1.md`：執行摘要 + 範圍框架 + 縱向（札幌、小樽）
    - `research_02_vertical_part2_and_horizontal_overview.md`：縱向（函館、美瑛）+ 橫向 1（四城角色互補）
    - `research_03_horizontal_attractions.md`：橫向 2（三大夜景 / 海鮮市場 / 紅磚老建築 / 三大拉麵流派 / 不接預約文化）
    - `research_04_itinerary_matrix_and_picks.md`：橫向 3（行程矩陣 × 季節 × 自駕）+ 四城精選必訪清單（景點 19 處 + 餐廳 21 家）
    - `research_05_caveats_and_limits.md`：跨城共通注意事項 + 8 條能力限制聲明 + 速查表
  - `sources.md`：分四城 + 跨城共通五大區塊，120+ URL，繁中旅遊媒體 + 北海道官方 + Tabelog + 店家官網交叉驗證
- `raw-materials/2026-05-hokkaido-attractions-restaurants/`：四城分檔素材
  - `sapporo.md`（17 景點 + 21 餐廳）、`otaru.md`（10 景點 + 10 餐廳）、`hakodate.md`（10 景點 + 12 餐廳）、`biei.md`（13 景點 + 11 餐廳）
- 縱向章主軸：四城歷史身分（札幌 1869 開拓使機能性都市 / 小樽 1923 運河 + 1986 保存運動 / 函館 1854 開港西洋混血 / 美瑛 1971 前田真三 + 1970s 廣告 + 2012 Apple 桌布三波視覺敘事）如何形塑今日旅遊體驗
- 橫向章主軸：「角色互補不重疊」（札幌樞紐 / 小樽衛星懷舊 / 函館跳島歷史 / 美瑛自然田園）+ 同類景點橫切對比表 + 行程設計矩陣（天數 × 月份 × 自駕）
- 重要時效資訊：札幌雪祭 2026 第 76 屆（約 2/4–2/11）/ 小樽雪燈之路 2026/2/7–2/14 / 美瑛青池ライトアップ 2025/10/24–2026/4/22 / 北海道新幹線札幌延伸延後至 2038 年度末

### Changed
- `CLAUDE.md`：新增 §「Claude Code 操作約束」段，5 條硬約束（編號任務一次一個 / 單 tool call ≤150 行 / 對話 >20 tool call 開新 session / grep 加過濾 / timeout retry 縮 scope），插在 §前置依賴 與 §慣例 之間

## [2026-04-30] (鼻中膈手術 × lean PCOS 研究 v2 ── 首席專科醫師四主治圓桌審查修訂)

### Added
- `REVIEW_chief_specialist_v1.md` — 四主治圓桌（鼻科 / 內分泌 / 麻醉 / 婦產生殖）+ 6 軸加權評分總分 89/100 + 行動建議三級分類（Critical/High/Medium）
- `鼻中膈手術_橫縱分析報告_v2.pdf`（A4，1.44 MB，含 review doc 完整附錄）
- §1.4.4 舒眠麻醉的 lean phenotype 氣道風險（v2 新增）— 解釋為何 BMI ≤ 21 + 鼻部填塞 + 仰躺建議優先全麻
- §3.2.6 PONV 雙重預防章節（**🔴 v2 新增 — Critical**）— Apfel score 自評 + dual prophylaxis 主動爭取 + lean phenotype 後果倍增論述
- §5.6 麻醉藥 / 抗生素 / X 光對隨後懷孕的明確安全聲明（v2 新增）— FDA Cat B/C 標註 + 卵子成熟週期論述消除常見擔憂
- §3.1 + §5.2 維他命 C 1000 mg/日（v2 新增）— prolyl hydroxylase 輔因子，與口服膠原協同
- §5.3 陷阱 1 鼻塞期食慾下降的多口味 hack（v2 新增）— 6 種 hack 表格（湯類 / 多味道 / 室溫 / 質地對比 / 辣麻 / 餐前清湯）
- §6.6 簽手術同意書前清單分為 ENT / 麻醉 / 內分泌婦科三段，新增 PONV 麻醉項

### Changed
- §3.2.3 PCOS-VTE 引用 attribution 修正（v2 修正）— OR=5.23 改為單獨引自 Bird 2013 AJOG（PMC4408606）；CMAJ 2013 (Okoroh) 改為輔證（整體 PCOS-VTE 約 2 倍，未報告 phenotype 分層）
- §3.2.4 反應性低血糖樣本 caveat 加入（v2 修正）— 50% 改為 30-50%，標註 n=64、BMI ≤ 25 lean 定義較寬
- §4.3 情境 B Floseal 96% 止血率加 evidence caveat（v2 修正）— 該數字主要來自 FESS RCT，septoplasty 單獨情境 evidence 較弱
- §5.6 備孕用詞改保守（v2 重寫）— 「下個月經週期即可」對 PCOS 月經不規則者偏激進，改為「術後 1-3 個月確認月經週期回到 baseline + 抗生素 ≥ 60 天」
- §2.4 caudal strut 詢問升級（v2 升級）— 從「保留策略」精準到「具體 mm 數」3 連問（≥ 12-15 mm + 女性是否調整 + columellar strut graft 補強）
- §00 前言：safety constraints 第 6 條 levothyroxine 從「待補」改為自查路徑 + 圍術期續用論述；新增第 7 條 PONV 高風險族群識別
- §00 Executive Summary：三句話核心結論升級為四句話（PONV 為新增第 1 條 Critical）
- §3.5 結論：補入 PONV 為「最容易被忽略的點」第 1 項

## [2026-04-29] (Agent 長期記憶系統研究 v2 ── CTO Review 修訂)

### Added
- `agent-memory-systems_橫縱分析報告_v2.pdf`（A4，1.4 MB，1563 行 markdown）
- §2.6 新增「Long Context + Prompt Cache」對照路線（強調閉源 API only、自部署開源模型 1M 落地可行性差、5 min cache TTL）
- §2.7 新增「Anthropic Memory tool + Claude Skills」（tool primitive vs service-layer 兩種設計哲學對比；四件套：Memory tool / Files API / CLAUDE.md / Skills）
- §2.8 新增「OpenAI Memory / ChatGPT Personalization」（市佔最大 memory layer、52.9% LongMemEval、developer-side 限制）
- §2.9 LangMem 從次主流升為獨立節（LangChain 生態 first-class memory；三類 modular API）
- §4.3 新增 LongMemEval / LoCoMo 自身 dataset bias 分析（對 coding / domain / 多 agent / 中文場景代表性弱）
- §7 重繪選型決策樹：兩層 gate（session 規模 + 部署環境）+ 三條主路徑；新增場景表 3 條（短歷史 / Claude 生態 / Self-host enterprise）
- §8 補入四條失敗模式：cost runaway / Long Context cache 失效成本 / GDPR-用戶刪除權 / hosted memory 資料主權風險
- §10 補入第 10-12 條能力限制：Karpathy-centric 取材偏誤聲明、Long Context 數字未實測、Anthropic Memory tool 規格演進
- `sources.md` 補 Model Provider 官方資源 12 條（Anthropic Memory tool / Files API / Skills / Prompt Caching / 1M Context；OpenAI Memory / Responses；Gemini Long Context / Caching；LangMem；Qwen2.5-1M / GLM-4-1M）
- §1.3 新增第四種解法（Long Context + Cache）；圖 1 重繪為四條路覆蓋圖
- §0 摘要新增「v2 修訂重點」、「三條對照路線」表、「兩條暗線（service-layer vs tool-primitive 張力 + 企業 self-host 限制）」

### Changed
- §3.4 中文場景從 13 行擴寫到 50+ 行：四層問題（embedding / NER / temporal / token cost）+ 五條台灣團隊工程建議
- §9.1 cognitive core 雛形主推改為 Anthropic Haiku 4.5 + Memory tool（Phi-3.5 / Llama 3.2 退為開源側佐證）
- §1.2 「Karpathy 多次強調的隱含項」改為具體標註出處（Dwarkesh podcast + X 推文）
- §2.4 MemPalace stars 數字統一為「48 hr 22K → 兩週 ~47K」（v1 §0 與 §2.4 數字不一致已修正）
- §2.11（原 §2.7）forgetting curve 公式加註「轉錄自 emergentmind 的整理筆記，並非標準 Ebbinghaus，Gompertz-like 形式建議以原論文為準」
- §2.10（原 §2.6）次主流框架表格移除 LangMem 條目（已升 §2.9）

## [2026-04-29] (Agent 長期記憶系統研究 v1)

### Added
- `reports/2026-04-agent-memory-systems/`：A 類一般主題研究第一版交付
  - `agent-memory-systems_橫縱分析報告.md`（27 頁、~52K 字元、含 9 張內嵌 SVG + 9 張表格）
  - `agent-memory-systems_橫縱分析報告.pdf`（A4，1.3 MB）
  - `sources.md`（30+ 來源，含 Karpathy 一手 / 官方 / 第三方 / 學術論文 / 批評 / 產業實踐五分類）
- 五大主流框架橫向對比：Mem0 / Zep+Graphiti / Letta(MemGPT) / MemPalace / Karpathy LLM Wiki
- Karpathy 三條觀點線穿插全文：anterograde amnesia + Decade of Agents（§1）/ LLM Wiki 編譯器路線（§2.5）/ Beyond RAG 之爭（§3.3）/ System Prompt Learning 第三範式（§5.2）/ Episodic→Semantic→In-Weights 三階段 consolidation（§5.4）/ Cognitive Core + Wiki→Fine-tune loop 應用想像（§9）
- `raw-materials/2026-04-agent-memory-systems/`：素材消化檔（Karpathy gist / Decade of Agents / Mem0 / Letta forum / MemPalace / Atlan landscape / 實作批評 / 認知架構 / Letta+MemGPT+Graphiti 架構共 9 份摘要）
- 9 張 SVG 視覺驗證通過（pdftoppm 高 DPI 確認文字未截斷、跨頁皆有 page-break-before 處理）

### Changed
- `README.md` Reports 索引新增 A 類「Agent 長期記憶系統」一筆

---

## [2026-04-28] (TSMC PI v4.6 — 製程/封裝應用點濃縮列點式)

### Changed
- `TSMC_v4_01_統一大表.md`：S+A+B 級 55 位 PI 的「製程/封裝應用點」欄從原本「[節點/段別]；[核心痛點]；TRL X」單行 ≤ 20 字格式，改為列點式 4 條 bullet（1 條節點段別 + 2 條核心痛點 / 量化效益 + 1 條 TRL/時程），將 Profile §3「製程/封裝應用點（詳述）」的 4-5 條痛點主軸 + 量化目標濃縮至大表，主管不必翻 Profile 即可掌握每位 PI 的具體應用方向；C 級 6 位（C56-C61）因無詳述 Profile 維持原單行格式
- `TSMC_v4_00_封面與執行摘要.md`：§九 §2 欄位描述追加 v4.6 列點式說明
- 大表頂部欄位說明 blockquote 同步更新格式定義

### Output
- 重新生成 `TSMC_PI_彙整大表_v4.6.pdf`（直向）+ `TSMC_PI_統一大表_橫式_v4.6.pdf`（A3 速查）

---

## [2026-04-27] (TSMC PI v4.5 fixed — Profile bullet 三層保留)

  - 解決了原本 Profile 中「建議合作方式」等區塊三層 bullet 被壓平成兩層，導致視覺過於密集（視覺牆壁）的問題。無需大幅修改 Markdown 原稿即可提升易讀性。

### Changed
- 重新生成 `TSMC_PI_彙整大表_v4.5_fixed.pdf` 等 PDF，應用修正後的清單排版。

---

# Changelog

All notable changes to the hv-research project.

Format: `## [YYYY-MM-DD]` with Added / Changed / Fixed / Removed subsections.

## [2026-04-27] (TSMC PI v4.5 — 大表欄位重整 13→11 欄)

### Changed
- `TSMC_v4_01_統一大表.md`：13 欄 → 11 欄，三項結構性變更：
  - **移除「落地程度」欄**：值（研究級 / 原型級 / 量產級）已隱含在 Profile 雙區塊的「可導入時程（TRL）」，大表不再重複
  - **「製程/封裝應用點」從第 8 欄前移至第 5 欄**（「代表實績」前），閱讀動線改善：校系 → 專長 → 應用點 → 實績
  - **欄內容精修**：
    - 「製程/封裝應用點」統一為「[節點/段別]；[核心痛點]；TRL X」格式（≤ 20 字）
    - 「建議合作方式」統一為「[主題目 A 短名]（[制度簡稱]）」格式（≤ 15 字），詳情連結至 Profile §3
- `TSMC_v4_00_封面與執行摘要.md`：§九報告結構 §2 欄數描述 13 → 11，標注 v4.5 欄位重整
- 欄位說明 blockquote 新增製程/封裝應用點與建議合作方式的格式定義

### Added
- `TSMC_PI_彙整大表_v4.5.pdf`（1185 KB，直向）
- `TSMC_PI_統一大表_橫式_v4.5.pdf`（534 KB，橫式）

### Removed
- v4.4 PDF 搬至 `archive/pdfs-old-versions/`

---

## [2026-04-27] (TSMC PI v4.4 — 雙區塊強化 61/61 全完成)

### Changed
- `TSMC_v4_03_統一Profile.md`：61 位教授全部升級雙區塊（製程/封裝應用點 5 軸 + 建議合作方式 6 軸）
  - S01-S15（Round 1）、A16-A30（Round 2）、B31-B55（Round 3）、C56-C61（Round 4）
  - 特殊狀態（借調 / 法務觀察 / 不啟動）均標注特殊定位，保留 v4.3 判斷脈絡
  - 檔案行數：1402 → 3177（+1775 行累計）
- PDF 重生待執行（TSMC_PI_彙整大表_v4.4.pdf + 橫式）

## [2026-04-27] (TSMC × 台灣學界 PI 盡職調查 v4.3 — 「建議合作方式」wording 雙 check)

### Added
- `reports/2026-04-tw-univ-semi-ai-professors/v4.3-final/TSMC_PI_彙整大表_v4.3.pdf`（872 KB，直向主檔）
- `reports/2026-04-tw-univ-semi-ai-professors/v4.3-final/TSMC_PI_統一大表_橫式_v4.3.pdf`（550 KB，A3 橫式）
- B47 李宏毅 Profile 補上完整跨域題目表（5 條，依橋接成本 + 對應目的軸排序）+ KPI 細項

### Changed
- **B47 李宏毅**（最大改動）：原「無半導體題目可接觸 / 無明確應用點 / 研究軌與半導體無交集」過於否定 → 重定位為**工程師效率軸方法論候補**（非主軸 PI），列出 5 條跨域題目：
  1. LLM-as-Evaluator SOP/ECN/FMEA 文件審查（首選 PoC，3-6 月最低橋接成本）
  2. 無塵室 hands-free LALM 語音操作
  3. 交班報告 ASR + LLM 結構化轉寫
  4. 自監督學習應用於設備聲學異常偵測
  5. TSMC 內部 AI 素養 / reskilling 課程共製
- **B53 陳正剛**：「方法論顧問池」→ Tier 2 顧問（依 Jakey Blue 案需求橋接 SPC/APC 方法論會診）
- **B54 謝旻甫**：「轉給 Fab 設施部門」→ 補上題目細節（馬達/風機 ML 預測維護 + chiller 節能調度）+ 軸定位（fab 設施軸非製程 AI 軸）
- **B55 洪英超**：「方法論顧問池」→ Granger 因果統計單次諮詢顧問（橋接 SPC 多變量根因分析）
- **C56 林清安**：「不建議進階」→ 機械視覺/手臂與 AMHS/封裝視覺定位有間接接點，候補位待主軸 PI 飽和再重評
- **C57 柏林 Berlin Chen**：補上與 B47 LALM 路徑競合說明（李宏毅優先）
- **C58 王振興**：「不建議；AIoT 邊緣另案」→ 補上員工穿戴監測另案軸定位
- **C60 鄭少為**：「理論 PoC 配套」→ 高維 GP/DoE 統計支援（非獨立 PI）
- **C61 李祈均**：「COI 需簽約後考慮」→ 補上員工關懷軸（情感語音 → 工程師壓力/疲勞偵測）+ 雙 COI 資訊牆要求
- 大表附註 §C ranking 微調說明（B47 條目）同步更新
- 執行摘要 §八不啟動池 B47 條目同步更新
- README.md：v4.2 → v4.3 路徑、PDF 主檔引用、archive 清單更新

### Removed
- v4.2 PDF 從 `v4.3-final/`（前 v4.2-final/）移至 `archive/pdfs-old-versions/`
- 資料夾 `v4.2-final/` 重命名為 `v4.3-final/`

---

## [2026-04-26] (Lean PCOS 膠原蛋白研究 v2 — 保澎潤框架重定位)

### Added
- `reports/2026-04-lean-pcos-collagen/lean-pcos-collagen_橫縱分析報告_v2.md`（1321 行，+200 行）
- `reports/2026-04-lean-pcos-collagen/lean-pcos-collagen_橫縱分析報告_v2.pdf`（1.41 MB）
- 新增 1 張 SVG 圖（圖 2「澎潤的四層解剖結構與口服膠原可介入性」）
- 新增 §2.1「澎潤的解剖學分層」核心章節 — 四層解剖：脂肪墊 60-70% / 真皮 20-25% / 表皮 10-15% / 骨架
- 新增 §6.6「保澎潤內服真正的對手：口服玻尿酸 HA」對照表 — HA RCT 證據比膠原直接
- 新增 §6.7「保澎潤醫美選項位階」對照表 — Sculptra / 玻尿酸填充 / Skinbooster / Polynucleotide / Rejuran
- 擴充 §6.8「替代方案綜合表」 — 加入 spironolactone、外用 retinoid、口服 HA 等 17 項
- 新增 §8.7「補膠原前該驗的檢驗清單」 — TSH/SHBG/HOMA-IR/25(OH)D/eGFR 等 7 項
- 重寫 §1 一句話定義 + 圖 1（從預算決策樹改為 P0-P3 階梯流程）
- 重寫 §5 PCOS 章框定（從 outcome 降為 safety constraint）
- §5.5 新增 lean phenotype 脂肪墊結構性劣勢段落
- 重寫 §7.4 三劇本（保澎潤框架 4 劇本，含「劇本 D 踩雷高糖膠原飲」）
- 重寫 §8.1 SOP（從 Tier 1-4 改為 P0-P3 整合外用 + 內服 + 醫美）
- 升級 §8.6 風險清單 — 加入「過度減重 → 脂肪墊流失」「孕期/備孕」「魚過敏」三項；oxalate 風險升級警示「5-10 g/日恰在文獻訊號劑量區」
- 增補 16 個 v2 新引用（oral HA RCT × 4、PN/Rejuran × 2、buccal fat 文獻 × 2、Ito 修正引用、CSA 反駁、isotretinoin/spironolactone 等）

### Fixed
- §5.3「Sugihara 2018」引用錯誤更正為「Ito, Seki, Ueda 2018（Marine Drugs）」 — 正確的 CPO + IGF-1 RCT 作者群
- §5.3 補強：純膠原 vs 複方（含 ornithine / arginine / glutamine）對 IGF-1 影響的差異說明

### Changed
- 圖 2-6 因新增 §2.1「圖 2 澎潤分層」而重新編號為圖 3-7
- 標題「25 歲 Lean PCOS 女性的膠原蛋白決策」 → 「25 歲 Lean PCOS 女性的保澎潤膠原蛋白決策（v2）」
- 領域標籤順序「女性內分泌 × 營養補充 × 美容皮膚」 → 「美容皮膚 × 女性內分泌 × 營養補充」
- 口服膠原從 v1「Tier 4 美容輔助」重新定位為 v2「P2 marginal play」
- §9 能力限制聲明從 4 項擴充為 6 項（加入「無 head-to-head HA vs 膠原 RCT」「醫美 cost-per-effect 缺長期資料」）

### Lessons
- 報告框架（PCOS outcome vs 美容 outcome）必須在 v1 開頭與使用者對齊；錯框會導致正確的醫學論述指向錯誤的決策建議
- 對 lean phenotype 個案做美容類研究時，「皮下脂肪墊」必須單獨成段討論 — 這是 lean 與 normal/obese 患者最大的解剖差異，但常被歸類在「BMI 影響」一帶而過
- 口服 HA 作為口服膠原的「真實對手」在台灣消費市場長期被低估；2023-2025 的 oral HA RCT 證據已穩定支持其作為「保水」首選

## [2026-04-26] (Lean PCOS 25 歲女性膠原蛋白決策研究 v1)

### Added
- `reports/2026-04-lean-pcos-collagen/lean-pcos-collagen_橫縱分析報告.md`
- `reports/2026-04-lean-pcos-collagen/lean-pcos-collagen_橫縱分析報告.pdf`（1.29 MB，23 頁）
- 6 張 SVG 示意圖：
  - 圖 1「決策樹 + 為什麼這個排序」（§一）
  - 圖 2「膠原補充品 270 年時間軸」（§3.5）
  - 圖 3「訊號路徑：口服到 fibroblast」（§4.4）
  - 圖 4「Lean vs Obese PCOS 病理對照」（§5.5）
  - 圖 5「12 款主流產品 PCOS 友善度排序」（§6.5）
  - 圖 6「12 週試補期評估時間軸」（§8.5）
- 縱向：1754 工業明膠 → 2025 Am J Med 資金偏差爭議；橫向：12 款台/日/歐美品牌 PCOS 友善度評分；交匯：lean PCOS + 痘痘 + 低 GI 三軸整合
- 與「痘痘外油內乾報告」「PCOS 低 GI 飲食報告」呼應整合

### Fixed
- `scripts/md_to_pdf.py` CSS 加 `svg { break-inside: avoid; page-break-inside: avoid; }`（雖 weasyprint SVG break 支援有限，仍補上以求嚴謹）

### Lessons
- WeasyPrint 對 SVG 的 `break-inside: avoid` 支援不完整 — 高度 ≥ 280px 的 SVG 若放在頁面下半，仍會被切割跨頁。穩定解法是在 SVG 之前手動加 `<div style="page-break-before: always; height: 0;"></div>`，並把圖內容壓縮到 ≤ 280px viewBox 高度

## [2026-04-26] (Agentic AI v3 — 補圖版：6 → 10 張 SVG)

### Added
- `reports/2026-04-agentic-ai-tech/最新_agentic_ai_技術細節與實現方式_橫縱分析報告_v3.md`
- `reports/2026-04-agentic-ai-tech/最新_agentic_ai_技術細節與實現方式_橫縱分析報告_v3.pdf`（1.30 MB）
- 新增 4 張 SVG（總圖數 6 → 10）：
  - 圖 3「三協議分層」（§3.5）— agent 三個外部接口的協議承擔與戰況色碼
  - 圖 5「Reasoning Loop 範式對比」（§3.7.1）— ReAct 三節點 vs Extended + Interleaved Thinking 雙面板對照
  - 圖 6「Agentic RL 範式對比」（§3.7.1.5）— RLHF 單步 MDP vs Agentic RL trajectory POMDP
  - 圖 9「四個 2026 真實威脅地圖」（§3.7.7）— 4 攻擊面 + 防禦標籤 quadrant 圖

### Changed
- 圖號重編：原 圖 3 / 4 / 5 / 6 → 圖 4 / 7 / 8 / 10（依章節先後順序）
- 標題與摘要更新為 v3，註明 10 張示意圖

### Fixed
- 圖 5 `auto re-plan` pill 寬度由 56 → 70px，避免文字溢出 pill 邊界
- 圖 9 Q2 / Q4 防禦文字（右側）改用 `text-anchor: end` + `defense-text-r` class，避免超出 SVG 寬度被裁切
- 圖 3 layer label 由 y=65 上移至 y=50（與 protocol pill 留 12px 緩衝），消除原 3px 垂直重疊

## [2026-04-26] (Agentic AI v2 — 評審修訂 + 6 張 SVG 示意圖)

### Added
- `reports/2026-04-agentic-ai-tech/最新_agentic_ai_技術細節與實現方式_橫縱分析報告_v2.md` — 大幅修訂版（從 960 行擴至 ~1100 行）
- `reports/2026-04-agentic-ai-tech/最新_agentic_ai_技術細節與實現方式_橫縱分析報告_v2.pdf`（1.26 MB）
- 新增 6 張 SVG 示意圖：五條演化線匯流（圖 1）、三陣營三協議格局（圖 2）、七層工程棧（圖 3）、Context Lifecycle（圖 4）、Multi-agent 四模式（圖 5）、三個未定賭注（圖 6）
- 新增 §2.4「Agent Skills 開放標準」（agentskills.io 2025-12 開源）+ 第三層協議完整化
- 新增 §3.7.1.5「Agentic RL 訓練範式革命」（ARTIST、Agent Lightning、Kimi K2.5、LiteResearcher）
- 新增 §4.5「訓練 vs Scaffold 派分歧」+ §4.6「三個未定的賭注」
- 新增 附錄 A「2026 Q2 Agent Stack 起手套件」三層

### Changed
- 修正 Opus 4.7 定價：v1 寫 $15+/M，正確為 **$5/M input、$25/M output**（與 4.6 同價，no long-context premium）
- 修正 Agentic Misalignment 研究時間：v1 標 2024，正確為 **2025-06**
- 補上 Claude Managed Agents（2026-04-08 發布）作為官方託管 runtime
- 擴展 Computer Use API 2026 Q1 變更：vision + a11y fallback、action batching（延遲 -60%）、Native Windows
- 擴展 Evals：補 SWE-Lancer / AgentBench-2 / LiveSWEBench 三個新世代 benchmark
- 擴展 §3.7.7 安全章節：從 3 威脅擴為 4 威脅（補 tool poisoning、memory poisoning、multi-agent collusion）

### Fixed
- 全 SVG `font: bold ...` 縮寫改為 `font-weight + font-size + font-family` 顯式三屬性，解決 WeasyPrint 不渲染粗體標題問題
- 修正 SVG 內 `&` 需轉義為 `&amp;` 才能通過 cairosvg / WeasyPrint XML parsing
- 圖 1 Lane 5（訓練）與 Lane 4（編排）節點重疊：節點重新分散
- 圖 3 L5 / L6 layer-name + layer-desc 過長超出 280px 框：精簡用 `·` 連接

### Lessons Learnt（追加 lessons.md）
- **WeasyPrint SVG 字型 quirk**：`font: bold 11px sans-serif` 縮寫不被 WeasyPrint 正確解析，導致粗體 `<text>` 元素完全不渲染。必須拆成 `font-weight: bold; font-size: 11px; font-family: sans-serif` 三個顯式屬性。cairosvg 本機渲染卻 OK，所以本機 PNG 預覽能看到、PDF 卻消失，極易漏抓
- **SVG 在 Markdown 內須 escape `&`**：`L3 Memory & Context` 會破壞 cairosvg/lxml XML parsing；改 `&amp;`。WeasyPrint 對寬鬆 HTML 容忍度較高但仍不應依賴
- **視覺驗證流程**：cairosvg 抽 SVG 預覽（檢測排版重疊）+ pdftoppm 抽 PDF 頁（檢測字型/中文渲染）兩步缺一不可——前者沒 CJK font 但版面準、後者中文準但無法 isolate SVG bug
- **SVG 箭頭 polygon apex 方向**：`<polygon points="x1,y1 x2,y2 x3,y3" />` 的 apex 看哪個點偏離其他兩點最遠的那個方向。例如 `points="180,75 170,70 170,80"` 三點中 (180,75) 是右側單獨一點、(170,70)/(170,80) 是左側兩點 → apex 在右、base 在左 → 箭頭指右。畫錯極易反向（v2 第一版圖 4 整批箭頭反向，因為原寫成「base 兩點在右」的順序）。**規則：apex 要朝目標、base 兩點 y 座標應對稱於 line 的 y 座標**
- **Event bus 視覺化**：用 dashed line 表達 bus 不直觀（讀者讀不出 pub/sub）；應畫成清晰的 pill 形 `<rect rx>` channel，所有 publisher/subscriber 用實線連接到 bus 上下緣。Enterprise integration patterns 的標準視覺化即如此
- **VS / 對抗徽章不要直接用大字**：28px 文字會佔 50px 寬，常溢出鄰近 box；改用直徑 24-26px 的圓 badge 配 11px 白色粗體文字，對比強且不溢界
- **AI 繪 SVG 三步驗證 SOP**：(1) 寫完先在 head 用 cairosvg 抽看排版（無中文 OK）→ (2) 改 PDF 後用 pdftoppm 200dpi 抽圖頁→ (3) 用 Read tool 視覺核驗 — 三步至少各做一次再交付

## [2026-04-24] (v4.0 — 統一大表 71 位 + Rubric v2.0 披露規則)

### Added
- `templates/scoring-rubric-v2.md` — 新版 5 維度評分標準；**維度 4 改漸進打分**（0-10）取代 v1 排除規則；新增「與外部公司合作狀況」專欄
- `reports/2026-04-tw-univ-semi-ai-professors/TSMC_v4_00_封面與執行摘要.md` — v4.0 關鍵變更、S 級 15 位摘要、第一波 8 位建議
- `reports/2026-04-tw-univ-semi-ai-professors/TSMC_v4_01_統一大表.md` — **71 位統一大表**（取代 Top 15 / Backup 二分）
- `reports/2026-04-tw-univ-semi-ai-professors/TSMC_v4_05_合作狀況披露附錄.md` — 🚩 12 位完整披露（A/B/C/D/E 5 池 + 決策矩陣）
- `reports/2026-04-tw-univ-semi-ai-professors/TSMC_v4_06_方法論與版本差異.md` — Rubric v2.0、v3.4→v4.0 差異表、題目軸覆蓋對比
- `reports/2026-04-tw-univ-semi-ai-professors/phase5-haiku-scan/` — **16 位 Haiku 快掃新增**（4 組並行）：
  - G1 NCKU（4 位）：游濟華 6.9 / 羅裕龍 6.8 / 劉禹辰 6.4 / 謝旻甫 5.6
  - G2 NYCU（4 位）：王蒞君 7.3 / 吳添立 6.9 🚩 / 郭浩中 6.9 🚩 / 陳柏宏 6.9
  - G3 NCU（4 位）：陳以錚 6.6 / 林錦德 6.15 / 杜長慶 5.75 / 鄭永斌 4.95 🚩
  - G4 技職/其他（4 位）：**楊哲化 8.1 ⭐⭐** / 陸元平 5.1 / 羅明琇 4.7 / 林清安 4.0
- `TSMC_PI_彙整大表_v4.0.pdf`（976 KB）— 單一交付 PDF

### Changed
- **取消 Top 15 / Backup 二分**：所有 71 位併入單一大表，依分數 S/A/B/C 四級
- **取消 E ❌ 剔除類**：張耀文、張孟凡、彭文志、水野潤、林勇志 5 位重新納入大表；合作狀況欄披露
- **取消 D 類媒體熱度獨立歸類**：依 5 維度加權降至 C 級
- **藍啓航 → 藍俊宏**（NTU 工工副教授正名；Jakey Blue）
- **高宏宇 NTHU 正教授 → NTHU 助理教授**（2024/8 從 NCKU 轉校後重建 Lab）
- **蔡佩璇 S → A**（降至 A 級；Fulbright 2024-2025 Pittsburgh 期間）
- **陳朝鈞移出主表**（勘誤：主軸實為豬隻飼養/ADAS）

### Lessons
- 漸進打分優於二元排除：決策權還給主管 + 狀況可動態追蹤
- 技職院校不應扣分：NTUT 楊哲化 8.1 S 是本 refactor 最大發現（3D 封裝雷射超音波）
- Haiku 跨組偏差：G2 NYCU 組 -0.3 校準必要

## [2026-04-24 earlier] (TSMC Top 15 v3.4 + Backup v1.4 — Phase 4 補強重排)

### Added
- `reports/2026-04-tw-univ-semi-ai-professors/` Phase 4 補強：14 位新 profile（10 完整 + 5 mini）+ 3 位 Top 15 退場移到 Backup
  - **NCKU IYM 三人組**：phase4-profile-cheng-fan-tien.md（鄭芳田，戰略顧問）/ phase4-profile-hsieh-yu-ming.md（謝昱銘，⭐ 進 Top 15）/ phase4-profile-tieng-hao.md（丁顥，C 類）
  - **NTHU IEEM 兩位**：張國浩（A 類首選遞補，7.8 分）/ 許嘉裕（A 類，6.5 分）
  - **NTU 補位兩位**：蔡坤諭（C 類，EUV/DFM 而非 Test）/ 陳亮嘉（⭐ 進 Top 15，8.9 分）
  - **技職院校四位**：范書愷（A+ 類，7.5）/ 郭鴻飛（A+ 類，7.5 / Mask AI 補位）/ 黃乾怡（B+，6.5）/ 曾釋鋒（B' 設備合作獨立，5.5）
  - **類別 B 五位 mini**：江蕙如（⭐ 進 Top 15，9.0）、李建模、李淑敏、陳朝鈞、蕭宏章
- `phase4-补强說明.md` — 補強動機 + 系統盲點根因 + 重排決策原則
- `TSMC_Top15_長期投資分析_v3.4.pdf`（832 KB） — Top 15 主名單 v3.4 重排，3 進 3 出
- `TSMC_Backup_備選候選名單_v1.4.pdf`（1017 KB） — Backup 擴至 55 位（v1.0 38 + Phase 4 14 + Top 15 退場 3）

### Changed
- Top 15 主名單 v3.3 → v3.4：嚴格按 5 維度評分，3 進 3 出
  - **進入**：江蕙如 9.0（NTU EE，AI-EDA 補張耀文空缺）/ 陳亮嘉 8.9（NTU 機械，光學量測補空白）/ 謝昱銘 8.3（NCKU IMIS，IYM 接班人）
  - **退出**：林嘉文 7.5（光刻 EDA 需 12 月 PoC）/ 蔡銘峰 7.0（RAG 軸退場）/ 黃瀚萱 7.0（CAG 同樣退場）
  - **邊際決策**：張國浩 7.8 vs 蔡佩璇 7.7 邊際 0.1 差，因張國浩 Powerchip + Micron Chair 🟡 待釐清，最終留任蔡佩璇
- 主管摘要：第一波從 6 位 → 8 位；NCKU IYM 學派叢一次串聯（謝昱銘執行 PI + 鄭芳田顧問 + 銀慶剛跨校）
- 5 年預算：v3.3 約 5,800-9,200 萬 → v3.4 約 7,300-11,600 萬（保守估計 5,000-8,000 萬）
- Backup 結構：v1.0 38 位 5 類 → v1.4 擴增 §1B Phase 4 補強 17 位 + §2B 個別內容 + §4 補強說明
- vault `lessons.md` 新增 4 條：系祖追溯法、跨校合作叢識別、技職院校 quota、Phase 1 標籤偏見再 4 條

### Fixed
- 重大盲點：v1.0 完全沒掃到 NCKU 製造資訊系系祖鄭芳田（IYM/AVM 創始人 + TSMC 終生合作對象）；v1.4 補上戰略顧問定位 + 弟子謝昱銘進 Top 15
- 主管原則嚴格遵守：「**不因主管點到名而上推 Top 15**」，依 5 維度校準後評分排序

## [2026-04-24]

### Added
- 新增 agentic AI 技術細節研究報告（reports/2026-04-agentic-ai-tech/）：四年演化縱向史 + 2026-04 橫向框架格局 + 七層技術實現深潛 + 橫縱交匯五組洞察。約 22000 中文字、PDF 1.4 MB、40+ 引用來源。

### Fixed
- **痘痘肌報告圖 5、圖 6 整張重畫**
  - **圖 5**：原本 8 節點圓周佈局 + 曲線/直線箭頭都不理想（線段太短、方向不直觀）。重畫成「4 上 4 下兩排閉環」— 上排生理鏈路（紅 1→2→3→4，左至右）、右側垂直箭頭（4→5）、下排混合鏈路（5→6→7→8，右至左；紅轉藍標示生理→行為轉場）、左側垂直箭頭（8→1 行為回饋上溯屏障），中央一顆「打破閉環 = 同時介入 3+ 節點」callout。
  - **圖 6**：原本 IGA 標籤飄在分支箭頭上造成重疊、虛線拖泥帶水、劇本 D 連接不清。重畫成三層決策樹 — 根節點（IGA 評估）→ 4 分支（白底小框內嵌 IGA 標籤蓋在箭頭線上，避免重疊）→ 劇本 A/B/C 匯流到「女性週期性？」問題 → 是/否分叉到劇本 D / 維持原劇本 → 匯流到「3 個月無效」鑑別診斷檢核。全圖用直線 + 精算多邊形箭頭端，所有連線都落在方框邊界上。
  - 已重新生成 PDF（1416.5 KB / 41 頁），圖 5、圖 6 分別位於第 33、34 頁。

## [2026-04-23]

### Added
- **新竹東區關埔/光埔購屋決策研究 v2 PDF**(912 KB / 51,775 字)— 基於一份審視意見書的補強版本,新增六個章節:
  - `§3.3` **平台均價差異解釋**(樂居/591/5168 差距的四個結構性原因)
  - `§5.5` **租金投報率與持有成本試算**(2~3 房毛投報 1.6~2.1%、跨區比較、房屋稅 2.0、管理費長期走勢)
  - `§5.6` **風險揭露**(土壤液化潛勢、淹水潛勢、嫌惡設施清查、耐震規格問題清單)
  - `§5.7` **學區設籍年限細則**(關埔國小 2 年設籍門檻、實務買房時程建議)
  - `§6` **v2 變更記錄**(透明交代補做什麼 / 未做什麼)
  - 附 v1 版本(843 KB / 41,050 字)作為對照
- **新竹東區關埔/光埔購屋決策研究 v1 PDF**(843 KB / 41,050 字)— 竹科工程師 2~3 房決策研究,涵蓋:
  - 縱向:從 2007 重劃起源 → 2018 悅揚/潤隆定調期 → 2020~2022 狂飆期 → 2023 平均地權 → 2024 第 7 波限貸 → 2025 量縮 42.2% → 2026 Q1 光埔二期整地 80%
  - 橫向:25+ 建商派系表 (T1 坤山/惠宇/國泰 / T2 富宇/春福 / T3 寶佳/興富發/昌益/豐邑) + 8 代表建案逐案拆解 (富宇天雋、竹科悅揚、竹科潤隆、富春居、豐邑相對論、國泰 TWIN PARK、興富發巨人愛家、遠雄文華匯) + 四區對比表(關埔/光埔二期/竹北高鐵/縣治三期)
  - 公設比解析(雨遮實坪制歷史根源 + 得房率換算 + 車位灌水陷阱)
  - 三劇本未來推演(續漲 35% / 盤整 45% / 鬆動 20%)
  - 購屋檢核清單:15 條避雷、議價框架、財務壓力測試表
- `reports/2026-04-hsinchu-east-guanpu-housing/sources.md` — 126 個引用來源分類清單
- `raw-materials/2026-04-hsinchu-east-guanpu-housing/研究筆記_縱向.md` / `研究筆記_橫向.md` — 三個並行聯網 agent 產出的原始研究素材(其中補充 agent 因 API 限流未完成,主執行緒自行補做學區/交通/醫療/台積電 A14 時程搜尋)
- **TSMC Top 15 教授投資分析 v3.2 PDF**（38 頁 / 692 KB）— 兩層結構：主管摘要 → 統一大表 → 個別教授三段細節（技術契合度 / 學生素養 / 合作分析）→ 附錄（策略/預算/法務/76 個 Reference URL）
- **TSMC 備選候選名單 v1.2 PDF**（23 頁 / 931 KB）— 38 位備選（A 差一點 4 / B 待觀察 6 / C 方向偏 3 / D 名氣大但未入選 20 / E 已失效 5）
- `phase3-verification-notes.md` — 16 位 WebSearch 平行驗證紀錄
- `templates/pi-due-diligence-framework.md` — PI 盡職調查 template（5 維度評分框架 v1.0）
- 附錄 E：每位教授 Reference URL（76 個公開連結）+ 能力限制聲明

### Changed
- 移除所有內部流程字樣（Phase 1/2/3、Batch A/B、Wave）— 主管版只有兩層結構
- 關鍵字矩陣表（20 欄）→ 改為每位教授 section 頂部「專長標籤列」（解決 PDF 寬表格切斷）
- Backup PDF 結構統一為 Top 15 式兩層（原四章四格式 confuse → 三章兩層式）
- CLAUDE.md 新增 PI 盡職調查工作流程 + 慣例（PDF 寬表格上限 / 必附 Reference URL / Companion 結構對齊）

### Fixed
- 彭文志從 Top 15 移除（已借調 TSMC 當處長，非合作候選；WebSearch 未能抓到）
- 王俊明 TSMC 綁定顧慮取消（SAT 中心為 TSMC 支持設立，體制內合作方 ≠ 離職自由身）

### Removed
- `TSMC_Top15_v3_04_關鍵字矩陣.md`（PDF 寬表格切斷問題）

## [2026-04-22]

### Added
- Phase 1-3 台灣 11 校半導體 AI 教授盤點完成
- Top 15 PDF v1 / v2
- `phase3-integrated-ranking.md`、`phase3-batch-a-llm-rag-candidates.md`、`phase3-batch-b-packaging-candidates.md`

### Changed
- Top 10 → Top 15 擴充（Batch A/B 各補 3 位）

## [2026-04-20]

### Added
- 專案初始化（CLAUDE.md / README.md / 目錄結構）
- 第一份研究：Claude Code 橫縱分析報告（13,860 中文字 / 1.1 MB PDF）
- `scripts/md_to_pdf.py`（weasyprint + markdown 工具）

## [2026-04-23]
### Added
- 新增研究報告：`reports/2026-04-acne-dehydrated-skincare/` — 痘痘肌 × 外油內乾 × 粉刺 × 內包痘的橫縱分析（縱向六階段認知史 + 橫向六大流派 + 化學成分／保養品／醫美／口服藥／內調五大治療類別 + 三個劇本推演）

## [2026-04-23] (補強版)
### Changed
- `reports/2026-04-acne-dehydrated-skincare/`：根據專業級審查意見大幅補強（7.38 → 預期 9+/10）
  - **新增 2.0 節**：IGA/GAGS/Leeds 嚴重度分級工具 + 8 種鑑別診斷（Malassezia folliculitis、Rosacea、Perioral Dermatitis、脂漏性皮膚炎、藥源性、機械性、髮蠟、Demodex）
  - **新增 H 類處方外用藥**：Dapsone gel、Minocycline foam、Epiduo/Epiduo Forte、Clindamycin 複方、Ivermectin、Ketoconazole
  - **大修 2.5 口服藥物**：補上 Metformin、Diane-35 / CPA、GLP-1（Semaglutide / Tirzepatide）、Bicalutamide、Flutamide、Finasteride、40:1 Myo+D-chiro-Inositol；Spironolactone 劑量修正為 50–200 mg/day，註明健康女性不必例行驗 K+；Isotretinoin 補上 ≥220 mg/kg 新證據、維持治療策略、IBD/情緒平衡論述
  - **新增 2.6 PCOS 合併痤瘡診療框架**：Rotterdam 2003 / 2023 指南、Phenotype A–D、完整檢驗套組（OGTT/DHEAS/17-OHP/SHBG/FAI/Vit D/Lipid/TSH/Prolactin/AMH）、鑑別診斷（NCCAH/Cushing's/甲狀腺/泌乳素瘤/雄激素腫瘤/Acromegaly）、Ferriman–Gallwey + Ludwig 臨床工具、四階治療階梯、子宮內膜保護
  - **新增 2.7 痘疤分型治療**：Ice Pick / Rolling / Boxcar / Hypertrophic 四種疤型對應表、痘印 PIH vs PIE 分治
  - **新增劇本 D**：女性 PCOS 型荷爾蒙痤瘡專屬治療方案（三角醫療 + 四階段 + 長期維持 + 子宮內膜保護）
  - **擴充結語**：8 條 → 10 條關鍵原則
  - **補充參考文獻**：2023 International PCOS Guideline、Endocrine Society Hirsutism 2018、Thiboutot JAAD 2023、Plovanich JAMA Derm 2015、Blasiak 2013、Coloe 2011
- 總字數：31,793 → 45,421（擴增 43%）
- PDF 大小：1.14 MB → 1.34 MB

## [2026-04-24]
### Added
- **新竹東區關埔/光埔購屋決策研究 v3 PDF**(1.19 MB / 77,510 字)— v2 基礎上加入 6 張 SVG 示意圖,讓一般讀者更快抓到關鍵觀念:
  - **圖 1 · 公設比 → 得房率**(§3.4):橫條並列 28%~40% 下的 40 坪室內實際大小
  - **圖 2 · 關埔房價歷時 2010~2026**(§2.7):折線 + 關鍵事件標註(Costco/悅揚/2nm/平均地權/第 7 波限貸)
  - **圖 3 · 四大竹科通勤區相對位置**(§3.7):以竹科為錨點的區位示意 + 價格梯度
  - **圖 4 · 戶數甜蜜點曲線**(§4.1):U 型曲線標出 <100 戶 / 200~400(甜蜜點) / 800+ 三區,點出悅揚/潤隆/相對論實際位置
  - **圖 5 · 未來 5 年三劇本樹**(§4.5):決策樹樣式,左側當前 → 中層分叉條件 → 右側 2030 結果
  - **圖 6 · 新竹建商派系金字塔**(§3.2):T1/T2/T3 三層 + 光埔二期進場名單對照
- `reports/2026-04-acne-dehydrated-skincare/`：加入 6 張 SVG 示意圖輔助理解
  - **圖 1 粉刺演化鏈**（Ch 1.2）：7 階段病灶演化 + 皮膚剖面 + 對應治療強度
  - **圖 2 皮膚屏障磚牆模型**（Ch 1.3）：健康 vs 受損屏障並排對比，解釋外油內乾物理基礎
  - **圖 3 月經週期 × 荷爾蒙 × 下顎痘痘**（Ch 2.6.1）：雌激素/黃體素/雄激素比曲線 + 濾泡/黃體期分區 + 下顎痘嚴重度色條
  - **圖 4 四種痘疤剖面形態**（Ch 2.7）：Ice Pick / Rolling / Boxcar / Hypertrophic 4 型並列剖面 + 治療對應
  - **圖 5 複合型膚質正回饋閉環**（Ch 3.2）：8 節點環形圖 + 中央「打破閉環」說明（取代舊 ASCII 圖）
  - **圖 6 治療決策樹**（Ch 3.3）：IGA 0-4 分級 → 劇本 A/B/C + 女性週期性 diamond → 劇本 D + 3 月無效 → 鑑別診斷回診
### Fixed
- `scripts/md_to_pdf.py`：加入 SVG 區塊抽出 / 重插邏輯，避免被 `nl2br` 擴充破壞（SVG 換行會被轉成 `<br>`，shapes 無法渲染）。同時去除 markdown 自動包上的 `<p>…</p>` 外殼。此修正對所有後續含 SVG 的報告皆有效。
- PDF 大小：1.34 MB → 1.41 MB；總頁數擴至 41 頁

## [2026-04-24] (圖 5/6 流程圖修正)
### Fixed
- `reports/2026-04-acne-dehydrated-skincare/` 圖 5/6 流程圖渲染問題
  - **圖 5 閉環圖**：WeasyPrint 的 SVG `<marker>` 渲染太細幾乎看不到箭頭；改用顯式 polygon 箭頭，並加粗主線（1.6 → 2.2）。節點 6 標籤「色沉 · PIE」修正為「色沉 · 紅斑」（PIE 是紅斑，色沉是 PIH，兩者並列才正確）。
  - **圖 6 決策樹**：4 個主要問題全部修正：
    1. Root → 4 分支線原本無箭頭 → 加上顯式 polygon 箭頭
    2. IGA 0–1/2/3/4 標籤原本壓在分支線上 → 改用獨立色塊容器
    3. IGA 2/3/4 到 diamond 的虛線原本懸空 → 改為 L 形折線實連到 diamond 頂點
    4. 「3 個月無效」底部盒子原本完全斷開 → 加上橘色垂直連線 + 箭頭
  - 新增底部 takeaway 總結線


## [2026-04-30]
### Added
- `reports/2026-04-septoplasty-lean-pcos/`：鼻中膈手術全圖研究（D 類個人健康，B+C 框架）
  - 術前後最佳化 + 加購膠原蛋白評估
  - 個人化基於 lean PCOS（BMI 19-21, phenotype B）+ 25 歲女性 + 計畫備孕 + 現有補品清單（魚油/葉黃素/合利他命/藍莓精華/表飛鳴）
  - 7 章分檔結構：00 前言 + 01 術式與彎曲解析 + 02 後遺症風險全圖 + 03 術前準備 + 04 術中與加購評估 + 05 術後恢復 + 06 新竹資源與決策清單
  - 3 張 SVG 示意圖：加購膠原決策樹、圍術期補品時間軸、PCOS 風險加成圖
  - 40 頁 PDF（1.5 MB）
