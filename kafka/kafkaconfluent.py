import time

from multiprocessing import Process
from confluent_kafka import Producer, Consumer


# Two processs : a producer (sending words) and a consumer (catching them)
# N.B : requires to start a kafka zookeeper, a kafka server and create a
# "test" topic :
# $bin/zookeeper-server-start.sh config/zookeeper.properties
# $bin/kafka-server-start.sh config/server.properties
# $bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test

KAFKA_SERVER = 'localhost:9092'
KAFKA_TOPIC = 'test_confluent'


def produce():

    p = Producer({'bootstrap.servers': KAFKA_SERVER})
    i = 0
    while True:
        p.produce(KAFKA_TOPIC, "message" + str(i))
        i += 1

def consume():

    c = Consumer({'bootstrap.servers': KAFKA_SERVER, 'group.id': 'mygroup',
              'default.topic.config': {'auto.offset.reset': 'smallest'}})
    c.subscribe([KAFKA_TOPIC])
    while True:
        msg = c.poll()
        if not msg.error():
            print('Received message: %s' % msg.value().decode('utf-8'))
    c.close()

producer_process = Process(target=produce)
consumer_process = Process(target=consume)

consumer_process.start()
producer_process.start()

consumer_process.join()
producer_process.join()
