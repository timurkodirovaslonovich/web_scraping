import requests
import json
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

data = []

def parser(category):
    load_dotenv()
    URL = 'https://openshop.uz/'
    HOST = os.getenv("HOST")
    HEADERS = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }

    html = requests.get(URL + category, headers=HEADERS).text
    soup = BeautifulSoup(html, 'html.parser')
    blocks = soup.find_all('div', attrs={'class': 'product-wrap'})
    for block in blocks:
        name = block.find('h3').text.replace('\n', '')
        image = block.find('img')['src']
        price = block.find('div', class_='product-price').text.replace('\n', '')
        data.append({
            'name': name,
            'image': image,
            'price': price
        })


with open('phones_openshop.json', 'w', encoding='utf-8') as outfile:
    parser('shop/category/phones-and-gadgets/')
    json.dump(data, outfile, ensure_ascii=False, indent=4)