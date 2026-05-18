# Markdownエコシステム（変換・生成）

## 概要
「何かをMarkdownに変換する」「MarkdownからXXXを生成する」用途と
そのツール・手法の全体像。

## 理解したこと

### → Markdownに変換（インポート）
| 元フォーマット | 手法・ツール | 備考 |
|--------------|------------|------|
| 方眼紙Excel | LLM（テキストモード推奨） | 50列問題があるため機械変換では品質不足 |
| 通常のExcel / CSV | pandas, openpyxl | 単純な表構造ならそのまま変換可能 |
| PDF / Word | docling（IBM）, markitdown | 品質はドキュメント構造に依存 |

### Markdown → に変換（エクスポート）
| 出力フォーマット | 手法・ツール | 備考 |
|---------------|------------|------|
| スライド（HTML/PDF） | Marp | `---` でスライド区切り、VSCode拡張あり |
| PDF | pandoc, md-pdf | 汎用変換ツール |
| HTML | 各種静的サイトジェネレータ | Next.js, Jekyll, etc. |

## 関連概念
- markdown_conversion（Excel→MD変換の詳細）
- rag（変換後のMDをRAGに投入する用途）

## ソース
- 2026-03-22・会話から整理

## タグ
Markdown, Marp, 変換, ドキュメント, RAG, Excel, スライド
