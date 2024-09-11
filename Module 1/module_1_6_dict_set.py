my_dict = {'Игорь': 1997, 'Макс': 1987, 'Яна': 2003, 'Анастасия': 1999, 'Мария': 1978, 'Лолита': 2000}
print(my_dict)

print(my_dict.get('Мария'))  # существующий элемент
print(my_dict.get('Леонид', 'Такого ключа не найдено'))  # несуществующий элемент

my_dict.update({'Ольга': 1984, 'Кирилл': 1994})
print(my_dict)
print(my_dict.pop('Яна'))
print(my_dict)


my_set = {'Кот', 'Мышь', 29, 55, 'Мышь', 29}
print(my_set)
my_set.add(94)
my_set.add('Собака')
print(my_set)
my_set.remove('Мышь')
print(my_set)