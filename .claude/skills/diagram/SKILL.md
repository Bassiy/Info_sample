---
name: diagram
description: >
  会話・テキスト・knowledge/ の内容からMermaid図を生成・表示・保存するスキル。
  「図にして」「mermaidで書いて」「可視化して」「ダイアグラムにして」など図の生成を求められたときに使う。
  /study や /learn の会話中でも積極的に使う。生成した図は関連する knowledge/concepts/ ファイルに追記する。
---

会話の内容からMermaid図を生成し、VS Codeのプレビューで表示しながら、関連する `knowledge/concepts/` ファイルに追記する。

## プレビューファイル

`.claude/skills/diagram/scripts/preview.md` を固定ファイルとして使う。
リポジトリ内に置くことでGitHubのMermaidレンダリングでも確認できる。
Write ツールで直接上書きすればVS Codeのプレビューが自動更新される。

ファイルのフォーマット：
```markdown
# Diagram Preview

```mermaid
...
```
```

## 手順

### 1. Mermaidコードを生成する

Mermaidのデフォルトスタイルのみ使う。`style` による色指定は行わない。
ノード内の改行は `\n` ではなく `<br/>` を使う。
技術仕様・注釈などの補足情報は矢印ラベル（`-->|テキスト|`）に含めず、別途Noteノードを作成して `-.-` の点線で接続する。
補足Noteノードの形状は `("テキスト")` （角丸）＋点線ボーダーを使う。メインノードの `["テキスト"]`（四角・実線）と視覚的に区別するため。
点線ボーダーは `classDef` で定義し、各Noteノードに適用する：
```
classDef note stroke-dasharray: 5 5
class NoteA,NoteB note
```

図の種類の選び方：
- フロー・手順・依存関係 → `graph TD` / `graph LR`
- クラス・モジュール構造 → `classDiagram`
- 時系列・シーケンス → `sequenceDiagram`
- 状態遷移 → `stateDiagram-v2`

### 2. プレビューファイルを更新する

`.claude/skills/diagram/scripts/preview.md` を Write で上書きする。
VS Codeで開いていれば `Cmd+Shift+V` でプレビューが確認できる。GitHubでもMermaidがレンダリングされる。

### 3. 関連する knowledge/concepts/ ファイルに追記する

図の内容に関連する概念ファイルを特定して Mermaidブロックを追記する。

**対象ファイルの判断：**
- 会話の文脈やトピックから関連概念を推定する
- `knowledge/concepts/` に既存ファイルがあれば追記、なければ `/learn` で作成を提案する
- 追記先が複数候補あればユーザーに確認する

**追記フォーマット：**
```markdown
## 構成図

<!-- {出典・日付} -->
```mermaid
...
```
```

既存の `## 構成図` セクションがあれば図を差し替え、なければ末尾に追加する。
