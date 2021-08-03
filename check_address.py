from coincurve import keys
from web3 import HTTPProvider, Web3
import web3
from address_generator import genPrivateKey, privateKeyToEthAddress

w3 = Web3(HTTPProvider('https://bsc-dataseed.binance.org/'))
MAX_LIMIT = 200000
count = 0
duplicate = 0
addr_used = {}
while(count < MAX_LIMIT):

    priv = genPrivateKey()
    addr_str = '0x' + privateKeyToEthAddress(priv).hex()
    addr = Web3.toChecksumAddress(addr_str)
    if addr_str in addr_used.keys():
        duplicate += 1
        continue
    addr_used[addr_str] = True
    balance = w3.eth.get_balance(addr)

    if(balance > 0):
        print()
        print(priv.hex())
        print(addr)
        print(balance)
        break

    print("Count:", count, "Duplicate:", duplicate)
    count += 1

