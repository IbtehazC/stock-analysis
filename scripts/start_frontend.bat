@echo off
cd /d "%~dp0\..\frontend"
echo Starting ASX Analytics Frontend...

REM Check if node_modules exists
if not exist "node_modules" (
    echo Installing npm dependencies...
    npm install
) else (
    echo Dependencies already installed, starting development server...
)

echo Starting React development server...
npm start