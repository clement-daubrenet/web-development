import confluent_kafka
import re
import time
import uuid
import sys

def producer():

    conf = {'bootstrap.servers': 'localhost:9092'}
    p = confluent_kafka.Producer(**conf)
    topic = 'test'
    msgcnt = 1
    msg_pattern = 'pattern sent'
    t_produce_start = time.time()
    msgs_produced = 0
    msgs_backpressure = 0
    print('# producing %d messages to topic %s' % (msgcnt, topic))
    for i in range(0, msgcnt):
        p.produce('test', value=msg_pattern)
        msgs_produced += 1
        p.poll(0)

    t_produce_spent = time.time() - t_produce_start
    print('waiting for %d/%d deliveries' % (len(p), msgs_produced))
    # Wait for deliveries
    p.flush()
    t_delivery_spent = time.time() - t_produce_start


def consumer():
    """ Verify Consumer performance """

    conf = {'bootstrap.servers': 'localhost9092',
            'group.id': uuid.uuid1()}

    c = confluent_kafka.Consumer(**conf)
    c.subscribe(["test"])
    max_msgcnt = 1
    msgcnt = 0
    print('Will now consume %d messages' % max_msgcnt)
    while True:
        # Consume until EOF or error
        msg = c.poll()
        msgcnt += 1
        if msgcnt == 1:
            t_first_msg = time.time()
        if msgcnt >= max_msgcnt:
            break
    t_spent = time.time() - t_first_msg
    print('consumed in %.10fs' % \
          t_spent)
    c.close()

producer()
consumer()