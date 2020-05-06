import urllib.request
import json


ticker = 'WIPRO.BO'

url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols="+ ticker + "&range=1d&interval=5m&indicators=close&includeTimestamps=false&includePrePost=false&corsDomain=finance.yahoo.com&.tsrc=finance"


new_data = urllib.request.urlopen(url)

string = new_data.read().decode('utf-8')
data_parsed = json.loads(string)
data_parsed = data_parsed["quoteResponse"]["result"][0]
print(json.dumps(data_parsed, indent=4))
