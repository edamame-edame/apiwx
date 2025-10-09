import os
import sys
import subprocess

def run_test(test_file):
    print(f"\n{'='*50}")
    print(f"Running: {test_file}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run([sys.executable, f"test/{test_file}"], 
                              capture_output=True, text=True, encoding='utf-8')
        
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        success = result.returncode == 0
        status = "PASS" if success else "FAIL"
        print(f"[{status}] {test_file}")
        return success
        
    except Exception as e:
        print(f"[ERROR] {test_file}: {e}")
        return False

def main():
    print("apiwx Master Test Runner")
    print("=" * 50)
    
    tests = [
        "quick_test.py",
        "basic_test_runner.py",
        "pattern_tests.py", 
        "integration_tests.py",
        "comprehensive_test_runner.py",
        "test_mixins_core_changes.py"
    ]
    
    passed = 0
    total = 0
    
    for test in tests:
        if os.path.exists(f"test/{test}"):
            total += 1
            if run_test(test):
                passed += 1
        else:
            print(f"[SKIP] {test} (not found)")
    
    print(f"\n{'='*50}")
    print(f"SUMMARY: {passed}/{total} tests passed")
    print(f"{'='*50}")
    
    return passed == total and total > 0

if __name__ == "__main__":
    success = main()
    print(f"\nOverall result: {'SUCCESS' if success else 'FAILURE'}")
    sys.exit(0 if success else 1)