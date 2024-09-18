n = int(input('Введите число из первой вставки: '))
result = []

# поиск всех пар делителя
def search_number_pairs(value):
    for i in range(1, (value - value // 2)):
        num_1 = i
        num_2 = value - num_1
        pair = [num_1, num_2]
        result.append(pair)

    return result

# поиск всех делителей
for i in range(3, n + 1):
    if n % i == 0:
        divider = i
    else:
        continue
    search_number_pairs(divider)

result.sort()
for char in result:
    print(*char, sep='', end='')