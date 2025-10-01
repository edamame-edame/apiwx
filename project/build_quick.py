#!/usr/bin/env python3
"""
Quick Build Helper Script for apiwx
Simplified interface for common build operations
"""
import sys
import os
from pathlib import Path

# Add current directory to Python path to import auto_build
sys.path.insert(0, str(Path(__file__).parent))

from auto_build import BuildAutomation

def main():
    """Simple interactive build script"""
    print("=== apiwx Quick Build Tool ===")
    print("1. Build wheel (no tests)")
    print("2. Build wheel with new version")
    print("3. Build with tests")
    print("4. Clean only")
    print("0. Exit")

    choice = input("\nChoose option (0-4): ").strip()

    if choice == "0":
        print("Exiting...")
        return

    # Change to project root directory for build operations
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)
    print(f"Changed to project root: {project_root}")

    automation = BuildAutomation()

    if choice == "1":
        # Build without tests
        automation.config['test']['run_tests_before_build'] = False
        success = automation.build()

    elif choice == "2":
        # Build with version update
        version = input("Enter new version (e.g., 0.1.18): ").strip()

        if not version:
            print("No version provided, exiting...")
            return
        
        automation.config['test']['run_tests_before_build'] = False
        success = automation.build(version)

    elif choice == "3":
        # Build with tests
        success = automation.build()

    elif choice == "4":
        # Clean only
        print("Cleaning build artifacts...")
        success = automation.clean_build()

    else:
        print("Invalid choice!")
        return

    if success:
        print("\n Operation completed successfully!")
        
    else:
        print("\n Operation failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()