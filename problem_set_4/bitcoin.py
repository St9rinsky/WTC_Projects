import requests
import sys

def main():
    if len(sys.argv) == 2:
        try:
            amount = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")
        else:
            converted = get_bitcoinprice() * amount
            print(f"${converted:,.4f}")
    else:
        sys.exit("Missing command-line argument")



def get_bitcoinprice():
    try:
        r = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=07ef87549d2feabaa146c94b0df4919b0053d196b0e1e0f681e688cd14824619")
    except requests.RequestException:
        sys.exit("website down")
    else:
        responce = r.json()
        usd_value = responce["data"]["priceUsd"]
        return float(usd_value)

main()