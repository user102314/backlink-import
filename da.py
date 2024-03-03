import requests
from bs4 import BeautifulSoup

def trouver_backlinks(site):
    url = f"https://www.google.com/search?q=%2F{site}"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = soup.find_all('a')
        
        backlinks = []
        for result in results:
            href = result.get('href')
            if 'http' in href and site in href:
                backlinks.append(href)
        
        return backlinks
    else:
        return None

site = input("donné votre site  :  ")

backlinks = trouver_backlinks(site)  

if backlinks:
    for link in backlinks:
        print(link + '\n')
else:
    print("La recherche de backlinks a échoué.")
