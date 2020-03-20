import credentials
import tweepy
import time
import pymongo
import json
from bson import BSON

#this class handles authenatication for twitter API
class Authenticator():
    def authenticate_twitter(self):
        auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_KEY_SECRET)
        auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

        return auth
    
 
class TwitterListener(tweepy.StreamListener):

    def on_data(self, data):
        try:
            #connect to MongoDB
            client = pymongo.MongoClient("mongodb://localhost:27017/")

            #use database
            db = client["AE"]

            #decode the json data from twitter
            datajson = json.loads(data)
            
            #print the data to console as it's collected
            print(datajson)
            
            #store the tweet data in a collection
            db['tweets'].insert(datajson)

        except BaseException as e:
           print(e)
        return True

    def on_error(self, status_code):
        if status_code == 420:
            print("error 420")
            return False
        print(status_code)




class Streamer():
    def __init__(self):
        self.authenticator = Authenticator()
    def stream_tweets(self, hash_tag_list, mining_time):
        auth = self.authenticator.authenticate_twitter()
        listener = TwitterListener(api=tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True,parser=tweepy.parsers.JSONParser()))
        stream = tweepy.Stream(auth,  listener)
        stream.filter(track=hash_tag_list, is_async=True)
        time.sleep(mining_time)
        stream.disconnect()



if __name__ == '__main__':

    #select the keyword by which you want to query Twitter data
    hash_tag_list = ['coronavirus']

    #select for how long in seconds to mine
    mining_time = 10
    streamer = Streamer()
    streamer.stream_tweets(hash_tag_list, mining_time)