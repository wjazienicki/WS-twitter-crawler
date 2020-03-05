import pymongo
import json
from bson import BSON


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['WebScience']
mycol = mydb['tweets']

with open('tweets_streaming.json') as f:
    file_data = json.load(f)

mycol.insert_many(file_data)





# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# mydict = { "name": "John", "address": "Highway 37" }

# x = mycol.insert_one(mydict)