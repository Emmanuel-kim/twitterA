# import some tweepy packages
import sys
from typing import List

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
# get the authentication credentials from the twitter_credential file
import Credentials

# accessing auth keys
auth = tweepy.OAuthHandler(Credentials.API_KEY, Credentials.API_SECRET_KEY)
auth.set_access_token(Credentials.ACCESS_TOKEN, Credentials.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)


class StreamListener(tweepy.StreamListener):
   def on_status(self, status):
      print(status.text)
      def on_error(self, status_code):
           if status_code == 420:
              return False


streamListener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=StreamListener(), tweet_mode='extended')
tags: List[str] = ["ifikieruto"]
stream.filter(track=tags)

