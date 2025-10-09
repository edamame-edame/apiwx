#!/usr/bin/env python3
"""
Comprehensive Test Suite for apiwx
Automatically generated from source code analysis and conversation history
"""
import sys
import os
import importlib
import time
import traceback
from pathlib import Path
from typing import Dict, List, Any, Optional

# Ensure UTF-8 encoding for Windows console
if os.name == 'nt':  # Windows
    import codecs
    sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
    sys.stderr = codecs.getwriter("utf-8")(sys.stderr.detach())

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "apiwx"))

class TestResult:
    def __init__(self, name: str, passed: bool, duration: float, error: Optional[str] = None):
        self.name = name
        self.passed = passed
        self.duration = duration
        self.error = error

class TestRunner:
    def __init__(self):
        self.results: List[TestResult] = []
        self.start_time = time.time()
    
    def run_test(self, test_name: str, test_func) -> bool:
        """Run a single test function"""
        print(f"\n{'='*60}")
        print(f"Running: {test_name}")
        print(f"{'='*60}")
        
        start = time.time()
        try:
            result = test_func()
            duration = time.time() - start
            
            passed = result if isinstance(result, bool) else True
            self.results.append(TestResult(test_name, passed, duration))
            
            status = "PASSED" if passed else "FAILED"
            print(f"Result: {status} ({duration:.2f}s)")
            return passed
            
        except Exception as e:
            duration = time.time() - start
            error_msg = str(e)
            self.results.append(TestResult(test_name, False, duration, error_msg))
            
            print(f"Result: ERROR ({duration:.2f}s)")
            print(f"Error: {error_msg}")
            print("\nTraceback:")
            traceback.print_exc()
            return False
    
    def print_summary(self):
        """Print test results summary"""
        total_time = time.time() - self.start_time
        
        print(f"\n{'='*80}")
        print("TEST SUMMARY")
        print(f"{'='*80}")
        
        total_tests = len(self.results)
        passed_tests = sum(1 for r in self.results if r.passed)
        failed_tests = total_tests - passed_tests
        
        print(f"Total tests: {total_tests}")
        print(f"Passed: {passed_tests}")
        print(f"Failed: {failed_tests}")
        print(f"Success rate: {passed_tests/total_tests*100:.1f}%" if total_tests > 0 else "No tests run")
        print(f"Total time: {total_time:.2f}s")
        
        if self.results:
            print(f"\nDetailed Results:")
            for result in self.results:
                status = "[PASS]" if result.passed else "[FAIL]"
                time_str = f"{result.duration:.2f}s"
                error_str = f" - {result.error}" if result.error else ""
                print(f"  {result.name:<30} {status} {time_str}{error_str}")
        
        if failed_tests == 0:
            print(f"\nAll tests passed! The apiwx project is working correctly.")
        else:
            print(f"\n{failed_tests} test(s) failed. Please check the output above.")
        
        return passed_tests == total_tests

# Test Functions
def test_basic_imports():
    """Test basic module imports"""
    try:
        import apiwx
        from apiwx import debug, core, mixins_core, mixins_base
        from apiwx.mixins_base import Singleton, Multiton
        from apiwx.mixins_core import MixinsType, BaseMixins
        print("Basic imports successful")
        return True
    except Exception as e:
        print(f"Import failed: {e}")
        return False

def test_debug_system():
    """Test debug and logging system"""
    try:
        from apiwx import debug
        from apiwx.debug import Logger, LogLevel
        
        # Test Logger class creation
        logger = Logger(
            logger_name="TEST_LOGGER",
            log_dir="./log",
            log_timestamp="%Y/%m/%d %H:%M:%S",
            log_tag_length=8,
            log_maxline=1000,
            log_maxfiles=5,
            log_level=LogLevel.DEBUG
        )
        
        # Test log levels
        logger.debug("TEST", "Debug message")
        logger.info("TEST", "Info message")
        logger.warning("TEST", "Warning message")
        logger.error("TEST", "Error message")
        
        # Test internal logging
        debug.internallog("TEST", "Internal log message")
        
        print("Debug system working correctly")
        return True
    except Exception as e:
        print(f"Debug system test failed: {e}")
        return False

def test_singleton_pattern():
    """Test Singleton pattern implementation"""
    try:
        from apiwx.mixins_base import Singleton
        from apiwx.mixins_core import MixinsType
        
        class TestClass(metaclass=MixinsType):
            def __init__(self, name="test"):
                self.name = name
                self.counter = 0
        
        SingletonTest = TestClass[Singleton]
        
        # Test singleton behavior
        obj1 = SingletonTest("first")
        obj2 = SingletonTest("second")
        
        # Should be the same instance
        if obj1 is not obj2:
            print("Singleton test failed: Different instances returned")
            return False
        
        # Should preserve first constructor args
        if obj1.name != "first":
            print(f"Singleton test failed: Name should be 'first', got '{obj1.name}'")
            return False
        
        # Test state sharing
        obj1.counter = 5
        if obj2.counter != 5:
            print("Singleton test failed: State not shared")
            return False
        
        print("Singleton pattern working correctly")
        return True
    except Exception as e:
        print(f"Singleton test failed: {e}")
        return False

def test_multiton_pattern():
    """Test Multiton pattern implementation"""
    try:
        from apiwx.mixins_base import Multiton
        from apiwx.mixins_core import MixinsType
        
        class TestClass(metaclass=MixinsType):
            def __init__(self, name="test"):
                self.name = name
                self.counter = 0
        
        MultitonTest = TestClass[Multiton]
        
        # Test multiton behavior
        obj1 = MultitonTest("first")
        obj2 = MultitonTest("second")
        obj3 = MultitonTest("third")
        
        # Should be different instances
        if obj1 is obj2 or obj2 is obj3 or obj1 is obj3:
            print("Multiton test failed: Same instances returned")
            return False
        
        # Should have separate names
        if obj1.name != "first" or obj2.name != "second" or obj3.name != "third":
            print("Multiton test failed: Incorrect names")
            return False
        
        # Test separate state
        obj1.counter = 1
        obj2.counter = 2
        obj3.counter = 3
        
        if obj1.counter != 1 or obj2.counter != 2 or obj3.counter != 3:
            print("Multiton test failed: State not separate")
            return False
        
        print("Multiton pattern working correctly")
        return True
    except Exception as e:
        print(f"Multiton test failed: {e}")
        return False

def test_mixins_system():
    """Test core generics system"""
    try:
        from apiwx.mixins_core import MixinsType, BaseGenerics
        from apiwx.mixins_base import Singleton, Multiton
        
        class TestBase(metaclass=MixinsType):
            def __init__(self, value=42):
                self.value = value
        
        # Test generic class creation
        SingletonClass = TestBase[Singleton]
        MultitonClass = TestBase[Multiton]
        
        # Test MRO structure
        singleton_mro = [cls.__name__ for cls in SingletonClass.__mro__]
        multiton_mro = [cls.__name__ for cls in MultitonClass.__mro__]
        
        print(f"Singleton MRO: {singleton_mro}")
        print(f"Multiton MRO: {multiton_mro}")
        
        # Test metaclass replacement
        if type(SingletonClass).__name__ != "Singleton":
            print(f"Generics test failed: Expected Singleton metaclass, got {type(SingletonClass).__name__}")
            return False
        
        if type(MultitonClass).__name__ != "Multiton":
            print(f"Generics test failed: Expected Multiton metaclass, got {type(MultitonClass).__name__}")
            return False
        
        print("Generics system working correctly")
        return True
    except Exception as e:
        print(f"Generics test failed: {e}")
        return False

def test_core_components():
    """Test core apiwx components"""
    try:
        from apiwx import core
        
        # Test that core classes are importable
        components = ['WrappedApp', 'WrappedWindow', 'WrappedPanel']
        for component in components:
            if not hasattr(core, component):
                print(f"Core test failed: {component} not found in core module")
                return False
        
        print("Core components available")
        return True
    except Exception as e:
        print(f"Core components test failed: {e}")
        return False

def test_message_system():
    """Test message box system"""
    try:
        from apiwx import message
        
        # Test message types and enums
        required_items = ['MessageType', 'MessageResult', 'MessageBox']
        for item in required_items:
            if not hasattr(message, item):
                print(f"Message test failed: {item} not found")
                return False
        
        # Test MessageType enum
        msg_type = message.MessageType.INFO
        if msg_type is None:
            print("Message test failed: MessageType.INFO not accessible")
            return False
        
        print("Message system components available")
        return True
    except Exception as e:
        print(f"Message system test failed: {e}")
        return False

def test_constants_and_enums():
    """Test constants and enumerations"""
    try:
        from apiwx import constants
        
        # Test that constants module is importable
        print("Constants module imported successfully")
        return True
    except Exception as e:
        print(f"Constants test failed: {e}")
        return False

def test_mixins_integration():
    """Test advanced generics integration"""
    try:
        from apiwx.mixins_core import MixinsType
        from apiwx.mixins_base import Singleton, Multiton
        
        # Test inheritance with generics
        class BaseClass:
            def __init__(self, name="base"):
                self.base_name = name
            
            def base_method(self):
                return "base_method"
        
        class TestClass(BaseClass, metaclass=MixinsType):
            def __init__(self, name="test", extra="extra"):
                super().__init__(name)
                self.extra = extra
            
            def test_method(self):
                return "test_method"
        
        # Test with Singleton
        SingletonTest = TestClass[Singleton]
        s1 = SingletonTest("singleton", "extra1")
        s2 = SingletonTest("singleton2", "extra2")
        
        if s1 is not s2:
            print("Generics integration test failed: Singleton not working with inheritance")
            return False
        
        if not hasattr(s1, 'base_method') or s1.base_method() != "base_method":
            print("Generics integration test failed: Inheritance not working")
            return False
        
        # Test with Multiton
        MultitonTest = TestClass[Multiton]
        m1 = MultitonTest("multiton1", "extra1")
        m2 = MultitonTest("multiton2", "extra2")
        
        if m1 is m2:
            print("Generics integration test failed: Multiton not working with inheritance")
            return False
        
        if m1.base_name != "multiton1" or m2.base_name != "multiton2":
            print("Generics integration test failed: Constructor args not preserved")
            return False
        
        print("Generics integration working correctly")
        return True
    except Exception as e:
        print(f"Generics integration test failed: {e}")
        return False

def test_error_handling():
    """Test error handling and edge cases"""
    try:
        from apiwx.mixins_core import MixinsType
        from apiwx.mixins_base import Singleton
        
        # Test empty class with generics
        class EmptyClass(metaclass=MixinsType):
            pass
        
        EmptySingleton = EmptyClass[Singleton]
        es1 = EmptySingleton()
        es2 = EmptySingleton()
        
        if es1 is not es2:
            print("Error handling test failed: Empty Singleton not working")
            return False
        
        print("Error handling tests passed")
        return True
    except Exception as e:
        print(f"Error handling test failed: {e}")
        return False

def test_auto_build_compatibility():
    """Test compatibility with auto_build.py"""
    try:
        # Import auto_build module
        auto_build_path = project_root / "project" / "auto_build.py"
        if auto_build_path.exists():
            spec = importlib.util.spec_from_file_location("auto_build", auto_build_path)
            auto_build = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(auto_build)
            
            # Test BuildAutomation class
            if hasattr(auto_build, 'BuildAutomation'):
                # Test basic instantiation
                build_automation = auto_build.BuildAutomation("project/build.json")
                
                # Test that config is loaded
                if hasattr(build_automation, 'config') and build_automation.config:
                    print("auto_build.py compatibility verified")
                    return True
                else:
                    print("auto_build.py config loading failed")
                    return False
            else:
                print("auto_build.py missing BuildAutomation class")
                return False
        else:
            print("auto_build.py not found, skipping compatibility test")
            return True
    except Exception as e:
        print(f"auto_build compatibility test failed: {e}")
        return False

def run_all_tests():
    """Run the complete test suite"""
    runner = TestRunner()
    
    print("apiwx Comprehensive Test Suite")
    print("=" * 80)
    print(f"Python version: {sys.version}")
    print(f"Platform: {sys.platform}")
    print(f"Working directory: {os.getcwd()}")
    print(f"Project root: {project_root}")
    
    # Define test suite
    test_functions = [
        ("Basic Imports", test_basic_imports),
        ("Debug System", test_debug_system),
        ("Singleton Pattern", test_singleton_pattern),
        ("Multiton Pattern", test_multiton_pattern),
        ("Generics System", test_mixins_system),
        ("Core Components", test_core_components),
        ("Message System", test_message_system),
        ("Constants and Enums", test_constants_and_enums),
        ("Generics Integration", test_mixins_integration),
        ("Error Handling", test_error_handling),
        ("Auto-Build Compatibility", test_auto_build_compatibility),
    ]
    
    # Run all tests
    for test_name, test_func in test_functions:
        runner.run_test(test_name, test_func)
    
    # Print summary and return result
    return runner.print_summary()

def run_specific_test(test_name: str):
    """Run a specific test by name"""
    test_map = {
        "imports": test_basic_imports,
        "debug": test_debug_system,
        "singleton": test_singleton_pattern,
        "multiton": test_multiton_pattern,
        "generics": test_mixins_system,
        "core": test_core_components,
        "message": test_message_system,
        "constants": test_constants_and_enums,
        "integration": test_mixins_integration,
        "errors": test_error_handling,
        "autobuild": test_auto_build_compatibility,
    }
    
    if test_name in test_map:
        runner = TestRunner()
        result = runner.run_test(test_name.title(), test_map[test_name])
        runner.print_summary()
        return result
    else:
        print(f"Unknown test: {test_name}")
        print(f"Available tests: {', '.join(test_map.keys())}")
        return False

if __name__ == "__main__":
    import importlib.util
    
    if len(sys.argv) > 1:
        # Run specific test
        test_name = sys.argv[1].lower()
        success = run_specific_test(test_name)
    else:
        # Run all tests
        success = run_all_tests()
    
    sys.exit(0 if success else 1)