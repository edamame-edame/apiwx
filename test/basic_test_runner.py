#!/usr/bin/env python3
"""
Basic Test Framework for apiwx
Simplified testing framework for core functionality
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

def test_imports():
    """Test basic import functionality"""
    print("Testing imports...")
    try:
        import apiwx
        from apiwx import core, debug, generics_core, generics_base
        from apiwx.generics_base import Singleton, Multiton
        print("[PASS] Basic imports successful")
        return True
    except Exception as e:
        print(f"[FAIL] Import error: {e}")
        return False

def test_singleton_basic():
    """Test basic Singleton functionality"""
    print("Testing Singleton pattern...")
    try:
        from apiwx.generics_core import GenericsType
        from apiwx.generics_base import Singleton
        
        class TestClass(metaclass=GenericsType):
            def __init__(self, name="test"):
                self.name = name
        
        SingletonTest = TestClass[Singleton]
        
        obj1 = SingletonTest("first")
        obj2 = SingletonTest("second")
        
        assert obj1 is obj2, "Singleton should return same instance"
        assert obj1.name == "first", "Singleton should preserve first constructor"
        
        print("[PASS] Singleton working correctly")
        return True
    except Exception as e:
        print(f"[FAIL] Singleton error: {e}")
        return False

def test_multiton_basic():
    """Test basic Multiton functionality"""
    print("Testing Multiton pattern...")
    try:
        from apiwx.generics_core import GenericsType
        from apiwx.generics_base import Multiton
        
        class TestClass(metaclass=GenericsType):
            def __init__(self, name="test"):
                self.name = name
        
        MultitonTest = TestClass[Multiton]
        
        obj1 = MultitonTest("first")
        obj2 = MultitonTest("second")
        
        assert obj1 is not obj2, "Multiton should return different instances"
        assert obj1.name == "first", "First instance should have correct name"
        assert obj2.name == "second", "Second instance should have correct name"
        
        print("[PASS] Multiton working correctly")
        return True
    except Exception as e:
        print(f"[FAIL] Multiton error: {e}")
        return False

def test_debug_system():
    """Test debug system"""
    print("Testing debug system...")
    try:
        from apiwx import debug
        from apiwx.debug import Logger, LogLevel
        
        # Test Logger class instantiation
        logger = Logger(
            logger_name="TEST_LOGGER",
            log_dir="./log",
            log_timestamp="%Y/%m/%d %H:%M:%S",
            log_tag_length=8,
            log_maxline=1000,
            log_maxfiles=5,
            log_level=LogLevel.DEBUG
        )
        
        # Test logger methods
        logger.info("TEST", "Test info message")
        logger.debug("TEST", "Test debug message")
        logger.warning("TEST", "Test warning message")
        
        # Test convenience functions
        debug.uilog("TEST", "UI log test")
        debug.internallog("TEST", "Internal log test")
        
        print("[PASS] Debug system working")
        return True
    except Exception as e:
        print(f"[FAIL] Debug system error: {e}")
        return False

def run_basic_tests():
    """Run all basic tests"""
    print("=" * 50)
    print("APIWX Basic Test Suite")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_singleton_basic,
        test_multiton_basic,
        test_debug_system,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Results: {passed}/{total} tests passed")
    if passed == total:
        print("All tests PASSED!")
    else:
        print(f"{total - passed} test(s) FAILED")
    print("=" * 50)
    
    return passed == total

if __name__ == "__main__":
    success = run_basic_tests()
    sys.exit(0 if success else 1)