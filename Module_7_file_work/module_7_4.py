# использование %
team1_num = 5  # "Мастера кода"
team2_num = 7  # "Волшебники данных"
print('В команде "Мастера кода" участников: %s' % team1_num)
print('В команде "Волшебники данных" участников: %s' % team2_num)
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))

# использование format()
score_1 = 77
score_2 = 68
print('Команда "Мастера кода" решила задач: {}'.format(score_1))
print('Команда "Волшебники данных" решила задач: {}'.format(score_2))
team1_time = 1552
team2_time = 2153
print('"Волшебники данных" решили задачи за {0} сек., а "Мастера кода" справились за {1} сек.'.format(team2_time,
                                                                                                      team1_time))

# использование f-строк
print(f'Команды решили {score_1} и {score_2} задач.')
tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg)} секунды на задачу!')

if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды "Мастера кода"!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды "Волшебники данных"!'
else:
    challenge_result = 'Ничья!'
print(f'Результат битвы: {challenge_result}')
