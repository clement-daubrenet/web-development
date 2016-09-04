from celery import Celery

# 1. Install RABITMQ to get a message broker
# 2. Run it through invoke-rc.d rabbitmq-server start 
# 3. launch celery -A celeryapp worker --loglever=info
# See doc Celery online

app = Celery('celeryapp', broker='amqp://guest@localhost//')
@app.task
def add(x, y):
    return x + y
