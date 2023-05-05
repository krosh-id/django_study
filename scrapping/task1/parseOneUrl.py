#парсинг отдельной страницы  с ноутбуком 
import requests
from bs4 import BeautifulSoup


def parseOneUrl(url):
    notebooks = {'name': '', 'decsription': '', 'price': ''}
    
    try:
        response = requests.get(url)   
    except:
        print("Неудалось подключиться к сайту: ", url)

    soup = BeautifulSoup(response.text, 'lxml')
    
    #название ноутбука
    quotes = soup.find('h4', class_='')
    notebooks['name'] = quotes.text 

    #описание  
    quotes = soup.find('p', class_='description')
    notebooks['decsription'] = quotes.text

    #цена
    quotes = soup.find('h4', class_='pull-right price')
    notebooks['price'] = quotes.text

    return notebooks
 
