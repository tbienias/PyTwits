"""Provides a basic example of muting/unmuting a StockTwits user."""

import pytwits


def main():

    access_token = 'TOKEN'
    stocktwits = pytwits.StockTwits(access_token=access_token)

    user = stocktwits.mutes(path='create', id='391833')
    print("Muted {}".format(user.name))

    user = stocktwits.mutes(path='destroy', id='391833')
    print("Unmuted {}".format(user.name))


if __name__ == '__main__':
    main()
