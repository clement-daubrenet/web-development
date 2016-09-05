import requests
from datetime import timedelta
from celery import Celery
from celery.schedules import crontab
from celery.decorators import periodic_task

# 1. Install RABITMQ to get a message broker
# 2. Run it through invoke-rc.d rabbitmq-server start 
# 3. launch celery -A celeryapp worker --loglever=info
# See doc Celery online

app = Celery('celeryapp', broker='amqp://guest@localhost//')

# Periodic task 
# Planning the execution a request to openweather API.
# nb: here we fetch every 10 seconds. 
# To launch the job, -B is needed
# e.g : celery -A celeryapp worker --loglevel=info -B

@periodic_task(run_every=timedelta(seconds=10))
def weather():
    city_id = 2643743
    base_url = "http://api.openweathermap.org/data/2.5/forecast/"
    daily_url = "daily?id={}&APPID=64af4014d4d7321058115459dfc67525".format(city_id)
    url = base_url + daily_url
    return requests.get(url)
