"""Provides a basic example of searching for a user ('deviltraders')
and printing some information."""

import pytwits


def main():

    access_token = 'Token'  # This would also work without passing token.
    stocktwits = pytwits.StockTwits(access_token=access_token)

    users = stocktwits.search(path='search/users',
                              q='deviltraders')

    user = users[0]
    print("Username: {} - Name: {}".format(user.username, user.name))


if __name__ == '__main__':
    main()
