import tweepy
import json

from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener
from kafka import KafkaConsumer, KafkaProducer

# TODO :
#        1. Consume all the messages from Kakfa based on a spout (Storm)
#        2. unittest everything


class TwitterClient(StreamListener):
    """
    A client to get "cold" information from Twitter (no streaming)
    """
    def __init__(self):
        config = json.loads(open('connexion.json').read())
        consumer_key = config["consumer_key"]
        consumer_secret = config["consumer_secret"]
        access_token = config["access_token"]
        access_secret = config["access_secret"]
        self.auth = OAuthHandler(consumer_key, consumer_secret)
        self.auth.set_access_token(access_token, access_secret)
        self.twitter_api = tweepy.API(self.auth)

    def get_first_10_timeline_items(self):
        for status in tweepy.Cursor(self.twitter_api.home_timeline).items(10):
            print(status.text)

    def get_all_my_tweets(self):
        for tweet in tweepy.Cursor(self.twitter_api.user_timeline).items():
            print tweet._json


class TwitterListener(StreamListener):
    """
    A listener to get a data stream from Twitter
    """
    def __init__(self):
        self.kafka_conf = json.loads(open('kafka_conf.json').read())
        self.kafka_topic = self.kafka_conf["kafka_topic"]
        self.kafka_server = self.kafka_conf["kafka_server"]
        self.kafka_producer = KafkaProducer(bootstrap_servers=self.kafka_server)

    def on_data(self, data):
        print data
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                self.kafka_producer.send(self.kafka_topic, str(data))
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

if __name__ == "__main__":
    twitter_client = TwitterClient()
    twitter_stream = Stream(twitter_client.auth, TwitterListener())
    twitter_stream.filter(track=['Python'])
