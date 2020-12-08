"""Provides a basic example of blocking a StockTwits user."""

import pytwits


def main():

    access_token = 'TOKEN'
    stocktwits = pytwits.StockTwits(access_token=access_token)

    user = stocktwits.blocks(path='create', id='391833')
    print("Blocked {}".format(user.name))

    user = stocktwits.blocks(path='destroy', id='391833')
    print("Unblocked {}".format(user.name))


if __name__ == '__main__':
    main()
