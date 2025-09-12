#!/bin/sh

python manage.py collectstatic --noinput

python manage.py migrate --noinput

exec gunicorn educational.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 4 \
  --threads 2 \
  --timeout 60
