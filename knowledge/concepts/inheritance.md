# 継承（Inheritance）

## 概要
「AはBの一種（Is-a関係）」を表す仕組み。親クラスのプロパティ・メソッドをサブクラスが引き継ぐ。C# は単一継承のみ（親クラスは1つ）。

## 継承ツリー

```mermaid
classDiagram
    Character <|-- Hero
    Character <|-- Monster
    class Character {
        +string Name
        +int Hp
        +virtual Attack()
        +Introduce()
    }
    class Hero {
        +override Attack()
    }
    class Monster {
        +override Attack()
    }
```

## クラスの種類

| | 通常クラス | 抽象クラス | インターフェース |
|---|---|---|---|
| インスタンス化 | 可 | 不可 | 不可 |
| 実装の有無 | あり | 混在可 | なし（署名のみ） |
| 親の数 | 1つ | 1つ | 複数可 |
| 関係性 | Is-a | Is-a | Can-do |

## virtual vs abstract

| | virtual | abstract |
|---|---|---|
| 中身 | あり | なし |
| override | 任意 | 強制 |
| インスタンス化 | 可 | 不可 |

## メソッド呼び出しの流れ（virtual / override）

```mermaid
flowchart TD
    A["hero.Attack() を呼ぶ"] --> B{Hero に override あり？}
    B -->|Yes| C["Hero の Attack() を実行"]
    B -->|No| D["Character の virtual Attack() を実行"]
```

## base キーワード

親のコンストラクタを子クラスから呼ぶ仕組み。共通の初期化処理を親に一箇所まとめられる。

```csharp
abstract class Character {
    public string Name { get; private set; }
    public int Hp { get; private set; }

    public Character(string name, int hp) {
        Name = name;
        Hp = hp;
    }
}

class Hero : Character {
    public Hero(string name, int hp) : base(name, hp) { }  // 親のコンストラクタに委譲
}
```

## インスタンスのイメージ

継承したインスタンスは「親を先に生成し、子で包む」構造になっている。
サブクラス視点では、自分全体が `this`、内包する親が `base`。

```mermaid
flowchart TD
    subgraph this : Hero インスタンス
        subgraph base : Character 部分
            N["Name: Alice"]
            H["Hp: 100"]
            PA["Attack()（親の実装）"]
        end
        CA["override Attack()（Hero）\n↑ base.Attack() で上の親メソッドを呼べる"]
    end
```

## コンストラクタの実行順

`new Hero()` を呼んだとき、`base`（親）から順に初期化が走る。

```mermaid
sequenceDiagram
    participant caller as new Hero()
    participant c as base : Character()
    participant h as this : Hero()
    caller->>c: base(name, hp) で先に呼ぶ
    c-->>h: Character 部分の初期化完了
    h-->>caller: Hero インスタンス完成
```

## base.メソッド名() による親処理の活用

`override` の中で `base.Attack()` を呼ぶと、親の実装を活かしつつ子固有の処理を追加できる。

```mermaid
sequenceDiagram
    participant caller
    participant hero as this : Hero
    participant c as base : Character
    caller->>hero: hero.Attack()
    hero->>c: base.Attack()（親の共通処理）
    c-->>hero: 完了
    hero->>hero: 聖なる一撃！（子固有の処理）
    hero-->>caller: 完了
```

## 関連概念
- oop_interface
- polymorphism
- oop_encapsulation

## ソース
- 2026-05-17：会話ベースの整理（C# .NET を題材に）

## タグ
継承, OOP, C#, abstract, virtual, override, base, Is-a, this
