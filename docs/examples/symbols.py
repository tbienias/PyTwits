"""Provides a basic example of retrieving a list of symbols you are
following from StockTwits."""

import pytwits


def main():

    access_token = 'TOKEN'
    stocktwits = pytwits.StockTwits(access_token=access_token)

    cursor, symbols = stocktwits.graph(path='symbols')
    print('\n\n'.join([symbol.title for symbol in symbols]))


if __name__ == '__main__':
    main()
