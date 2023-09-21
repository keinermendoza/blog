#! /bin/bash

echo 'collecting static files'
python manage.py collectstatic --no-input --settings=mysite.settings.prod

echo 'Aplaying migrations'
python manage.py migrate --settings=mysite.settings.prod

echo 'Running gunicorn server'
gunicorn --env DJANGO_SETTINGS_MODULE=mysite.settings.prod mysite.wsgi:application --bind 0.0.0.0:8000
