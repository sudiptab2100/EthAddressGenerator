from secrets import token_bytes
from coincurve import PublicKey
from sha3 import keccak_256

def genPrivateKey():
    return keccak_256(token_bytes(32)).digest()

def privateToPublicKey(priv_key):
    return PublicKey.from_valid_secret(priv_key).format(compressed=False)[1:]

def privateKeyToEthAddress(priv_key):
    pub_key = privateToPublicKey(priv_key)
    return keccak_256(pub_key).digest()[-20:]

# private_key = genPrivateKey()
# addr = privateKeyToEthAddress(private_key)
# print('private_key:', private_key.hex())
# print('eth addr: 0x' + addr.hex())