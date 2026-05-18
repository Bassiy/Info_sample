# Markdown変換（Excel・各種ドキュメント→Markdown）

## 概要
構造化されていないドキュメント（方眼紙Excelなど）をMarkdownに変換する手法。
RAGやAI活用への投入に必要な前処理として重要。

## 理解したこと
- **方眼紙Excel特有の問題（50列問題）**：
  - セル結合を機械的に展開すると空白列が大量発生してRAGで使い物にならない
  - Markdownにはcolspan/rowspanの概念がないため、機械変換では意味が失われる
- **解決策：LLMに意味推論させる**
  - セル値をタブ区切りテキストでLLMに渡し、「意味が伝わるMarkdown」として再構成させる
  - テキストモード（gpt-4o-mini等）がビジョンモードより優秀（OCR誤り・色情報欠落がない）
- **手法別使い分け**：
  - 速度優先・品質不問 → pandas（0.1秒・無料）
  - 品質重視 → GitHub Models API テキストモード（無料枠あり・~20秒）
  - Copilotユーザー → Copilot SDK（claude-sonnet・~56秒）

## 関連概念
- rag（変換後のMarkdownをRAGに投入する用途）
- markdown_ecosystem（Marpなど他のMD活用と合わせて参照）

## ソース
- 2026-03-22・https://zenn.dev/ougotti/articles/houganshi-excel-to-markdown

## タグ
Markdown, Excel, RAG, LLM, ドキュメント変換, 方眼紙Excel
