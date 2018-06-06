"""Provides a basic example of destroying a new watchlist on StockTwits."""

import pytwits


def main():

    access_token = 'TOKEN'
    stocktwits = pytwits.StockTwits(access_token=access_token)

    watchlist = stocktwits.watchlists(path='destroy',
                                      id='1400357')
    print(watchlist.name)


if __name__ == '__main__':
    main()
