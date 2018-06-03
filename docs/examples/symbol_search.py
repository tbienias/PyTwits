"""Provides a basic example of searching for a symbol ('AAPL')
and printing some information."""

import pytwits


def main():

    access_token = 'TOKEN'  # This would also work without passing token.
    stocktwits = pytwits.StockTwits(access_token=access_token)

    symbols = stocktwits.search(path='search/symbols',
                                q='AAPL')

    aapl = symbols[0]
    print("Symbol: {} - Title: {}".format(aapl.symbol, aapl.title))


if __name__ == '__main__':
    main()
