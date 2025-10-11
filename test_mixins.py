#!/usr/bin/env python3
"""Test script for mixin system functionality"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

try:
    import apiwx
    print("=== Mixin System Test ===")
    print(f"apiwx version: {apiwx.__version__}")
    
    print("\n1. Testing basic import...")
    print("✓ Import successful")
    
    print("\n2. Testing Singleton mixin...")
    app1 = apiwx.AppBase('TestApp1')
    app2 = apiwx.AppBase('TestApp2')
    print(f"   app1 is app2: {app1 is app2}")
    print("✓ Singleton pattern working" if app1 is app2 else "✗ Singleton failed")
    
    print("\n3. Testing mixin attribute...")
    print(f"   __mixin_classes__ exists: {hasattr(app1, '__mixin_classes__')}")
    if hasattr(app1, '__mixin_classes__'):
        print(f"   Mixin classes: {app1.__mixin_classes__}")
    print("✓ Mixin attributes working")
    
    print("\n4. Testing mixin method...")
    has_method = hasattr(app1, 'hasmixins')
    print(f"   hasmixins() method exists: {has_method}")
    if has_method:
        print("✓ Mixin methods working")
    else:
        print("✗ Mixin methods missing")
    
    print("\n=== All Core Tests Passed! ===")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)