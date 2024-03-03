# backlink-import
des scripte pour importé des backlink depuis recherche google

import requests
from bs4 import BeautifulSoup
# Methode 1
print("# Methode 1")

url = "www.sofirux.com"
google_search = requests.get(f'https://www.google.com/search?q=link:{url}')
soup = BeautifulSoup(google_search.text, "html.parser")
links = soup.find_all('a')
for link in links:
    href = link.get('href')
    if href and href.startswith('/url?q='):
        actual_link = href.split('/url?q=')[1].split('&')[0]
        print(actual_link)
    
# Methode 2
print("# Methode 2")

url = "www.turquiesante.com"
# Modifier l'URL pour effectuer une recherche sur Yandex
page_number = 0
while True:
    yandex_search = requests.get(f'https://yandex.com/search/?text=link:{url}&p={page_number}')
    soup = BeautifulSoup(yandex_search.text, "html.parser")
    # Trouver les balises 'a' qui contiennent les liens
    links = soup.find_all('a')
    # Afficher les liens
    for link in links:
        href = link.get('href')
        if href and href.startswith('https://yandex.com/'):
            # Les liens directs de Yandex commencent généralement par 'https://yandex.com/'
            actual_link = href
            print(actual_link)
    # Aller à la page suivante
    next_page = soup.find('a', class_='pager__item_kind_next')
    if not next_page:
        break
    page_number += 1
    
# Methode 3
print("# Methode 3")

url = "www.turquiesante.com"
page_number = 0

while True:
    bing_search_url = f'https://www.bing.com/search?q=link:{url}&first={page_number * 10}'
    bing_search = requests.get(bing_search_url)
    soup = BeautifulSoup(bing_search.text, "html.parser")
    links = soup.find_all('a', href=True)
    for link in links:
        href = link['href']
        if href.startswith('http') or href.startswith('https'):
            print(href)
    next_page = soup.find('a', class_='sb_pagN')
    if not next_page:
        break
    
    page_number += 1

