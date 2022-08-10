import requests
import sys
import json

def main():

    bitcoin_dict = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()

    if len(sys.argv) == 2:
        try:
            amount = float(sys.argv[1])
        except:
            sys.exit('Command-line argument is not a number')

    else:
        sys.exit('Invalid command-line argument')

    unit_value = bitcoin_dict["bpi"]['USD']['rate_float']
    total_value = unit_value * amount
    print(f'${total_value:,.4f}')

main()