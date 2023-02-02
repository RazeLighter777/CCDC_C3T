#!/bin/bash

# SSH Honeypot

ENABLED_SERVICES = ""

echo "Installing SSH Honeypot using fail2ban and endlessh..."

while getopts u:a:f: flag
do
    case "${flag}" in
        s) ENABLED_SERVICES+="${OPTARG} ";;
    esac
done

sudo apt update
sudo apt install fail2ban

echo "fail2ban service status:"
systemctl status fail2ban.service

echo "Access fail2ban config at /etc/fail2ban/jail.local"

F2B_ENABLER_CONFIG=""

for service in ENABLED_SERVICES
do
    F2B_ENABLER_CONFIG+="[$service]
enabled = true
"
done

sudo echo $F2B_ENABLER_CONFIG >> /etc/fail2ban/jail.local

echo "Installing endlessh..."

git clone https://github.com/skeeto/endlessh.git
sudo apt-get install build-essential -y
cd endlessh
make
sudo make install
sudo cp util/endlessh.service /etc/systemd/system


echo "Installing fail2ban-endlessh honeypot..."
sudo cp action.d/endlessh.conf /etc/fail2ban/action.d/endlessh.conf