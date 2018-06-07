"""Provides a basic example of retrieving a list of trending symbols
from StockTwits."""

import pytwits


def main():

    access_token = 'TOKEN'
    stocktwits = pytwits.StockTwits(access_token=access_token)

    symbols = stocktwits.trending(path='symbols')
    print('\n\n'.join([symbol.title for symbol in symbols]))


if __name__ == '__main__':
    main()
