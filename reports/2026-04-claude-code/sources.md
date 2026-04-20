# Sources — Claude Code 橫縱分析報告

研究時間：2026-04-20 ~ 2026-04-21
訪問日期：同上（除特別標註）

## 本地素材（Claude Code v2.1.88 逆向分析）

- 位置：`~/vault/projects/claude-code-sourcemap_v2.1.88/`
- 結構：chapters/ 15 章 + diagrams/ 38 張 SVG + writing-best-practices.md
- 來源說明：基於 npm 套件 `@anthropic-ai/claude-code` v2.1.88 的 source map 逆向還原。source map 在 2026-03-31 因 `.npmignore` 配置錯誤被意外公開發布，內含 1,884 個 TS/TSX 檔案、37 個頂層目錄

## 一手來源（Anthropic 官方）

### 產品/模型發布新聞
- https://www.anthropic.com/news/model-context-protocol
- https://www.anthropic.com/news/claude-3-7-sonnet
- https://www.anthropic.com/news/claude-4
- https://www.anthropic.com/news/Introducing-code-with-claude
- https://www.anthropic.com/news/claude-opus-4-1
- https://www.anthropic.com/news/claude-sonnet-4-5
- https://www.anthropic.com/news/enabling-claude-code-to-work-more-autonomously
- https://www.anthropic.com/news/claude-opus-4-5
- https://www.anthropic.com/news/claude-code-on-the-web
- https://www.anthropic.com/news/updates-to-our-consumer-terms

### Engineering 部落格
- https://www.anthropic.com/engineering/building-agents-with-the-claude-agent-sdk
- https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

### Claude.com 部落格（2026 年之後官方改用此網址）
- https://claude.com/blog/1m-context-ga
- https://claude.com/blog/claude-code-desktop-redesign
- https://claude.com/skills
- https://claude.com/product/claude-code

### 官方文檔
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/checkpointing
- https://code.claude.com/docs/en/scheduled-tasks
- https://code.claude.com/docs/en/discover-plugins
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/vs-code
- https://code.claude.com/docs/en/desktop
- https://support.claude.com/en/articles/12138966-release-notes
- https://github.com/anthropics/claude-code/releases
- https://www.npmjs.com/package/@anthropic-ai/claude-code

### 官方 Plugin Marketplace
- https://github.com/anthropics/claude-plugins-official

## 一手近一手：深度訪談

- https://newsletter.pragmaticengineer.com/p/how-claude-code-is-built
- https://newsletter.pragmaticengineer.com/p/building-claude-code-with-boris-cherny
- https://newsletter.pragmaticengineer.com/p/dhhs-new-way-of-writing-code
- https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens
- https://www.developing.dev/p/boris-cherny-creator-of-claude-code
- https://stationf.co/news/boris-cherny
- https://every.to/podcast/how-to-use-claude-code-like-the-people-who-built-it
- https://sidb.io/about

## 一手近一手：Simon Willison（值得單列，因為他是最早期、最深度的外部觀察者）

- https://simonwillison.net/2025/May/22/code-with-claude-live-blog/
- https://simonwillison.net/2025/Oct/16/claude-skills/
- https://simonwillison.net/2025/Oct/20/claude-code-for-web/
- https://simonwillison.net/2025/Nov/24/claude-opus/
- https://simonwillison.net/2025/Mar/19/vibe-coding/
- https://simonwillison.net/tags/claude-code/

## 社群推文（X / Threads）

- https://x.com/AnthropicAI/status/1894092430560965029 — Claude 3.7 Sonnet + Claude Code 發布
- https://x.com/AnthropicAI/status/1925591505332576377 — Opus 4 + Sonnet 4 發布
- https://www.threads.com/@boris_cherny/post/DTOyRyBD018/ — Boris Cherny v2.1.0 公告
- https://x.com/karpathy/status/1886192184808149383 — vibe coding 原文
- https://x.com/karpathy/status/2015883857489522876 — Karpathy 80% agent coding
- https://x.com/swyx/status/2016258918297829719 — swyx Claude Cowork

## 產業媒體

### 商業與模型發布
- https://techcrunch.com/2025/04/09/anthropic-rolls-out-a-200-per-month-claude-subscription/
- https://techcrunch.com/2025/07/28/anthropic-unveils-new-rate-limits-to-curb-claude-code-power-users/
- https://techcrunch.com/2025/09/29/anthropic-launches-claude-sonnet-4-5-its-best-ai-model-for-coding/
- https://techcrunch.com/2025/10/20/anthropic-brings-claude-code-to-the-web/
- https://techcrunch.com/2025/06/05/cursors-anysphere-nabs-9-9b-valuation-soars-past-500m-arr/
- https://techcrunch.com/2025/08/01/more-details-emerge-on-how-windsurfs-vcs-and-founders-got-paid-from-the-google-deal/
- https://www.cnbc.com/2025/11/13/cursor-ai-startup-funding-round-valuation.html
- https://www.cnbc.com/2026/02/05/anthropic-claude-opus-4-6-vibe-working.html
- https://www.bloomberg.com/news/articles/2025-04-09/anthropic-to-offer-200-monthly-claude-chatbot-subscription
- https://finance.yahoo.com/news/anthropic-arr-surges-19-billion-151028403.html
- https://www.saastr.com/anthropic-just-hit-14-billion-in-arr-up-from-1-billion-just-14-months-ago/
- https://www.stormy.ai/blog/claude-code-gtm-strategy-anthropic-revenue-2026

### 深度報導
- https://www.infoq.com/news/2024/12/anthropic-model-context-protocol/
- https://www.infoq.com/news/2025/06/claude-code-sdk/
- https://www.infoq.com/news/2025/10/anthropic-claude-code/
- https://venturebeat.com/orchestration/claude-code-2-1-0-arrives-with-smoother-workflows-and-smarter-agents
- https://venturebeat.com/orchestration/we-tested-anthropics-redesigned-claude-code-desktop-app-and-routines-heres-what-enterprises-should-know
- https://www.macrumors.com/2026/04/15/anthropic-rebuilds-claude-code-desktop-app/
- https://sdtimes.com/ai/anthropic-releases-claude-3-7-sonnet-and-claude-code/
- https://winbuzzer.com/2026/03/09/anthropic-claude-code-cron-scheduling-background-worker-loop-xcxwbn/
- https://www.constellationr.com/insights/news/anthropics-claude-code-revenue-doubled-jan-1
- https://tech-insider.org/cursor-60-billion-valuation-anysphere-ai-coding-2026/
- https://thenextweb.com/news/cursor-anysphere-2-billion-funding-50-billion-valuation-ai-coding
- https://fortune.com/2025/06/03/openai-deepmind-anthropic-loosing-engineers-ai-talent-war/
- https://www.semafor.com/article/02/11/2026/anthropic-safety-researcher-quits-warning-world-is-in-peril
- https://www.cnn.com/2026/02/11/business/openai-anthropic-departures-nightcap

## 競品分析

### Cursor
- https://www.builder.io/blog/cursor-vs-claude-code
- https://www.56kode.com/posts/moving-from-cursor-to-claude-code/
- https://forum.cursor.com/t/stick-with-cursor-or-switch-to-claude-code/156673

### Cline
- https://vibecoding.app/blog/cline-review-2026
- https://github.com/cline/cline/issues/9174
- https://devtoolsreview.com/reviews/cline-review/
- https://cline.bot/blog/cline-raises-32m-series-a-and-seed-funding-building-the-open-source-ai-coding-agent-that-enterprises-trust
- https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev
- https://www.latent.space/p/cline

### Aider
- https://aider.chat/HISTORY.html
- https://aider.chat/2024/09/26/architect.html
- https://aider.chat/docs/leaderboards/edit.html
- https://aider.chat/2025/01/24/r1-sonnet.html
- https://www.morphllm.com/comparisons/morph-vs-aider-diff

### Codex CLI
- https://developers.openai.com/codex/cli
- https://developers.openai.com/codex/changelog
- https://www.infoq.com/news/2025/06/codex-cli-rust-native-rewrite/
- https://simonwillison.net/2025/Nov/9/gpt-5-codex-mini/
- https://smartscope.blog/en/generative-ai/chatgpt/codex-vs-claude-code-2026-benchmark/
- https://openai.com/index/introducing-upgrades-to-codex/
- https://www.gradually.ai/en/codex-statistics/
- https://blakecrosley.com/blog/codex-vs-claude-code-2026

### Gemini CLI
- https://blog.google/technology/developers/introducing-gemini-cli-open-source-ai-agent/
- https://github.com/google-gemini/gemini-cli
- https://developers.googleblog.com/plan-mode-now-available-in-gemini-cli/
- https://developers.googleblog.com/conductor-update-introducing-automated-reviews/
- https://github.com/google-gemini/gemini-cli/issues/5582
- https://github.com/google-gemini/gemini-cli/issues/14754
- https://yakhil25.medium.com/the-gemini-hallucination-crisis-how-google-antigravity-is-destroying-developer-trust-55d0773302f1

### 次要競品
- https://elephas.app/blog/windsurf-ai-3-billion-collapse-72-hours
- https://www.builder.io/blog/zed-ai-2026
- https://vibecoding.app/blog/junie-review
- https://github.blog/changelog/2026-02-25-github-copilot-cli-is-now-generally-available/
- https://smartscope.blog/en/generative-ai/github-copilot/github-copilot-cli-practical-guide-2026/
- https://www.warp.dev/
- https://ampcode.com/
- https://github.com/continuedev/continue
- https://www.augmentcode.com/tools/best-devin-alternatives
- https://hackceleration.com/replit-review/

## 社群生態

- https://github.com/obra/superpowers
- https://github.com/obra/superpowers-marketplace
- https://github.com/forrestchang/andrej-karpathy-skills
- https://github.com/affaan-m/everything-claude-code
- https://github.com/hesreallyhim/awesome-claude-code
- https://github.com/jqueryscript/awesome-claude-code
- https://github.com/travisvn/awesome-claude-skills
- https://github.com/ComposioHQ/awesome-claude-skills
- https://github.com/ComposioHQ/awesome-claude-plugins
- https://github.com/VoltAgent/awesome-claude-code-subagents
- https://github.com/rohitg00/awesome-claude-code-toolkit
- https://claudemarketplaces.com/
- https://buildwithclaude.com/
- https://awesome-skills.com/
- https://blog.fsck.com/2025/10/09/superpowers/

## Reddit / HN / 用戶情緒分析

- https://www.aiengineering.report/p/claude-code-vs-codex-sentiment-analysis-reddit
- https://www.aitooldiscovery.com/guides/claude-code-reddit
- https://www.arsturn.com/blog/top-claude-code-alternatives-according-to-reddit-users
- https://chandlernguyen.com/blog/2026/03/31/dropping-my-200-claude-code-plan-after-two-weeks-with-codex/
- https://www.ksred.com/why-im-back-using-cursor-and-why-their-cli-changes-everything/
- https://news.ycombinator.com/item?id=47505768
- https://news.ycombinator.com/item?id=47609294
- https://news.ycombinator.com/item?id=47586778
- https://news.ycombinator.com/item?id=47772282
- https://news.ycombinator.com/item?id=45416228
- https://news.ycombinator.com/item?id=44713757

## GitHub Issues（Claude Code 倉庫）

- https://github.com/anthropics/claude-code/issues/9424
- https://github.com/anthropics/claude-code/issues/11810
- https://github.com/anthropics/claude-code/issues/19567
- https://github.com/anthropics/claude-code/issues/3274
- https://github.com/anthropics/claude-code/issues/4878
- https://github.com/anthropics/claude-code/issues/6004
- https://github.com/anthropics/claude-code/issues/44683
- https://github.com/anthropics/claude-code/issues/19468
- https://github.com/anthropics/claude-code/issues/42796
- https://github.com/anthropics/claude-code/issues/49244

## 源碼洩漏與安全事件

- https://www.securityweek.com/critical-vulnerability-in-claude-code-emerges-days-after-source-leak/
- https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak
- https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/
- https://thehackernews.com/2026/04/claude-code-tleaked-via-npm-packaging.html
- https://layer5.io/blog/engineering/the-claude-code-source-leak-512000-lines-a-missing-npmignore-and-the-fastest-growing-repo-in-github-history/
- https://fortune.com/2026/03/31/anthropic-source-code-claude-code-data-leak-second-security-lapse-days-after-accidentally-revealing-mythos/
- https://cybernews.com/tech/claude-code-leak-spawns-fastest-github-repo/
- https://www.theregister.com/2026/04/02/trojanized_claude_code_leak_github/
- https://socradar.io/blog/mexican-government-breach-claude-chatgpt/
- https://www.trendmicro.com/en_us/research/26/d/weaponizing-trust-claude-code-lures-and-github-release-payloads.html
- https://www.straiker.ai/blog/claude-code-source-leak-with-great-agency-comes-great-responsibility

## 企業案例

- https://claude.com/customers/stripe
- https://claude.com/customers/shopify

## 黑客松

- https://cerebralvalley.ai/e/claude-code-hackathon
- https://www.adwaitx.com/claude-code-hackathon-opus-4-6/
- https://blockchain.news/ainews/claude-code-hackathon-returns-for-opus-4-7-100k-api-credits-developer-access-and-2026-trends-analysis

## Vibe Coding 文化分析

- https://en.wikipedia.org/wiki/Vibe_coding
- https://thenewstack.io/vibe-coding-is-passe/
- https://www.slashgear.com/2136931/vibe-coding-downsides-problems-grow-open-source/

## Wikipedia / 參考百科

- https://en.wikipedia.org/wiki/Claude_(language_model)
- https://en.wikipedia.org/wiki/Model_Context_Protocol

## 搜尋補充資料（關鍵詞式確認）

- Pixelmojo: https://www.pixelmojo.io/blogs/claude-code-hooks-production-quality-ci-cd-patterns
- ClaudeLog: https://claudelog.com/faqs/claude-code-release-notes/、https://claudelog.com/mechanics/task-agent-tools/
- Medium 教學與評論（散見於各章節引用，如 Plugin Beta 公告、Haiku 4.5 review）

---

## 未能驗證 / 誠實標註

以下資訊在報告中有使用，但未找到可直接引用的一手 URL：

1. **Hooks 初版的確切發布日**（2025 年 6 月，日未確定）
2. **Claude Code v1.0.0 的確切 npm publish 日期**（推測 2025-05-22 或前後一天）
3. **Claude Code v2.1.0 的確切發布日**（Boris Cherny 在 Threads 的公告未標日期）
4. **CronCreate 的確切發布日**（僅定位到 2026 年 3 月初）
5. **Plugin Marketplace 101 個 plugin 的精確時間**（僅知到 2026 年 3 月）

在報告中對應位置已用「（確切日期未見於 Anthropic 的一手 release note）」或「（2026 年 X 月 / Q1）」的方式標註。
