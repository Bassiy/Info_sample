#!/usr/bin/env python3
"""
整合性チェックスクリプト
Write/Edit フック後に呼ばれ、パス参照の整合性をチェックする

チェック対象：
- CLAUDE.md に書かれたフォルダパスが存在するか
- SKILL.md 内のファイルパス参照が存在するか（CLAUDE.md のフォルダ構成を基準に判定）
"""

import sys
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent


def check_claude_md():
    """CLAUDE.md の「## フォルダ構成」セクションに書かれたパスと実際のフォルダを照合"""
    claude_md = PROJECT_ROOT / ".claude" / "CLAUDE.md"
    if not claude_md.exists():
        return []

    content = claude_md.read_text()

    # 「## フォルダ構成」セクションのみ抽出（次の ## まで）
    match = re.search(r'## フォルダ構成\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if not match:
        return []
    section = match.group(1)

    # インデント構造を解析して完全パスを再構築
    # 例: `sources/` → sources/
    #       `tech/`  → sources/tech/
    full_paths = []
    stack = []  # (indent_level, path_component)

    for line in section.splitlines():
        m = re.match(r'^(\s*)- `([a-zA-Z][a-zA-Z0-9_-]*/)`', line)
        if not m:
            continue
        indent = len(m.group(1))
        component = m.group(2)

        # インデントに合わせてスタックを調整
        level = indent // 2
        stack = stack[:level]
        stack.append(component)

        full_path = "".join(stack)
        full_paths.append(full_path)

    # 順方向チェック：CLAUDE.md に書いてあるフォルダが実在するか
    errors = []
    for path_str in full_paths:
        if not (PROJECT_ROOT / path_str).exists():
            errors.append(f"CLAUDE.md: `{path_str}` が存在しません")

    # 逆方向チェック：実在するトップレベルフォルダが CLAUDE.md に書いてあるか
    # 隠しフォルダ（.で始まる）と数字始まり（日付・連番フォルダ）は除外
    documented_top = {p.split("/")[0] + "/" for p in full_paths}
    for d in PROJECT_ROOT.iterdir():
        if not d.is_dir():
            continue
        if d.name.startswith(".") or d.name[0].isdigit():
            continue
        folder = d.name + "/"
        if folder not in documented_top:
            errors.append(f"CLAUDE.md: `{folder}` が存在するが未記載です")

    return errors


def get_top_level_dirs():
    """CLAUDE.md のフォルダ構成からトップレベルディレクトリ名を取得"""
    claude_md = PROJECT_ROOT / ".claude" / "CLAUDE.md"
    if not claude_md.exists():
        return set()

    content = claude_md.read_text()
    match = re.search(r'## フォルダ構成\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if not match:
        return set()

    dirs = set()
    for line in match.group(1).splitlines():
        m = re.match(r'^- `([a-zA-Z][a-zA-Z0-9_-]*/)`', line)
        if m:
            dirs.add(m.group(1))
    return dirs


def check_skill_md(file_path):
    """SKILL.md 内のパス参照をチェック（CLAUDE.md のトップレベルパスを基準に）"""
    errors = []
    content = Path(file_path).read_text()
    skill_name = Path(file_path).parent.name

    # CLAUDE.md のトップレベルディレクトリを取得（例: {"sources/", "meal/", "knowledge/", ...}）
    top_dirs = get_top_level_dirs()

    # バッククォート内のパスを抽出し、トップレベルディレクトリで始まるものをチェック
    for match in re.finditer(r'`([a-zA-Z][a-zA-Z0-9/_.-]+)`', content):
        ref = match.group(1)
        # プレースホルダーを除外（{...}、YYYY、slug、N番など）
        if '{' in ref or 'YYYY' in ref or 'slug' in ref or re.search(r'[A-Z]{2,}', ref):
            continue
        # いずれかのトップレベルディレクトリで始まるパスが対象
        if not any(ref.startswith(d) for d in top_dirs):
            continue
        if not (PROJECT_ROOT / ref).exists():
            errors.append(f"{skill_name}/SKILL.md: `{ref}` が存在しません")

    # ../xxx 形式の相対リンクもチェック
    for match in re.finditer(r'\]\((\.\./[a-zA-Z0-9/_.-]+)\)', content):
        ref = match.group(1)
        if '{' in ref or 'slug' in ref:
            continue
        full_path = (Path(file_path).parent / ref).resolve()
        if not full_path.exists():
            errors.append(f"{skill_name}/SKILL.md: `{ref}` が存在しません")

    return errors



def main():
    sys.stdin.read()  # フック経由の stdin を読み捨て（ファイル種別によらず全チェック）

    # ファイルの種類に関わらず毎回全チェック
    errors = []

    # CLAUDE.md のフォルダ構成チェック
    errors.extend(check_claude_md())

    # 全 SKILL.md のパス参照チェック
    skills_dir = PROJECT_ROOT / ".claude" / "skills"
    for skill_md in skills_dir.glob("*/SKILL.md"):
        errors.extend(check_skill_md(str(skill_md)))

    if errors:
        print("⚠️  整合性チェック")
        for err in errors:
            print(f"  {err}")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
