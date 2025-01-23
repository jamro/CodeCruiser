#!/bin/bash

cd ~

sudo apt-get update -y
sudo apt-get install git -y
sudo apt install python3 python3-pip
pip install uvicorn --user --break-system-packages

REPO_URL="https://github.com/jamro/CodeCruiser.git"
REPO_DIR="CodeCruiser"

if [ -d "$REPO_DIR" ]; then
  echo "Directory '$REPO_DIR' exists. Pulling latest changes..."
  cd "$REPO_DIR"
  git pull
else
  echo "Cloning repository..."
  git clone "$REPO_URL" "$REPO_DIR"
  cd "$REPO_DIR"
fi


cd app-runner/backend
pip install -r requirements.txt --user --break-system-packages