#!/bin/bash
set -e # Increase bash strictness
set -o pipefail

# Configure Git user identity
git config --global user.email "action@github.com"
git config --global user.name "GitHub Action"

git config --global --add safe.directory /github/workspace
python /main.py
ls -la /github/workspace