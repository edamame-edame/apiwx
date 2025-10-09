#!/usr/bin/env python3
"""
Integration Tests for apiwx Components
Tests the interaction between different apiwx components
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

def test_debug_with_patterns():
    """Test debug system with singleton/multiton patterns"""
    print("Testing debug system with patterns...")
    
    try:
        from apiwx import debug
        from apiwx.mixins_core import MixinsType
        from apiwx.mixins_base import Singleton, Multiton
        
        class LoggedClass(metaclass=MixinsType):
            def __init__(self, name):
                self.name = name
                # Use debug convenience functions instead of get_logger
                debug.uilog("INIT", f"Created instance: {name}")
            
            def do_work(self):
                debug.uilog("WORK", f"{self.name} doing work")
                return f"{self.name}_work_done"
        
        # Test with Singleton
        SingletonLogged = LoggedClass[Singleton]
        s1 = SingletonLogged("singleton_test")
        s2 = SingletonLogged("singleton_test2")
        
        assert s1 is s2, "Singleton logging test failed"
        
        work1 = s1.do_work()
        work2 = s2.do_work()
        
        assert work1 == work2, "Singleton work result should be same"
        
        # Test with Multiton
        MultitonLogged = LoggedClass[Multiton]
        m1 = MultitonLogged("multiton_test1")
        m2 = MultitonLogged("multiton_test2")
        
        assert m1 is not m2, "Multiton logging test failed"
        
        work3 = m1.do_work()
        work4 = m2.do_work()
        
        assert work3 != work4, "Multiton work results should be different"
        
        print("[PASS] Debug with patterns integration working")
        return True
        
    except Exception as e:
        print(f"[FAIL] Debug with patterns integration failed: {e}")
        return False

def test_message_system_availability():
    """Test message system components"""
    print("Testing message system availability...")
    
    try:
        from apiwx import message
        
        # Check message types exist
        assert hasattr(message, 'MessageType'), "MessageType not found"
        assert hasattr(message, 'MessageResult'), "MessageResult not found"
        assert hasattr(message, 'MessageBox'), "MessageBox not found"
        
        # Test enum access
        info_type = message.MessageType.INFO
        assert info_type is not None, "MessageType.INFO not accessible"
        
        print("[PASS] Message system components available")
        return True
        
    except Exception as e:
        print(f"[FAIL] Message system test failed: {e}")
        return False

def test_core_component_availability():
    """Test core component availability"""
    print("Testing core component availability...")
    
    try:
        from apiwx import core
        
        # Check core classes exist
        core_classes = ['WrappedApp', 'WrappedWindow', 'WrappedPanel']
        for cls_name in core_classes:
            assert hasattr(core, cls_name), f"{cls_name} not found in core"
        
        print("[PASS] Core components available")
        return True
        
    except Exception as e:
        print(f"[FAIL] Core component test failed: {e}")
        return False

def test_mixins_with_inheritance():
    """Test generics system with inheritance"""
    print("Testing generics with inheritance...")
    
    try:
        from apiwx.mixins_core import MixinsType
        from apiwx.mixins_base import Singleton, Multiton
        
        class BaseComponent:
            def __init__(self, name):
                self.name = name
                self.base_initialized = True
            
            def base_method(self):
                return f"base_{self.name}"
        
        class DerivedComponent(BaseComponent, metaclass=MixinsType):
            def __init__(self, name, extra_param="default"):
                super().__init__(name)
                self.extra_param = extra_param
                self.derived_initialized = True
            
            def derived_method(self):
                return f"derived_{self.name}_{self.extra_param}"
        
        # Test with Singleton
        SingletonDerived = DerivedComponent[Singleton]
        s1 = SingletonDerived("test", "extra1")
        s2 = SingletonDerived("test2", "extra2")
        
        assert s1 is s2, "Singleton inheritance test failed"
        assert hasattr(s1, 'base_initialized'), "Base initialization missing"
        assert hasattr(s1, 'derived_initialized'), "Derived initialization missing"
        assert s1.base_method() == "base_test", "Base method not working"
        assert s1.derived_method() == "derived_test_extra1", "Derived method not working"
        
        # Test with Multiton
        MultitonDerived = DerivedComponent[Multiton]
        m1 = MultitonDerived("test1", "extra1")
        m2 = MultitonDerived("test2", "extra2")
        
        assert m1 is not m2, "Multiton inheritance test failed"
        assert m1.name == "test1" and m2.name == "test2", "Multiton args not preserved"
        assert m1.extra_param == "extra1" and m2.extra_param == "extra2", "Multiton extra args not preserved"
        
        print("[PASS] Generics with inheritance working")
        return True
        
    except Exception as e:
        print(f"[FAIL] Generics with inheritance failed: {e}")
        return False

def test_mixed_pattern_usage():
    """Test using both singleton and multiton in same session"""
    print("Testing mixed pattern usage...")
    
    try:
        from apiwx.mixins_core import MixinsType
        from apiwx.mixins_base import Singleton, Multiton
        
        class SharedBase(metaclass=MixinsType):
            instances_created = 0
            
            def __init__(self, identifier):
                SharedBase.instances_created += 1
                self.identifier = identifier
                self.instance_number = SharedBase.instances_created
            
            def get_info(self):
                return f"ID:{self.identifier}, Instance#{self.instance_number}"
        
        # Create both patterns from same base
        SingletonShared = SharedBase[Singleton]
        MultitonShared = SharedBase[Multiton]
        
        # Test mixed creation
        s1 = SingletonShared("S1")
        m1 = MultitonShared("M1")
        s2 = SingletonShared("S2")
        m2 = MultitonShared("M2")
        m3 = MultitonShared("M3")
        
        # Validate singleton behavior
        assert s1 is s2, "Singleton instances should be identical"
        assert s1.identifier == "S1", "Singleton should preserve first identifier"
        
        # Validate multiton behavior
        assert m1 is not m2 and m2 is not m3 and m1 is not m3, "Multiton instances should be different"
        assert m1.identifier == "M1" and m2.identifier == "M2" and m3.identifier == "M3", "Multiton identifiers should be preserved"
        
        # Check instance counting
        print(f"Total instances created: {SharedBase.instances_created}")
        print(f"Singleton info: {s1.get_info()}")
        print(f"Multiton 1 info: {m1.get_info()}")
        print(f"Multiton 2 info: {m2.get_info()}")
        print(f"Multiton 3 info: {m3.get_info()}")
        
        assert SharedBase.instances_created == 4, f"Expected 4 instances, got {SharedBase.instances_created}"
        
        print("[PASS] Mixed pattern usage working")
        return True
        
    except Exception as e:
        print(f"[FAIL] Mixed pattern usage failed: {e}")
        return False

def test_mixins_system_integrity():
    """Test generics system internal integrity"""
    print("Testing generics system integrity...")
    
    try:
        from apiwx.mixins_core import MixinsType, BaseGenerics
        from apiwx.mixins_base import Singleton, Multiton
        
        # Test BaseGenerics is properly configured as a metaclass
        assert issubclass(BaseGenerics, type), "BaseGenerics should be a metaclass type"
        
        # Test metaclass relationships
        assert isinstance(Singleton, type), "Singleton should be a metaclass"
        assert isinstance(Multiton, type), "Multiton should be a metaclass"
        
        # Test that generics work with various class configurations
        class MinimalClass(metaclass=MixinsType):
            pass
        
        class ComplexClass(metaclass=MixinsType):
            def __init__(self, a, b=None, *args, **kwargs):
                self.a = a
                self.b = b
                self.args = args
                self.kwargs = kwargs
        
        # Test minimal class
        MinimalSingleton = MinimalClass[Singleton]
        ms1 = MinimalSingleton()
        ms2 = MinimalSingleton()
        assert ms1 is ms2, "Minimal singleton failed"
        
        # Test complex class
        ComplexMultiton = ComplexClass[Multiton]
        cm1 = ComplexMultiton(1, b=2, extra="test", keyword=True)
        cm2 = ComplexMultiton(3, b=4, other="value")
        
        assert cm1 is not cm2, "Complex multiton failed"
        assert cm1.a == 1 and cm1.b == 2, "Complex multiton args failed"
        assert cm2.a == 3 and cm2.b == 4, "Complex multiton args failed"
        assert cm1.kwargs.get('extra') == 'test', "Complex multiton kwargs failed"
        
        print("[PASS] Generics system integrity verified")
        return True
        
    except Exception as e:
        print(f"[FAIL] Generics system integrity failed: {e}")
        return False

def run_integration_tests():
    """Run all integration tests"""
    print("=" * 70)
    print("APIWX Integration Test Suite")
    print("=" * 70)
    
    tests = [
        test_debug_with_patterns,
        test_message_system_availability,
        test_core_component_availability,
        test_mixins_with_inheritance,
        test_mixed_pattern_usage,
        test_mixins_system_integrity,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 70)
    print(f"Integration Test Results: {passed}/{total} tests passed")
    if passed == total:
        print("All integration tests PASSED!")
    else:
        print(f"{total - passed} integration test(s) FAILED")
    print("=" * 70)
    
    return passed == total

if __name__ == "__main__":
    success = run_integration_tests()
    sys.exit(0 if success else 1)