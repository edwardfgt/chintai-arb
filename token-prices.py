import requests
from lxml import html


def eth_price():
    eth_url = "https://www.diadata.org/app/price/asset/Ethereum/0x9Ce84F6A69986a83d92C324df10bC8E64771030f/"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(eth_url, headers=headers)
    tree = html.fromstring(response.content)


    if response.status_code == 200:
        eth_price_div = tree.xpath("/html/body/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/div/div[2]")
        eth_price_text = eth_price_div[0].text_content().strip()
        print(eth_price_text)
        return eth_price_text
    else:
        print("Failed to retrieve the webpage: HTTP Status Code", response.status_code)


def sol_price():
    sol_url = "https://www.geckoterminal.com/solana/pools/D8JjVpFdXjFvHmsX7LyFy8iHXEqzhbQo576Rt8rZkyiq"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(sol_url, headers=headers)
    tree = html.fromstring(response.content)

    if response.status_code == 200:
        sol_price_div = tree.xpath('//*[@id="pool-price-display"]/span')
        sol_price_text = sol_price_div[0].text_content().strip()
        print(sol_price_text)
        return sol_price_text
    else:
        print("Failed to retrieve the webpage: HTTP Status Code", response.status_code)

eth_price()
sol_price()