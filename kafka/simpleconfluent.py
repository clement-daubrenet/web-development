import confluent_kafka
import re
import time
import uuid
import sys

def producer(broker_name, topic_name, number_of_messages):
    """
    This fucntion instantiates a producer
    :topic_name: name of the topic
    e.g : test_topic
    :broker_name: name of the broker
    e.g: localhost:9092
    """

    conf = {'bootstrap.servers': broker_name}
    p = confluent_kafka.Producer(**conf)
    topic = topic_name
    messages_number_to_send = number_of_messages
    msgs_produced = 0
    message = 'pattern sent'
    print('# producing %d messages to topic %s' % (messages_number_to_send, topic))
    for _ in range(0, messages_number_to_send):
        p.produce(topic_name, value=message.encode('utf8'))
        msgs_produced += 1
        p.poll(0)
    print('waiting for %d/%d deliveries' % (len(p), msgs_produced))
    # Wait for deliveries
    p.flush()

def consumer(broker_name, topic_name, number_of_messages):
    """
    This function consumes based on a
    broker name and a topic name.
    """
    conf = {'bootstrap.servers': broker_name,
            'group.id': uuid.uuid1(),
            'session.timeout.ms': 6000,
            'default.topic.config': {
                'auto.offset.reset': 'earliest'
            }}
    c = confluent_kafka.Consumer(**conf)
    c.subscribe([topic_name])
    max_msgcnt = number_of_messages
    msgcnt = 0
    print('Will now consume %d messages' % max_msgcnt)
    while True:
        # Consume until EOF or error
        msg = c.poll()
        if msgcnt == 0:
            t_start = time.time()
        msgcnt += 1
        if msgcnt >= max_msgcnt:
            break
    t_spent = time.time() - t_start
    print('consumed in %.10fs' % \
          t_spent)
    c.close()

broker_name = "prod-cruncher-broker-1.apps.artefact.is:6667"
topic_name = "test_clement_kafka"
number_of_messages = 500
producer(broker_name, topic_name, number_of_messages)
consumer(broker_name, topic_name, number_of_messages)