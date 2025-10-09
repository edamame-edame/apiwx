# apiwx v0.5.0 型スタブ再生成 ToDo リスト

**作成日**: 2025年10月8日  
**対象バージョン**: apiwx v0.5.0 (PEP 8/257準拠版)  
**目的**: 最新ソースコードから漏れなく重複なく型スタブを再生成

## 📋 全体概要

### ソースファイル一覧 (18ファイル)
1. `__init__.py` - メインエクスポートモジュール
2. `colors.py` - 色定数クラス
3. `constants.py` - アライメント・定数定義
4. `core.py` - メインGUIコンポーネント群
5. `debug.py` - ロギング・デバッグシステム
6. `fontmanager.py` - フォント管理システム
7. `framestyle.py` - フレームスタイル定数
8. `generics_alias.py` - ジェネリクス型エイリアス
9. `generics_app.py` - アプリケーション用ジェネリクス
10. `generics_base.py` - Singleton/Multitonパターン
11. `generics_button.py` - ボタン用ジェネリクス
12. `generics_common.py` - 共通ジェネリクス機能
13. `generics_core.py` - ジェネリクスコアシステム
14. `generics_panel.py` - パネル用ジェネリクス
15. `generics_window.py` - ウィンドウ用ジェネリクス
16. `message.py` - メッセージボックス・ダイアログ
17. `painttool.py` - 描画ツール
18. `paneltransmodel.py` - パネル遷移管理
19. `signals.py` - シグナル・イベント処理
20. `styleflags.py` - スタイルフラグ定数
21. `uiarg.py` - UI引数・オプション管理

### 既存スタブファイル確認
- `stubs/core.pyi` ✅ (要更新)
- `stubs/generics_app.pyi` ✅ (要更新)
- `stubs/generics_common.pyi` ✅ (要更新)
- `stubs/__init__.pyi` ✅ (要更新)
- `stubs/py.typed` ✅ (維持)

---

## 🎯 フェーズ1: 基礎モジュール型スタブ生成

### ✅ Phase 1-1: コア基盤モジュール
- [ ] **colors.pyi** - 色定数とColorsクラス型定義
- [ ] **constants.pyi** - アライメント定数と基本定数型定義
- [ ] **styleflags.pyi** - スタイルフラグとenum型定義
- [ ] **framestyle.pyi** - フレームスタイル定数型定義

### ✅ Phase 1-2: コア機能モジュール  
- [ ] **core.pyi** - GUIコンポーネント群の型定義 (既存更新)
- [ ] **debug.pyi** - Logger, LogLevel, ログ関数群型定義
- [ ] **signals.pyi** - シグナル・イベント処理型定義

---

## 🎯 フェーズ2: ジェネリクスシステム型スタブ生成

### ✅ Phase 2-1: ジェネリクス基盤
- [ ] **generics_core.pyi** - BaseGenericsメタクラス・ジェネリクスコア型定義
- [ ] **generics_base.pyi** - Singleton/Multitonパターン型定義
- [ ] **generics_common.pyi** - AutoDetect, FixSize等共通ジェネリクス型定義 (既存更新)

### ✅ Phase 2-2: コンポーネント別ジェネリクス
- [ ] **generics_app.pyi** - DetectWindow等アプリ用ジェネリクス型定義 (既存更新)
- [ ] **generics_window.pyi** - ByPanelSize, DetectPanel等ウィンドウ用型定義
- [ ] **generics_panel.pyi** - WithBoarder, DetectChildren等パネル用型定義  
- [ ] **generics_button.pyi** - SingleClickDisable等ボタン用ジェネリクス型定義

### ✅ Phase 2-3: ジェネリクス統合
- [ ] **generics_alias.pyi** - 型エイリアス群 (AppBase, WindowWithPanel等) 型定義

---

## 🎯 フェーズ3: UI機能モジュール型スタブ生成

### ✅ Phase 3-1: メッセージ・ダイアログ
- [ ] **message.pyi** - MessageBox, InputDialog, show_*関数群型定義

### ✅ Phase 3-2: UI補助機能
- [ ] **uiarg.pyi** - Options, get_option等UI引数管理型定義
- [ ] **fontmanager.pyi** - FontManager型定義
- [ ] **painttool.pyi** - 描画ツール型定義

### ✅ Phase 3-3: パネル管理
- [ ] **paneltransmodel.pyi** - PanelTransModel, NotTransition型定義

---

## 🎯 フェーズ4: 統合・検証

### ✅ Phase 4-1: メイン型スタブ統合
- [ ] **__init__.pyi** - 全エクスポート型の統合定義 (v0.5.0対応更新)

### ✅ Phase 4-2: 品質検証
- [ ] **構文チェック** - 全.pyiファイルのPython構文検証
- [ ] **型チェッカー検証** - mypy/pyrightでの型チェック確認
- [ ] **IDEサポート確認** - VS Codeでの自動補完・定義ジャンプ確認
- [ ] **インポート検証** - 全型のインポート可能性確認

---

## 📝 作業ルール

### 型スタブ生成ガイドライン
1. **PEP 561準拠** - 型スタブファイル標準に従う
2. **完全性** - 全パブリックAPI要素を網羅
3. **一貫性** - 既存の型注釈と整合性を保つ
4. **精度** - ソースコードの実装と型定義の一致
5. **簡潔性** - 実装詳細を含めず型情報のみ記載

### 品質基準
- **構文エラーゼロ** - 全.pyiファイルがPython構文として有効
- **型エラーゼロ** - mypy --strict での型チェック通過
- **IDE完全サポート** - VS Code, PyCharmでの完全な自動補完
- **ドキュメント統合** - docstring情報の適切な型スタブ化

### 進捗管理
- ✅ **完了** - 型スタブ生成・検証完了
- 🔄 **作業中** - 現在作業中  
- ⏸️ **一時停止** - 作業中断可能ポイント
- ❌ **エラー** - 問題発生・要修正
- ⚠️ **警告** - 注意が必要な項目

---

## 🎯 現在の状況

**現在位置**: Phase 1-1 開始前  
**次のアクション**: colors.pyi 生成開始  
**完了率**: 0% (0/21ファイル)

### 最新の変更 (v0.5.0)
- PEP 8/257 完全準拠
- 25件のコード品質修正
- 全テスト100%通過
- docstring品質向上

これらの改善を反映した型スタブを生成する必要があります。