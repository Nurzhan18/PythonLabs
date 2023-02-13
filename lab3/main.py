# Вводим строку с русскими и латинскими буквами
string = input("Введите строку: ")

# Создаем словарь для перевода букв
t = {
    'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
    'е': 'e', 'ё': 'e', 'ж': 'zh', 'з': 'z', 'и': 'i',
    'й': 'i', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n',
    'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
    'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch',
    'ш': 'sh', 'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '',
    'э': 'e', 'ю': 'yu', 'я': 'ya',
    'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e',
    'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j',
    'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o',
    'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't',
    'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y',
    'z': 'z'
}

# Приводим строку к нижнему регистру
string = string.lower()

# Заменяем символы " ?!;:" на символ дефиса (-)
string = string.replace(' ', '-')
string = string.replace('?', '-')
string = string.replace('!', '-')
string = string.replace(';', '-')
string = string.replace(':', '-')

# Переводим строку в латиницу с помощью словаря
transliterated = ''
for char in string:
    if char in t:
        transliterated += t[char]
    else:
        transliterated += char

# Выводим результат
print(transliterated)
