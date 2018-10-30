# this import code is only necessary because I am struggling to set the
# path for python to look for modules in my 3.6 environment. this code
# can be commented out in the case that cryptocompare imports correctly

#import sys
#sys.path.append('/Users/David/anaconda/envs/environment_for_py3/lib/python3.6/site-packages')

# the following is necessary code

import cryptocompare

class CryptoCompareAPI:

    def get_coin_list(self):
        list = cryptocompare.get_coin_list(format=False)
        return list

    def get_price(self, crypto):
        price = cryptocompare.get_price(crypto, curr='USD')
        return price

    def get_historical_price(self, crypto, datetime):
        price = cryptocompare.get_historical_price(crypto, 'USD', datetime)
        return price

    def get_average(self, crypto, exchange):
        avg = cryptocompare.get_avg(crypto, curr='EUR', exchange=exchange)
        return avg

    def get_exchanges(self):
        exchanges = cryptocompare.get_exchanges()
        return exchanges
