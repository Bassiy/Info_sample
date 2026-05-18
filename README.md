# Info_sample

Claude Code を使った知識管理・学習システムのサンプルです。

## 前提

- [Claude Code](https://claude.ai/code) がインストールされていること

## 構成

```
.
├── knowledge/
│   ├── concepts/   # 技術概念（1ファイル1概念）
│   └── map/        # クロスドメインなパターン・原則
├── sources/        # 収集した情報の生データ（.gitignore 対象）
├── note/           # 一時メモ（.gitignore 対象）
└── .claude/
    ├── CLAUDE.md   # プロジェクト指示
    ├── skills/     # スキル一覧
    └── hooks/      # 自動チェック・同期
```

## 使い方

```bash
git clone https://github.com/Bassiy/Info_sample
cd Info_sample
claude  # Claude Code を起動
```

起動後、`/guide` でスキル一覧を確認できます。

## 主なスキル

| スキル | 説明 |
|--------|------|
| `/study` | 本・記事の内容をフェインマン式で深掘り |
| `/learn` | 学んだことを knowledge/ に保存 |
| `/recall` | knowledge/ の内容を検索・復習 |
| `/gather` | 技術トレンドを収集 |
| `/note` | その日のメモを作成 |
| `/connect` | 概念間のつながりを発見 |
| `/diagram` | Mermaid 図を生成 |
