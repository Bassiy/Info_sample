---
name: gather
description: >
  情報を収集して一覧表示するスキル。引数でドメインを指定する（デフォルトは tech）。
  「トレンド見せて」「ニュース収集して」「ビジネス動向まとめて」「--news」「--business」「--tech」
  など、情報収集・まとめを求められたときに使う。
---

引数でドメインを判定し、対応するスクリプトを実行して収集・表示する。

> **収集ルール**: スクリプト修正・新ソース追加を行う前に `.claude/docs/data-collection.md` を確認すること。RSSフィードと公式APIのみ許可。個別記事URLへのHTTPアクセス禁止。

## ドメイン判定

引数を確認して以下を対応付ける。引数なし・`--tech` はどちらも tech。

| 引数 | ドメイン | スクリプト | 保存先 |
|------|---------|-----------|--------|
| （なし）/ `--tech` | エンジニア系トレンド | `.claude/skills/gather/scripts/tech/gather.py` | `sources/tech/YYYY-MM-DD.md` |
| `--news` | 政治・時事ニュース | `.claude/skills/gather/scripts/news/gather.py` | `sources/news/YYYY-MM-DD.md` |
| `--business` | ビジネス・業界動向 | `.claude/skills/gather/scripts/business/gather.py` | `sources/business/YYYY-MM-DD.md` |

## 手順

1. ドメインに対応したスクリプトを実行する

   ```bash
   python3 ~/.claude/skills/gather/scripts/{domain}/gather.py
   ```

2. スクリプト出力の `---RELEASES---` セクションを読み取り、リリース情報を表示する

   リリースがある場合のみ、記事一覧の**前に**以下の形式で表示する：

   ### 最新リリース（直近7日）

   | プロジェクト | バージョン | 日付 | 内容 |
   |--|--|--|--|
   | Claude Code | v1.x.x | 2026-03-22 | 概要... |

   リリースが0件の場合はこのセクション自体を省略する。

3. スクリプト出力の `---ITEMS---` セクションを読み取り、収集した記事をカテゴリごとにグループ化して以下の形式で表示する

   ### カテゴリ名

   | # | タイトル | 概要 | ソース |
   |---|---------|------|--------|
   | 1 | [タイトル](URL) | 概要テキスト | NHK |

   HTMLの `<a>` タグには必ず `target="_blank"` を付けて新しいタブで開くようにする。

   IDはカテゴリをまたいで全記事で通し番号にする。

   **tech のカテゴリ例：** AI・機械学習 / 開発・設計 / セキュリティ / インフラ・ネットワーク / ガジェット・ハードウェア / その他テック

   **news のカテゴリ例：** 国内政治 / 経済・財政 / 外交・安全保障 / 社会 / その他

   **business のカテゴリ例：** 企業動向 / スタートアップ / 新サービス・プロダクト / 業界トレンド / その他

4. スクリプト出力の `# HTML保存先:` の行からパスを読み取る。
   ステップ3でカテゴリ分けした内容を使い、以下の構造のHTMLを **Write ツールで上書き保存** する。

   ```html
   <!DOCTYPE html>
   <html lang="ja">
   <head>
   <meta charset="UTF-8">
   <title>テックトレンド YYYY-MM-DD</title>
   <style>
     body { font-family: -apple-system, sans-serif; padding: 24px; color: #222; max-width: 1200px; margin: 0 auto; }
     h1 { font-size: 1.4em; }
     h2 { font-size: 1.1em; margin-top: 2em; border-bottom: 1px solid #ddd; padding-bottom: 4px; }
     table { border-collapse: collapse; width: 100%; margin-top: 8px; }
     th { background: #f5f5f5; text-align: left; padding: 6px 10px; font-size: 0.85em; }
     td { padding: 6px 10px; border-bottom: 1px solid #eee; font-size: 0.85em; vertical-align: top; }
     td:first-child { width: 2em; text-align: center; color: #999; }
     td:last-child { width: 5em; color: #666; }
     a { color: #0066cc; text-decoration: none; }
     a:hover { text-decoration: underline; }
   </style>
   </head>
   <body>
   <h1>テックトレンド YYYY-MM-DD</h1>
   <!-- リリースセクション（リリースがある場合のみ） -->
   <h2>最新リリース（直近7日）</h2>
   <table><thead><tr><th>プロジェクト</th><th>日付</th><th>内容</th></tr></thead>
   <tbody>…</tbody></table>
   <!-- カテゴリごとのセクション。リンクはすべて target="_blank" を付ける -->
   <h2>AI・機械学習</h2>
   <table><thead><tr><th>#</th><th>タイトル</th><th>概要</th><th>ソース</th></tr></thead>
   <tbody>…</tbody></table>
   …
   </body></html>
   ```

   書き出し後、ブラウザで開く：
   ```bash
   open {html_path}
   ```

5. 「気になる記事の番号を教えてください。」と伝える

6. ユーザーが数字（記事のID）を返答したら、確認なしで即座に `/deep-dive` スキルを実行する
