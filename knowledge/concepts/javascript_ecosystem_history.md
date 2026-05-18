# JavaScriptエコシステムの歴史

## 概要
2011〜2025年のJSエコシステムの変遷。JSer.infoの15年分（13,606件）のデータに基づく定量的な記録。

## 理解したこと

### フェーズ別の変遷

**黎明期（2011-2013）**
- jQuery / Backbone.js / CoffeeScript / RequireJS / Grunt / Bower が主役
- 情報源は個人ブログ（はてなダイアリー）中心

**フレームワーク戦争（2016-2019）**
- React がピーク（2017年: 153件）、Vue は一貫して低調
- webpack がビルドツールを独占（2017年: 43件）
- 情報源が Medium・公式ブログへ移行

**標準化・高速化（2020-2025）**
- TypeScript・ESM・WebAssembly が「当たり前」に
- Rust製ツール（SWC, Rspack, Biome）が急増（言及1件→40件）
- esbuild(Go製)→Viteの台頭でwebpackから離脱が始まる
- Node.js一強からDeno（2020年1.0）・Bun（2022年）へ多様化

### 消滅した技術（言及ほぼ0件）
- Backbone.js（75件→0）、CoffeeScript（71件→0）、RequireJS/AMD（74件→3）、Grunt（49件→0）、PhantomJS（37件→0）、Bower（13件→0）

### 持続的に伸びているもの
- ESM: 2件→117件（仕様標準化の力）
- WebAssembly: 0件→51件
- a11y（アクセシビリティ）: 6件→23件（技術トレンドでなく社会的要請）
- Rust製ツール: 1件→40件

### 情報源の変化
- 個人ブログ: 213件→70件（1/3に縮小）
- 公式ドキュメント: 204件→479件（約2倍）
- 日本語ソース比率: 22.2%→4.7%（一次情報の英語化）

### 「残るもの」のパターン
仕様として標準化されたもの（ESM、WebAssembly）は長期的に増え続ける。流行ツールは5年以内に消えることが多い。

## 関連概念
- garbage_collection（ランタイムレベルの技術変遷の文脈）
- harness_engineering（JSer.infoの運用フロー自体がハーネス設計の好例）

## ソース
- 2026-01-16・https://jser.info/2026/01/16/jser-info-15th/

## タグ
JavaScript, エコシステム, 歴史, トレンド, React, TypeScript, WebAssembly, Rust, ESM, Vite, webpack
