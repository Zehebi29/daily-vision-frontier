#!/bin/bash
# Git credential helper for cron: reads token from a secure file
# Usage: git credential fill < <(echo "protocol=https"); git -c credential.helper=/path/to/this ...
read -r line
if [[ "$line" == "protocol=https" ]]; then
  echo "username=Zehebi29"
  echo "password=$(cat /home/ubuntu/.git-token)"
fi
