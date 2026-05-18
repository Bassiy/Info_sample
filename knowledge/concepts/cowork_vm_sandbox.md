# Cowork VM サンドボックス

## 概要
Claude Coworkが内部で使用するLinux VM（Ubuntu 22）の実行環境と制約。

## 理解したこと
- CoworkはユーザーのMac上でLinux VMを起動し、その中でタスクを実行する
- ファイル操作はマウントしたディレクトリ（~/Dropbox/info など）経由で可能
- **外部HTTP通信は制限されている** — RSSフィード取得・外部APIコールなど、スクリプトによる直接の外部アクセスは不可（WebSearch/WebFetchツール経由は可）
- **Macのローカルリソースにアクセス不可** — `localhost:XXXX` で動くサービス（VOICEVOXなど）には届かない
- **MacアプリのGUI起動不可** — `open -a` や `osascript` は使えない
- **Macのターミナルを直接操作する手段はない**
- Claude Codeとの違い：Claude CodeはMac上で直接動くため上記制限はない。Coworkは常にVM経由

## 実例
- podcastスキル実行時、`gather.py`（RSSフィード収集）がVM内から失敗 → WebSearchで代替
- VOICEVOXのAPI（localhost:50021）にVM内からアクセス不可 → 音声変換のみ手動対応が必要

## 関連概念
- claude_dispatch.md
- cloud_infrastructure.md

## ソース
- 2026-03-22・Coworkでpodcastスキルを実行した際の実経験

## タグ
cowork, vm, sandbox, linux, 実行環境, 制約, claude
