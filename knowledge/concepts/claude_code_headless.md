# Claude Code 非対話実行（Headless）

## 概要
`claude -p` フラグでClaude Codeをスクリプトやcronジョブから非対話的に1回実行する手法。

## 理解したこと
- `claude -p "プロンプト"` で対話なしに実行して終了する
- cronに登録すれば定期自動実行が可能
- Proプランの認証を使うためAPIキー・API料金が不要
- ラズパイ等の常時起動サーバーで使うのに向いている
- CLAUDE.md・スキル・既存設定がそのまま動くため移植コストが低い
- `--output-format json` を付けるとJSONで結果が返り、プログラムから扱いやすくなる
- Python/TypeScriptからsubprocessとして呼び出すことで「LLMをAPIのように使う」実装が可能
- `--allowedTools WebSearch,WebFetch` でMCPツールの使用を許可できる
- トークン消費を抑えるには「渡す文字数を絞る」「バッチ処理」「再生成条件を設ける」の3つが有効
- Feed Curatorがこのパターンの実践例：TypeScriptから `spawn("claude", ["-p", "--output-format", "json", prompt])` で呼び出し、RSSキュレーションを実現

```python
# Pythonからの呼び出し例
import subprocess, json

result = subprocess.run(
    ["claude", "-p", "--output-format", "json", "この記事を要約して"],
    input="記事本文...",
    capture_output=True, text=True
)
data = json.loads(result.stdout)
```

## 関連概念
- claude_code_context_management
- openclaw
- ci_cd
- bun
- llm_as_judge

## ソース
- 2026-03-22・会話から
- 2026-04-04・https://zenn.dev/caphtech/articles/feed-curator-ai-rss-with-claude-code

## タグ
Claude Code, automation, cron, headless, raspberry pi, scripting, subprocess, pipe mode
