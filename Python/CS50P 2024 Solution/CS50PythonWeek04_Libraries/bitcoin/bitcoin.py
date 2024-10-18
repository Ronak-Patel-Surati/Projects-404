import requests
from sys import argv, exit

# Using webhook
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    exit("Failed to retrieve current price")

# Using JSON file for price
try:
    json_data = response.json()
    last_price_str = json_data["bpi"]["USD"]["rate"].replace(",", "")
    last_price = float(last_price_str)
except (KeyError, ValueError):
    exit("Failed to parse JSON or retrieve last price")

# Handling command-line arguments
if len(argv) != 2:
    exit("Missing or incorrect command-line argument")
else:
    try:
        ltp = float(argv[1])
    except ValueError:
        exit("Invalid command-line argument")

# Calculate total price
total = ltp * last_price
formatted_total = "${:,.4f}".format(total)
print("Total price:", formatted_total)
# could not identify myself therefore used library @discord
