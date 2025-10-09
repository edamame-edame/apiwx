# apiwx v0.5.0 型スタブ分離完了

## ✅ **完了した変更**

### 1. **PEP 561準拠の型スタブパッケージ作成**
```
apiwx-stubs/              # 型スタブ専用パッケージ
├── *.pyi                 # 21個の型スタブファイル
├── py.typed              # PEP 561マーカー
├── setup.py              # 独立したセットアップ
└── README.md             # 使用方法説明
```

### 2. **メインパッケージから型スタブ除去**
```
apiwx/                    # ランタイム専用パッケージ
├── *.py                  # ソースコードのみ
├── py.typed              # ランタイム型情報マーカー
└── __init__.py           # 空の型情報
```

### 3. **設定ファイル更新**
- `pyproject.toml`: 型スタブ参照を削除
- メインパッケージは型スタブを含まない

## 🚀 **使用方法**

### インストール (2パッケージ)
```bash
# ランタイムライブラリ
pip install ./apiwx

# 型スタブ (開発時)
pip install ./apiwx-stubs
```

### 型チェッカーの動作
```python
import apiwx  # VSCodeは apiwx-stubs/*.pyi を参照

app = apiwx.AppBase("MyApp")           # 型チェック有効
window = apiwx.WindowWithPanel(app)    # 自動補完有効
```

## 🎯 **解決される問題**

1. **VSCode「宣言元を見る」が型スタブを参照**
2. **どんな環境でも一貫した動作**
3. **PEP 561完全準拠**
4. **型チェッカーの最適化**

## 📦 **配布戦略**

### Option A: 2つの独立パッケージ
- `apiwx` (ランタイム)
- `apiwx-stubs` (型情報)

### Option B: extras_require
```bash
pip install apiwx[typing]  # 両方インストール
```

## ✅ **確認済み**
- 21個の型スタブファイル正常コピー
- メインパッケージから型スタブ完全除去
- PEP 561準拠構造
- setup.py設定完了