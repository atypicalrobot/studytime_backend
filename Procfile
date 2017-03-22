web: gunicorn config.wsgi:application
worker: celery worker --app=studytime.taskapp --loglevel=info
