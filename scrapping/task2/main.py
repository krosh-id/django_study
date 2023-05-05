from pars import pars
from prettytable import PrettyTable


def viewTable(table_data):

    table = PrettyTable()
    #заголовок таблицы 
    table.field_names = ["Apr 2023", "Apr 2022", "Programming Language", "Ratings", "Change"]
    #добавление строк в таблицу 
    for stroka in table_data:
        table.add_row([stroka["Apr 2023"], stroka["Apr 2022"], stroka["Programming Language"], stroka["Ratings"], stroka["Change"]])
        
    print(table)

while True:
    print("""Menu:
    1. Load top programming language
    2. Update information from the table
    3. Exit  
        """)
    answer = int(input('Please enter number:'))
    
    match answer:
        case 1:
            viewTable(pars())
        case 2:
            viewTable(pars())
        case 3:
            break
        case _:
            print("Введите цифру 1-3\n")