"""Provides a basic example of retrieving all watchlists of a user from
StockTwits."""

import pytwits


def main():

    access_token = 'TOKEN'
    stocktwits = pytwits.StockTwits(access_token=access_token)

    watchlists = stocktwits.watchlists(path='watchlists')
    print('\n\n'.join([watchlist.name for watchlist in watchlists]))


if __name__ == '__main__':
    main()
