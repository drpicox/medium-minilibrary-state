#!/bin/bash
# Mini Library Manager - Web Edition Startup Script

# Try to find Python with Flask installed
# First try conda python if available
if command -v conda &> /dev/null; then
    PYTHON_CMD=$(conda run which python3)
elif command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
else
    echo "Error: Python 3 not found. Please install Python 3 and Flask."
    exit 1
fi

# Run the Flask app
"$PYTHON_CMD" "$(dirname "$0")/app.py"
