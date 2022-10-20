from web3 import Web3

w3 = Web3(Web3.HTTPProvider(
    'https://goerli.infura.io/v3/30e093dfb77d47589bda8b56ae38e7c1'))
result = w3.isConnected()
print('Web3 is connected: ', result)
