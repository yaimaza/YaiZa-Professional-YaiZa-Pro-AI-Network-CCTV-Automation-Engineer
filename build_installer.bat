@echo off
REM YaiZa-Pro Windows Installer Builder
REM Requires: Inno Setup (https://jrsoftware.org/isinfo.php)

echo.
echo ================================
echo YaiZa-Pro Installer Builder
echo ================================
echo.

REM Check if Inno Setup is installed
where iscc >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Inno Setup is not installed or not in PATH
    echo Please download from: https://jrsoftware.org/isdl.php
    echo.
    pause
    exit /b 1
)

echo [OK] Inno Setup found
echo.

REM Check if EXE exists
if not exist "dist\YaiZa-Pro.exe" (
    echo [ERROR] dist\YaiZa-Pro.exe not found
    echo Please run: python build_exe.py
    echo.
    pause
    exit /b 1
)

echo [OK] YaiZa-Pro.exe found
echo.

REM Build installer
echo [*] Building installer...
iscc setup.iss

if errorlevel 1 (
    echo [ERROR] Failed to build installer
    pause
    exit /b 1
)

echo.
echo ================================
echo [OK] Installer created successfully!
echo ================================
echo.
echo Location: output\YaiZa-Pro-Setup.exe
echo.
pause
