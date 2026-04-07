@echo off
REM ============================================================
REM run_project.bat
REM One-click script to set up and run the ModelOps project
REM Double-click this file or run it from Command Prompt
REM ============================================================

echo.
echo =========================================
echo   ModelOps - End-to-End ML Pipeline
echo =========================================
echo.

REM ---- Step 1: Check if Python is installed ----
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python 3.11 from https://python.org
    pause
    exit /b 1
)

echo [OK] Python found.

REM ---- Step 2: Move to the backend folder ----
cd /d "%~dp0backend"
echo [OK] Changed directory to backend.

REM ---- Step 3: Install Python dependencies ----
echo.
echo Installing Python packages...
echo (This may take 1-2 minutes on first run)
echo.
pip install -r requirements.txt

IF ERRORLEVEL 1 (
    echo ERROR: Failed to install requirements. Check your internet connection.
    pause
    exit /b 1
)

echo [OK] Packages installed.

REM ---- Step 4: Train the model ----
echo.
echo Training the Machine Learning model...
echo.
python train_model.py

IF ERRORLEVEL 1 (
    echo ERROR: Model training failed. Check the error message above.
    pause
    exit /b 1
)

echo [OK] Model trained and saved as model.pkl

REM ---- Step 5: Start FastAPI server and open UI ----
echo.
echo =========================================
echo   Starting FastAPI server...
echo   Opening UI in your browser...
echo.
echo   Press Ctrl+C to stop the server.
echo =========================================
echo.

REM Open index.html automatically (using "start")
start "" "%~dp0frontend\index.html"

REM Start the FastAPI server (blocking)
python -m uvicorn app:app --host 0.0.0.0 --port 8000 --reload

