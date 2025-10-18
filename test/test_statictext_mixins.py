"""Test module for StaticText mixins functionality.

This module tests the new LocateByParent mixin for StaticText components,
verifying alignment functionality and positioning behavior.
"""

import sys
import os

# Add the parent directory to the path to import apiwx
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    import apiwx
    from apiwx.mixins_statictext import TextAlign, LocateByParent
    from apiwx import App, Window, Panel, StaticText
except ImportError as e:
    print(f"Import error: {e}")
    print("Please ensure apiwx is installed or run from the correct directory")
    sys.exit(1)


def test_text_align_enum():
    """Test TextAlign enum values."""
    print("Testing TextAlign enum...")
    
    # Test all enum values
    expected_values = {
        'TOP': 't',
        'TOPLEFT': 'tl', 
        'LEFT': 'l',
        'BOTTOMLEFT': 'bl',
        'BOTTOM': 'b',
        'BOTTOMRIGHT': 'br',
        'RIGHT': 'r',
        'TOPRIGHT': 'tr',
        'CENTER': 'c'
    }
    
    for name, value in expected_values.items():
        enum_member = getattr(TextAlign, name)
        assert enum_member.value == value, f"TextAlign.{name} should have value '{value}', got '{enum_member.value}'"
    
    print("✅ TextAlign enum test passed")


def test_locate_by_parent_mixin():
    """Test LocateByParent mixin functionality."""
    print("Testing LocateByParent mixin...")
    
    # Create test application and window
    app = apiwx.App("StaticText Mixin Test")
    window = apiwx.Window(app, title="Test Window", size=(400, 300))
    
    # Create StaticText with LocateByParent mixin
    class AlignedStaticText(StaticText[LocateByParent]):
        pass
    
    # Test center alignment
    text_center = AlignedStaticText(window, label="Center", align="c")
    assert text_center.align == TextAlign.CENTER, "Align should be CENTER"
    
    # Test setting alignment with enum
    text_center.align = TextAlign.TOPRIGHT
    assert text_center.align == TextAlign.TOPRIGHT, "Align should be TOPRIGHT"
    
    # Test setting alignment with string
    text_center.align = "bl"
    assert text_center.align == TextAlign.BOTTOMLEFT, "Align should be BOTTOMLEFT"
    
    print("✅ LocateByParent mixin test passed")


def test_position_calculation():
    """Test position calculation logic."""
    print("Testing position calculation...")
    
    app = apiwx.App("Position Test")
    window = apiwx.Window(app, title="Position Test", size=(400, 300))
    
    class AlignedStaticText(StaticText[LocateByParent]):
        pass
    
    # Create text component
    text = AlignedStaticText(window, label="Test Text", align="c")
    
    # Test different alignments and verify positioning logic exists
    alignments_to_test = [
        ("c", TextAlign.CENTER),
        ("tl", TextAlign.TOPLEFT), 
        ("tr", TextAlign.TOPRIGHT),
        ("bl", TextAlign.BOTTOMLEFT),
        ("br", TextAlign.BOTTOMRIGHT),
        ("t", TextAlign.TOP),
        ("b", TextAlign.BOTTOM),
        ("l", TextAlign.LEFT),
        ("r", TextAlign.RIGHT)
    ]
    
    for align_str, align_enum in alignments_to_test:
        text.align = align_str
        assert text.align == align_enum, f"Setting align to '{align_str}' should result in {align_enum}"
        
        # Verify update_location method exists and works
        text.update_location(align_enum)
        assert text.align == align_enum, f"update_location should maintain alignment as {align_enum}"
    
    print("✅ Position calculation test passed")


def test_mixin_integration():
    """Test integration with other mixin components."""
    print("Testing mixin integration...")
    
    app = apiwx.App("Integration Test")
    window = apiwx.Window(app, title="Integration Test", size=(500, 400))
    
    # Test that the mixin works with basic StaticText
    class AlignedText(StaticText[LocateByParent]):
        pass
    
    text1 = AlignedText(window, label="Top Left", align=TextAlign.TOPLEFT)
    text2 = AlignedText(window, label="Center", align=TextAlign.CENTER)
    text3 = AlignedText(window, label="Bottom Right", align=TextAlign.BOTTOMRIGHT)
    
    # Verify all texts have correct alignment
    assert text1.align == TextAlign.TOPLEFT
    assert text2.align == TextAlign.CENTER
    assert text3.align == TextAlign.BOTTOMRIGHT
    
    print("✅ Mixin integration test passed")


def test_error_handling():
    """Test error handling for invalid inputs."""
    print("Testing error handling...")
    
    app = apiwx.App("Error Test")
    window = apiwx.Window(app, title="Error Test", size=(300, 200))
    
    class AlignedText(StaticText[LocateByParent]):
        pass
    
    # Test with valid string alignment
    try:
        text = AlignedText(window, label="Valid", align="c")
        print("✅ Valid alignment string accepted")
    except Exception as e:
        print(f"❌ Unexpected error with valid alignment: {e}")
        return False
    
    # Test invalid alignment string (should raise ValueError)
    try:
        invalid_text = AlignedText(window, label="Invalid", align="invalid")
        print("❌ Invalid alignment should have raised an error")
        return False
    except ValueError:
        print("✅ Invalid alignment string properly rejected")
    except Exception as e:
        print(f"❌ Unexpected error type: {e}")
        return False
    
    print("✅ Error handling test passed")
    return True


def run_all_tests():
    """Run all StaticText mixin tests."""
    print("="*50)
    print("Running StaticText Mixin Tests")
    print("="*50)
    
    try:
        test_text_align_enum()
        test_locate_by_parent_mixin()
        test_position_calculation()
        test_mixin_integration()
        if not test_error_handling():
            return False
        
        print("="*50)
        print("🎉 ALL STATICTEXT MIXIN TESTS PASSED!")
        print("="*50)
        return True
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)