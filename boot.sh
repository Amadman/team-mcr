#!/bin/sh
source venv/bin/activate
exec gunicorn --worker-class gevent --timeout 60 -b :5000 --access-logfile - --error-logfile - mcr:app
