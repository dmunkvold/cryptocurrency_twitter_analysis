from textblob import TextBlob

class SentimentBot:

    def __init__(self, tweets):
        self.tweets = tweets
        self.analyzed_tweets = []

    def clear_tweets(self):
        self.tweets = []
        self.analyzed_tweets = []

    def add_tweet(self, tweet):
        self.tweets.append(tweet)

    def add_tweets(self, tweets):
        self.tweets.extend(tweets)

    def analyze_sentiments(self):
        for i in self.tweets:
            tweet = TextBlob(i)
            sentiment = tweet.sentiment
            self.analyzed_tweets.append([sentiment.polarity, sentiment.subjectivity])
