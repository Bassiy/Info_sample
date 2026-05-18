# Claude Code Hooks

## 概要
Claude Codeが特定の操作をしたタイミングで、自動でシェルスクリプトを実行する仕組み。

## 理解したこと
- 設定はCLAUDE.mdではなく `.claude/settings.json` に書く
- スクリプト本体は `.claude/hooks/*.sh` に置くのが慣習
- タイミングは4種類:
  - PreToolUse: 操作の前（危険なコマンドをブロックするなど）
  - PostToolUse: 操作の後（Linter自動実行など）
  - Stop: 終了しようとする前（テストが通らなければ止めるなど）
  - PreCompact: コンテキスト圧縮前（重要情報を逃がさない）
- PostToolUse Hookでエラーをエージェントに返すと、エージェントが次のアクションで自分で修正する（自己修正ループ）
- Hookの存在がClaude CodeとCodexの最大の差別化点。Codexにはnotify（タスク完了時）しかない

## 関連概念
- harness_engineering

## ソース
- 2026-03-10・https://nyosegawa.github.io/posts/harness-engineering-best-practices-2026/

## タグ
Claude Code, Hook, 自動化, 開発環境
