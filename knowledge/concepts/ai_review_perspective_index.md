# ai_review_perspective_index

## 概要
バイブコーディングを含むAI活用開発において、設計・実装の品質を高めるためにAIに聞くべき観点の索引。
「今日必要な2〜3項目だけ拾えばいい」という段階的活用が前提。

## 使い方
各項目についてAIに「初心者にもわかるように教えて」と質問することで、知識を都度補完していく。
new-project スキルでは、プロジェクト種別（API / フロントエンド / フルスタック）に応じて参照するセクションを絞る。

## 設計レビュー観点

### A. アーキテクチャ設計
レイヤードアーキテクチャ / ヘキサゴナルアーキテクチャ(Ports and Adapters) / オニオンアーキテクチャ / クリーンアーキテクチャ / マイクロサービス vs モノリス vs モジュラーモノリス / イベント駆動アーキテクチャ(EDA) / CQRS / イベントソーシング / BFF(Backend for Frontend) / サーバーレスアーキテクチャ

### B. データとインターフェース
正規化と非正規化のトレードオフ / ERモデリング / スタースキーマ / スノーフレークスキーマ / イミュータブルデータモデル / Single Source of Truth / REST原則 / GraphQL vs REST vs gRPC / バージョニング戦略 / ページネーション / HATEOAS / OpenAPI / Swagger仕様 / 冪等性キー(Idempotency Key) / エラーレスポンス設計(RFC 7807) / ACID特性 / 楽観ロック vs 悲観ロック / 分散トランザクション / Sagaパターン / 結果整合性(Eventual Consistency) / 冪等性 / Outboxパターン / At-least-once / At-most-once / Exactly-once delivery / Dead Letter Queue(DLQ) / Pub/Sub vs メッセージキュー / cache-aside / write-through / write-back パターン / キャッシュスタンピード対策 / CDNエッジキャッシュ

### C. UX設計
ペルソナ / カスタマージャーニーマップ / Jobs to Be Done(JTBD) / メンタルモデル / ユーザビリティテスト / A/Bテスト / ワイヤーフレーム / プロトタイピング / マイクロインタラクション / フィードバック設計 / エラー防止・エラーリカバリー / Undo/Redo / オンボーディング設計 / 空状態(Empty State)設計 / ニールセンの10ユーザビリティヒューリスティクス / 認知負荷(Cognitive Load) / ヒックの法則 / フィッツの法則 / ミラーの法則(7±2) / ゲシュタルト原則 / WCAG / WAI-ARIA / インクルーシブデザイン / HEART フレームワーク / NPS / SUS

### D. 非機能・運用
水平スケーリング vs 垂直スケーリング / ステートレス設計 / データシャーディング / レプリケーション / CAP定理 / PACELC定理 / サーキットブレーカーパターン / バルクヘッドパターン / 指数バックオフとリトライ / カナリアリリース / Blue-Greenデプロイ / フィーチャーフラグ / RTO/RPO / ログ・メトリクス・トレース(3本柱) / 分散トレーシング(OpenTelemetry) / SLI/SLO/SLA / ゴールデンシグナル / Infrastructure as Code / 12 Factor App / Kubernetes / GitOps / サービスメッシュ / Zero-downtime deployment

### E. セキュリティ設計
Defense in Depth / 侵害前提の設計(Assume Breach) / ゼロトラスト(Zero Trust) / 最小権限の原則 / デフォルト拒否(Deny by Default) / 監査証跡(Audit Trail) / データ分類 / マルチテナントのテナント隔離 / クラウドのセキュリティベースライン

## コードレビュー観点

### F. UI設計・フロントエンド
タイポグラフィ / カラー理論 / グリッドシステム / 視覚的階層 / CRAP原則 / デザイントークン / アトミックデザイン / Storybook / Figma / Presentational Component vs Container Component / Compound Component / Controlled vs Uncontrolled / Composition over Configuration / CSS Modules / CSS-in-JS / Utility-First(Tailwind CSS) / Container Queries / ダークモード対応 / Redux / Zustand / Jotai / TanStack Query / 楽観的更新(Optimistic Update) / Core Web Vitals / Code Splitting / Lazy Loading / Tree Shaking / 仮想スクロール / React.memo / useMemo / useCallback / SSR/SSG/ISR/CSR / セマンティックHTML / ARIA属性 / フォーカス管理 / prefers-reduced-motion

### G. 設計原則とパターン
SOLID原則(SRP/OCP/LSP/ISP/DIP) / DRY / KISS / YAGNI / 関心の分離 / Tell, Don't Ask / Law of Demeter / Composition over Inheritance / Fail Fast / GoFデザインパターン全種（Factory Method / Builder / Singleton / Adapter / Decorator / Facade / Observer / Strategy / Template Method 等） / Repository パターン / Unit of Work / Service Layer / Specification パターン / Null Object パターン

### H. コード品質
意味のある命名 / 単一責任の関数 / 副作用の最小化 / コメントは「なぜ」を書く / マジックナンバーの排除 / Code Smell全種（長すぎるメソッド / 神クラス / Feature Envy / Data Clumps 等） / リファクタリング手法（メソッドの抽出 / ガード節の導入 等） / 型駆動設計 / Make Illegal States Unrepresentable / 値オブジェクト / Null安全 / 不変性(Immutability) / 純粋関数 / モナド(Option/Either/Result) / 例外 vs Result型 / Fail Fast / 指数バックオフ with jitter

### I. テスト
テストピラミッド / テスティングトロフィー / TDD / Red-Green-Refactor / BDD / テストカバレッジの罠 / Flaky テスト対策 / ユニット/統合/E2E/コンポーネント/スナップショット/プロパティベース/ミューテーション/Visual Regression/アクセシビリティ/負荷/ストレス/ペネトレーション/ファジング テスト / コントラクトテスト / Dummy/Stub/Spy/Mock/Fake / 同値分割 / 境界値分析 / デシジョンテーブル

### J. 実装技術
スレッドセーフティ / レースコンディション / TOCTOU / デッドロック対策 / async/await / Reactive Programming / N+1問題 / インデックス設計 / EXPLAIN / Big O記法 / メモリリーク / プロファイリング / 早すぎる最適化を避ける / バッチ処理 vs ストリーム処理 / コネクションプール / バックプレッシャー / gzip/Brotli圧縮 / CDN活用

### K. プロセスとドキュメント
ADR / README / APIドキュメント / C4モデル / UML / シーケンス図 / Gitコミット粒度 / Conventional Commits / ブランチ戦略 / PRレビュー作法 / SemVer / CI/CD / フィーチャーフラグ

### L. セキュアコーディング
STRIDE / NIST攻撃者分類 / TLS 1.2以上 / HSTS / CSP / CORS / CRYPTREC暗号リスト / bcrypt/Argon2/scrypt / KMS/HSM/Vault / Authorization Code Flow + PKCE / OIDC / MFA(TOTP/WebAuthn/FIDO2) / Cookie属性(Secure/HttpOnly/SameSite) / JWT / RBAC/ABAC / IDOR対策 / ホワイトリスト方式 / SQLインジェクション / OSコマンドインジェクション / LDAP/NoSQLインジェクション / テンプレートインジェクション / デシリアライズ攻撃 / XSS（コンテキスト別エスケープ） / オープンリダイレクト / SSRF対策（DNS Rebinding / IMDSv2 等） / サプライチェーン攻撃対策 / SBOM / Dependabot/Snyk/Trivy / OWASP Top 10 / OWASP ASVS

### M. 参考書籍・フレームワーク
Clean Architecture / Clean Code / リファクタリング / エリック・エヴァンスのDDD / 達人プログラマー / リーダブルコード / OWASP Top 10・ASVS・Testing Guide / IPA「安全なウェブサイトの作り方」 / CWE(Common Weakness Enumeration)

## 関連概念
- `vibe_coding_security.md`
- `attack_surface_management.md`
- `solid_principles.md`
- `ci_cd.md`
- `adr.md`
- `ddd.md`

## ソース
- 2026-04-12・https://qiita.com/Akira-Isegawa/items/00f23d206c504db2ac3b

## タグ
vibe-coding, review-checklist, security, design-patterns, testing, frontend, architecture
