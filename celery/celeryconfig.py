from celery.schedules import crontab

BROKER_URL = "amqp://guest@localhost//"
CELERYBEAT_SCHEDULE = {
    'every-minute': {
        'task': 'celeryapp.weather',
        'schedule': crontab(minute='*/1'),
        'args': [[2643743, 2950159, 2988507, 5344157]],
    },
}


