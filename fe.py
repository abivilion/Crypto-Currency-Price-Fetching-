import datetime
import json
import time
import requests
import sys
import confg_tele  # this file should contain API key, and DEVICE ID
from boltiot import Bolt

n = 0
# OWNER: Ayush Bhardwaj(abivilion)



def start_buzzer():
    """Return the sensor value. Return -999 if request fails"""
    geqo = Bolt(confg_tele.bolt_api_key, confg_tele.device_id)
    render = ""

    try:
        status = geqo.digitalWrite("0", "HIGH")
        print("Success Buzzer Turned On")
        # time.sleep(1)
        print("Turing Off..", geqo.digitalWrite("0", "LOW"))
        render = "Success"
    except:
        dw = """The problems occur in buzzer activation underline are the few possibilities that may happens: 
        1. Buzzer driver crashed or failed.
        2. Chip-set is blown.
        3. Chip is not connected or offline.
        4. No Internet Connectivity
        5. Connection disturbed or are not correct properly."""
        print(dw)
        render = "Fatal Error Occur"
    return render


def get_crypt_price(fsym, tsyms):
    URL = "https://min-api.cryptocompare.com/data/price?fsym=" + fsym + "&tsyms=" + tsyms  # REPLACE WITH CORRECT URL
    response = requests.request("GET", URL)
    response = json.loads(response.text)
    current_price = response[tsyms]
    if tsyms == "USD":
        print(f"The current price of {fsym} is ${current_price}")
        print(f"Time of retrieval {datetime.datetime.now()} - ",start_buzzer())

        print("\nRE - A C T I V A T I N G  S U B M I S S I O N \n\n".center(100))
    elif tsyms == "INR":
        print(f"The current price of {fsym} is ₹{current_price}")
        print(f"Time of retrieval {datetime.datetime.now()} - ",start_buzzer())

        print("\nRE - A C T I V A T I N G  S U B M I S S I O N \n\n".center(100))
    elif tsyms == "EUR":
        print(f"The current price of {fsym} is €{current_price}")
        print(f"Time of retrieval {datetime.datetime.now()} - ",start_buzzer())
        print("\nRE - A C T I V A T I N G  S U B M I S S I O N \n\n".center(100))
    else:
        C = " Irregular Container Inputs "
        print(C.center(100, 'x'))
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
