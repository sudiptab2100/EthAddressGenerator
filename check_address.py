from web3 import HTTPProvider, Web3
import web3
from address_generator import genPrivateKey, privateKeyToEthAddress

w3 = Web3(HTTPProvider('https://bsc-dataseed.binance.org/'))
MAX_LIMIT = 200000
count = 0

while(count < MAX_LIMIT):
    print(count)
    count += 1

    priv = genPrivateKey()
    addr = Web3.toChecksumAddress('0x' + privateKeyToEthAddress(priv).hex())
    balance = w3.eth.get_balance(addr)
    # print(addr)
    # print(balance)
    # print(type(balance))

    if(balance > 0):
        print()
        print(priv.hex())
        print(addr)
        print(balance)
        break

