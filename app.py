from web3 import Web3, EthereumTesterProvider
from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

my_address = os.getenv('WALLET_ADDRESS')
infura_api = os.getenv('INFURA_API')
private_key = os.getenv('PRIVATE_KEY')

w3 = Web3(Web3.HTTPProvider(infura_api))

result = w3.isConnected()
print('Web3 is connected: ', result)

# print(w3.eth.get_block('latest'))
# print(w3.eth.get_balance(my_address))

nonce = w3.eth.get_transaction_count(my_address)

tx = {
    'nonce': nonce,
    'to': '0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266',
    'value': w3.toWei(1, 'ether'),
    'gasPrice': w3.eth.gas_price
}

gas = w3.eth.estimate_gas(tx)
tx['gas'] = gas
print(tx)

signed_tx = w3.eth.account.sign_transaction(tx, private_key)
tx_hash = w3.eth.sendRawTransaction(signed_tx.rawTransaction)

receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print(receipt)

print('sender balance: ', w3.eth.get_balance(my_address))
print('receiver balance: ', w3.eth.get_balance(
    '0x8Ff966Ab0DadaDC70C901dD5cDc2C708d3A229AA'))
