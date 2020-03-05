import credentials

import tweepy


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
            return True
        except BaseException as e:
            print('Error on data: %s' %str(e))
        return True

    def on_error(self, status_code):
        print(status_code)


class Streamer():
    def __init__(self):
        self.authenticator = Authenticator()
    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        listener = TwitterListener()
        auth = self.authenticator.authenticate_twitter()
        stream = tweepy.Stream(auth,  listener)
        stream.filter(track=hash_tag_list)



if __name__ == '__main__':
    hash_tag_list = ["nba"]
    fetched_tweets_filename = "tweets_streaming.json"

    streamer = Streamer()
    streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)