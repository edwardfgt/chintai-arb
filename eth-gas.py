from web3 import Web3
from dotenv import load_dotenv
import os

load_dotenv()

def eth_gas():
    alchemy_url = os.getenv('ALCHEMY_URL')
    if not alchemy_url:
        raise ValueError("Alchemy URL not set in environment variables")
    w3 = Web3(Web3.HTTPProvider(alchemy_url))

    print(w3.is_connected())

eth_gas()