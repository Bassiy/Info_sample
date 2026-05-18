"""
DevelopersIO (クラスメソッド) の記事取得スクリプト
AWS・クラウド・インフラ・バックエンド系が充実した日本語技術ブログ
"""

import urllib.request
import xml.etree.ElementTree as ET


def fetch_developers_io(count=20):
    """DevelopersIO の RSS フィードから記事を取得する"""
    url = "https://dev.classmethod.jp/feed/"

    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urllib.request.urlopen(req, timeout=10) as response:
        xml_data = response.read()

    root = ET.fromstring(xml_data)

    items = []
    for entry in root.findall("channel/item")[:count]:
        title = entry.find("title")
        link = entry.find("link")
        description = entry.find("description")

        desc_text = ""
        if description is not None and description.text:
            # HTMLタグを簡易除去
            import re
            desc_text = re.sub(r"<[^>]+>", "", description.text or "")
            desc_text = desc_text.replace("\n", " ").strip()[:200]

        items.append({
            "title": title.text if title is not None else "",
            "link": link.text if link is not None else "",
            "description": desc_text,
        })

    return items
