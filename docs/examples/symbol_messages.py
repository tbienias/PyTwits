"""Provides a basic example of retrieving the last 5 messages containing the
'AAPL' symbol and prints them."""

import pytwits


def main():

    access_token = 'TOKEN'  # This would also work without passing token.
    stocktwits = pytwits.StockTwits(access_token=access_token)

    symbol, cursor, messages = stocktwits.streams(path='symbol',
                                                  id='AAPL',
                                                  limit=5)

    print('Messages for symbol: {} - {}\n\n'.format(symbol.symbol,
                                                    symbol.title))
    print('\n\n'.join([message.body for message in messages]))


if __name__ == '__main__':
    main()
