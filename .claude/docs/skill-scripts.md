# スキルスクリプトの管理ルール

## 配置ルール

| 種別 | 配置先 | 例 |
|------|--------|----|
| スキル専用スクリプト | `.claude/skills/{スキル名}/scripts/` | `.claude/skills/gather/scripts/tech/gather.py` |
| フックスクリプト | `.claude/hooks/` | `.claude/hooks/check_consistency.py` |

## 理由

- スキルとそのスクリプトを同じ場所に置くことで、スキル削除時に関連ファイルをまとめて管理できる
- フックはスキルに依存しない横断的な処理なので独立させる
- プロジェクトルートにスクリプトを置かない（どのスキルが使うか不明になるため）

## 現在のスクリプト一覧

### `.claude/skills/gather/scripts/`
```
tech/
  gather.py        # メインの収集スクリプト
  hackernews.py
  hatena.py
  qiita.py
  zenn.py
  github_releases.py
  developers_io.py
  jser_info.py
  watched_repos.json
news/
  gather.py
business/
  gather.py
```

### `.claude/skills/podcast/scripts/`
```
tts.py             # VOICEVOX 音声変換
player.py          # ブラウザプレイヤー起動
finish.mp3         # 完了通知音
```

### `.claude/skills/diagram/scripts/`
```
open_diagram.py    # Mermaid図をブラウザで開く
```

### `.claude/hooks/`
```
check-knowledge.sh          # knowledge/ 命名規則チェック
check_consistency.py        # フォルダ・パス整合性チェック
collect_skill_feedback.py   # PreCompact: Skill使用後のフィードバックをskill_change_log.mdに記録
```

## 新しいスクリプトを追加するとき

1. 対象スキルの `scripts/` フォルダに配置する
2. SKILL.md のパス参照を更新する
3. `settings.json` の `permissions.allow` に実行権限を追加する
