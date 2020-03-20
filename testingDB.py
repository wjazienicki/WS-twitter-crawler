import pymongo
import json
from bson import BSON


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient['WebScience']
mycol = mydb['tweets']

myquery = { id : "1235688967976214529"}

mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)





# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# mydb = myclient["mydatabase"]
# mycol = mydb["customers"]

# mydict = { "name": "John", "address": "Highway 37" }

# x = mycol.insert_one(mydict)