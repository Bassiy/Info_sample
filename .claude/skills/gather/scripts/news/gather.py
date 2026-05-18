"""
政治・時事ニュースを収集して一つのレポートにまとめるスクリプト

収集方針:
  Step1: NHK RSS（政治カテゴリ）で「今日何が重要か」を把握する
  Step2: 各NHK記事タイトルをキーワードにGoogle News RSSを検索し、
         複数媒体（日経・読売・産経・時事など）の見出しを取得して description を補完する
  Step3: Yahoo!ニュース・TBS NEWS DIG からも収集し、NHK未収録の話題を補う

すべてRSSフィードのみ使用。個別記事ページへのHTTPアクセスは行わない。
"""

import html as html_lib
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime


# ── ソース定義 ──────────────────────────────────────────────────────────

NHK_RSS = "https://www.nhk.or.jp/rss/news/cat4.xml"   # 政治カテゴリ

SUPPLEMENTAL_SOURCES = [
    {"name": "Yahoo!ニュース",  "url": "https://news.yahoo.co.jp/rss/topics/domestic.xml"},
    {"name": "TBS NEWS DIG",   "url": "https://newsdig.tbs.co.jp/rss/articles.rss"},
]

GOOGLE_NEWS_SEARCH = "https://news.google.com/rss/search?q={query}&hl=ja&gl=JP&ceid=JP:ja"

# NHK記事のうち上位何件をGoogle Newsで補完するか
ENRICH_LIMIT = 15


# ── RSS 取得 ─────────────────────────────────────────────────────────────

def fetch_rss(url, source_name, limit=25):
    """RSSフィードを取得してアイテムリストを返す"""
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            xml_data = resp.read()
    except Exception as e:
        print(f"  ✗ {source_name}: RSS取得失敗 - {e}", flush=True)
        return []

    try:
        root = ET.fromstring(xml_data)
    except ET.ParseError as e:
        print(f"  ✗ {source_name}: XML解析失敗 - {e}", flush=True)
        return []

    items_raw = root.findall(".//item")
    if not items_raw:
        ns = {"rss": "http://purl.org/rss/1.0/"}
        items_raw = root.findall(".//rss:item", ns)

    items = []
    for item in items_raw[:limit]:
        title = item.findtext("title") or ""
        link  = item.findtext("link") or ""
        desc  = (item.findtext("description") or "").replace("\n", " ").strip()
        if title and link:
            items.append({
                "title": title.strip(),
                "link": link.strip(),
                "description": desc[:200],
                "source": source_name,
            })
    return items


# ── Google News 補完 ──────────────────────────────────────────────────────

def fetch_google_headlines(keyword, max_headlines=6):
    """
    キーワードでGoogle News RSS検索し、関連する複数媒体の見出しを返す。
    Google NewsのdescriptionはHTML形式で複数ソースの見出しリストが入っている。
    これをデコードして「見出し（媒体名）」のリストとして返す。
    """
    query = urllib.parse.quote(keyword[:60])
    url = GOOGLE_NEWS_SEARCH.format(query=query)
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            rss_text = resp.read().decode("utf-8", errors="replace")
    except Exception:
        return []

    # 最初のitemだけ見ればよい（検索結果の先頭 = 最も関連度の高いクラスタ）
    item_match = re.search(r'<item>.*?</item>', rss_text, re.DOTALL)
    if not item_match:
        return []

    desc_match = re.search(r'<description>(.*?)</description>', item_match.group(), re.DOTALL)
    if not desc_match:
        return []

    raw = html_lib.unescape(desc_match.group(1))
    # <a href="...">見出しテキスト</a>&nbsp;&nbsp;媒体名 の形式を抽出
    pattern = re.compile(r'<a[^>]+>([^<]{5,})</a>\s*(?:&nbsp;\s*)*([^<\n]{2,30})')
    headlines = []
    for m in pattern.finditer(raw):
        headline = m.group(1).strip()
        source   = m.group(2).strip().rstrip('</li>').strip()
        if headline and source:
            headlines.append(f"{headline}（{source}）")
    return headlines[:max_headlines]


def enrich_with_google_news(items):
    """NHK記事リストをGoogle News検索で補完する"""
    enriched = []
    for i, item in enumerate(items):
        if i >= ENRICH_LIMIT:
            enriched.append(item)
            continue

        headlines = fetch_google_headlines(item["title"])
        if headlines:
            item = dict(item)
            item["google_headlines"] = headlines
            print(f"    → Google News補完: {len(headlines)}件の関連見出し", flush=True)
        else:
            item = dict(item)
            item["google_headlines"] = []

        enriched.append(item)
        time.sleep(0.4)  # レート制限への配慮

    return enriched


# ── 収集メイン ────────────────────────────────────────────────────────────

def gather_all():
    print("  [Step1] NHK RSSを取得...", flush=True)
    nhk_items = fetch_rss(NHK_RSS, "NHK")
    print(f"  ✓ NHK: {len(nhk_items)} 件", flush=True)

    print(f"  [Step2] 上位{ENRICH_LIMIT}件をGoogle Newsで補完...", flush=True)
    nhk_items = enrich_with_google_news(nhk_items)

    print("  [Step3] 補完ソースを取得...", flush=True)
    supplemental = []
    for src in SUPPLEMENTAL_SOURCES:
        items = fetch_rss(src["url"], src["name"])
        supplemental.extend(items)
        print(f"  ✓ {src['name']}: {len(items)} 件", flush=True)

    return nhk_items, supplemental


# ── 保存 ─────────────────────────────────────────────────────────────────

def save_report(nhk_items, supplemental, date_str):
    output_dir = os.path.expanduser("~/Documents/info/sources/news")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{date_str}.md")

    lines = [
        "# 政治・時事ニュース",
        f"取得日: {date_str}",
        "",
        "---",
        "",
        "## NHK厳選ニュース（Google News補完あり）",
        "",
    ]

    for item in nhk_items:
        lines.append(f"### {item['title']}")
        lines.append(f"- **ソース**: {item['source']}")
        lines.append(f"- **URL**: {item['link']}")
        if item.get("description"):
            lines.append(f"- **NHK概要**: {item['description']}")
        if item.get("google_headlines"):
            lines.append("- **関連報道**:")
            for h in item["google_headlines"]:
                lines.append(f"  - {h}")
        lines.append("")

    if supplemental:
        lines += [
            "---",
            "",
            "## その他ソース",
            "",
            "| タイトル | 概要 | ソース |",
            "|---------|------|--------|",
        ]
        for item in supplemental:
            title = f"[{item['title']}]({item['link']})"
            desc  = item.get("description", "").replace("|", "｜")[:120]
            lines.append(f"| {title} | {desc} | {item['source']} |")

    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return output_path


# ── エントリポイント ──────────────────────────────────────────────────────

def main():
    date_str = datetime.now().strftime("%Y-%m-%d")
    print("# 政治・時事ニュース収集")
    print(f"# 取得日時: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")

    nhk_items, supplemental = gather_all()
    total = len(nhk_items) + len(supplemental)
    print(f"\n合計 {total} 件を収集しました。")

    output_path = save_report(nhk_items, supplemental, date_str)
    print(f"# レポート保存先: {output_path}")


if __name__ == "__main__":
    main()
