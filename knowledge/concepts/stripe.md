# Stripe

## 概要
決済処理をAPIで実装できるSaaS。クレカ管理・定期課金・Webhook通知・不正検知をまるごと肩代わりしてくれる決済インフラ。

## 理解したこと
- Payment IntentでAPIから1回払い、Subscriptionで定期課金を管理できる
- 決済イベント（成功・失敗・解約など）はWebhookでサーバーに通知される
  - `payment_succeeded` → DBのフラグをアクティブに
  - `subscription_canceled` → アクセス権を剥奪
- カスタマーポータルを有効化すると、ユーザーが自分でプラン変更・解約できるUIが数行で完成
  → サポート対応が不要になる（個人SaaS開発者に特に有効）
- PCI DSS準拠・3Dセキュア・クレカ番号の安全管理をStripe側が担うため自前実装が不要
- 国内カード決済の手数料は3.6%
- 個人開発の鉄板スタック：Stripe + Supabase + Vercel

## 関連概念
- cloud_infrastructure

## ソース
- 2026-03-16・https://zenn.dev/nnze/articles/e3f648e335a947

## タグ
決済, SaaS, API, Webhook, サブスク, Stripe, 個人開発
