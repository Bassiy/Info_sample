# Everything Claude Code (ECC)

## 概要
Anthropicハッカソン優勝者が公開した、Claude Codeのハーネス設計ベストプラクティスを
agents/skills/rules/hooks としてパッケージ化・配布するOSSプラグイン集。

## 理解したこと
- Claude Code自体はフレームワークのみ提供。ECCはその「中身」をコピーして使えるようにした
- 構成要素：Agents 28個 / Skills 116個 / Commands 60個 / Rules 34個 / Hooks
- 選択的インストール（manifest-driven）。プロジェクトに必要な部品だけ入れればよい
- AgentShield：ECCに含まれるセキュリティスキャナ。prompt injectionなどをred-team的に検出。CIに組み込んでexit code 2でブロックできる
- 情報収集・知識管理系プロジェクト（info/のような）には不向き。ガッツリ開発プロジェクト向け
- 導入の現実的な推奨：planner + code-reviewer + security-reviewer の最小構成から始める
- Hooksのセッション記憶はグローバル（~/.claude/hooks/）にも導入できる

## 関連概念
- harness_engineering
- ai_subagent
- claude_code_hooks
- prompt_injection

## ソース
- 2026-03-23・https://github.com/affaan-m/everything-claude-code

## タグ
Claude Code, エージェント, ハーネス, OSS, セキュリティ, AgentShield, プラグイン
