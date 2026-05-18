# Claude Dispatch

## 概要
スマホからPC上のClaude Coworkにタスクをリモート指示できるAnthropicの公式機能。
2026/3/17リリース（リサーチプレビュー）。

## 理解したこと
- アーキテクチャ：スマホ → E2E暗号化通信 → PC上のClaude Cowork という構造
- QRコードでペアリング → PCのフォルダ・アプリアクセスを許可するだけでセットアップ完了
- 対応タスク例：スプレッドシート集計・Slack/メールから資料作成・ファイル整理
- 安全設計：ファイル削除・大量移動などの重要操作はスマホへプッシュ通知で承認要求
- クラウドにデータをアップロードしない（E2E暗号化でローカル↔ローカル通信）
- 制約：PC起動 + アプリ開放が必須。完全自律型ではなく「席を外している間の非同期実行」が現実的用途
- 先行OSSのOpenClawと違い、公式による安全設計が組み込まれている点が差別化
- 料金：Max 5x（$100/月）/ Max 20x（$200/月）から利用可能。Proは数日後、無料は2026年中予定

## 関連概念
- openclaw.md（OSS先行実装。同様の「外部→Claudeへの指示」構造）
- claude_code_hooks.md
- ai_subagent.md

## ソース
- 2026-03-22・https://zenn.dev/ap_com/articles/claude-dispatch-cowork-20260319

## タグ
Claude, Dispatch, Cowork, remote, mobile, async, E2E encryption, agent
