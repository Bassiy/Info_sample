# Linter / Formatter

## 概要
コードを自動チェック・整形するツール。Linterが「問題検出」、Formatterが「見た目の自動整形」という役割分担。

## 理解したこと
| | Linter | Formatter |
|--|--|--|
| 役割 | 問題点を**検出**して報告 | インデント・スペースなど見た目を**自動整形** |
| 例 | ESLint, Ruff, Flake8 | Prettier |
| 出力 | エラーメッセージ | 修正済みコード |

- コンパイラとの違い：コンパイラは「動くか動かないか」、Linterは「動くけどよくないコード」を検出する
- **Harness Engineeringにおける役割**：決定論的ツールの代表例
  - AIがコード修正 → PostToolUse Hookで自動起動 → Linterがチェック → エラーをAIに返す → AIが自己修正 → ループ
  - 人間が介入しなくても品質が担保される環境が生まれる

## 関連概念
- harness_engineering
- claude_code_hooks

## ソース
- 2026-03-10・https://qiita.com/pumpkinpumkin/items/59eee7e1b46b407a210f

## タグ
開発環境, Linter, Formatter, 静的解析, コード品質, 自動化
