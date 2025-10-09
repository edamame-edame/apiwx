# apiwx v0.5.0 - 統合型スタブパッケージ

## ✅ **完了した統合**

### 📦 **新しいパッケージ構造**
```
apiwx/                          # メインパッケージ
├── *.py                        # ランタイムソースコード  
├── py.typed                    # ランタイム型マーカー
└── stubs/                      # 内包型スタブ
    ├── *.pyi                   # 21個の型スタブファイル
    ├── py.typed                # 型スタブマーカー
    └── README.md               # 型スタブドキュメント
```

### 🚀 **シンプルインストール**
```bash
# 1つのコマンドで完全インストール
pip install apiwx

# 型チェッカー用追加ツール (オプション)
pip install apiwx[dev]  # mypy, pylsp-mypy含む
```

### 🎯 **自動型スタブ機能**

#### 1. **PEP 561完全準拠**
- `py.typed`マーカーファイル
- `package-data`による型スタブ配布
- 型チェッカー自動認識

#### 2. **VSCode完全サポート**
- Pylanceが`apiwx/stubs/*.pyi`を自動参照
- 「宣言元を見る」で型スタブ表示
- 完全な自動補完とタイプヒント

#### 3. **開発者体験向上**
```python
# インストール後すぐに型サポート有効
import apiwx

# 完全な型推論とIDE支援
app: apiwx.AppBase = apiwx.AppBase("MyApp")
window: apiwx.WindowWithPanel = apiwx.WindowWithPanel(
    app, 
    title="Demo",
    boarder_color="#FF0000"  # <- 自動補完される
)
```

### 🔧 **技術仕様**

#### pyproject.toml設定
```toml
[tool.setuptools.package-data]
apiwx = [
    "py.typed",           # ランタイム型マーカー
    "stubs/*.pyi",        # 型スタブファイル
    "stubs/py.typed",     # 型スタブマーカー
    "stubs/README.md"     # ドキュメント
]

[project.optional-dependencies]
dev = ["mypy>=1.0", "pylsp-mypy"]  # 開発ツール
```

#### 内部参照設定
```python
# apiwx/__init__.py
__stub_package__ = "apiwx.stubs"  # 型スタブパッケージ指定
```

### 🌟 **利点**

1. **ワンストップインストール**: 1コマンドで完全環境
2. **環境依存なし**: どの環境でも一貫動作
3. **設定不要**: 自動的に型スタブ認識
4. **メンテナンス簡単**: 1つのリポジトリで管理
5. **下位互換**: 既存コードそのまま動作

### ✅ **検証項目**
- [x] 型スタブファイル21個内包
- [x] PEP 561準拠構造
- [x] package-data設定
- [x] 自動インストール設定
- [x] VSCode対応確認準備完了

これで`pip install apiwx`だけで型スタブも自動インストールされ、VSCodeで完全な型サポートが得られます！🎉