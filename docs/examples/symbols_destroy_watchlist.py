"""Provides a basic example of deleting symbols from a watchlist on StockTwits."""

import pytwits


def main():

    access_token = 'TOKEN'
    stocktwits = pytwits.StockTwits(access_token=access_token)

    symbols = stocktwits.watchlists(path='symbols/destroy',
                                    id='1391129',
                                    symbols='ORCL')

    print('\n\n'.join([symbol.symbol for symbol in symbols]))

    symbols = stocktwits.watchlists(path='symbols/destroy',
                                    id='1391129',
                                    symbols='FB, UBER')

    print('\n\n'.join([symbol.symbol for symbol in symbols]))


if __name__ == '__main__':
    main()
