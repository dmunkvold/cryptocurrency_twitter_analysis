from twitter_api.twitter_api import TwitterAPI
from crypto_compare_api.crypto_compare_api import CryptoCompareAPI

class DataSetBuilder:

    def __init__(self, crypto, hashtags):
        self.crypto = crypto
        self.hashtags = hashtags
        self.twitter_api = TwitterAPI()
        self.cryptocompare_api = CryptoCompareAPI()
        self.sample_set = [[],[]]

    def generate_data_set(self, start_date, num_samples, days_offset):
        self.fetch_tweets(start_date, num_samples)
        self.fetch_prices(days_offset)

    def fetch_tweets(self, start_date, num_samples):
        for hashtag in self.hashtags:
            tweets = self.twitter_api.find_tweets_by_hashtag(hashtag, start_date, num_samples)
            self.sample_set[0] += tweets

    def fetch_prices(self, offset_days):
        for tweet in self.sample_set[0]:
            price = self.cryptocompare_api.get_historical_price(self.crypto, tweet.created_at + timedelta(days=offset_days))
            self.sample_set[1].append (price)
