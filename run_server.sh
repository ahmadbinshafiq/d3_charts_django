#!/bin/bash

python3 manage.py makemigrations
python3 manage.py migrate

if ! python3 manage.py test; then
    echo "Tests failed. Server not started."
    exit 1
fi

python3 manage.py runserver
