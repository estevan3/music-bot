@echo off

IF NOT EXIST "venv" (
    echo Creating virtual environment...
    python -m venv venv --upgrade-deps
)

call venv\Scripts\activate

echo Checking and installing necessary packages...
pip install -r requirements.txt
pip install --upgrade yt-dlp

echo Starting...
python main.py
