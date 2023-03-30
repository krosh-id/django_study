def calc():
    a = int(input("Введите любое число: "))
    b = int(input("Введите пограничное число: "))
    print(f'a {">= 3 *" if a/b >= 3  else "<" if a < b else " < " if a > b else "=" } b\n')

while True: calc()
