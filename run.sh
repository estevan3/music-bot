#!/bin/bash

if [ ! -d "venv" ]; then
  echo -e "\nCreating virtual environment...\n"
  python -m venv venv --upgrade-deps
fi

source venv/Scripts/activate

echo -e "\nChecking and installing necessary packages...\n"
pip install -r requirements.txt
pip install --upgrade yt-dlp

echo -e "\nStarting...\n"
python main.py
