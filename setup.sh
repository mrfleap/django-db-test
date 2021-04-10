#!/usr/bin/env bash

echo "Installing requirements"
pip install -r requirements.txt

echo "Applying DB migrations"
python manage.py migrate