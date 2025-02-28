import requests
import json
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv



data = []
def parser(category):
    load_dotenv()
    URL = os.getenv("URL")
    HOST = os.getenv("HOST")
    HEADERS = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }

    html = requests.get(URL+category, headers=HEADERS).text
    soup = BeautifulSoup(html, 'html.parser')

    products = soup.find_all('div', attrs={'class': 'product-item-wrapper'})
    for product in products:
        img = product.find('img').get('data-src')
        title = product.find('h2').text
        price = product.find('div', attrs={'class': 'product-price__current'}).text.replace("\n", "").strip()

        data.append({
            'image': img,
            'title': title,
            'price': price,

        })

with open("laptops.json", "w", encoding="utf-8") as f:
    parser('noutbuki/')
    json.dump(data, f, ensure_ascii=False, indent=4)


with open('telefony.json', 'w', encoding="utf-8") as telefony_file:
    parser('smartfony/')
    json.dump(data, telefony_file, ensure_ascii=False, indent=4)




