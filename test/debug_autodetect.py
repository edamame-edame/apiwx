"""Simple test to debug AutoDetect behavior."""
import sys
import os

# Add parent directory to sys.path to import apiwx
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import apiwx
from apiwx import core
from apiwx import mixins_common


def simple_debug_test():
    """Simple test to see what's happening."""
    print("=== Simple Debug Test ===")
    
    # Create a simple AutoDetect class
    DetectPanel = mixins_common.AutoDetect[core.Panel]
    
    print(f"DetectPanel.detect_target = {DetectPanel.detect_target}")
    
    class TestApp(core.App[DetectPanel]):
        main_panel = core.Panel
        
        def __init__(self):
            print("TestApp.__init__ started")
            super().__init__("TestApp")
            print("TestApp.__init__ completed")
    
    # Create instance
    print("Creating TestApp instance...")
    app = TestApp()
    
    # Check what we have
    print(f"app.children = {app.children}")
    print(f"app._children_namelist = {getattr(app, '_children_namelist', 'Not found')}")
    print(f"app.main_panel = {getattr(app, 'main_panel', 'Not found')}")
    print(f"type(app.main_panel) = {type(getattr(app, 'main_panel', None))}")
    
    # Test the method
    print("\nTesting search_child_indexor...")
    indexors = app.search_child_indexor(core.Panel)
    print(f"Result: {indexors}")
    
    # Manual check of children
    print("\nManual children check:")
    for key, value in app.children.items():
        print(f"  {key}: {value} (type: {type(value)})")


if __name__ == "__main__":
    simple_debug_test()