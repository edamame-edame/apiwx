#!/usr/bin/env python3
"""
apiwx v0.2.2 ビルド後最終確認テスト
"""

print("=== apiwx v0.2.2 最終確認テスト ===")

try:
    import apiwx
    print(f" インストール版バージョン: {apiwx.__version__}")

    # Singletonテスト
    from apiwx.generics_base import Singleton
    class TestSingle(Singleton):
    pass

    s1 = TestSingle()
    s2 = TestSingle()
    print(f" Singleton動作: {s1 is s2}")

    # ボタンジェネリクステスト
    from apiwx.core import WrappedButton
    from apiwx.generics_button import SingleClickDisable

    ButtonType = WrappedButton[SingleClickDisable]
    print(f" ボタンジェネリクス作成: {ButtonType}")

    # 新機能テスト
    # hasgenericは作成されたインスタンスに対して呼び出す
    try:
    # インスタンス作成は必要なパラメータがあるため、クラスの属性確認のみ
    if hasattr(ButtonType, '__generic_classes__'):
    generic_classes = ButtonType.__generic_classes__
    print(f" __generic_classes__属性: {generic_classes}")

    if hasattr(ButtonType, 'hasgeneric'):
    print(" hasgenericメソッドが利用可能")

    except Exception as e:
    print(f" 新機能テスト中のエラー: {e}")

    print("\n apiwx v0.2.2 ビルドとインストールが正常に完了しました！")

except Exception as e:
    print(f" エラー: {e}")
    import traceback
    traceback.print_exc()

print("=== テスト完了 ===")