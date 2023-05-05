from parseAllUrl import parseAllUrl
from parseOneUrl import parseOneUrl

import csv

urls = parseAllUrl()

with open("./notebooks.csv", "w", newline="") as file:
      print('данные очищены')

with open("./notebooks.csv", "a", newline="") as file:
        print('скрапинг данных ....')
        #список словарей содержащий ноутбуки
        notebooks = []
        for url in urls:
            notebooks.append(parseOneUrl(url))

        writer = csv.DictWriter(file, fieldnames=notebooks[0].keys())
        
        # Записать заголовок CSV файла
        writer.writeheader()
        
        # Записать данные из списка словарей
        for row in notebooks:
            writer.writerow(row)
        print('успешно сохранено в notebooks.csv')

    