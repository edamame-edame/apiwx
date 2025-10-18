"""Test cases for the new search_child_indexor method in AutoDetect mixin.

This module tests the functionality of the search_child_indexor method
added to the AutoDetect class in mixins_common.py for apiwx v0.5.4.
"""
import sys
import os

# Add parent directory to sys.path to import apiwx
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    import apiwx
    from apiwx import core
    from apiwx import mixins_common
except ImportError as e:
    print(f"Failed to import apiwx: {e}")
    print("Make sure apiwx is properly installed or in the Python path")
    sys.exit(1)


def test_search_child_indexor_basic():
    """Test basic functionality of search_child_indexor method."""
    print("=== Testing search_child_indexor - Basic Functionality ===")
    
    try:
        # Create AutoDetect subclass that detects Window and Button
        DetectComponents = mixins_common.AutoDetect[
            core.Window,
            core.Button
        ]
        
        class TestApp(core.App[DetectComponents]):
            # Define some child components as class attributes for AutoDetect
            main_window = core.Window
            dialog_window = core.Window
            
            def __init__(self):
                # Also add some components as instance attributes
                self.help_window = core.Window
                
                super().__init__("TestApp")
        
        # Create test app instance
        app = TestApp()
        
        # Debug: Print children information
        print(f"Children dict: {app.children}")
        print(f"Children namelist: {getattr(app, '_children_namelist', 'Not found')}")
        print(f"Detect target: {DetectComponents.detect_target}")
        
        # Test search for Window instances
        window_indexors = app.search_child_indexor(core.Window)
        print(f"Found {len(window_indexors)} window indexors: {window_indexors}")
        
        # Test search for Button instances (should be empty as none defined)
        button_indexors = app.search_child_indexor(core.Button)
        print(f"Found {len(button_indexors)} button indexors: {button_indexors}")
        
        # Verify indexor types
        for indexor in window_indexors:
            assert isinstance(indexor, core.UIIndexor), f"Expected UIIndexor, got {type(indexor)}"
            assert indexor in app.children, f"Indexor {indexor} not found in children dict"
            assert isinstance(app.children[indexor], core.Window), f"Expected Window for indexor {indexor}"
        
        # Verify we found both class and instance attributes
        # Should have 3 windows (main_window, dialog_window, help_window)
        assert len(window_indexors) == 3, f"Expected 3 window indexors, got {len(window_indexors)}"
        assert len(button_indexors) == 0, f"Expected 0 button indexors, got {len(button_indexors)}"
        
        # Verify total children count
        total_expected = len(window_indexors) + len(button_indexors)
        assert len(app.children) == total_expected, f"Expected {total_expected} children, got {len(app.children)}"
        
        print("✓ Basic functionality test passed")
        return True
        
    except Exception as e:
        print(f"✗ Basic functionality test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_search_child_indexor_empty():
    """Test search_child_indexor with no matching components."""
    print("\n=== Testing search_child_indexor - Empty Results ===")
    
    try:
        # Create AutoDetect subclass that only detects Window
        DetectWindows = mixins_common.AutoDetect[core.Window]
        
        class TestApp(core.App[DetectWindows]):
            # Only define button components (not detected since not in detect_target)
            ok_button = core.Button
            cancel_button = core.Button
            
            def __init__(self):
                super().__init__("TestApp")
        
        # Create test app instance
        app = TestApp()
        
        # Search for windows (should find none)
        window_indexors = app.search_child_indexor(core.Window)
        print(f"Window indexors found: {window_indexors}")
        
        # Search for buttons (should find none since not in detect_target)
        button_indexors = app.search_child_indexor(core.Button)
        print(f"Button indexors found: {button_indexors}")
        
        # Verify empty results
        assert len(window_indexors) == 0, f"Expected 0 window indexors, got {len(window_indexors)}"
        assert len(button_indexors) == 0, f"Expected 0 button indexors, got {len(button_indexors)}"
        assert isinstance(window_indexors, tuple), f"Expected tuple, got {type(window_indexors)}"
        assert isinstance(button_indexors, tuple), f"Expected tuple, got {type(button_indexors)}"
        
        print("✓ Empty results test passed")
        return True
        
    except Exception as e:
        print(f"✗ Empty results test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_search_child_indexor_singleton():
    """Test search_child_indexor with singleton mixin (single component)."""
    print("\n=== Testing search_child_indexor - Singleton Mixin ===")
    
    try:
        # Create AutoDetect subclass that detects only Window
        DetectWindow = mixins_common.AutoDetect[core.Window]
        
        class TestApp(core.App[DetectWindow]):
            # Define single window component as class attribute
            main_window = core.Window
            
            def __init__(self):
                super().__init__("TestApp")
        
        # Create test app instance
        app = TestApp()
        
        # Search for windows (should find exactly one)
        window_indexors = app.search_child_indexor(core.Window)
        print(f"Window indexors found: {window_indexors}")
        
        # Verify singleton result
        assert len(window_indexors) == 1, f"Expected 1 window indexor, got {len(window_indexors)}"
        assert isinstance(window_indexors, tuple), f"Expected tuple, got {type(window_indexors)}"
        
        # Verify the single indexor
        indexor = window_indexors[0]
        assert isinstance(indexor, core.UIIndexor), f"Expected UIIndexor, got {type(indexor)}"
        assert indexor in app.children, f"Indexor {indexor} not found in children dict"
        assert isinstance(app.children[indexor], core.Window), f"Expected Window for indexor {indexor}"
        
        print("✓ Singleton mixin test passed")
        return True
        
    except Exception as e:
        print(f"✗ Singleton mixin test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_search_child_indexor_multiton():
    """Test search_child_indexor with multiton mixin (multiple components)."""
    print("\n=== Testing search_child_indexor - Multiton Mixin ===")
    
    try:
        # Create AutoDetect subclass that detects multiple types
        DetectMultiple = mixins_common.AutoDetect[
            core.Window
        ]
        
        class TestApp(core.App[DetectMultiple]):
            # Define multiple components as class attributes
            window1 = core.Window
            window2 = core.Window
            window3 = core.Window
            
            def __init__(self):
                # Add more windows as instance attributes
                self.window4 = core.Window
                self.window5 = core.Window
                
                super().__init__("TestApp")
        
        # Create test app instance
        app = TestApp()
        
        # Search for different component types
        window_indexors = app.search_child_indexor(core.Window)
        
        print(f"Window indexors found: {window_indexors} (count: {len(window_indexors)})")
        
        # Verify multiton results - should have 5 windows total
        assert len(window_indexors) == 5, f"Expected 5 window indexors, got {len(window_indexors)}"
        
        # Verify all are tuples
        assert isinstance(window_indexors, tuple), f"Expected tuple for windows, got {type(window_indexors)}"
        
        # Verify total children count
        total_expected = 5  # 5 windows
        assert len(app.children) == total_expected, f"Expected {total_expected} children, got {len(app.children)}"
        
        print("✓ Multiton mixin test passed")
        return True
        
    except Exception as e:
        print(f"✗ Multiton mixin test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_all_tests():
    """Run all test cases for search_child_indexor method."""
    print("Starting search_child_indexor method tests...\n")
    
    tests = [
        test_search_child_indexor_basic,
        test_search_child_indexor_empty,
        test_search_child_indexor_singleton,
        test_search_child_indexor_multiton
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"Test {test.__name__} raised exception: {e}")
            failed += 1
    
    print(f"\n=== Test Results ===")
    print(f"Passed: {passed}")
    print(f"Failed: {failed}")
    print(f"Total: {passed + failed}")
    
    if failed == 0:
        print("🎉 All tests passed!")
        return True
    else:
        print("❌ Some tests failed.")
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)