my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
num = 0

while len(my_list) > 0:
    num = my_list.pop(0)
    if num == 0:
        continue
    elif num < 0:
        break
    print(num)