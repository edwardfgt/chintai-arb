from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

def eth_gas():
    alchemy_url = os.getenv('ALCHEMY_URL')
    if not alchemy_url:
        raise ValueError("Alchemy URL not set in environment variables")
    w3 = Web3(Web3.HTTPProvider(alchemy_url))

    if w3.is_connected():
        gas_price = w3.eth.gas_price
        print(f"Current gas price: {gas_price} wei")
        gas_price_gwei = w3.from_wei(gas_price, 'gwei')
        print(f"Current gas price: {gas_price_gwei} gwei")
    else:
        print("Failed to connect to Ethereum network")

eth_gas()