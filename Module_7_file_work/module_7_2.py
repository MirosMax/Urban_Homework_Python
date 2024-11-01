def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    for i in range(1, len(strings) + 1):
        strings_positions[(i, file.tell())] = strings[i - 1]
        file.write(strings[i - 1] + '\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
