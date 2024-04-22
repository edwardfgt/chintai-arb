import requests
from lxml import html

eth_url = "https://www.diadata.org/app/price/asset/Ethereum/0x9Ce84F6A69986a83d92C324df10bC8E64771030f/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(eth_url, headers=headers)
tree = html.fromstring(response.content)


if response.status_code == 200:
    price_div = tree.xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div[2]")
    price_text = price_div[0].text_content().strip()
    print(price_text)
else:
    print("Failed to retrieve the webpage: HTTP Status Code", response.status_code)
