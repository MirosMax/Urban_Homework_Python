from math import pi, sqrt


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = self.__correct_sides(sides)
        self.__color = list(color)
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if (isinstance(r, int) and 0 <= r <= 255 and
                isinstance(g, int) and 0 <= g <= 255 and
                isinstance(b, int) and 0 <= b <= 255):
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
            print(f'Цвет изменен на {self.__color}')
        else:
            print(f'Некорректный ввод данных. Цвет остался прежним: {self.__color}')

    def __is_valid_sides(self, args):
        # проверка, чтобы все числа были целыми, положительными и
        # количество аргументов были равны числу заданных сторон или 1
        if 1 < len(args) < len(self.__sides):
            return False
        for arg in args:
            if arg < 0 or isinstance(arg, float):
                return False
        return True

    def __correct_sides(self, args):
        # задание правильных сторон, в зависимости от фигуры
        #
        # частный случай для куба, если заданы все 12 сторон, но они не равны
        if len(args) == 12 and self.sides_count == 12:
            for i in range(1, len(args)):
                if args[i] != args[0]:
                    return [1] * self.sides_count
            return list(args)
        # частные случаи при задании 1 аргумента: для куба (т.к. у него всегда равные стороны), и
        # равностороннего треугольника
        elif (len(args) == 1 and self.sides_count == 12) or (len(args) == 1 and self.sides_count == 3):
            return list(args) * self.sides_count
        elif len(args) == self.sides_count:
            return list(args)
        else:
            return [1] * self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            if len(new_sides) == 1:
                self.__sides = list(new_sides) * len(self.__sides)
                print(f'Стороны фигуры изменены на: {self.__sides}')
            elif len(new_sides) == len(self.__sides):
                self.__sides = list(new_sides)
                print(f'Стороны фигуры изменены на: {self.__sides}')
        else:
            print(f'Некорректный ввод данных. Стороны фигуры остались без изменений: {self.__sides}')


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_radius()

    def get_square(self):
        s = self.__len__() ** 2 / (4 * pi)
        return s

    def get_radius(self):
        r = len(self) / (2 * pi)
        return r


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        # возвращает площадь треугольника
        p = self.__len__() / 2
        a = self.get_sides()[0]
        b = self.get_sides()[1]
        c = self.get_sides()[2]
        s = sqrt(p * (p - a) * (p - b) * (p - c))
        return s


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_volume(self):
        # возвращает объем куба
        v = (len(self) / self.sides_count) ** 3
        return int(v)


print('Создание объектов:')
circle1 = Circle((200, 200, 100), 10, 15, 6)  # (Цвет, стороны)
circle2 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
print(circle1.get_sides())
print(circle2.get_sides())

cube1 = Cube((222, 35, 130), 6)
cube2 = Cube((222, 35, 130), 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)
cube3 = Cube((222, 35, 130), 1, 5, 6, 6, 6, 6, 8, 6, 6, 6, 6, 6)
print(cube1.get_sides())
print(cube2.get_sides())
print(cube3.get_sides())

triangle1 = Triangle((200, 155, 15), 5, 15, 8)
triangle2 = Triangle((200, 155, 15), 7)
triangle3 = Triangle((200, 155, 15), 7, 2)
print((triangle1.get_sides()))
print((triangle2.get_sides()))
print((triangle3.get_sides()))

# Проверка на изменение цвета:
print('\nПроверка на изменение цвета:')
print(circle1.get_color())
circle1.set_color(55, 66, 77)  # Изменится

print(cube1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится


# Проверка на изменение сторон:
print('\nПроверка на изменение сторон:')
print(cube1.get_sides())
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится

print(cube3.get_sides())
cube3.set_sides(15)  # Изменится

print(circle1.get_sides())
circle1.set_sides(15)  # Изменится

print((triangle1.get_sides()))
triangle1.set_sides(5, 3)  # Не изменится
triangle1.set_sides(5)  # Изменится
print((triangle1.get_sides()))

# Проверка периметра (круга), это и есть длина:
print('\nПроверка периметра (круга), это и есть длина, и радиуса:')
print(len(circle1))

# Проверка радиуса и площади круга:
print('\nПроверка радиуса и площади круга:')
print(circle1.get_radius())
print(circle1.get_square())

# Проверка объёма (куба):
print('\nПроверка объёма (куба):')
print(cube1.get_sides())
print(cube1.get_volume())

# Проверка площади треугольника:
print('\nПроверка площади треугольника:')
print(triangle1.get_sides())
print(triangle1.get_square())
