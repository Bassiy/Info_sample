"""
Zenn トレンド記事取得スクリプト
"""

import os
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime


def fetch_zenn_trending(count=20):
    """Zenn の RSS フィードから記事を取得する"""
    url = "https://zenn.dev/feed"

    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urllib.request.urlopen(req) as response:
        xml_data = response.read()

    root = ET.fromstring(xml_data)
    ns = {"atom": "http://www.w3.org/2005/Atom"}

    items = []
    for entry in root.findall("channel/item")[:count]:
        title = entry.find("title")
        link = entry.find("link")
        description = entry.find("description")

        items.append({
            "title": title.text if title is not None else "",
            "link": link.text if link is not None else "",
            "description": (description.text or "")[:200].replace("\n", " ") if description is not None else "",
        })

    return items


def save_report(items, date_str):
    """取得した記事をMarkdownレポートとして保存する"""
    output_dir = os.path.expanduser("~/Documents/info/sources/zenn")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{date_str}.md")

    lines = [
        f"# Zenn トレンド記事",
        f"取得日: {date_str}\n",
        "| # | タイトル | 概要 |",
        "|---|---------|------|",
    ]
    for i, item in enumerate(items, 1):
        title = f"[{item['title']}]({item['link']})"
        description = item['description'].replace("|", "｜")
        lines.append(f"| {i} | {title} | {description} |")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return output_path


def main():
    date_str = datetime.now().strftime("%Y-%m-%d")
    print(f"# Zenn トレンド記事")
    print(f"# 取得日時: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

    items = fetch_zenn_trending()

    for i, item in enumerate(items, 1):
        print(f"{i}. {item['title']}")
        print(f"   {item['link']}")
        if item['description']:
            print(f"   {item['description']}...")
        print()

    output_path = save_report(items, date_str)
    print(f"# レポート保存先: {output_path}")


if __name__ == "__main__":
    main()
