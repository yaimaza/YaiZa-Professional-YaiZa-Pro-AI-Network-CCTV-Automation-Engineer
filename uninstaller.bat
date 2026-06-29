@echo off
REM YaiZa-Pro Uninstaller Script
REM Removes YaiZa-Pro and virtual environment

echo.
echo ============================
echo YaiZa-Pro Uninstaller
echo ============================
echo.

echo [*] Removing virtual environment...
if exist "venv" (
    rmdir /s /q venv
    echo [OK] Virtual environment removed
) else (
    echo [INFO] Virtual environment not found
)

echo.
echo [*] Cleaning up Python cache files...
for /d /r . %%d in (__pycache__) do @if exist "%%d" rmdir /s /q "%%d"
echo [OK] Cache cleaned

echo.
echo ============================
echo Uninstallation Complete!
echo ============================
echo.
pause
