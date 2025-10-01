@echo off
REM Windows Build Automation Script for apiwx
REM Usage: build.bat [options]

setlocal EnableDelayedExpansion

set PROJECT_NAME=apiwx
set BUILD_SCRIPT=build.py
set PYTHON=python

REM Colors for Windows (limited)
set GREEN=[92m
set YELLOW=[93m
set RED=[91m
set NC=[0m

if "%1"=="help" goto :help
if "%1"=="--help" goto :help
if "%1"=="-h" goto :help

if "%1"=="test" goto :test
if "%1"=="clean" goto :clean
if "%1"=="validate" goto :validate
if "%1"=="info" goto :info
if "%1"=="quick" goto :quick

REM Default action - build
if "%1"=="" goto :build

REM Build with version
if "%1"=="--version" (
    if "%2"=="" (
        echo %RED%Error: Version not specified. Use: build.bat --version x.y.z%NC%
        exit /b 1
    )
    goto :release
)

goto :build

:help
echo %GREEN%apiwx Build Automation%NC%
echo.
echo Available commands:
echo   %YELLOW%build.bat%NC%              - Build packages with current version
echo   %YELLOW%build.bat --version x.y.z%NC% - Build packages with version bump
echo   %YELLOW%build.bat test%NC%         - Run test suite
echo   %YELLOW%build.bat clean%NC%        - Clean build artifacts
echo   %YELLOW%build.bat validate%NC%     - Validate environment
echo   %YELLOW%build.bat info%NC%         - Show package information  
echo   %YELLOW%build.bat quick%NC%        - Quick build without tests
echo   %YELLOW%build.bat help%NC%         - Show this help
echo.
echo Examples:
echo   build.bat
echo   build.bat --version 0.1.15
echo   build.bat test
goto :end

:build
echo %GREEN%Building %PROJECT_NAME%...%NC%
%PYTHON% %BUILD_SCRIPT%
if %ERRORLEVEL% NEQ 0 (
    echo %RED%Build failed%NC%
    exit /b %ERRORLEVEL%
)
echo %GREEN%Build completed successfully%NC%
goto :end

:release
echo %GREEN%Building %PROJECT_NAME% version %2...%NC%
%PYTHON% %BUILD_SCRIPT% --version %2
if %ERRORLEVEL% NEQ 0 (
    echo %RED%Build failed%NC%
    exit /b %ERRORLEVEL%
)
echo %GREEN%Release build completed successfully%NC%
goto :end

:test
echo %GREEN%Running tests...%NC%
%PYTHON% test/run_tests.py
if %ERRORLEVEL% NEQ 0 (
    echo %RED%Tests failed%NC%
    exit /b %ERRORLEVEL%
)
echo %GREEN%Tests passed%NC%
goto :end

:clean
echo %GREEN%Cleaning build artifacts...%NC%
%PYTHON% setup.py clean --all
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
for /r %%i in (*.egg-info) do if exist "%%i" rmdir /s /q "%%i"
for /r %%i in (__pycache__) do if exist "%%i" rmdir /s /q "%%i"
del /s /q *.pyc >nul 2>&1
echo %GREEN%Clean completed%NC%
goto :end

:validate
echo %GREEN%Validating environment...%NC%
if not exist "build.json" (
    echo %RED%Error: Configuration file build.json not found%NC%
    exit /b 1
)
if not exist "setup.py" (
    echo %RED%Error: setup.py not found%NC%
    exit /b 1
)
if not exist "test\run_tests.py" (
    echo %RED%Error: Test script test\run_tests.py not found%NC%
    exit /b 1
)
echo %GREEN%Environment validation passed%NC%
goto :end

:info
echo %GREEN%Package Information:%NC%
%PYTHON% -c "import sys; sys.path.insert(0, '.'); import %PROJECT_NAME%; print(f'Version: {%PROJECT_NAME%.__version__}'); print(f'Location: {%PROJECT_NAME%.__file__}')" 2>nul || echo Package not importable
if exist dist (
    echo.
    echo %GREEN%Build Artifacts:%NC%
    dir dist
)
goto :end

:quick
echo %GREEN%Quick build (no tests)...%NC%
%PYTHON% %BUILD_SCRIPT% --no-tests
if %ERRORLEVEL% NEQ 0 (
    echo %RED%Quick build failed%NC%
    exit /b %ERRORLEVEL%
)
echo %GREEN%Quick build completed%NC%
goto :end

:end
endlocal