import requests
import json
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv


data = []

def parser(category):
    load_dotenv('.env.gazeta')
    URL = 'https://www.gazeta.uz/oz/'
    HOST = 'https://www.gazeta.uz'

    HEADERS = {
        'USER-AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
    }

    html = requests.get(URL + category, headers=HEADERS).text
    soup = BeautifulSoup(html, 'html.parser')

    blocks = soup.find_all('div', attrs={'class': 'nblock'})
    for block in blocks:
        img = block.find('img').get('data-src')
        title = block.find('h3').text.replace('\n', '')
        text = block.find('p').text
        date = block.find('div', class_ = 'ndt').text

        data.append({
            'img': img,
            'title': title,
            'text': text,
            'date': date,
        })

with open('politics.json', 'w', encoding='utf-8') as outfile:
    parser('politics/')
    json.dump(data, outfile, ensure_ascii=False, indent=4)

print(len(data))