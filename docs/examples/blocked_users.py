"""Provides a basic example of retrieving a list of blocked users from
StockTwits."""

import pytwits


def main():

    access_token = 'TOKEN'
    stocktwits = pytwits.StockTwits(access_token=access_token)

    cursor, users = stocktwits.graph(path='blocking')
    print('\n\n'.join([user.name for user in users]))


if __name__ == '__main__':
    main()
