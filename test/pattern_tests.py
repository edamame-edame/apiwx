#!/usr/bin/env python3
"""
Singleton and Multiton Pattern Tests
Focused testing of core singleton and multiton functionality
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

def test_singleton_detailed():
    """Detailed Singleton pattern testing"""
    print("Detailed Singleton Pattern Test")
    print("-" * 40)
    
    try:
        from apiwx.generics_core import GenericsType
        from apiwx.generics_base import Singleton
        
        class Counter(metaclass=GenericsType):
            def __init__(self, start=0):
                self.count = start
            
            def increment(self):
                self.count += 1
                return self.count
            
            def get_count(self):
                return self.count
        
        SingletonCounter = Counter[Singleton]
        
        print("Creating first instance with start=10...")
        counter1 = SingletonCounter(10)
        print(f"Initial count: {counter1.get_count()}")
        
        print("Creating second instance with start=50...")
        counter2 = SingletonCounter(50)
        print(f"Second instance count: {counter2.get_count()}")
        
        print(f"Are instances identical? {counter1 is counter2}")
        
        print("Incrementing through first reference...")
        count = counter1.increment()
        print(f"Count after increment: {count}")
        
        print(f"Count from second reference: {counter2.get_count()}")
        
        # Validation
        assert counter1 is counter2, "Singleton instances should be identical"
        assert counter1.count == 11, f"Expected count 11, got {counter1.count}"
        assert counter2.count == 11, f"Expected count 11, got {counter2.count}"
        
        print("[PASS] Singleton detailed test passed")
        return True
        
    except Exception as e:
        print(f"[FAIL] Singleton detailed test failed: {e}")
        return False

def test_multiton_detailed():
    """Detailed Multiton pattern testing"""
    print("\nDetailed Multiton Pattern Test")
    print("-" * 40)
    
    try:
        from apiwx.generics_core import GenericsType
        from apiwx.generics_base import Multiton
        
        class NamedCounter(metaclass=GenericsType):
            def __init__(self, name, start=0):
                self.name = name
                self.count = start
            
            def increment(self):
                self.count += 1
                return self.count
            
            def get_info(self):
                return f"{self.name}: {self.count}"
        
        MultitonCounter = NamedCounter[Multiton]
        
        print("Creating counter 'A' with start=1...")
        counter_a = MultitonCounter("A", 1)
        print(f"Counter A info: {counter_a.get_info()}")
        
        print("Creating counter 'B' with start=10...")
        counter_b = MultitonCounter("B", 10)
        print(f"Counter B info: {counter_b.get_info()}")
        
        print("Creating counter 'C' with start=100...")
        counter_c = MultitonCounter("C", 100)
        print(f"Counter C info: {counter_c.get_info()}")
        
        print(f"Are A and B different? {counter_a is not counter_b}")
        print(f"Are B and C different? {counter_b is not counter_c}")
        print(f"Are A and C different? {counter_a is not counter_c}")
        
        print("Incrementing each counter...")
        counter_a.increment()
        counter_b.increment()
        counter_c.increment()
        
        print(f"After increment - A: {counter_a.get_info()}")
        print(f"After increment - B: {counter_b.get_info()}")
        print(f"After increment - C: {counter_c.get_info()}")
        
        # Validation
        assert counter_a is not counter_b, "Multiton instances should be different"
        assert counter_b is not counter_c, "Multiton instances should be different"
        assert counter_a is not counter_c, "Multiton instances should be different"
        
        assert counter_a.count == 2, f"Expected A count 2, got {counter_a.count}"
        assert counter_b.count == 11, f"Expected B count 11, got {counter_b.count}"
        assert counter_c.count == 101, f"Expected C count 101, got {counter_c.count}"
        
        print("[PASS] Multiton detailed test passed")
        return True
        
    except Exception as e:
        print(f"[FAIL] Multiton detailed test failed: {e}")
        return False

def test_metaclass_behavior():
    """Test metaclass behavior and MRO"""
    print("\nMetaclass Behavior Test")
    print("-" * 40)
    
    try:
        from apiwx.generics_core import GenericsType
        from apiwx.generics_base import Singleton, Multiton
        
        class BaseClass(metaclass=GenericsType):
            def __init__(self, value):
                self.value = value
        
        SingletonClass = BaseClass[Singleton]
        MultitonClass = BaseClass[Multiton]
        
        print(f"Original class metaclass: {type(BaseClass)}")
        print(f"Singleton class metaclass: {type(SingletonClass)}")
        print(f"Multiton class metaclass: {type(MultitonClass)}")
        
        print(f"Original class MRO: {[cls.__name__ for cls in BaseClass.__mro__]}")
        print(f"Singleton class MRO: {[cls.__name__ for cls in SingletonClass.__mro__]}")
        print(f"Multiton class MRO: {[cls.__name__ for cls in MultitonClass.__mro__]}")
        
        # Test instance creation
        s1 = SingletonClass("singleton_value")
        s2 = SingletonClass("singleton_value2")
        
        m1 = MultitonClass("multiton_value1")
        m2 = MultitonClass("multiton_value2")
        
        print(f"Singleton instances identical: {s1 is s2}")
        print(f"Singleton value: {s1.value}")
        print(f"Multiton instances different: {m1 is not m2}")
        print(f"Multiton values: {m1.value}, {m2.value}")
        
        # Validation
        assert type(SingletonClass).__name__ == "Singleton", "Singleton metaclass check failed"
        assert type(MultitonClass).__name__ == "Multiton", "Multiton metaclass check failed"
        assert s1 is s2, "Singleton behavior check failed"
        assert m1 is not m2, "Multiton behavior check failed"
        
        print("[PASS] Metaclass behavior test passed")
        return True
        
    except Exception as e:
        print(f"[FAIL] Metaclass behavior test failed: {e}")
        return False

def test_edge_cases():
    """Test edge cases and error conditions"""
    print("\nEdge Cases Test")
    print("-" * 40)
    
    try:
        from apiwx.generics_core import GenericsType
        from apiwx.generics_base import Singleton, Multiton
        
        # Test with no-argument constructor
        class SimpleClass(metaclass=GenericsType):
            def __init__(self):
                self.created = True
        
        SimpleSingleton = SimpleClass[Singleton]
        SimpleMultiton = SimpleClass[Multiton]
        
        # Test singleton with no args
        s1 = SimpleSingleton()
        s2 = SimpleSingleton()
        assert s1 is s2, "Singleton no-args test failed"
        
        # Test multiton with no args
        m1 = SimpleMultiton()
        m2 = SimpleMultiton()
        assert m1 is not m2, "Multiton no-args test failed"
        
        print("No-args constructor tests passed")
        
        # Test with keyword arguments
        class KeywordClass(metaclass=GenericsType):
            def __init__(self, name="default", value=0):
                self.name = name
                self.value = value
        
        KeywordSingleton = KeywordClass[Singleton]
        KeywordMultiton = KeywordClass[Multiton]
        
        ks1 = KeywordSingleton(name="first", value=1)
        ks2 = KeywordSingleton(name="second", value=2)
        assert ks1 is ks2, "Keyword singleton test failed"
        assert ks1.name == "first", "Keyword singleton preservation failed"
        
        km1 = KeywordMultiton(name="first", value=1)
        km2 = KeywordMultiton(name="second", value=2)
        assert km1 is not km2, "Keyword multiton test failed"
        assert km1.name == "first" and km2.name == "second", "Keyword multiton args failed"
        
        print("Keyword arguments tests passed")
        
        print("[PASS] Edge cases test passed")
        return True
        
    except Exception as e:
        print(f"[FAIL] Edge cases test failed: {e}")
        return False

def run_pattern_tests():
    """Run all pattern tests"""
    print("=" * 60)
    print("APIWX Singleton/Multiton Pattern Test Suite")
    print("=" * 60)
    
    tests = [
        test_singleton_detailed,
        test_multiton_detailed,
        test_metaclass_behavior,
        test_edge_cases,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    print("\n" + "=" * 60)
    print(f"Pattern Test Results: {passed}/{total} tests passed")
    if passed == total:
        print("All pattern tests PASSED!")
    else:
        print(f"{total - passed} pattern test(s) FAILED")
    print("=" * 60)
    
    return passed == total

if __name__ == "__main__":
    success = run_pattern_tests()
    sys.exit(0 if success else 1)