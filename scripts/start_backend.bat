@echo off
cd /d "%~dp0\.."
echo Starting ASX Analytics Backend...

REM Check if virtual environment exists
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Check if .env file exists
if not exist ".env" (
    echo Creating .env file from template...
    copy .env.example .env
    echo Please update .env file with your API keys!
)

REM Start the backend
echo Starting FastAPI server...
cd backend
python main.py