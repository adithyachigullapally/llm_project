@echo off
setlocal
title AutoMate AI Setup Script

REM Fix encoding just in case
chcp 65001 >nul

echo ================================================================
echo [INFO] AUTOMATE AI - Windows Setup Script
echo        Voice-Enabled Global Car Concierge
echo ================================================================
echo.

REM 1. Check Python
echo [STEP 1] Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found! Please install Python 3.10 or newer.
    echo         Download: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo [OK] Python found.
echo.

REM 2. Project Structure Setup
echo [STEP 2] Setting up project folder structure...
if exist "setup_project.py" (
    python setup_project.py
) else (
    echo [WARN] setup_project.py not found. Assuming folders are correct.
)
echo.

REM 3. Virtual Environment
if not exist "venv" (
    echo [STEP 3] Creating virtual environment...
    python -m venv venv
) else (
    echo [INFO] Virtual environment already exists.
)

REM 4. Activate Venv
echo [STEP 4] Activating virtual environment...
call venv\Scripts\activate
if errorlevel 1 (
    echo [ERROR] Failed to activate virtual environment.
    pause
    exit /b 1
)
echo [OK] Virtual environment activated.
echo.

REM 5. Install Dependencies
echo [STEP 5] Installing dependencies from requirements.txt...
python -m pip install --upgrade pip
pip install -r requirements.txt

REM 5b. Windows Audio Fixes (PyAudio)
echo [STEP 5b] Checking Windows Audio drivers...
python -c "import pyaudio" 2>nul
if errorlevel 1 (
    echo    [WARN] Standard PyAudio install failed. Trying pipwin workaround...
    pip install pipwin
    pipwin install pyaudio
)
echo [OK] Dependencies installed.
echo.

REM 6. Environment Variables
if not exist ".env" (
    echo [STEP 6] Creating .env file template...
    echo OPENAI_API_KEY=paste_your_key_here > .env
    echo [WARN] IMPORTANT: A new .env file was created. 
    echo        Please open it and paste your OpenAI API Key before running!
) else (
    echo [OK] .env file found.
)
echo.

REM 7. Success
echo ================================================================
echo [SUCCESS] SETUP COMPLETE!
echo ================================================================
echo.
echo HOW TO RUN:
echo    1. Ensure your OpenAI API Key is in the .env file.
echo    2. Type the following command to start:
echo.
echo       python main.py
echo.
pause