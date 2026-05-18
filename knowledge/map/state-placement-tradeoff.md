# 状態の置き場所トレードオフ

## 捉えるもの
「確認コストを減らすために状態をどこに置くか」という問いが、セッション管理・DNS・HTTP・認証など複数ドメインで同じトレードオフ構造として現れる。

## 関連概念
- [session_management.md](../concepts/session_management.md) — セッション管理（Cookie + Redis / JWT）
- [dns.md](../concepts/dns.md) — ネットワーク（DNSキャッシュ・TTL）
- [http.md](../concepts/http.md) — Web（HTTPキャッシュ）
- [load_balancer.md](../concepts/load_balancer.md) — インフラ（分散サーバーでの状態管理）

## 構造

### 中心にある問い
毎回確認するのはコストがかかる。だから「どこかに覚えておく」。  
**誰が覚えるか**によって速さと制御可能性が変わる。

### 3つの置き場所と具体例

| 置き場所 | 具体例 | 速さ | 無効化しやすさ |
|---|---|---|---|
| サーバー側 | Cookie + Redis | ×（毎回問い合わせ） | ◎（即時反映できる） |
| 中間サーバ | DNSキャッシュ / CDN | ○（問い合わせ削減） | △（TTLで管理） |
| クライアント側 | JWT / HTTPキャッシュ | ◎（問い合わせゼロ） | ×（有効期限頼み） |

### 各パターンのフロー

**① サーバー側に置く（Cookie + Redis）**

```mermaid
sequenceDiagram
    box クライアント
        participant C as ブラウザ
    end
    box サーバー
        participant S as アプリサーバー
        participant R as Redis
    end

    C->>S: ログイン
    S->>R: セッション書き込み（id=abc）
    S-->>C: Set-Cookie: id=abc

    C->>S: 次のリクエスト（Cookie: id=abc）
    S->>R: id=abc を照会
    R-->>S: ログイン済み
    S-->>C: レスポンス
```

**② 中間サーバに置く（DNSキャッシュ）**

```mermaid
sequenceDiagram
    box クライアント
        participant C as PC / ブラウザ
    end
    box 中間サーバ
        participant CS as キャッシュサーバ
    end
    box サーバー
        participant DNS as DNSサーバ
    end

    C->>CS: google.com の IP は？
    CS->>DNS: google.com の IP は？（初回・キャッシュなし）
    DNS-->>CS: 142.250.x.x（TTL=300s）
    CS-->>C: 142.250.x.x（キャッシュに保存）

    C->>CS: google.com の IP は？（2回目）
    CS-->>C: 142.250.x.x（キャッシュから即答・DNSサーバに聞かない）

    Note over CS: TTL切れで自動消去
```

**③ クライアント側に置く（JWT）**

```mermaid
sequenceDiagram
    box クライアント
        participant C as ブラウザ
    end
    box サーバー
        participant S as アプリサーバー
    end

    C->>S: ログイン
    S-->>C: JWT（ユーザー情報＋有効期限を暗号化したもの）

    C->>S: 次のリクエスト（JWT付き）
    Note over S: JWTを復号して確認<br/>どこにも問い合わせない
    S-->>C: レスポンス

    Note over C,S: 有効期限が来るまでサーバーは無効化できない
```

### 共通する原則
> 速さと制御のトレードオフは、**状態をどこに置くか**で決まる

- サーバーに近いほど制御しやすく、遅い
- クライアントに近いほど速く、無効化しにくい
- TTL・有効期限は「時間で鮮度を管理する」という共通の解法

### 派生する実務パターン
- JWTの有効期限を短く（15分〜1時間）設定するのはなぜか → クライアント側に置いた状態を疑似的に早く無効化するため
- DNSのTTLをサーバ移転前に短くするのはなぜか → 中間キャッシュの古い状態が早く消えるようにするため

## ソース
- 2026-05-14：/study「イラスト図解式ネットワークの基本 第5章」→ /connect での壁打ちから発見
