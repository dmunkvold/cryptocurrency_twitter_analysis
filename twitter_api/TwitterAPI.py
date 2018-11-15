import sys
sys.path.append('/Users/David/anaconda/envs/environment_for_py3/lib/python3.6/site-packages')

import tweepy
from TwitterAPI_keys import consumer_key, consumer_secret, access_token, access_token_secret

class TwitterAPI:

    consumer_key = consumer_key
    consumer_secret = consumer_secret
    access_token = access_token
    access_token_secret = access_token_secret

    def __init__(self):
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth,wait_on_rate_limit=True)

    def find_tweets_by_hashtag(self, hashtag, start_date, count):
        for tweet in tweepy.Cursor(self.api.search, q = hashtag,count = count,
                                   lang="en",
                                   since=start_date).items():
            print (tweet.created_at, tweet.text)
