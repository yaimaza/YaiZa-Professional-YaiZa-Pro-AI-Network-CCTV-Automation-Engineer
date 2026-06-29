@echo off
REM YaiZa-Pro Windows Installer Script
REM Automated installation for Windows systems

echo.
echo ============================
echo YaiZa-Pro Installer
echo AI Network CCTV Automation
echo ============================
echo.

REM Check for Python installation
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    echo Make sure to check "Add Python to PATH" during installation
    pause
    exit /b 1
)

echo [OK] Python found
python --version
echo.

REM Check for pip
pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip is not available
    pause
    exit /b 1
)

echo [OK] pip found
echo.

REM Create virtual environment
echo [*] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo [ERROR] Failed to create virtual environment
    pause
    exit /b 1
)

echo [OK] Virtual environment created
echo.

REM Activate virtual environment
echo [*] Activating virtual environment...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment
    pause
    exit /b 1
)

echo [OK] Virtual environment activated
echo.

REM Upgrade pip
echo [*] Upgrading pip...
python -m pip install --upgrade pip
if errorlevel 1 (
    echo [WARNING] Failed to upgrade pip, continuing...
)

echo.

REM Install dependencies
echo [*] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)

echo [OK] Dependencies installed
echo.

REM Install YaiZa-Pro in development mode
echo [*] Installing YaiZa-Pro...
pip install -e .
if errorlevel 1 (
    echo [ERROR] Failed to install YaiZa-Pro
    pause
    exit /b 1
)

echo [OK] YaiZa-Pro installed
echo.

REM Create necessary directories
echo [*] Creating required directories...
if not exist "logs" mkdir logs
if not exist "data" mkdir data
if not exist "config" mkdir config

echo [OK] Directories created
echo.

echo ============================
echo Installation Complete!
echo ============================
echo.
echo To run YaiZa-Pro:
echo   1. Activate virtual environment: venv\Scripts\activate.bat
echo   2. Run: python main.py
echo.
echo Or simply run: venv\Scripts\yaiza-pro.exe
echo.
pause
