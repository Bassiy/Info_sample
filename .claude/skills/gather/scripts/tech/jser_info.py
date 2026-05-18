"""
JSer.info の記事取得スクリプト
JavaScript全般の週次まとめ。日本語で高品質なキュレーション。
"""

import urllib.request
import xml.etree.ElementTree as ET


def fetch_jser_info(count=10):
    """JSer.info の RSS フィードから記事を取得する"""
    url = "https://jser.info/rss/"

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
            import re
            desc_text = re.sub(r"<[^>]+>", "", description.text or "")
            desc_text = desc_text.replace("\n", " ").strip()[:200]

        items.append({
            "title": title.text if title is not None else "",
            "link": link.text if link is not None else "",
            "description": desc_text,
        })

    return items
