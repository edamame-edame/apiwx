#!/usr/bin/env python3
"""
Automated Build Script for apiwx
Handles version updates, testing, and package building based on build.json configuration
"""
import json
import os
import sys
import subprocess
import re
import time
import shutil
import glob
from pathlib import Path
from typing import Dict, List, Any, Optional

class BuildAutomation:
    def __init__(self, config_file: str = "build.json"):
        # If config_file is relative, resolve it relative to this script's directory
        if not os.path.isabs(config_file):
            script_dir = Path(__file__).parent
            config_file = str(script_dir / config_file)

        self.config_file = config_file
        self.config = self._load_config()
        self.project_root = Path.cwd()
        self.start_time = time.time()

    def _load_config(self) -> Dict[str, Any]:
        """Load build configuration from JSON file"""
        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"[WARNING] Configuration file '{self.config_file}' not found, using defaults")
            return self._get_default_config()
        except json.JSONDecodeError as e:
            print(f"[ERROR] Invalid JSON in '{self.config_file}': {e}")
            return self._get_default_config()

    def _get_default_config(self) -> Dict[str, Any]:
        """Get default configuration when build.json is not available"""
        return {
            "project": {
                "name": "apiwx",
                "description": "wxPython API wrapper with advanced generics system",
                "author": "edamame",
                "license": "MIT"
            },
            "build": {
                "clean_before_build": True,
                "create_wheel": True,
                "create_source": True,
                "run_tests_before_build": True,
                "output_directory": "dist",
                "build_directory": "build"
            },
            "test": {
                "test_command": "python test/master_test.py",
                "require_100_percent_success": False,
                "timeout_seconds": 60,
                "run_tests_before_build": True
            },
            "version": {
                "files_to_update": [
                    {
                        "file": "pyproject.toml",
                        "pattern": "version = \"{old_version}\"",
                        "replacement": "version = \"{new_version}\""
                    },
                    {
                        "file": "apiwx/__init__.py",
                        "pattern": "__version__ = \"{old_version}\"",
                        "replacement": "__version__ = \"{new_version}\""
                    }
                ]
            },
            "commands": {
                "clean": "python -c \"import shutil; shutil.rmtree('build', ignore_errors=True); shutil.rmtree('dist', ignore_errors=True)\"",
                "build": "python -m build",
                "wheel": "python -m build --wheel",
                "source": "python -m build --sdist",
                "test": "python test/master_test.py"
            },
            "validation": {
                "check_files_exist": [
                    "pyproject.toml",
                    "apiwx/__init__.py"
                ]
            },
            "post_build": {
                "list_output_files": True,
                "verify_import": True,
                "show_package_info": True
            }
        }

    def _run_command(self, command: str, description: str = None, timeout: int = 60) -> tuple[bool, str]:
        """Run a shell command and return success status and output"""
        if description:
            print(f">> {description}")
        
        try:
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding='utf-8',
                errors='replace'
            )

            try:
                stdout, stderr = process.communicate(timeout=timeout)
                
                if process.returncode == 0:
                    if description:
                        print(f"[OK] Success: {description}")
                    return True, stdout
                else:
                    if description:
                        print(f"[ERROR] Failed: {description}")
                    if stderr:
                        print(f"Error: {stderr}")
                    return False, stderr or stdout

            except subprocess.TimeoutExpired:
                print(f"[TIMEOUT] Command timed out after {timeout}s")
                process.kill()
                stdout, stderr = process.communicate()
                return False, f"Command timed out after {timeout} seconds"

        except Exception as e:
            print(f"[EXCEPTION] {description or command}: {e}")
            return False, str(e)

    def validate_environment(self) -> bool:
        """Validate that all required files exist"""
        print("\n>> Validating Environment...")

        validation_config = self.config.get('validation', {})
        required_files = validation_config.get('check_files_exist', [])
        
        for file_path in required_files:
            if not Path(file_path).exists():
                print(f"[ERROR] Required file missing: {file_path}")
                return False
            else:
                print(f"[OK] Found: {file_path}")

        print("[OK] Environment validation passed")
        return True

    def get_current_version(self) -> Optional[str]:
        """Extract current version from pyproject.toml"""
        try:
            pyproject_path = Path('pyproject.toml')
            if pyproject_path.exists():
                with open(pyproject_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                match = re.search(r'version\s*=\s*["\']([^"\']+)["\']', content)
                if match:
                    return match.group(1).strip()
            
            # Fallback: try to get from __init__.py
            init_path = Path('apiwx/__init__.py')
            if init_path.exists():
                with open(init_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', content)
                if match:
                    return match.group(1).strip()
            
            return None
        except Exception as e:
            print(f"[ERROR] Failed to read current version: {e}")
            return None

    def update_version(self, new_version: str) -> bool:
        """Update version in all configured files"""
        print(f"\n>> Updating version to {new_version}...")

        current_version = self.get_current_version()
        if not current_version:
            print("[ERROR] Could not determine current version")
            return False

        print(f"Current version: {current_version}")
        print(f"New version: {new_version}")

        version_config = self.config.get('version', {})
        files_to_update = version_config.get('files_to_update', [])

        for file_info in files_to_update:
            file_path = file_info['file']
            pattern = file_info['pattern']
            replacement = file_info['replacement']

            try:
                if not Path(file_path).exists():
                    print(f"[WARNING] File not found: {file_path}")
                    continue

                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                old_pattern = pattern.format(old_version=current_version)
                new_replacement = replacement.format(new_version=new_version)

                if old_pattern in content:
                    content = content.replace(old_pattern, new_replacement)

                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)

                    print(f"[OK] Updated {file_path}")
                else:
                    print(f"[WARNING] Pattern not found in {file_path}: {old_pattern}")

            except Exception as e:
                print(f"[ERROR] Failed to update {file_path}: {e}")
                return False

        return True

    def run_tests(self) -> bool:
        """Run test suite if configured"""
        test_config = self.config.get('test', {})
        build_config = self.config.get('build', {})
        
        # Check both test config and build config for test execution flag
        run_tests = (
            test_config.get('run_tests_before_build', True) and 
            build_config.get('run_tests_before_build', True)
        )
        
        if not run_tests:
            print("[SKIP] Skipping tests (disabled in config)")
            return True

        print("\n>> Running Tests...")

        # Use master_test.py if run_tests.py doesn't exist
        test_command = test_config.get('test_command', 'python test/master_test.py')
        
        # Auto-detect test runner
        if not Path('test/run_tests.py').exists() and Path('test/master_test.py').exists():
            test_command = 'python test/master_test.py'
            print(f"[INFO] Using master_test.py as test runner")
        elif Path('test/run_tests.py').exists():
            test_command = 'python test/run_tests.py'
            print(f"[INFO] Using run_tests.py as test runner")

        timeout = test_config.get('timeout_seconds', 120)  # Increased default timeout
        require_success = test_config.get('require_100_percent_success', False)

        success, output = self._run_command(
            test_command,
            "Running test suite",
            timeout
        )

        if not success:
            if require_success:
                print("[ERROR] Tests failed - aborting build")
                return False
            else:
                print("[WARNING] Tests failed but continuing build")

        return True

    def clean_build(self) -> bool:
        """Clean previous build artifacts"""
        build_config = self.config.get('build', {})

        if not build_config.get('clean_before_build', True):
            print("[SKIP] Skipping clean (disabled in config)")
            return True

        print("\n>> Cleaning Previous Builds...")

        try:
            # Remove common build directories
            for dir_name in ['build', 'dist']:
                if Path(dir_name).exists():
                    shutil.rmtree(dir_name)
                    print(f"[OK] Removed {dir_name} directory")

            # Remove egg-info directories
            for egg_info in glob.glob('*.egg-info'):
                if Path(egg_info).exists():
                    shutil.rmtree(egg_info)
                    print(f"[OK] Removed {egg_info}")

            # Remove __pycache__ directories
            for cache_dir in Path('.').rglob('__pycache__'):
                try:
                    shutil.rmtree(cache_dir)
                    print(f"[OK] Removed {cache_dir}")
                except:
                    pass  # Skip if in use

            return True

        except Exception as e:
            print(f"[WARNING] Error during cleanup: {e}")
            return False

    def build_packages(self) -> bool:
        """Build wheel and source packages"""
        print("\n>> Building Packages...")

        build_config = self.config.get('build', {})
        commands = self.config.get('commands', {})

        # Check if build module is available
        success, _ = self._run_command(
            'python -c "import build"',
            "Checking build module availability"
        )

        if not success:
            print("[INFO] Installing build module...")
            install_success, _ = self._run_command(
                'pip install build',
                "Installing build module",
                timeout=120
            )
            if not install_success:
                print("[ERROR] Failed to install build module")
                return False

        # Determine what to build
        create_wheel = build_config.get('create_wheel', True)
        create_source = build_config.get('create_source', True)

        if create_wheel and create_source:
            # Build both wheel and source distribution
            build_command = commands.get('build', 'python -m build')
            success, output = self._run_command(
                build_command,
                "Building wheel and source packages",
                timeout=180
            )
            if not success:
                print(f"[ERROR] Build failed: {output}")
                return False
        else:
            # Build individually
            if create_wheel:
                wheel_command = commands.get('wheel', 'python -m build --wheel')
                success, output = self._run_command(
                    wheel_command,
                    "Creating wheel package",
                    timeout=120
                )
                if not success:
                    print(f"[ERROR] Wheel build failed: {output}")
                    return False

            if create_source:
                source_command = commands.get('source', 'python -m build --sdist')
                success, output = self._run_command(
                    source_command,
                    "Creating source distribution",
                    timeout=120
                )
                if not success:
                    print(f"[ERROR] Source build failed: {output}")
                    return False

        return True

    def post_build_validation(self) -> bool:
        """Perform post-build validation and reporting"""
        print("\n>> Post-Build Validation...")

        post_config = self.config.get('post_build', {})
        build_config = self.config.get('build', {})
        dist_dir = build_config.get('output_directory', 'dist')

        # List output files
        if post_config.get('list_output_files', True):
            try:
                dist_path = Path(dist_dir)
                if dist_path.exists():
                    print(f"\nBuild artifacts in {dist_dir}:")
                    total_size = 0
                    for file in dist_path.iterdir():
                        if file.is_file():
                            size = file.stat().st_size
                            total_size += size
                            print(f" - {file.name} ({size:,} bytes)")
                    print(f"Total size: {total_size:,} bytes")
                else:
                    print(f"[WARNING] Output directory {dist_dir} not found")
            except Exception as e:
                print(f"[WARNING] Could not list output files: {e}")

        # Verify import
        if post_config.get('verify_import', True):
            project_name = self.config['project']['name']
            success, output = self._run_command(
                f'python -c "import sys; sys.path.insert(0, \'.\'); import {project_name}; print(f\'{project_name} imported successfully\')"',
                "Verifying package import"
            )
            if success:
                print(f"[OK] Import verification successful")
            else:
                print(f"[WARNING] Import verification failed")

        # Show package info
        if post_config.get('show_package_info', True):
            current_version = self.get_current_version()
            if current_version:
                print(f"\n[INFO] Package: {self.config['project']['name']} v{current_version}")

        return True

    def build(self, version: str = None) -> bool:
        """Execute complete build process"""
        print("=" * 60)
        print(">> Starting Automated Build Process")
        print(f"Project: {self.config['project']['name']}")
        print(f"Config: {self.config_file}")
        print("=" * 60)

        # Step 1: Validate environment
        if not self.validate_environment():
            return False

        # Step 2: Update version if specified
        if version:
            if not self.update_version(version):
                return False

        # Step 3: Run tests
        if not self.run_tests():
            return False

        # Step 4: Clean previous builds
        if not self.clean_build():
            return False

        # Step 5: Build packages
        if not self.build_packages():
            return False

        # Step 6: Post-build validation
        if not self.post_build_validation():
            return False

        # Success!
        elapsed = time.time() - self.start_time
        print("=" * 60)
        print(f">> Build completed successfully in {elapsed:.2f} seconds!")
        print("=" * 60)
        return True

def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description="Automated build script for apiwx")
    parser.add_argument('--version', help='New version to set (e.g., 0.1.18)')
    parser.add_argument('--config', default='build.json', help='Configuration file path')
    parser.add_argument('--no-tests', action='store_true', help='Skip running tests')
    parser.add_argument('--no-clean', action='store_true', help='Skip cleaning previous builds')
    parser.add_argument('--wheel-only', action='store_true', help='Build wheel package only')
    parser.add_argument('--source-only', action='store_true', help='Build source distribution only')

    args = parser.parse_args()

    # Load automation with config
    automation = BuildAutomation(args.config)

    # Apply command line overrides
    if args.no_tests:
        automation.config['build']['run_tests_before_build'] = False
        automation.config['test']['run_tests_before_build'] = False
    
    if args.no_clean:
        automation.config['build']['clean_before_build'] = False
    
    if args.wheel_only:
        automation.config['build']['create_wheel'] = True
        automation.config['build']['create_source'] = False
    
    if args.source_only:
        automation.config['build']['create_wheel'] = False
        automation.config['build']['create_source'] = True

    # Run build
    success = automation.build(args.version)
    
    if success:
        print("\n🎉 Build completed successfully!")
    else:
        print("\n❌ Build failed!")
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
