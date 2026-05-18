"""
監視リポジトリの GitHub Releases を取得するスクリプト。
watched_repos.json に登録されたリポジトリを対象に、直近 N 日以内のリリースを返す。
GitHub API は認証なしで利用（public リポジトリのみ対応）。
"""

import json
import os
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta


WATCHED_REPOS_PATH = os.path.join(os.path.dirname(__file__), "watched_repos.json")
GITHUB_API_BASE = "https://api.github.com"


def load_watched_repos():
    with open(WATCHED_REPOS_PATH, encoding="utf-8") as f:
        return json.load(f)["repos"]


def fetch_releases_for_repo(owner, repo, display, days=7):
    """指定リポジトリの直近 days 日以内のリリースを取得する"""
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}/releases?per_page=10"
    req = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "info-gatherer/1.0",
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            releases = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"GitHub API error {e.code}: {url}")

    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    items = []

    for release in releases:
        if release.get("draft") or release.get("prerelease"):
            continue

        published_at = release.get("published_at", "")
        if not published_at:
            continue

        pub_date = datetime.fromisoformat(published_at.replace("Z", "+00:00"))
        if pub_date < cutoff:
            break

        # リリースノートの冒頭を概要として使う
        body = (release.get("body") or "").strip()
        # Markdown の見出し・チェックボックスを除去して読みやすくする
        import re
        body = re.sub(r"^#{1,3}\s+", "", body, flags=re.MULTILINE)
        body = re.sub(r"- \[[ x]\] ", "- ", body)
        body = body.replace("\r\n", " ").replace("\n", " ").strip()
        summary = body[:200] + ("..." if len(body) > 200 else "")

        items.append({
            "display": display,
            "repo": f"{owner}/{repo}",
            "version": release.get("tag_name", ""),
            "title": release.get("name") or release.get("tag_name", ""),
            "link": release.get("html_url", ""),
            "published_at": pub_date.strftime("%Y-%m-%d"),
            "summary": summary,
        })

    return items


def fetch_github_releases(days=7):
    """watched_repos.json の全リポジトリのリリースを取得する"""
    repos = load_watched_repos()
    all_releases = []

    for repo_conf in repos:
        try:
            releases = fetch_releases_for_repo(
                repo_conf["owner"],
                repo_conf["repo"],
                repo_conf["display"],
                days=days,
            )
            all_releases.extend(releases)
            print(f"  ✓ {repo_conf['display']}: {len(releases)} 件のリリース", flush=True)
        except Exception as e:
            print(f"  ✗ {repo_conf['display']}: {e}", flush=True)

    return all_releases


if __name__ == "__main__":
    releases = fetch_github_releases(days=7)
    if not releases:
        print("直近7日以内のリリースはありません。")
    for r in releases:
        print(f"[{r['published_at']}] {r['display']} {r['version']}")
        print(f"  {r['title']}")
        print(f"  {r['link']}")
        if r["summary"]:
            print(f"  {r['summary'][:100]}")
        print()
