from celery.schedules import crontab

BROKER_URL = "amqp://guest@localhost//"
CELERYBEAT_SCHEDULE = {
    'every-minute': {
        'task': 'celeryapp.weather',
        'schedule': crontab(minute='*/1'),
        'args': [2643733],
    },
}


