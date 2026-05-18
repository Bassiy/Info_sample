# C4モデル

## 概要
システムのアーキテクチャをContext・Container・Component・Codeの4階層で段階的にズームインして描く設計思想。

## 理解したこと
- 「何を描くか」の思想であって、記法（UMLやMermaid）とは別軸の話
- 4階層がそれぞれ「読者」と「粒度」を決めている
  - Context  : 外の世界との境界。非エンジニアにも見せられる
  - Container: システム内部の実行単位（アプリ・DB・Queueなど）。開発チームの共通言語
  - Component: コンテナの内部構造。担当エンジニア向け
  - Code     : クラス・関数レベル。ほぼ省略される
- 実際に管理するのはContext・Container・Deployment図が現実的
- PlantUMLやMermaidなどテキストで書けるので、Gitで差分管理・PRレビューができる
- AIとの相性が良い：LLMへのインプットにもアウトプットにもなれる「人間とLLMの共通言語」
- C4単体では「現状の構造」しか残らない → ADR（意思決定の記録）と組み合わせるのがトレンド

## 関連概念
- uml.md
- adr.md

## ソース
- 2026-03-09・[アーキテクチャ図、コードで書こう - C4モデル入門](https://zenn.dev/uniquevision/articles/625e00137b75af)
- 2026-03-09・[「アーキテクチャ図はもう要らない」は本当か？LLM時代のC4モデル再考](https://zenn.dev/uniquevision/articles/1ddf3a6ecb0ad7)

## タグ
アーキテクチャ, 設計, C4, PlantUML, Mermaid, ドキュメント
