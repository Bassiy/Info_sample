"""
HackerNews トップストーリー取得スクリプト
"""

import json
import os
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime


def fetch_item(item_id):
    """HackerNews の個別アイテムを取得する"""
    url = f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json"
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())


def fetch_hackernews_top(count=20):
    """HackerNews のトップストーリーを取得する"""
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    with urllib.request.urlopen(url) as response:
        top_ids = json.loads(response.read())[:count]

    items = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(fetch_item, id_): id_ for id_ in top_ids}
        results = {}
        for future in as_completed(futures):
            id_ = futures[future]
            try:
                results[id_] = future.result()
            except Exception:
                pass

    for id_ in top_ids:
        item = results.get(id_)
        if not item or item.get("type") != "story":
            continue
        items.append({
            "title": item.get("title", ""),
            "link": item.get("url", f"https://news.ycombinator.com/item?id={item.get('id')}"),
            "description": "",
            "score": item.get("score", 0),
            "comments": item.get("descendants", 0),
        })

    return items


def save_report(items, date_str):
    """取得した記事をMarkdownレポートとして保存する"""
    output_dir = os.path.expanduser("~/Documents/info/sources/hackernews")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{date_str}.md")

    lines = [
        f"# HackerNews Top Stories",
        f"取得日: {date_str}\n",
        "| # | タイトル | スコア | コメント |",
        "|---|---------|--------|---------|",
    ]
    for i, item in enumerate(items, 1):
        title = f"[{item['title']}]({item['link']})"
        lines.append(f"| {i} | {title} | {item['score']} | {item['comments']} |")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return output_path


def main():
    date_str = datetime.now().strftime("%Y-%m-%d")
    print(f"# HackerNews Top Stories")
    print(f"# 取得日時: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

    items = fetch_hackernews_top()

    for i, item in enumerate(items, 1):
        print(f"{i}. {item['title']} (score: {item['score']}, comments: {item['comments']})")
        print(f"   {item['link']}")
        print()

    output_path = save_report(items, date_str)
    print(f"# レポート保存先: {output_path}")


if __name__ == "__main__":
    main()
