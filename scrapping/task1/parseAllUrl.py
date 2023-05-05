import requests
from bs4 import BeautifulSoup

def parseAllUrl():
    allUrl = []

    url = 'https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops/'
    try:
        response = requests.get(url)   
    except:
        print("Неудалось подключиться к сайту: ", url)
    
    soup = BeautifulSoup(response.text, 'lxml')

    for link in soup.find_all('a', {'class': 'title'}):
        links = 'https://webscraper.io'+str(link.get('href'))
        allUrl.append(links)
    
    return allUrl