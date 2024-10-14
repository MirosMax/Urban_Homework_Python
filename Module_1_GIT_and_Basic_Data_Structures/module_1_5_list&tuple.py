immutable_var = 5, 7, 'pen', 'phone', True
print(immutable_var)
print(type(immutable_var))
print(type(immutable_var[0]))
print(type(immutable_var[2]))
print(type(immutable_var[-1]))

# immutable_var[1] = 15  # попытка изменения элемента выдаст ошибку, т.к. кортеж это неизменяемый объект

immutable_var += [3, 15, 22, 18], 0
print(immutable_var)

immutable_var[-2][0] = 77
print(immutable_var)

mutable_list = [True, 8, 5, 'juice']
print(mutable_list)
mutable_list[0] = 77
print(mutable_list)