text = input("Введите текст: ")

# Разбиваем текст на список слов
words = text.split()

# Считаем частоту встречаемости слов
word_frequency = {}
for word in words:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

# Находим наиболее часто встречающееся слово
most_frequent_word = max(word_frequency, key=word_frequency.get)

# Находим самое длинное слово
longest_word = max(words, key=len)

# Выводим результаты
print("Наиболее часто встречающееся слово: ", most_frequent_word)
print("Самое длинное слово: ", longest_word)