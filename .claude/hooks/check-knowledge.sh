#!/bin/bash
# knowledge/ 以下のファイル命名規則チェック

INPUT=$(cat)
FILE=$(echo "$INPUT" | jq -r ".tool_input.file_path // empty")

# knowledge/ 以下のファイルでなければスルー
[[ "$FILE" != *"/knowledge/"* ]] && exit 0

BASENAME=$(basename "$FILE")

# concepts/ のチェック：英語スネークケース（小文字・アンダースコア・数字）
if [[ "$FILE" == *"/knowledge/concepts/"* ]]; then
  if ! echo "$BASENAME" | grep -qE '^[a-z][a-z0-9_]*\.md$'; then
    echo "ERROR: concepts/ のファイル名は英語スネークケースにしてください"
    echo "  NG: $BASENAME"
    echo "  OK 例: tcp_ip.md, docker_compose.md"
    exit 2
  fi
fi

# map/ のチェック：ケバブケース（小文字・ハイフン・数字）＋フラット構造（サブフォルダなし）
if [[ "$FILE" == *"/knowledge/map/"* ]]; then
  # サブフォルダに置くのはNG（フラット構造を強制）
  RELATIVE="${FILE##*/knowledge/map/}"
  if [[ "$RELATIVE" == *"/"* ]]; then
    echo "ERROR: map/ はフラット構造です。サブフォルダを作らず直下に置いてください"
    echo "  NG: map/$RELATIVE"
    echo "  OK 例: map/osi-and-tcp-ip.md, map/encapsulation-as-extension.md"
    exit 2
  fi

  if ! echo "$BASENAME" | grep -qE '^[a-z][a-z0-9-]*\.md$'; then
    echo "ERROR: map/ のファイル名はケバブケースにしてください"
    echo "  NG: $BASENAME"
    echo "  OK 例: osi-and-tcp-ip.md, github-auth.md"
    exit 2
  fi
fi

exit 0
