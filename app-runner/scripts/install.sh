#!/bin/sh

cd "$(dirname "$0")/../backend"

# Setup virtual environment
python3 -m venv venv
source venv/bin/activate

# Install requirements
pip3 install -r requirements.txt