names = input().split()  # ввод имен студентов через пробел
filtered_names = [name for name in names if 'ва' in name]  # фильтрация имен по наличию фрагмента "ва"
result = ' '.join(filtered_names)  # объединение имен в строку через пробел
print(result)  # вывод результата
#Андреев Иванов Петров Васильева Сидорова