#!/usr/bin/env bash

echo "Installing Django 3.1.8"
pip install django==3.1.8

echo "Running test on 3.1.8"
python manage.py test

echo "Installing Django 3.2"
pip install django==3.2

echo "Running test on 3.2"
python manage.py test