# 状態（State）と性質（Property）

## 概要
状態は時間とともに変化しうるもの、性質は対象に紐づく不変なもの。関数設計では混在させないことが重要。

## 理解したこと
- **性質**：生まれついての属性。時間が経っても変わらない（例：ファイル形式、商品の年齢制限）
- **状態**：今この瞬間どうなっているか。変わりうる（例：アップロード完了か否か、在庫があるか）
- 状態と性質が混在した関数はバグ調査の範囲が広がる
- 「操作の可否」は状態と性質の合成結果であることが多い
- 1つの関数が扱う責任は1種類にする（SRP）：状態を扱う関数は状態だけ、性質を扱う関数は性質だけ
- 両方必要なときはそれぞれの関数を組み合わせる

```python
# 分けた設計
def is_supported_type(file_type): ...   # 性質
def is_upload_complete(state): ...      # 状態

def can_convert(file_type, state):
    return is_supported_type(file_type) and is_upload_complete(state)
```

- 性質だけを扱う関数は純粋関数に近くなり、テストしやすい
- 機能追加のたびに状態が引数に紛れ込むのが混在の典型パターン

## 関連概念
- solid_principles.md（SRP：単一責任の原則）
- dependency_inversion.md

## ソース
- 2026-03-06・Zenn「状態と性質を区別して考える」
  https://zenn.dev/knowledgework/articles/95f30cfd155b5d

## タグ
設計, 状態管理, 純粋関数, 単一責任, ソフトウェア設計
