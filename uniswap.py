from uniswap import Uniswap
from dotenv import load_dotenv
import os

load_dotenv()

version = 2 
provider = os.getenv('ALCHEMY_URL')

usdc_ca = "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48"
chex_ca = "0x9Ce84F6A69986a83d92C324df10bC8E64771030f"