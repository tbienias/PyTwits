"""Provides a basic example of creating a new watchlist on StockTwits."""

import pytwits


def main():

    access_token = 'TOKEN'
    stocktwits = pytwits.StockTwits(access_token=access_token)

    watchlist = stocktwits.watchlists(path='create',
                                      name='Super Secret Watchlist')
    print(watchlist.name)


if __name__ == '__main__':
    main()
