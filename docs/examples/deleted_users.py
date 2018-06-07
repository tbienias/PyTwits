"""Provides a basic example of showing deleted users."""

import pytwits


def main():

    access_token = 'TOKEN'
    stocktwits = pytwits.StockTwits(access_token=access_token)

    cursor, users = stocktwits.deletions(path='users')
    print('\n\n'.join([user.name for user in users]))


if __name__ == '__main__':
    main()
