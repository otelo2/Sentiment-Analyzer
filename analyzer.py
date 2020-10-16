import tweepy
from tweepy import OAuthHandler
from keys import *

auth = OAuthHandler(apiKey, apiKeySecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(3):
    print(status.text)