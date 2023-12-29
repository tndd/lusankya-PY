import json

# Load the JSON data from the file
with open('mock/asset.json') as f:
    data = json.load(f)

# Filter the symbols based on the 'active' property
active_symbols = [asset['symbol'] for asset in data if asset['status'] == 'active']

print(active_symbols)
