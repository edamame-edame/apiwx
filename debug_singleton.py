#!/usr/bin/env python3

import sys
import traceback
sys.path.insert(0, '.')

try:
    from apiwx.generics_core import GenericsType
    from apiwx.generics_base import Singleton
    print("Imports successful")

    class TestClass(metaclass=GenericsType):
        def __init__(self, value=42):
            self.value = value
    print("Base class created")

    SingletonTest = TestClass[Singleton]
    print("Singleton class created")
    print(f"Class type: {type(SingletonTest)}")
    print(f"Class MRO: {SingletonTest.__mro__}")

    print("Attempting to create first instance...")
    obj1 = SingletonTest(100)
    print("First instance created successfully")
    print(f"obj1.value = {obj1.value}")

    print("Attempting to create second instance...")
    obj2 = SingletonTest(200)
    print("Second instance created successfully")
    print(f"obj2.value = {obj2.value}")
    print(f"obj1 is obj2: {obj1 is obj2}")

except Exception as e:
    print(f"Error occurred: {e}")
    traceback.print_exc()