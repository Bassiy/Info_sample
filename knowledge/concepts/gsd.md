# GSD（Get Shit Done）

## 概要
Claude Code/Codexの弱点（コンテキスト劣化・状態管理・Git混沌化）を補うOSS。

## 理解したこと
- AIエージェントの問題は「コードが書けない」ではなく「状態管理・コンテキスト汚染・Git操作のミス」にある
- 核心思想：**再現性が必要な処理（スクリプトでできること）はLLMに任せない**
  - LLMが担う：判断・推論・フェーズ分解・実装方針決定
  - TypeScriptが担う：Git操作・ファイル検証・状態遷移・トークン予算管理
- 3層階層構造：Milestone（リリース単位）→ Phase（垂直機能単位）→ Plan/Task（1コンテキストに収まる）
- **Fractal Summaries**：タスク→フェーズ→マイルストーンと階層圧縮。各2,500トークン予算。「サマリーのサマリーは作らない」
- **検証ラダー**：Static（スタブ・配線検証）→ Command（ビルド実行）→ Behavioral（振る舞い）→ Human（UAT）
- セッション中断時は `/gsd:pause-work`、再開は `/gsd:resume-work` で即復帰できる
- `.planning/` ディレクトリにMarkdownとGitだけで完結。外部サービス不要

## 関連概念
- harness_engineering
- vertical_slice

## ソース
- 2026-03-10・https://zenn.dev/komlock_lab/articles/gsd-guide-handson

## タグ
AI, エージェント, 開発環境, Claude Code, OSS, コンテキスト管理
