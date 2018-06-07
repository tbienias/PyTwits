"""Provides a basic example of posting a message to StockTwits."""

import pytwits


def main():

    access_token = 'TOKEN'
    stocktwits = pytwits.StockTwits(access_token=access_token)

    message = "Another test message with: $AAPL $MSFT"
    sentiment = "bullish"

    message = stocktwits.messages(path='create',
                                  body=message,
                                  sentiment=sentiment)

    print('Message text: {}\n\n'.format(message.body))


if __name__ == '__main__':
    main()
