from twitter_api import TwitterAPI
from crypto_compare_api import CryptoCompareAPI

class DataSetBuilder:

    def __init__(self, crypto, hashtags):
        self.crypto = crypto
        self.hashtags = hashtags
        self.twitter_api = TwitterAPI()
        self.cryptocompare_api =

    def generate_data_set(self, start_date_time, end_date_time)
