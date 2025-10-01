#!/usr/bin/env python3
"""
Quick Test for Singleton and Multiton Core Functionality
Simple verification that the basic patterns are working
"""
import os
import sys
from pathlib import Path

# Setup UTF-8 encoding for Windows
if os.name == 'nt':
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())

# Add project to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "apiwx"))

def quick_test():
    """Quick verification of core functionality"""
    print("Quick Test: Singleton and Multiton Core Functionality")
    print("=" * 55)
    
    # Test 1: Basic imports
    print("1. Testing imports...")
    try:
        from apiwx.generics_core import GenericsType
        from apiwx.generics_base import Singleton, Multiton
        print("   [PASS] Imports successful")
    except Exception as e:
        print(f"   [FAIL] Import error: {e}")
        return False
    
    # Test 2: Singleton pattern
    print("2. Testing Singleton pattern...")
    try:
        class TestClass(metaclass=GenericsType):
            def __init__(self, value=42):
                self.value = value
        
        SingletonTest = TestClass[Singleton]
        obj1 = SingletonTest(100)
        obj2 = SingletonTest(200)
        
        if obj1 is obj2 and obj1.value == 100:
            print("   [PASS] Singleton working correctly")
        else:
            print(f"   [FAIL] Singleton failed - same instance: {obj1 is obj2}, value: {obj1.value}")
            return False
    except Exception as e:
        print(f"   [FAIL] Singleton error: {e}")
        return False
    
    # Test 3: Multiton pattern
    print("3. Testing Multiton pattern...")
    try:
        MultitonTest = TestClass[Multiton]
        obj3 = MultitonTest(300)
        obj4 = MultitonTest(400)
        
        if obj3 is not obj4 and obj3.value == 300 and obj4.value == 400:
            print("   [PASS] Multiton working correctly")
        else:
            print(f"   [FAIL] Multiton failed - different instances: {obj3 is not obj4}, values: {obj3.value}, {obj4.value}")
            return False
    except Exception as e:
        print(f"   [FAIL] Multiton error: {e}")
        return False
    
    print("\n" + "=" * 55)
    print("Quick test PASSED! Core Singleton/Multiton functionality verified.")
    print("=" * 55)
    return True

if __name__ == "__main__":
    success = quick_test()
    sys.exit(0 if success else 1)