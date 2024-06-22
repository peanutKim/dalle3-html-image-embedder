#!/bin/bash
set -e # Increase bash strictness
set -o pipefail

# Configure Git user identity
git config --global user.email "action@github.com"
git config --global user.name "GitHub Action"

git config --global --add safe.directory /github/workspace
chmod -R u+rwX,g+rwX,o+rwX .git

# Debugging permissions
ls -la .git
whoami

python /main.py
ls -la /github/workspace