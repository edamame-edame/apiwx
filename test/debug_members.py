"""Debug the get_all_members method behavior."""
import sys
import os

# Add parent directory to sys.path to import apiwx
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import apiwx
from apiwx import core
from apiwx import mixins_common


def debug_get_all_members():
    """Debug the get_all_members method."""
    print("=== Debug get_all_members ===")
    
    # Create a simple AutoDetect class
    DetectPanel = mixins_common.AutoDetect[core.WrappedPanel]
    
    class TestApp(core.WrappedApp[DetectPanel]):
        main_panel = core.WrappedPanel
        some_other_attr = "hello"
        
        def __init__(self):
            super().__init__("TestApp")
    
    # Test get_all_members on the class
    print("Before instance creation:")
    
    # Check each step of MRO processing
    print(f"\nMRO debug:")
    for i, cls in enumerate(TestApp.__mro__):
        print(f"  {i}: {cls}")
        if hasattr(cls, '__dict__'):
            attrs = {k: v for k, v in cls.__dict__.items() if not k.startswith('__')}
            if attrs:
                print(f"    Local attrs: {list(attrs.keys())}")
                if 'main_panel' in attrs:
                    print(f"      main_panel found here: {attrs['main_panel']}")
    
    members = TestApp.get_all_members()
    print(f"\nAll members found ({len(members)}):")
    relevant_members = {k: v for k, v in members.items() if not k.startswith('__')}
    for name, value in relevant_members.items():
        print(f"  {name}: {value} (type: {type(value)})")
    
    # Look specifically for main_panel
    print(f"\nLooking for 'main_panel':")
    if 'main_panel' in members:
        print(f"Found main_panel: {members['main_panel']}")
    else:
        print("main_panel not found in members")
        
    # Check class __dict__ directly
    print(f"\nTestApp.__dict__:")
    for name, value in TestApp.__dict__.items():
        if not name.startswith('__'):
            print(f"  {name}: {value}")
    
    # Check MRO
    print(f"\nTestApp.__mro__:")
    for i, cls in enumerate(TestApp.__mro__):
        print(f"  {i}: {cls}")
        if hasattr(cls, '__dict__'):
            relevant_attrs = {k: v for k, v in cls.__dict__.items() if not k.startswith('__')}
            if relevant_attrs:
                print(f"    Attributes: {list(relevant_attrs.keys())}")
    
    print("Creating TestApp instance...")
    try:
        app = TestApp()
        print("TestApp instance created successfully")
        
        print(f"Children dict: {app.children}")
        print(f"Children namelist: {getattr(app, '_children_namelist', 'Not found')}")
        
        # Test search
        panel_indexors = app.search_child_indexor(core.WrappedPanel)
        print(f"Panel indexors found: {panel_indexors}")
        
        return len(panel_indexors) > 0
    except Exception as e:
        print(f"Failed to create TestApp instance: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    debug_get_all_members()