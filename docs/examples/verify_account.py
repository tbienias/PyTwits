"""Provides a basic example of verifying a StockTwits account."""

import pytwits


def main():

    access_token = 'TOKEN'
    stocktwits = pytwits.StockTwits(access_token=access_token)

    user = stocktwits.account(path='verify')
    print("Verified {}".format(user.name))


if __name__ == '__main__':
    main()
