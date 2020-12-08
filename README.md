<p align="center">
  <img src="https://raw.githubusercontent.com/tbienias/PyTwits/master/logo.png">
</p>

PyTwits is a REST-API Wrapper for the Social Trading Network StockTwits.
Written in Python it enables the user to easily interact with StockTwits REST-API.

## Installation ##

```bash
pip install PyTwits
```

## Example Usage ##

Following example finds AAPL symbol and prints symbol label and title.

```python
import pytwits


def main():

    stocktwits = pytwits.StockTwits()
    symbols = stocktwits.search(path='search/symbols', q='AAPL')
    aapl = symbols[0]
    print("Symbol: {} - Title: {}".format(aapl.symbol, aapl.title))


if __name__ == '__main__':
    main()
```

### Output ###

`Symbol: AAPL - Title: Apple Inc.`

## Documentation ##

Documentation consists of examples for every API entry point.
See docs/examples folder.

## License ##

MIT
