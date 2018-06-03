"""Provides a basic example of retrieving the last 30 messages of the user
'investinghaven' and prints the latest message with the user's name."""

import pytwits


def main():

    access_token = 'TOKEN'  # This would also work without passing token.
    stocktwits = pytwits.StockTwits(access_token=access_token)

    user, cursor, messages = stocktwits.streams(path='user',
                                                id='investinghaven')

    print('Messages for user: {}\n\n'.format(user.name))
    print('\n\n'.join([message.body for message in messages]))


if __name__ == '__main__':
    main()
