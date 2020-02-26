# quote_fetcher

This library will provide you with the following functionality:
- Fetch market data for a specified list of tickers and time interval. Available data points:
  - Open
  - High
  - Low
  - Close
  - Volume
- Time interval can be set in two ways: 
  - period like 1d, 5d, 1mo, 3mo, 1y, 2y, 5y, 10y, ytd, etc. 1mo is used by default.
  - period specified by start and end dates in format "YYYY-MM-DD".
  The second option has a higher priority if specified.
- Get the fetched data as a Pandas Dataframe. Two view modes are available:
  - Regular (index consists of dates and columns are represented as two levels - symbols and data points). Used by default.
  - Transposed (columns are represented as dates and index consists of two levels - symbol and data points).
- Calculate the following date points:
  - Average Close Price
  - Average Volume
  - Average Daily Dollar Trade Volume
  - Beta-coefficient

### Installation

```sh
pip install quotes_fetcher
```

### Demo 
Ipynb notebook can be found [HERE](notebooks/demo.ipynb)

### CLI
If you're loking for a ready CLI application, there is one. It also supports an option to export data to a file. Please find the app [HERE](CLI/quotes_fetcher.py)

### Todos

 - [ ] Fix bugs
 - [ ] Increase test coverage
 - [ ] Get rid of yfinance library, used as a base, to decrease the number of dependencies and increase transparency.

License
----

MIT


