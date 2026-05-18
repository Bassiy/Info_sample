# データ収集ルール

情報収集スクリプト（`scripts/` 以下）の運用ルール。
利用規約・法的リスクを避けるための制約をまとめる。

## 基本方針

**RSSフィードと公式APIのみを使用する。**
個別記事ページへのHTTPアクセスは行わない。

## 許可されている収集方法

| 方法 | 理由 |
|------|------|
| RSSフィード（RSS 1.0 / 2.0） | 機械読み取り用に公開されているため |
| 公式API（認証不要・無料枠） | 利用規約で明示的に許可されているため |

## 禁止されている収集方法

| 方法 | 理由 |
|------|------|
| 個別記事URLへのHTTPリクエスト | サイト利用規約の機械的アクセス禁止条項に抵触する可能性がある |
| HTMLスクレイピング | 同上 |
| 有料記事コンテンツの取得 | 著作権・利用規約上問題がある |
| 大量・高頻度アクセス | サーバー負荷、DoS的扱いになる可能性がある |

## 現在の収集ソース一覧

### tech（`scripts/tech/`）

| ソース | 方法 | URL |
|--------|------|-----|
| はてなブックマーク | RSS | `https://b.hatena.ne.jp/hotentry/it.rss` |
| Qiita | 公式API v2 | `https://qiita.com/api/v2/items` |
| Zenn | RSS | `https://zenn.dev/feed` |
| DevelopersIO | RSS | `https://dev.classmethod.jp/feed/` |
| JSer.info | RSS | `https://jser.info/rss/` |
| GitHub Releases | GitHub API（認証なし） | `https://api.github.com/repos/{owner}/{repo}/releases` |
| HackerNews | Firebase API | `https://hacker-news.firebaseio.com/v0/` |

### news（`scripts/news/`）

| ソース | 方法 | URL |
|--------|------|-----|
| NHK（政治カテゴリ） | RSS | `https://www.nhk.or.jp/rss/news/cat4.xml` |
| Yahoo!ニュース（国内） | RSS | `https://news.yahoo.co.jp/rss/topics/domestic.xml` |
| TBS NEWS DIG | RSS | `https://newsdig.tbs.co.jp/rss/articles.rss` |

### business（`scripts/business/`）

| ソース | 方法 | URL |
|--------|------|-----|
| PR TIMES | RSS | `https://prtimes.jp/rss2.0/index.rdf` |
| ITmedia ビジネス | RSS | `https://rss.itmedia.co.jp/rss/2.0/business.xml` |
| Business Insider Japan | RSS | `https://www.businessinsider.jp/feed/index.xml` |
| ログミーBiz | RSS | `https://logmi.jp/feed` |

## 新しいソースを追加するときのチェックリスト

- [ ] RSSフィードまたは公式APIが存在するか確認する
- [ ] 利用規約に機械的アクセスの禁止条項がないか確認する
- [ ] 個別記事へのHTTPアクセスをコードに含めない
- [ ] 収集頻度は1日1回程度に抑える

## GitHub Releases の監視リポジトリ管理

監視対象は `scripts/tech/watched_repos.json` で管理する。

```json
{
  "repos": [
    { "owner": "anthropics", "repo": "claude-code", "display": "Claude Code" }
  ]
}
```

追加・削除はこのファイルを直接編集する。`owner`/`repo` は GitHub のリポジトリパスと一致させること。

## スクリプト修正時の注意

- `urllib.request` 等で個別記事URLにアクセスするコードを追加しない
- ペイウォール判定・本文取得のためのHTTPリクエストは禁止
- RSSの `<description>` に含まれる要約テキストの利用は問題なし（200文字以内に留める）
