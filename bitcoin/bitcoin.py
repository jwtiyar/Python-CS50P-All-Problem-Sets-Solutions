import sys
import requests
import json
jmare = sys.argv
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
try:
    jmare = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")
try:

    price = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Not number")
rate = price.json()
rate = rate["bpi"]
# for rates in rate.values():
amount = rate["USD"]["rate"]
amount = amount.replace(",", "")
amount = float(amount)
encam = amount * jmare

print(f"${encam:,.4f}")