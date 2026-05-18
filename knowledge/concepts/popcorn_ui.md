# ポップコーンUI

## 概要
複数のコンポーネントがバラバラにローディングを終えてコンテンツが次々と出現する、UXを損なうUIアンチパターン。

## 理解したこと
- コンポーネント単体で `useQuery()` + スピナーを書くのは「正しい実装」に見えるが、ページ全体で見るとポップコーンUIになる
- Layout Shiftを引き起こし、CLS（Cumulative Layout Shift）を悪化させる
- 解決策は「スピナーを1つにまとめる」こと。やり方は3つ：
  1. 親でまとめてフェッチ → Props Drillingが辛い
  2. `useIsFetching()` → TanStack Query限定。開発者の意識頼み
  3. `<Suspense>` で境界をまとめて囲む → 境界内が全部揃うまでfallbackを表示。自然と設計を誘導する
- `<Suspense>` を各コンポーネントに個別で付けると逆にポップコーンUIになるので乱用厳禁
- Next.jsのloading.tsxはフレームワークレベルでこれを防いでくれる

## 関連概念
- separation_of_concerns

## ソース
- 2026-03-16・https://zenn.dev/akfm/articles/popcorn-ui-anti-pattern

## タグ
React, Suspense, UX, ローディング, CLS, TanStack Query, Next.js, アンチパターン
