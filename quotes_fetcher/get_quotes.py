import requests

url = "https://query1.finance.yahoo.com/v8/finance/chart/AAPL?interval=2m"

r = requests.get(url)
print(r.json())
fsfsf

