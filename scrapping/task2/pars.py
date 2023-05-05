import requests
from bs4 import BeautifulSoup

def pars():
    
    url = 'https://www.tiobe.com/tiobe-index/'
    try:
        response = requests.get(url)   
    except:
        print("Неудалось подключиться к сайту: ", url)

    soup = BeautifulSoup(response.text, 'lxml')

    # Найти таблицу на странице
    table = soup.find("table")

    # Найти все строки таблицы
    rows = table.find_all("tr")

    #список для всех строк таблицы 
    allRating = []

    # Обойти каждую строку и получить значения столбцов
    for row in rows:
        # Найти все столбцы в текущей строке
        cols = row.find_all("td")
        
        
        #чтобы пропустить первый пустой список при скрапинге 
        if len(cols) != 0 :
            #добавление новой строки
            rating = {
                'Apr 2023':cols[0].text,
                'Apr 2022':cols[1].text,
                'Programming Language':cols[4].text,
                'Ratings':cols[5].text,
                'Change':cols[6].text
            }
            allRating.append(rating)
    
    return allRating
