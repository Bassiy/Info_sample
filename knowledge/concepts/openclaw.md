# OpenClaw

## 概要
AIエージェントをローカルで常駐させ、Discord/Telegram/WhatsAppなど複数のチャットアプリから呼び出せるようにするOSSのマルチチャネルGatewayツール。

## 理解したこと
- アーキテクチャ：チャットアプリ → OpenClaw Gateway → AIエージェント という中継構造
- MCPとの方向の違い：MCPは「ClaudeがDiscordを道具として使う」、OpenClawは「DiscordからClaudeが呼び出される」
- `~/.openclaw/workspace/SOUL.md` でエージェントのペルソナを定義（Claude CodeのCLAUDE.mdに相当）
- cronジョブとサブエージェント並列処理をサポート
- Proプランでは使えない（APIキー必要）。ただし claude -p をcronで叩く構成ならProのみで同等の自動化が可能

## 関連概念
- ai_subagent.md
- claude_code_hooks.md
- claude_dispatch.md（Anthropic公式の後継・同等機能。安全設計込み）

## ソース
- 2026-03-22・https://qiita.com/akira_papa_AI/items/5f2b9f176bad4ce5d2e7

## タグ
AI agent, gateway, multichannel, Discord, automation, OSS
