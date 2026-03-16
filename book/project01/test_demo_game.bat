@echo off
:: test_demo_game.bat
:: Usage: test_demo_game.bat demo_game.py
:: Or just double-click and type the filename when prompted.

if "%~1"=="" (
    set /p STUDENT_FILE="Enter the student's filename (e.g. demo_game.py): "
) else (
    set STUDENT_FILE=%~1
)

python test_demo_game.py %STUDENT_FILE%
pause
