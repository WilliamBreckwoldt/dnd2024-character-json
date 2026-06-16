@echo off
REM D&D 2024 Character Sheet Generator
REM Fills the D&D 2024 fillable template from JSON character data.
REM
REM Usage:  generate_sheets.bat
REM
REM Requires Python 3.7+ and pypdf:
REM   pip install pypdf

cd /d "%~dp0"

where python >nul 2>nul
if %errorlevel% neq 0 (
    echo ERROR: Python not found. Make sure Python 3.7+ is installed and on your PATH.
    pause
    exit /b 1
)

python -c "import pypdf" >nul 2>nul
if %errorlevel% neq 0 (
    echo pypdf not installed. Installing now...
    pip install pypdf
    if %errorlevel% neq 0 (
        echo ERROR: Failed to install pypdf. Try: pip install pypdf
        pause
        exit /b 1
    )
)

python generate_sheets.py %*
echo.
pause
