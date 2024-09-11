grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_list = list(students)  # преобразование неупорядоченного множества в упорядоченный список
students_list.sort()  # сортировка списка по алфавиту
average_score_of_students = {}  # создание нового словаря

for i in range(0, len(students_list)):  # перебирание по очереди всех студентов и сопоставление им ср.балла
    average_grades = sum(grades[i]) / len(grades[i])
    average_score_of_students[students_list[i]] = average_grades

print(average_score_of_students)