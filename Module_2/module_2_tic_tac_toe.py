area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]


def check_win():
    winner = False
    for str_ in area:
        if str_ == ['X', 'X', 'X']:
            print('Выиграли КРЕСТИКИ. Поздравляем!')
            winner = True
            break
        elif str_ == ['0', '0', '0']:
            print('Выиграли НОЛИКИ. Поздравляем!')
            winner = True
            break
    else:
        if (
            area[0][0] == area[1][1] == area[2][2] == 'X'
            or area[0][2] == area[1][1] == area[2][0] == 'X'
            or area[0][0] == area[1][0] == area[2][0] == 'X'
            or area[0][1] == area[1][1] == area[2][1] == 'X'
            or area[0][2] == area[1][2] == area[2][2] == 'X'
        ):
            print('Выиграли КРЕСТИКИ. Поздравляем!')
            winner = True
        elif (
            area[0][0] == area[1][1] == area[2][2] == '0'
            or area[0][2] == area[1][1] == area[2][0] == '0'
            or area[0][0] == area[1][0] == area[2][0] == '0'
            or area[0][1] == area[1][1] == area[2][1] == '0'
            or area[0][2] == area[1][2] == area[2][2] == '0'
        ):
            print('Выиграли НОЛИКИ. Поздравляем!')
            winner = True
    return winner


def print_area():
    for cell in area:
        print(*cell)


print('Приветствуем в игре Крестики Нолики!')
print()

print_area()

for step in range(1, 10):
    print()
    if step % 2 != 0:
        print(f'Ход № {step}. Ходят КРЕСТИКИ')
        row_ = int(input('Укажите номер колонки: ')) - 1
        str_ = int(input('Укажите номер строки: ')) - 1
        if 0 <= row_ <= 2 and 0 <= str_ <= 2:
            if area[str_][row_] == '*':
                area[str_][row_] = 'X'
            elif area[str_][row_] == 'X' or area[str_][row_] == '0':
                print('Эта клетка уже занята, вы пропускаете ход')
                print_area()
                continue
        else:
            print('Введены некорректные координаты, вы пропускаете ход')
            print_area()
            continue

    else:
        print(f'Ход № {step}. Ходят НОЛИКИ')
        row_ = int(input('Укажите номер колонки: ')) - 1
        str_ = int(input('Укажите номер строки: ')) - 1
        if 0 <= row_ <= 2 and 0 <= str_ <= 2:
            if area[str_][row_] == '*':
                area[str_][row_] = '0'
            elif area[str_][row_] == 'X' or area[str_][row_] == '0':
                print('Эта клетка уже занята, вы пропускаете ход')
                print_area()
                continue
        else:
            print('Введены некорректные координаты, вы пропускаете ход')
            print_area()
            continue
    print_area()
    if step >= 5:
        winner = check_win()
        if winner:
            break
