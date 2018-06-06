"""Provides a basic example of showing a watchlist on StockTwits."""

import pytwits


def main():

    access_token = 'TOKEN'
    stocktwits = pytwits.StockTwits(access_token=access_token)

    watchlist = stocktwits.watchlists(path='show',
                                      id='1391129')
    print('\n\n'.join([symbol['symbol'] for symbol in watchlist.symbols]))


if __name__ == '__main__':
    main()
