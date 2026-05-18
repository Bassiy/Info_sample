# ネットワーク診断コマンド

## 概要
TCP/IPネットワークの動作確認に使うOSコマンド群。WindowsとLinuxで対応するコマンドが異なる。

## 理解したこと

| 機能 | Windows | Linux |
|------|---------|-------|
| 疎通確認 | ping | ping |
| 名前解決確認 | nslookup | nslookup / dig |
| 経路確認（中継ルータ） | tracert | traceroute |
| IPアドレス・MACアドレス確認 | ipconfig | ifconfig / ip a |
| ルーティングテーブル確認 | route print | route / ip r |

- Linuxでは `ifconfig` / `route` は古いコマンドで、現在は `ip a` / `ip r` が主流
- `dig` は `nslookup` より詳細な情報を出せるLinux寄りのコマンド

## 関連概念
- routing.md
- domain_name.md
- ip_address.md

## ソース
- 2026-04-17：イラスト図解式ネットワークの基本 第3章

## タグ
ping, tracert, traceroute, nslookup, dig, ipconfig, route, ネットワーク診断, Windows, Linux
