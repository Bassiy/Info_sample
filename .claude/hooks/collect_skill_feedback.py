#!/usr/bin/env python3
"""
PreCompact フック: Skill使用後のフィードバックを収集する

コンテキスト圧縮前に会話履歴をスキャンし、
Skill呼び出し後のユーザー修正指示を sources/skill_change_log.md に保存する。
LLM不使用・ゼロトークンで動作する。
"""

import json
import sys
import re
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent.parent

CORRECTION_KEYWORDS = [
    '違う', 'ちがう', 'そうじゃない', 'そうではない',
    '修正して', '間違', 'もう少し', 'ちょっと違', '違います',
    'そうじゃなくて', 'おかしい', '変えて', '直して',
]

SKILL_PATTERN = re.compile(r'/([a-zA-Z][\w-]+)')

KNOWN_SKILLS = {
    'gather', 'deep-dive', 'learn', 'study', 'recall', 'digest',
    'idea', 'report', 'search', 'stock', 'podcast', 'recipe',
    'meal-plan', 'diagram', 'progress', 'skill-review', 'marp',
    'guide', 'fix-knowledge', 'new-project', 'skill-creator',
}


def extract_text(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return ' '.join(
            b.get('text', '') for b in content
            if isinstance(b, dict) and b.get('type') == 'text'
        )
    return ''


def parse_transcript(transcript_path):
    messages = []
    try:
        with open(transcript_path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                    if 'role' in obj:
                        messages.append(obj)
                    elif 'message' in obj and isinstance(obj['message'], dict):
                        messages.append(obj['message'])
                except json.JSONDecodeError:
                    continue
    except Exception:
        pass
    return messages


def find_feedbacks(messages):
    findings = []
    last_skill = None
    last_skill_idx = -1

    for i, msg in enumerate(messages):
        if msg.get('role') != 'user':
            continue

        content = extract_text(msg.get('content', ''))

        # スキル呼び出しを検出
        m = SKILL_PATTERN.search(content)
        if m and m.group(1).lower() in KNOWN_SKILLS:
            last_skill = m.group(1).lower()
            last_skill_idx = i
            continue

        # スキル呼び出し後10メッセージ以内の修正指示を検出
        if last_skill and (i - last_skill_idx) <= 10:
            if any(kw in content for kw in CORRECTION_KEYWORDS):
                findings.append({
                    'skill': last_skill,
                    'feedback': content[:300].replace('\n', ' '),
                })
                last_skill = None  # 1スキルにつき1件

    return findings


def append_to_log(findings):
    log_path = PROJECT_ROOT / 'sources' / 'skill_change_log.md'
    today = datetime.now().strftime('%Y-%m-%d')

    if not log_path.exists():
        log_path.write_text(
            '# Skill Change Log\n\n'
            '| 日付 | スキル | フィードバック | 対応 |\n'
            '|------|--------|---------------|------|\n'
        )

    with open(log_path, 'a') as f:
        for item in findings:
            feedback = item['feedback'].replace('|', '｜')
            f.write(f"| {today} | {item['skill']} | {feedback} | - |\n")


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    transcript_path = data.get('transcript_path', '')
    if not transcript_path or not Path(transcript_path).exists():
        sys.exit(0)

    messages = parse_transcript(transcript_path)
    findings = find_feedbacks(messages)

    if findings:
        append_to_log(findings)

    sys.exit(0)


if __name__ == '__main__':
    main()
