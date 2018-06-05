"""Provides a basic example of retrieving a message from StockTwits."""

import pytwits


def main():

    access_token = 'TOKEN'  # This would also work without passing token.
    stocktwits = pytwits.StockTwits(access_token=access_token)

    message = stocktwits.messages(path='show', id=125712744)
    print('Message text: {}\n\n'.format(message.body))


if __name__ == '__main__':
    main()
