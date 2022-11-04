#!/usr/bin/env bash
# exit on error
set -o errexit
sudo apt install tesseract-ocr-all -y
pip install --upgrade pip
pip install -r requirements.txt