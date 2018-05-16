import tweepy

class TwitterAPI:

    consumer_key = '?'
    consumer_secret = '?'
    access_token = '?'
    access_token_secret = '?'

    def __init__(self):
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.api = tweepy.API(self.auth,wait_on_rate_limit=True)

    def find_tweets_by_hashtag(self, hashtag):
        for tweet in tweepy.Cursor(self.api.search, q = hashtag,count = 100,
                                   lang="en",
                                   since="2018-04-03").items():
            print (tweet.created_at, tweet.text)
x = TwitterAPI()
x.find_tweets_by_hashtag('#bitcoin')
