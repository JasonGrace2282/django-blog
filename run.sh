#!/usr/bin/bash

celery -A blog worker -l info -B &> .celery-log &
./manage.py runserver
