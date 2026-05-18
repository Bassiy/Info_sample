"""
全ソースのトレンド記事を収集して一つのレポートにまとめるスクリプト
"""

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))

from hatena import fetch_hatena_hotentry
from qiita import fetch_qiita_trending
from zenn import fetch_zenn_trending
from github_releases import fetch_github_releases


SOURCES = [
    ("はてな", fetch_hatena_hotentry, {"count": 15}),
    ("Qiita",  fetch_qiita_trending,  {"count": 15}),
    ("Zenn",   fetch_zenn_trending,   {"count": 15}),
]


def gather_all():
    """全ソースから記事を収集し、ソース名を付けて返す"""
    all_items = []
    for source_name, fetch_fn, kwargs in SOURCES:
        try:
            items = fetch_fn(**kwargs)
            for item in items:
                item["source"] = source_name
            all_items.extend(items)
            print(f"  ✓ {source_name}: {len(items)} 件", flush=True)
        except Exception as e:
            print(f"  ✗ {source_name}: {e}", flush=True)
    return all_items


def save_report(items, date_str):
    """収集した記事を一つのMarkdownファイルに保存する"""
    output_dir = os.path.expanduser("~/Documents/info/sources/tech")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{date_str}.md")

    lines = [
        f"# トレンド記事",
        f"取得日: {date_str}\n",
        "| タイトル | 概要 | ソース |",
        "|---------|------|--------|",
    ]
    for item in items:
        title = f"[{item['title']}]({item['link']})"
        description = item.get("description", "").replace("\n", " ").replace("|", "｜")[:150]
        source = item.get("source", "")
        lines.append(f"| {title} | {description} | {source} |")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return output_path


def save_html_report(items, releases, date_str):
    """ブラウザで見られるHTMLファイルを生成する"""
    output_dir = os.path.expanduser("~/Documents/info/sources/tech")
    html_path = os.path.join(output_dir, f"{date_str}.html")

    def esc(s):
        return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

    rows = ""
    for i, item in enumerate(items, 1):
        title = esc(item["title"])
        link = esc(item["link"])
        desc = esc(item.get("description", "").replace("\n", " ")[:150])
        source = esc(item.get("source", ""))
        rows += f'<tr><td>{i}</td><td><a href="{link}" target="_blank">{title}</a></td><td>{desc}</td><td>{source}</td></tr>\n'

    release_rows = ""
    for r in releases:
        release_rows += f'<tr><td><a href="{esc(r["link"])}" target="_blank">{esc(r["display"])} {esc(r["version"])}</a></td><td>{esc(r["published_at"])}</td><td>{esc(r["summary"][:120])}</td></tr>\n'

    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>テックトレンド {date_str}</title>
<style>
  body {{ font-family: -apple-system, sans-serif; padding: 24px; color: #222; }}
  h1 {{ font-size: 1.4em; }}
  h2 {{ font-size: 1.1em; margin-top: 2em; border-bottom: 1px solid #ddd; padding-bottom: 4px; }}
  table {{ border-collapse: collapse; width: 100%; margin-top: 8px; }}
  th {{ background: #f5f5f5; text-align: left; padding: 6px 10px; font-size: 0.85em; }}
  td {{ padding: 6px 10px; border-bottom: 1px solid #eee; font-size: 0.85em; vertical-align: top; }}
  td:first-child {{ width: 2em; text-align: center; color: #999; }}
  td:last-child {{ width: 5em; color: #666; }}
  a {{ color: #0066cc; text-decoration: none; }}
  a:hover {{ text-decoration: underline; }}
</style>
</head>
<body>
<h1>テックトレンド {date_str}</h1>
{'<h2>最新リリース（直近7日）</h2><table><thead><tr><th>プロジェクト</th><th>日付</th><th>内容</th></tr></thead><tbody>' + release_rows + '</tbody></table>' if release_rows else ''}
<h2>記事一覧</h2>
<table>
  <thead><tr><th>#</th><th>タイトル</th><th>概要</th><th>ソース</th></tr></thead>
  <tbody>{rows}</tbody>
</table>
</body>
</html>"""

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    return html_path


def main():
    date_str = datetime.now().strftime("%Y-%m-%d")
    print(f"# トレンド記事収集")
    print(f"# 取得日時: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    print("収集中...")

    items = gather_all()

    print(f"\n合計 {len(items)} 件を収集しました。")

    print("\nリリース情報を取得中...")
    releases = fetch_github_releases(days=7)

    output_path = save_report(items, date_str)
    html_path = save_html_report(items, releases, date_str)
    print(f"# レポート保存先: {output_path}")
    print(f"# HTML保存先: {html_path}")

    # リリース情報を出力
    print("\n---RELEASES---")
    for r in releases:
        print(f"DISPLAY:{r['display']}")
        print(f"VERSION:{r['version']}")
        print(f"DATE:{r['published_at']}")
        print(f"TITLE:{r['title']}")
        print(f"LINK:{r['link']}")
        print(f"DESC:{r['summary']}")
        print("---")

    # 表示用にデータを出力
    print("\n---ITEMS---")
    for item in items:
        desc = item.get("description", "").replace("\n", " ").replace("|", "｜")[:150]
        print(f"TITLE:{item['title']}")
        print(f"LINK:{item['link']}")
        print(f"DESC:{desc}")
        print(f"SOURCE:{item.get('source', '')}")
        print("---")


if __name__ == "__main__":
    main()
