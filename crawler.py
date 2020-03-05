import credentials
import tweepy
import time


class Authenticator():
    def authenticate_twitter(self):
        auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_KEY_SECRET)
        auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

        return auth
    
 
class TwitterListener(tweepy.StreamListener):
    def on_data(self, data):
        try:
            print(data)
            with open(fetched_tweets_filename, 'a') as tf:
                tf.write(data)
                tf.write(",")
                #store(self,data)
            return True
        except BaseException as e:
            print('Error on data: %s' %str(e))
        return True

    def on_error(self, status_code):
        if status_code == 420:
            print("error 420")
            return False
        print(status_code)

    def store(self,data):
        t=json.loads(data)
        return t



class Streamer():
    def __init__(self):
        self.authenticator = Authenticator()
    def stream_tweets(self, fetched_tweets_filename, hash_tag_list, mining_time):
        auth = self.authenticator.authenticate_twitter()
        listener = TwitterListener(api=tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True,parser=tweepy.parsers.JSONParser()))
        stream = tweepy.Stream(auth,  listener)
        stream.filter(track=hash_tag_list, is_async=True)
        time.sleep(mining_time)
        stream.disconnect()



if __name__ == '__main__':
    # hash_tag_list = ["nba",'raptors','lakers','warriors','bucks','stephen curry','lebron james']
    hash_tag_list = ['coronavirus']
    fetched_tweets_filename = "tweets_streaming.json"
    mining_time = 10

    streamer = Streamer()
    streamer.stream_tweets(fetched_tweets_filename, hash_tag_list, mining_time)