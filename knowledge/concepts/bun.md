# Bun

## 概要
Node.jsと互換性を持ちながら、高速・オールインワンを目指したJavaScript実行環境。

## 理解したこと
- JavaScriptはブラウザ外で動かすのにNode.jsが必要だったが、BunはそのNode.jsの上位互換を目指している
- 起動速度がNode.jsの約4倍速い
- SQLite・テストランナー・パッケージマネージャーが本体に同梱されており、追加インストール不要
- 既存のNode.js用コードがほぼそのまま動く（互換性が高い）
- `typeof globalThis.Bun !== "undefined"` でBun環境かどうかを判定できる
- Feed CuratorではBun/Node.jsを自動判定してSQLiteバックエンドを切り替えている
  - Bun環境 → `bun:sqlite`（ネイティブ、高速）
  - Node.js環境 → `sql.js`（WebAssembly版、追加インストール不要）
- `bun build --compile` でCLIをシングルバイナリに変換できる（Tauriサイドカーとして同梱可能）

## 関連概念
- javascript_ecosystem_history
- claude_code_headless

## ソース
- 2026-04-04・https://zenn.dev/caphtech/articles/feed-curator-ai-rss-with-claude-code
- 2026-04-04・会話から

## タグ
JavaScript, runtime, Node.js, SQLite, パッケージ管理, Bun
