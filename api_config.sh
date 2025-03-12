#!/bin/bash

echo "Creating Python Virtual environment"
python3 -m venv pytenable
wait 10
echo "Activating virtual environment"
source pytenable/bin/activate
echo "Upgrading pip"
pip install --upgrade pip
wait 15
echo "Installing required packages"
pip install -r ./requirements.txt
wait 10
echo "Packages Installed $(pip list)"

