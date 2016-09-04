from celery import Celery
from celery.task import http

# 1. Install RABITMQ to get a message broker
# 2. Run it through invoke-rc.d rabbitmq-server start 
# 3. launch celery -A celeryapp worker --loglever=info
# See doc Celery online

app = Celery('celeryapp', broker='amqp://guest@localhost//')

@app.task
def weather(city_id):
    base_url = "http://api.openweathermap.org/data/2.5/forecast/"
    daily_url = "daily?id={}&APPID=64af4014d4d7321058115459dfc67525".format(city_id)
    url = base_url + daily_url
    #http.make_request(url, method="get",{"":""})
    
