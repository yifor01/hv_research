# 用戶資訊

本資料夾儲存使用者的長期持續性個人資料，作為任何研究（hv-analysis、khazix-writer、PI 盡職調查等）的預設背景脈絡。

## 用途

當使用者發起新研究主題時，研究框架應先檢查本資料夾，確認是否有與該主題相關的個人背景需要納入考量。例如：

- 健康類研究 → 讀 `health.md` 了解既有健康狀況、過敏、用藥、體質限制
- 產品 / 補充品決策 → 讀 `health.md` + `profile.md` 了解預算範圍、生活型態、地理可購性
- 飲食 / 美容 / 運動類研究 → 讀 `health.md` 了解 PCOS / 痘痘 / lean phenotype 等核心約束
- 投資 / 職涯類研究 → 讀 `profile.md` 了解職業背景、地區、家庭狀況

## 檔案結構

```
用戶資訊/
├── README.md          # 本檔案
├── profile.md         # 個人基本資料（年齡、性別、地區、職業）
└── health.md          # 健康狀況（PCOS / 痘痘 / 體質 / 飲食框架）
```

## 維護規則

- 重大健康狀況變化（驗血結果、新診斷、停藥）→ 更新 `health.md`，註記日期
- 研究品味偏好變化 → 在對應主題的 README.md 內補充
- 個人資料如有調整（搬遷、職涯轉換）→ 更新 `profile.md`，註記日期
- 過時資訊（如已不再執行的飲食框架、已停用的補充品）→ 移到「歷史」段落，保留時間戳，不刪除（留下決策軌跡）

## 既有研究關聯

- `reports/2026-04-tsmc-pcos-low-gi-diet/` — 低 GI 飲食研究，框架基於 `health.md` PCOS 條目
- `reports/2026-04-acne-dehydrated-skincare/` — 痘痘 / 外油內乾研究，框架基於 `health.md` 痘痘條目
- `reports/2026-04-lean-pcos-collagen/` — 膠原 / 保澎潤研究 v1+v2，框架基於 `health.md` lean phenotype 條目
