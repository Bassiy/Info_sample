# DDD（ドメイン駆動設計）

## 概要
ビジネスの言葉と構造をそのままコードに反映させる設計思想。

## 理解したこと

- ビジネス用語とコードの乖離が複雑化の根本原因。DDDはそれを解消する
- 「注文をキャンセルする」という業務言語がそのままメソッド名になる

### 層構成
```
Presentation層（画面・API）
Application層（UseCase）← 業務シナリオをオーケストレート
Domain層（集約・Repository I/F）← ビジネスルールの核心
Infrastructure層（DB・外部API）← Repository実装・SQL
```

### 集約（Aggregate）
- 「一緒に変更される単位」をまとめたもの
- ビジネスルールを集約の内部に閉じ込める（例：`order.cancel()`）
- Repositoryは集約単位でしか操作できない

### Repositoryの制約
- 集約をまたいだJOINができない
- 複数集約にまたがるデータ取得はN+1問題が発生する
- → 横断的な読み取りにはQueryServiceを使う（CQRSと組み合わせる）

## 関連概念
- cqrs.md（読み取りの限界をCQRSで補う）
- solid_principles.md（DIPがRepository設計の基盤）
- dependency_inversion.md（Repository I/FをDomain層に置く理由）
- separation_of_concerns.md

## ソース
- 2026-03-17・https://zenn.dev/135yshr/articles/9e3ec9a7d52c98
- 2026-03-11・sources/tech/2026-03-11.md

## タグ
DDD, ドメイン駆動設計, 集約, Repository, アーキテクチャ, 設計パターン
