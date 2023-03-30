from math import acos, factorial
from random import randint

def calculate():
    choose = int(input(f"""\n\nВыберите необходимое действие 
    1. A * B 
    2. A - B
    3. A ** B
    4. A / B
    5. random number A to B
    6. factorial x
    7. ArcCos( x )
    ИСПОЛЬЗУЙТЕ ТОЛЬКО ЦИФРЫ
    Choose: """))
    
    try:
        match choose:
            case 1 | 2 | 3 | 4:
                print(eval(input("Введите ваше выражение по выбранному шаблону >>>")))    
            case 5:
                a = int(input("Разброс от: "))
                b = int(input("\nРазброс до: "))
                print("\n", randint(a, b))
            case 6:
                  x = int(input("введите ваше значение x: "))
                  print("\n", factorial(x))
            case 7:
                  x = int(input("введите ваше значение x: "))
                  print("\n", acos(x)) 
            case _:
                print("Используйте только цифры")
    except Exception as e:
                print("Не правильное использование калькулятора \n", e)


while True: calculate()