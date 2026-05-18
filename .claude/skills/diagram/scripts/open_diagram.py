#!/usr/bin/env python3
"""
MermaidコードをVS Codeのプレビューで表示するスクリプト。
固定ファイル .claude/skills/diagram/scripts/preview.md に書き出し、VS Codeで開く。

Usage: python3 open_diagram.py "<mermaid_code>"
       echo "<mermaid_code>" | python3 open_diagram.py
       python3 open_diagram.py  # ファイルだけ開く（コードなし）
"""

import sys
import os
import subprocess

PREVIEW_FILE = os.path.join(os.path.dirname(__file__), "preview.md")


def write_diagram(mermaid_code: str):
    mermaid_code = mermaid_code.strip()

    # コードフェンスを除去
    if mermaid_code.startswith("```"):
        lines = mermaid_code.splitlines()
        lines = [l for l in lines if not l.strip().startswith("```")]
        mermaid_code = "\n".join(lines).strip()

    content = f"# Diagram Preview\n\n```mermaid\n{mermaid_code}\n```\n"
    os.makedirs(os.path.dirname(PREVIEW_FILE), exist_ok=True)
    with open(PREVIEW_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {PREVIEW_FILE}")


def open_vscode():
    try:
        subprocess.Popen(["code", PREVIEW_FILE])
        print("Opened in VS Code")
    except FileNotFoundError:
        print(f"VS Code CLI not found. Open manually: {PREVIEW_FILE}")


def main():
    if len(sys.argv) > 1:
        mermaid_code = sys.argv[1]
        write_diagram(mermaid_code)
        open_vscode()
    elif not sys.stdin.isatty():
        mermaid_code = sys.stdin.read()
        write_diagram(mermaid_code)
        open_vscode()
    else:
        # コードなし → ファイルだけ開く
        open_vscode()


if __name__ == "__main__":
    main()
