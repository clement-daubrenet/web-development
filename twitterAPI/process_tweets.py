import json
import re

from kafka import KafkaConsumer, KafkaProducer
from streamparse import Spout, Bolt


class TweetParse(Spout):

    def __init__(self, storm_conf, context):
        self.kafka_conf = json.loads(open('kafka_conf.json').read())
        self.kafka_consumer = KafkaConsumer(self.kafka_conf["kafka_topic"],
                                            bootstrap_servers=self.kafka_conf["kafka_server"])
        self.kafka_producer = KafkaProducer(value_serializer=lambda v: json.dumps(v),
                                            bootstrap_servers=self.kafka_conf["kafka_server"])

    def next_tuple(self):
        message = self.kafka_consumer.next()
        Spout.emit(message)
        return message

    def _send_ouput(self, message):
        self.kafka_producer.send(self._conf["kafka"]["tweeter-topic-parsed"], message)


class LocationBolt(Bolt):

    def process(self, tup):
        message = tup.values["location"]
        return message

class TimeBolt(Bolt): 

    def process(self,tup):
        message = tup.values["time"]
        return message
 
        

if __name__ == "__main__":
   tweet_parse = TweetParse("storm_conf", "context")
   tweet_parse.next_tuple()
