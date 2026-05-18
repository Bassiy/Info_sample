# クラウドインフラ

## 概要
物理サーバーを自前で持たず、AWS・GCPなどのクラウドサービスからサーバーを借りてアプリを動かす仕組み。

## 理解したこと
- クラウド = サーバーのレンタルサービス。AWSはAmazon、GCPはGoogle、AzureはMicrosoftが運営
- デフォルトでインターネットに繋がっているため、DBなど外に見せたくないものは保護が必要
- VPC（仮想プライベートネットワーク）でクラウド内に閉じた内部ネットワークを作り、DBを外から隔離する

## GCPの主要サービスの役割
| サービス | 役割 | 例え |
|---|---|---|
| Cloud Run | アプリが動く場所（サーバーレス） | 店舗 |
| Cloud SQL | マネージドDB | 倉庫 |
| VPC | 内部ネットワーク | 店舗と倉庫をつなぐ裏道 |
| GCLB + Cloud Armor + IAP | 入口の関所（ロードバランサー・WAF・認証） | 警備員・金属探知機・受付 |
| Artifact Registry | コンテナイメージの保管庫 | 完成品の倉庫 |
| Cloud Tasks | 非同期タスクキュー。レート制御・リトライ対応 | 順番待ちの受付窓口 |
| Cloud Scheduler | 定期バッチ実行（Cronに相当） | タイマー |
| Secret Manager | 認証情報の安全な保管庫 | 金庫 |

## AWSの主要サービスの役割
| サービス | 役割 | GCP対応 |
|---|---|---|
| ECS + Fargate | コンテナ実行（Fargateはサーバーレス版） | Cloud Run |
| ECR | コンテナイメージの保管庫 | Artifact Registry |
| RDS | マネージドDB | Cloud SQL |
| SQS | 非同期メッセージキュー | Cloud Tasks |
| EventBridge Scheduler | 定期バッチ実行（Cron相当） | Cloud Scheduler |
| Secrets Manager | 認証情報の安全な保管庫 | Secret Manager |
| Organizations | 複数AWSアカウントを一元管理 | 複数プロジェクト |
| Identity Center | 1回ログインで複数アカウントを使い分けるSSO | - |
| WAF | 不正リクエストを遮断するファイアウォール | Cloud Armor |
| Session Manager | ポートを開けずにEC2へ安全に接続 | IAP |

## インフラ設計の本質
「本番で何かあったとき、被害を最小限に止める設計」
- 環境分離（stg/prd）：別プロジェクト・別アカウントにして事故の波及を防ぐ
- 1リソース1サービスアカウント（GCP）/ 1リソース1セキュリティグループ（AWS）：侵害時の影響範囲を限定する
- 入口を一本化して関所を多層化する

## GCPのセキュリティポイント
- **Ingress=内部に設定**：Cloud RunのURLを直接公開せず、GCLB経由のみ受け付ける
- **JSONキー不使用**：権限借用（Impersonation）で一時トークンを取得
- **Direct VPC Egress**：Cloud RunからCloud SQLへVPC内プライベート接続

## AWSのセキュリティポイント
- **プライベートサブネットにECSを配置**：インターネットから直接到達不能にする
- **Session Manager**：SSHポート（22番）を開けずにEC2へ接続。攻撃の入口を減らす
- **NAT インスタンス**：NAT Gateway（月7,000円）の代わりにEC2で自作（月数百円以下）でコスト削減

## AWSのコスト削減のポイント
- **Fargate Spot**：通常Fargateの余剰リソース版。中断リスクあるがステートレスなWorkerに最適（月2,000円→数百円以下）
- **NAT EC2インスタンス**：NAT GatewayをEC2で自作（月7,000円→数百円以下）
- **RDS自動起動対策**：RDSは7日間停止すると自動起動する仕様があるため、EventBridgeで週1回手動起動して回避

## 非同期処理の選定基準
- GCP：Pub/Sub プル型（ゼロスケール不可）・プッシュ型（10分制限）→ Cloud Tasks採用
- AWS：SQS + サイドカーパターンでWorkerを配置。失敗メッセージはデッドレターキューへ

## 関連概念
- cloud_service_models.md（IaaS・PaaS・SaaSの分類）
- separation_of_concerns（セキュリティ設計にも同じ原則が効く）
- ci_cd
- short_lived_token（権限借用・JSONキー不使用の考え方）
- sidecar_pattern（ECS上でのWorker配置パターン）

## ソース
- 2026-03-08・https://zenn.dev/so_engineer/articles/728f4336a0aac4（GCP版）
- 2026-03-16・https://zenn.dev/so_engineer/articles/ff5d595a488df0（AWS版）

## タグ
クラウド, GCP, AWS, インフラ, VPC, セキュリティ, アーキテクチャ, ECS, Fargate, SQS, 権限借用
