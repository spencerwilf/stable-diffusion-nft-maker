from web3 import Web3
from web3.contract import ConciseContract
from solc import compile_source
import json

web3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))

# Load the contract ABI from a JSON file
with open('contract_abi.json', 'r') as f:
    contract_abi = json.load(f)

contract_address = '0xf9211AF30622499be9a5b31115461D285e8cD09F'  # Replace with your actual contract address
contract = web3.eth.contract(address=contract_address, abi=contract_abi)
user_address = '0x998c9f7644229890C7A1a81F9Ba7a50fe984A2fc'

def mint_artwork(artwork):
    try:
        # Mint the user's creation
        tx_hash = contract.functions.mint(user_address, artwork).transact({'from': user_address})

        # Wait for the transaction to be mined
        web3.eth.waitForTransactionReceipt(tx_hash)

        print("Artwork minted successfully!")
    except Exception as e:
        print(f"Error minting artwork: {e}")


