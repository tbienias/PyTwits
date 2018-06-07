import pytwits


def main():

    access_token = 'TOKEN'
    stocktwits = pytwits.StockTwits(access_token=access_token)

    user, cursor, messages = stocktwits.streams(path='user', id='deviltraders')

    symbol, cursor, messages = stocktwits.streams(path='symbol', id='MSFT')

    cursor, messages = stocktwits.streams(path='friends')

    cursor, messages = stocktwits.streams(path='mentions')

    cursor, messages = stocktwits.streams(path='direct')

    cursor, messages = stocktwits.streams(path='direct_sent')

    cursor, messages = stocktwits.streams(path='direct_received')

    watchlist, cursor, messages = stocktwits.streams(path='watchlist',
                                                     id='WATCHLISTID')

    cursor, messages = stocktwits.streams(path='all')

    cursor, messages = stocktwits.streams(path='charts')

    cursor, messages = stocktwits.streams(path='equities')

    cursor, messages = stocktwits.streams(path='forex')

    cursor, messages = stocktwits.streams(path='futures')

    cursor, messages = stocktwits.streams(path='private_companies')

    cursor, messages = stocktwits.streams(path='suggested')

    cursor, symbols, messages = stocktwits.streams(path='symbols',
                                                   symbols=['AAPL', 'MSFT'])

    cursor, messages = stocktwits.streams(path='trending')

    cursor, messages = stocktwits.streams(path='sectors',
                                          sector_path='healthcare')

    cursor, parent, messages = stocktwits.streams(path='conversation')

    print("hello")


if __name__ == '__main__':
    main()
