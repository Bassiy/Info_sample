# Claude Code スケジュールタスク

## 概要
Claude Codeに内蔵された、自然言語プロンプトを指定した時刻・頻度で定期実行する機能。
GitHub Actionsのcronを書かずに定期自動化ができる。

## 理解したこと
- 設定項目：タスク名・プロンプト・対象リポジトリ・Frequency + Time
- 実行形式は2種類：
  - **リモート実行**：Anthropicクラウド側でトリガー。ローカルマシンの起動状態に依存しない
  - **ローカル実行**：ローカルマシン上で実行。マシンが起動している必要がある
- リモート実行が動くのはGitHub APIなど**外部API経由の操作のみ**
  - ローカルファイルの読み書き・Pythonスクリプト実行・VOICEVOXなどはローカル実行が必要
- Claude Dispatchと同じ構造：「クラウドはトリガーと中継だけ、実行はローカル」
- GitHub Appのインストールが前提（https://github.com/apps/claude/）
- MCP経由でGitHub操作が可能（`mcp__github__list_issues` 等）

## 関連概念
- claude_code_headless（`claude -p` によるcron実行。ローカル定期実行の手段）
- claude_dispatch（同じ「クラウドトリガー・ローカル実行」構造）
- ci_cd

## ソース
- 2026-03-22・https://dev.classmethod.jp/articles/claude-code-scheduled-tasks-github-triage/

## タグ
Claude Code, スケジュール, 自動化, cron, GitHub Actions, MCP
