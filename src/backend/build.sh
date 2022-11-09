#!/usr/bin/env bash
# exit on error
set -o errexit
apt-get install -y tesseract-ocr-all
pip install --upgrade pip
pip install -r requirements.txt