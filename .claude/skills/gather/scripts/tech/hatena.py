"""
はてなブックマーク エンジニア向けホットエントリー取得スクリプト
"""

import os
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime


def fetch_hatena_hotentry(category="it", count=20):
    """はてブのホットエントリーをRSSから取得する"""
    url = f"https://b.hatena.ne.jp/hotentry/{category}.rss"

    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urllib.request.urlopen(req) as response:
        xml_data = response.read()

    root = ET.fromstring(xml_data)
    ns = {"rss": "http://purl.org/rss/1.0/",
          "dc": "http://purl.org/dc/elements/1.1/",
          "content": "http://purl.org/rss/1.0/modules/content/"}

    items = []
    for item in root.findall(".//rss:item", ns)[:count]:
        title = item.find("rss:title", ns)
        link = item.find("rss:link", ns)
        description = item.find("rss:description", ns)
        subject = item.find("dc:subject", ns)

        items.append({
            "title": title.text if title is not None else "",
            "link": link.text if link is not None else "",
            "description": (description.text or "")[:200] if description is not None else "",
            "category": subject.text if subject is not None else "",
        })

    return items


def save_report(items, date_str):
    """取得した記事をMarkdownレポートとして保存する"""
    output_dir = os.path.expanduser("~/Documents/info/sources/hatena")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{date_str}.md")

    lines = [
        f"# はてなブックマーク エンジニア向けホットエントリー",
        f"取得日: {date_str}\n",
        "| # | タイトル | 概要 |",
        "|---|---------|------|",
    ]
    for i, item in enumerate(items, 1):
        title = f"[{item['title']}]({item['link']})"
        description = item['description'].replace("\n", " ").replace("|", "｜")
        lines.append(f"| {i} | {title} | {description} |")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return output_path


def main():
    date_str = datetime.now().strftime("%Y-%m-%d")
    print(f"# はてなブックマーク エンジニア向けホットエントリー")
    print(f"# 取得日時: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

    items = fetch_hatena_hotentry()

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
