# apiwx v0.5.0 型システム修正案

## 修正案 1: インライン型注釈への移行 (推奨)

### 概要
- 型スタブ(.pyi)を削除
- ソースコード(.py)に直接型注釈を追加
- VSCodeが確実にソースの型情報を認識

### 利点
- VSCodeで「宣言元を見る」が正しく動作
- 型情報とソースコードが同期
- メンテナンスが簡単

### 実装
```python
# apiwx/core.py (例)
from typing import Optional, Union, TypeVar, Generic
import wx

T = TypeVar('T')

class App(Generic[T]):
    def __init__(self, name: str = "apiwx", redirect: bool = False) -> None:
        self.name = name
        # 実装...
```

### 必要作業
1. stubs/フォルダ削除
2. 各.pyファイルに型注釈追加
3. pyproject.toml更新

---

## 修正案 2: 別パッケージとして型スタブ配布

### 概要
- apiwx-stubs として別パッケージ作成
- メインパッケージと分離

### 利点
- PEP 561完全準拠
- ランタイムオーバーヘッドなし

### 実装
```
apiwx/                 # メインパッケージ
├── core.py
└── __init__.py

apiwx-stubs/          # 型スタブパッケージ  
├── core.pyi
└── __init__.pyi
```

---

## 修正案 3: パッケージ構造変更

### 概要
- ソースとスタブを完全分離
- 型スタブのみをインストール

### 実装
```
src/apiwx/            # ソースコード
├── core.py
└── __init__.py

apiwx/                # 型スタブのみ
├── core.pyi  
├── py.typed
└── __init__.pyi
```

---

## 推奨: 修正案 1

最も確実で保守性が高い方法です。
型情報がソースコードと直接結びついているため、
VSCodeでの開発体験が最適化されます。