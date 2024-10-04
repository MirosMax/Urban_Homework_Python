def get_multiplied_digits(number):
    str_number = str(number)
    if len(str_number) > 1:
        first = int(str_number[0])
        if first == 0:
            first = 1
        return first * get_multiplied_digits(int(str_number[1:]))
    elif number == 0:
        return 1
    else:
        return number


print(get_multiplied_digits(int(input())))
