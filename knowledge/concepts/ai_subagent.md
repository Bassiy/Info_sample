# AI Subagent

## 概要
親エージェントが別のエージェントを起動して仕事を並列で投げる仕組み。

## 理解したこと
- 通常のAIは「聞いたら答える」だけだが、Agentはツールを使いながら自律的にタスクを完遂する
- Subagentは親エージェントが起動する「別の独立したエージェントインスタンス」
- 並列で同時に動かせるため、専門を分けて速く・深くできる
- スキルとの違い：
  - スキル = 「マニュアル」。同じエージェントの動き方を変える知識・手順書
  - Subagent = 「別の人を雇う」。独立したコンテキストで同時並行に動く
- 典型的な構成：スキルでフロー開始 → Subagentを呼び出し → 各Subagentに特化スキルを持たせる → 並列処理
- Subagentの定義・設定ファイルは不要。「並列でSubagentを起動して」と書けばClaudeが自動でやる

### Agent Teams パターン（Claude Code実践）
- 調査フェーズ（Plan Mode）と実装フェーズを明確に分ける
  - Plan Mode = ファイル編集なし・読み取り専用。安全に並行調査できる
  - 実装フェーズ = implementer + reviewer のペアで品質を担保
- 調査エージェントの役割分担例：
  - docs-searcher：ドキュメントを横断検索
  - flow-diagram-generator：フロー図を生成
  - db-structure-analyzer：DBスキーマを解析
- 不明点は `AskUserQuestion` でユーザーに確認させる → 変な方向に暴走しなくなる
- 1エージェントに全情報を渡すとコンテキスト爆発して性能劣化する。役割分担が根本的な解決策

## 関連概念
- harness_engineering
- pull_request
- claude_code_context_management

## ソース
- 2026-03-05・https://zenn.dev/mgdx_blog/articles/8f7994ad84151d
- 2026-03-19・https://zenn.dev/n314/articles/e06f189f093902

## タグ
AI, エージェント, Claude Code, 並列処理, スキル, Agent Teams, Plan Mode
