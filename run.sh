#!/bin/bash
gunicorn -c gunicorn.conf.py web.wsgi:application -b 0.0.0.0:8000
# --log-driver json-file --log-opt max-size=10m
#docker run --restart always -d --log-driver json-file --log-opt max-size=10m --name django_app -p 8000:8000 -v `pwd`/logs:/var/www/app/logs hyhlinux/django_app
