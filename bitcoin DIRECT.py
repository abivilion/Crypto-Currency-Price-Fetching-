import json, time, datetime
import requests


# GET CRYPTO CURRENCY CURRENT VALUE
n = 0
# https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD


def get_crypt_price(fsym, tsyms):
    URL = "https://min-api.cryptocompare.com/data/price?fsym=" + fsym + "&tsyms=" + tsyms  # REPLACE WITH CORRECT URL
    response = requests.request("GET", URL)
    response = json.loads(response.text)
    current_price = response[tsyms]
    if tsyms == "USD":
        print(f"The current price of {fsym} is ${current_price}")
        print(f"Time of retrieval {datetime.datetime.now()}")
        print("\nRE - A C T I V A T I N G  S U B M I S S I O N \n\n".center(100))
    elif tsyms == "INR":
        print(f"The current price of {fsym} is ₹{current_price}")
        print(f"Time of retrieval {datetime.datetime.now()}")
        print("\nRE - A C T I V A T I N G  S U B M I S S I O N \n\n".center(100))
    elif tsyms == "EUR" or tsyms == "EURO":
        print(f"The current price of {fsym} is €{current_price}")
        print(f"Time of retrieval {datetime.datetime.now()}")
        print("\nRE - A C T I V A T I N G  S U B M I S S I O N \n\n".center(100))
    else:
        print("Irregular Container Inputs".center(5, "x"))
    return current_price


while n <= 2:
    print("Digital Currency Availability: ETH = Ethereum ,BTC = Bitcoin and XPR = RippleNet")
    print("Conversion Currency: USD,INR,EUR")
    cur = input("Which CRYPTO currency you want to get the price? ").lower()
    cnv = input("Conversion Currency:").lower()
    if cur == "eth" or cur == "Ethereum".lower():
        get_crypt_price("ETH", cnv.upper())
        n += 1
        time.sleep(5)
        continue
        # sys.exit()
    elif cur == "btc" or cur == "Bitcoin".lower():
        get_crypt_price("BTC", cnv.upper())
        n += 1
        time.sleep(5)
        continue
        # sys.exit()
    elif cur == "xpr" or cur == "RippleNet".lower():
        get_crypt_price("XPR", cnv.upper())
        n += 1
        time.sleep(5)
        continue
    else:
        print("\n")
        C = " Irregular Container Inputs "
        print(C.center(100, 'x'))
        print("RE - A C T I V A T I N G  S U B M I S S I O N \n\n".center(100))
    n += 1
