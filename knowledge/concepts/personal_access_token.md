# Personal Access Token (PAT)

## 概要
GitHubなどのサービスで、パスワードの代わりに使う認証用の文字列トークン。

## 理解したこと
- `ghp_xxxxxxxxxxxx` のような長い文字列
- HTTPS接続でgit操作するときに使う
- **PATそのものが認証情報**なので、漏洩したらそのまま不正アクセスに使われる
- AIエージェントが自動でgit操作するとき、設定ファイル（.envなど）に書く必要がある
- AIのコンテキストやログにPATが入ると漏洩リスクがある
- 1つのPATがGitHubアカウント全体に効く場合もあり、被害が広がりやすい

## 関連概念
- ssh_key_auth.md（より安全な代替手段）
- challenge_response_auth.md（SSHが安全な理由の仕組み）

## ソース
- 2026-03-06・Qiita「AI時代にすべてをGitHubで管理するあなたへ──HTTPS接続、今すぐやめてください」
  https://qiita.com/kenimo49/items/27e2a11e80fe3b835f96

## タグ
認証, GitHub, HTTPS, セキュリティ, トークン
