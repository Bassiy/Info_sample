# 仮想マシン（VM）

## 概要
物理サーバー1台の上に、OSごと独立した複数の仮想コンピュータを動かす技術。

## 理解したこと
- 「OSを人数分用意する」イメージ。各VMが独自のOSカーネルを持つ
- ハイパーバイザーがVMを管理し、ハードウェアリソースを分配する
- **Type 1（ベアメタル）**：ハイパーバイザーがハードウェアに直接乗る（VMware ESXi, Hyper-V）→ データセンター・本番向け
- **Type 2（ホスト型）**：ホストOSの上にハイパーバイザーが乗る（VirtualBox, VMware Fusion）→ 開発・学習向け
- 重い・起動遅い（分オーダー）・サイズGB単位だが、分離強度が強い
- Claude CoworkのLinux VMはMac上で動くType 2に相当。外部HTTP通信やlocalhost等はハイパーバイザー側で制限される

## 関連概念
- virtualization.md（仮想化の上位概念・2つの方向性）
- container.md（OSを共有するより軽量な仮想化手法）
- cowork_vm_sandbox.md（Claude CoworkにおけるVMの具体例）
- cloud_infrastructure.md（AWS EC2・GCP Compute EngineはVMの提供サービス）

## ソース
- 2026-03-22・会話による学習

## タグ
VM, 仮想マシン, 仮想化, hypervisor, Type1, Type2, インフラ
