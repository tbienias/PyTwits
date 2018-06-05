"""Provides a basic example of liking and unliking a message
from StockTwits."""

import pytwits


def main():

    access_token = 'TOKEN'
    stocktwits = pytwits.StockTwits(access_token=access_token)

    stocktwits.messages(path='like', id=125715135)
    stocktwits.messages(path='unlike', id=125715135)


if __name__ == '__main__':
    main()
