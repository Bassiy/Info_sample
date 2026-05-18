# LLM-as-Judge

## 概要
LLMの出力品質をLLM自身に評価させる品質検証パターン。

## 理解したこと
- 「生成するLLM（キュレーター）」と「評価するLLM（審査員）」を分離する二重構造
- スコアリング・要約・タグ付けなど、正解が一意に定まらない出力の品質測定に有効
- Feed Curatorの実装例：
  - キュレーターClaude：記事に0〜1のスコアをつける
  - 審査員Claude：そのスコアの精度・要約の質・タグの妥当性を1〜5で評価
  - 評価軸は `score_accuracy` / `summary_quality` / `tag_relevance` の3つ
- 行動指標（ユーザーが実際に読んだか）と判定指標（LLMの自己評価）を組み合わせることで、スコアリングの品質を継続的に改善できる
- バッチ処理（5記事単位）でClaudeを呼び出してコストを抑えている
- 同じClaudeを2役使うため、追加APIキー不要で実現できる

## 関連概念
- claude_code_headless
- harness_engineering
- ai_subagent

## ソース
- 2026-04-04・https://zenn.dev/caphtech/articles/feed-curator-ai-rss-with-claude-code

## タグ
LLM, 品質評価, AI, evaluation, judge, Claude Code
