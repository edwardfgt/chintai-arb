import requests
from lxml import html

def eth_price():
    eth_url = "https://www.geckoterminal.com/eth/pools/0xd3e9895230e8fb1460852f6cda3c4b926fbc29d8"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(eth_url, headers=headers)
    tree = html.fromstring(response.content)


    if response.status_code == 200:
        eth_price_div = tree.xpath('//*[@id="pool-price-display"]/span')
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

chex_eth = float(eth_price()[1:])
chex_sol = float(sol_price()[1:])


percentage_diff_sol_to_eth = ((chex_eth - chex_sol) / chex_sol) * 100
percentage_diff_eth_to_sol = ((chex_sol - chex_eth) / chex_eth) * 100

print(f"Percentage difference (Solana to Ethereum): {percentage_diff_sol_to_eth:.2f}%")
print(f"Percentage difference (Ethereum to Solana): {percentage_diff_eth_to_sol:.2f}%")
