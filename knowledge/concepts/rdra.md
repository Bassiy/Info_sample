# RDRA（要求分析フレームワーク）

## 概要
「要望→要求→要件→仕様→設計」の階層を整理するための要求分析フレームワーク。
仕様を書く前に「誰が・なぜ・何のため」を明確化する。

## 理解したこと
- SDDツール（Kiro・OpenSpec等）は「要件→仕様」を扱うが、その上流の「要望→要求→要件」が抜けがちになる
- RDRA はこの上流を埋める：アクター一覧・ゴール一覧・要求一覧をテキスト表形式で整理する
- テキスト表形式のため AI エージェントがそのままコンテキストとして読める（付箋ベースのイベントストーミングとの違い）
- 「Traces to」で要件からゴールまで遡れる参照関係を持つ → 「なぜこの仕様か」が追跡可能
- Claude Code との組み合わせワークフロー：
  1. Claude が Confluence/Notion/Slack を検索してアクター・ゴールの仮説を RDRA 形式で生成
  2. Mermaid でas-is業務フローを可視化、to-be候補を複数提案
  3. 人間は仮説の検証に集中（質問往復を減らせる）
  4. 成果物を Confluence 等に配置して非エンジニアも参加可能に

## 関連概念
- spec_doc_strategy.md
- adr.md
- claude_code_context_management.md

## ソース
- 2026-03-22・https://kosui.me/posts/2026/03/15/sdd-requirements-analysis

## タグ
RDRA, 要求分析, SDD, 仕様書, 設計, Claude Code, ドキュメント
