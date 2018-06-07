"""Provides a basic example of showing deleted messages."""

import pytwits


def main():

    access_token = 'TOKEN'
    stocktwits = pytwits.StockTwits(access_token=access_token)

    cursor, messages = stocktwits.deletions(path='messages')
    print('\n\n'.join([message.body for message in messages]))


if __name__ == '__main__':
    main()
