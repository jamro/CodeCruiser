#!/bin/bash

# Ensure the script runs only on a Raspberry Pi
if ! grep -q "Raspberry Pi" /proc/device-tree/model; then
  echo "This script must be run on a Raspberry Pi. Exiting..."
  exit 1
fi

sudo apt-get update -y
sudo apt-get install git -y
sudo apt install python3 python3-pip

# Configure Watchdog
sudo apt install watchdog -y
if ! grep -q "dtparam=watchdog=on" /boot/config.txt; then
  echo "Enabling watchdog in config.txt..."
  echo "dtparam=watchdog=on" | sudo tee -a /boot/config.txt
fi

sudo systemctl enable watchdog
sudo systemctl start watchdog

cd /home/pi/

# Clone or update the repository
REPO_URL="https://github.com/jamro/CodeCruiser.git"
REPO_DIR="CodeCruiser"
git config --global --add safe.directory /home/pi/CodeCruiser

if [ -d "$REPO_DIR" ]; then
  echo "Directory '$REPO_DIR' exists. Pulling latest changes..."
  cd "$REPO_DIR"
  sudo git stash --include-untracked
  sudo git pull
  sudo git stash pop
else
  echo "Cloning repository..."
  git clone "$REPO_URL" "$REPO_DIR"
  cd "$REPO_DIR"
fi

cd runberry/backend
sudo -H pip install -r requirements.txt --break-system-packages

# install codecruiser library
cd /home/pi/CodeCruiser/cruiserlib
sudo -H pip install -e . --break-system-packages


# Add start.sh to autostart with root privileges
SERVICE_NAME="runberry.service"
SERVICE_FILE="/etc/systemd/system/$SERVICE_NAME"

if [ ! -f "$SERVICE_FILE" ]; then
  echo "Creating systemd service for start.sh..."
  sudo bash -c "cat > $SERVICE_FILE" <<EOL
[Unit]
Description=App Runner Service
After=network.target

[Service]
ExecStart=/home/pi/CodeCruiser/runberry/scripts/start.sh
WorkingDirectory=/home/pi/CodeCruiser/runberry/scripts
StandardOutput=inherit
StandardError=inherit
Restart=always
User=root

[Install]
WantedBy=multi-user.target
EOL

  sudo chmod 644 "$SERVICE_FILE"
  sudo systemctl enable "$SERVICE_NAME"
  echo "Service '$SERVICE_NAME' created and enabled."
else
  echo "Service '$SERVICE_NAME' already exists. Restarting it..."
  sudo systemctl restart "$SERVICE_NAME"
fi

echo "Installation complete. Reboot the system to apply changes."

