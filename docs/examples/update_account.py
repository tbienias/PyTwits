"""Provides a basic example of updating a StockTwits account."""

import pytwits


def main():

    access_token = 'TOKEN'
    stocktwits = pytwits.StockTwits(access_token=access_token)

    user = stocktwits.account(path='update', name='MarketBeaterKing')
    print("Verified {}".format(user.name))


if __name__ == '__main__':
    main()
