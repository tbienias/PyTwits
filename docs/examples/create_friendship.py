"""Provides a basic example of creating a friendship on StockTwits."""

import pytwits


def main():

    access_token = 'TOKEN'
    stocktwits = pytwits.StockTwits(access_token=access_token)

    user = stocktwits.friendships(path='create', id='1511554')
    print(user.name)


if __name__ == '__main__':
    main()
