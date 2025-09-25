#!/usr/bin/env bash
# Build script for BMS Auto Glass on Render

set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate
