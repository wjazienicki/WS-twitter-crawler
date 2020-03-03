import credentials

import tweepy

 
class StdOutListener(tweepy.StreamListener):
    


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
        pass
    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        listener = StdOutListener()
        auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY,credentials.CONSUMER_KEY_SECRET)
        auth.set_access_token(credentials.ACCESS_TOKEN, credentials.ACCESS_TOKEN_SECRET)

        stream = tweepy.Stream(auth, listener)
        stream.filter(track=hash_tag_list)



if __name__ == '__main__':
    hash_tag_list = [""]
    fetched_tweets_filename = "tweets.json"

    streamer = Streamer()
    streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)