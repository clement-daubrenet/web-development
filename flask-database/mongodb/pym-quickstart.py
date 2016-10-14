from pymongo import MongoClient
from datetime import datetime 


client = MongoClient()
result = client.post.insert_one({'a':1})({'x': 1})
