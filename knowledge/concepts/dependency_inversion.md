# 依存性逆転の原則（DIP）

## 概要
具体的な実装に直接依存するな、間に抽象（インタフェース）を挟め。「差し替えできる設計にする」原則。

## 理解したこと
- 上位のコードが下位の詳細を知らなくていい状態にする
- 具体的な実装（メール送信・LINE送信など）に直接依存すると、変更のたびに上位コードを書き換えないといけない
- 抽象（インタフェース）を間に挟むことで、実装を外から差し替え可能になる

```python
# ❌ 違反：OrderServiceがEmailNotifierの具体に依存
class OrderService:
    def complete_order(self, order):
        email = EmailNotifier()
        email.send("注文完了しました")

# ✅ DIP：抽象(Notifier)に依存、実装は外から注入
class OrderService:
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    def complete_order(self, order):
        self.notifier.send("注文完了しました")

# メールでもLINEでも差し替えられる
service = OrderService(EmailNotifier())
service = OrderService(LineNotifier())
```

- 依存関係の図：`上位 → 抽象 ← 具体実装A / 具体実装B`
- テスト時に本物の代わりに「送ったふり」をする偽物（モック）を差し込める
- SOLIDの中で最初はイメージしにくいが「差し替えできる設計」と覚えればOK

## 関連概念
- solid_principles.md（SOLID原則の全体像）
- state_vs_property.md

## ソース
- 2026-03-06・会話から

## タグ
設計原則, DIP, SOLID, 依存性注入, モック, インタフェース
