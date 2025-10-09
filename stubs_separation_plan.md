# apiwx-stubs パッケージ作成計画

## 問題の根本原因
- apiwx/ 内にソースコード(.py)と型スタブ(.pyi)が混在
- VSCode/Pylanceはソースコードを優先参照
- PEP 561: 型スタブはソースと分離すべき

## 解決策: apiwx-stubs として別パッケージ化

### 新しい構造
```
apiwx/                    # メインパッケージ (型注釈なし)
├── core.py
├── colors.py
├── __init__.py
└── py.typed             # 空ファイル

apiwx-stubs/             # 型スタブ専用パッケージ
├── core.pyi
├── colors.pyi
├── __init__.pyi
├── py.typed
└── setup.py
```

### PEP 561準拠の利点
1. 型チェッカーが確実に.pyiを参照
2. どんな環境でも動作
3. 型情報とランタイムの完全分離
4. パフォーマンス向上

### 実装手順
1. apiwx-stubs/ ディレクトリ作成
2. 型スタブファイル移動
3. apiwx-stubs/setup.py 作成
4. メインパッケージから stubs/ 削除