import requests
from datetime import timedelta
from celery import Celery
from celery.schedules import crontab
from celery.decorators import periodic_task

# 1. Install RABITMQ to get a message broker
# 2. Run it through invoke-rc.d rabbitmq-server start
# 3. launch celery -A celeryapp worker --loglever=info
# See doc Celery online

app = Celery('celeryapp')
app.config_from_object('celeryconfig')

# Request to openweather API.
# lanch a beat worker : celery -A celeryapp worker --loglevel=info -B


@app.task
def weather(city_id_list):
    base_url = "http://api.openweathermap.org/data/2.5/forecast/"
    city_url = "daily?id={}&APPID=64af4014d4d7321058115459dfc67525"
    url = base_url + city_url
    temperatures = map(lambda city:
                       requests.get(
                           url.format(city)).json()["list"][1]["temp"]["day"],
                       city_id_list)
    return temperatures
