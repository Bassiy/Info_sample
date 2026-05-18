#!/bin/bash
# 編集後に自動でcommit + pushする

INPUT=$(cat)
FILE=$(echo "$INPUT" | jq -r ".tool_input.file_path // empty")
TOOL=$(echo "$INPUT" | jq -r ".tool_name // empty")

git add -A

# 変更がなければスキップ
git diff --cached --quiet && exit 0

# プロジェクトルートからの相対パスに変換
if [ -n "$FILE" ]; then
  ROOT=$(git rev-parse --show-toplevel 2>/dev/null)
  REL=$(python3 -c "import os; print(os.path.relpath('$FILE', '$ROOT'))" 2>/dev/null || basename "$FILE")
else
  REL="unknown"
fi

# Write=新規作成、Edit=更新
if [ "$TOOL" = "Write" ]; then
  MSG="add: $REL"
else
  MSG="update: $REL"
fi

git commit -m "$MSG"
git push
