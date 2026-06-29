@echo off
REM YaiZa-Pro Complete Build Script for Windows

echo.
echo =====================================================
echo YaiZa-Pro - Complete Build Process
echo =====================================================
echo.

REM Check Python
echo [1/3] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed
    pause
    exit /b 1
)
echo [OK] Python found
echo.

REM Install dependencies
echo [2/3] Installing dependencies...
pip install --upgrade pip
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo [OK] Dependencies installed
echo.

REM Build EXE
echo [3/3] Building EXE...
python build_exe.py
if errorlevel 1 (
    echo [ERROR] Failed to build EXE
    pause
    exit /b 1
)
echo [OK] EXE built successfully
echo.

echo =====================================================
echo Build Complete!
echo =====================================================
echo.
echo Next steps:
echo 1. Run installer builder: build_installer.bat
echo    (requires Inno Setup installed)
echo.
echo Or run directly: dist\YaiZa-Pro.exe
echo.
pause
