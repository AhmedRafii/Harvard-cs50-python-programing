import sys
import requests

if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
        print ("Command-line argument is not a number")
        sys.exit(1)

else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    responce = r.json()
    btc_price = responce['bpi']['USD']['rate_float']
    final_price = btc_price * value
    print(f"${final_price:,.4f}")
except requests.RequestException:
    print("Invalid Request")
    sys.exit(1)
