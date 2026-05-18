"""
Qiita トレンド記事取得スクリプト
"""

import json
import os
import urllib.request
from datetime import datetime, timedelta


def fetch_qiita_trending(count=20):
    """Qiita APIから人気記事を取得する"""
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    url = f"https://qiita.com/api/v2/items?per_page={count}&query=created:>{yesterday}&sort=stock"

    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read())

    items = []
    for item in data:
        items.append({
            "title": item.get("title", ""),
            "link": item.get("url", ""),
            "description": (item.get("body", "") or "")[:200].replace("\n", " "),
            "tags": ", ".join(t["name"] for t in item.get("tags", [])[:3]),
            "likes": item.get("likes_count", 0),
        })

    return items


def save_report(items, date_str):
    """取得した記事をMarkdownレポートとして保存する"""
    output_dir = os.path.expanduser("~/Documents/info/sources/qiita")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{date_str}.md")

    lines = [
        f"# Qiita トレンド記事",
        f"取得日: {date_str}\n",
        "| # | タイトル | タグ | 概要 |",
        "|---|---------|------|------|",
    ]
    for i, item in enumerate(items, 1):
        title = f"[{item['title']}]({item['link']})"
        description = item['description'].replace("|", "｜")
        lines.append(f"| {i} | {title} | {item['tags']} | {description} |")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return output_path


def main():
    date_str = datetime.now().strftime("%Y-%m-%d")
    print(f"# Qiita トレンド記事")
    print(f"# 取得日時: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

    items = fetch_qiita_trending()

    for i, item in enumerate(items, 1):
        print(f"{i}. {item['title']} (LGTM: {item['likes']})")
        print(f"   タグ: {item['tags']}")
        print(f"   {item['link']}")
        if item['description']:
            print(f"   {item['description']}...")
        print()

    output_path = save_report(items, date_str)
    print(f"# レポート保存先: {output_path}")


if __name__ == "__main__":
    main()
