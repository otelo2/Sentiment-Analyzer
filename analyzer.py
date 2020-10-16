#From https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
#http://docs.tweepy.org/en/latest/streaming_how_to.html
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from keys import *

auth = OAuthHandler(apiKey, apiKeySecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error onData: %s" % str(e))
        return True

    def on_status(self, status):
        return super().on_status(status)

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            #Returning false disconects from stream
            return False
        return True


myStreamListener = MyStreamListener()
twitterStream = tweepy.Stream(auth, myStreamListener)
twitterStream.filter(track=['AMLO'], languages=['es', 'en'])
