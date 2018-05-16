import tweepy

class TwitterAPI:

    consumer_key = 'SU1Dfyifja4iiIc81w3ZEQlCB'
    consumer_secret = '5PQvvGbA3iIpzZqwwdRKVJMAjPtCAVGh477QMHUxg4nXC8auIz'
    access_token = '996091583853481985-h7WPFVoDZiPTqEf5xIq3x5vkfOxOzPG'
    access_token_secret = '8Ziudx0rwmioHXF9mSXJTa7tVKCucjMPM5Mp43uMefR5w'

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
