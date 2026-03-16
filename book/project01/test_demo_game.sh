#!/bin/bash
# test_demo_game.sh
# Usage: ./test_demo_game.sh demo_game.py
# Or just run it and type the filename when prompted.

if [ -z "$1" ]; then
    read -p "Enter the student's filename (e.g. demo_game.py): " STUDENT_FILE
else
    STUDENT_FILE="$1"
fi

python3 test_demo_game.py "$STUDENT_FILE"
