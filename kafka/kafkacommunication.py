import time

from threading import Thread
from kafka import KafkaProducer, KafkaConsumer

# Two threads : a producer (sending words) and a consumer (catching them)
# N.B : requires to start a kafka zookeeper, a kafka server and create a
# "test" topic :
# $bin/zookeeper-server-start.sh config/zookeeper.properties
# $bin/kafka-server-start.sh config/server.properties
# $bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test


KAFKA_TOPIC = "test"
KAFKA_SERVER = "localhost:9092"
NB_MESSAGES = 5


def kafka_producer_call():
    kafka_producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
    for i in range(NB_MESSAGES):
        word = "yay"
        kafka_producer.send(KAFKA_TOPIC, word)
    kafka_producer.flush()
    return 1


def kafka_consumer_call():
    kafka_consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=KAFKA_SERVER)
    count = 0
    for message in kafka_consumer:
        count += 1
        print message
        if count == NB_MESSAGES:
            return 1

producer_thread = Thread(target=kafka_producer_call)
consumer_thread = Thread(target=kafka_consumer_call)

consumer_thread.start()
producer_thread.start()

consumer_thread.join()
producer_thread.join()

# todo :
#   - optimize synchronization time, something is wrong (too slow)
#   - connect to a storm topology to treat data
