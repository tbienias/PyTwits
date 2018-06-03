"""Provides a basic example of retrieving the latest message containing an image
and displays it."""

from io import BytesIO
from PIL import Image
import pytwits
import requests


def main():

    access_token = 'TOKEN'  # This would also work without passing token.
    stocktwits = pytwits.StockTwits(access_token=access_token)

    cursor, messages = stocktwits.streams(path='charts', limit=1)
    response = requests.get(messages[0].entities['chart']['original'])
    img = Image.open(BytesIO(response.content))
    img.show()


if __name__ == '__main__':
    main()
