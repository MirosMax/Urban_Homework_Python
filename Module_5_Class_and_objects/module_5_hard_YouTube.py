'''
Задание "Свой YouTube":
Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики на тему
IT (юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания
программирования.

Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут выполнять похожий
функционал на сайте.

Всего будет 3 класса: UrTube, Video, User.

Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео,
авторизации и регистрации пользователя и т.д.

Подробное ТЗ:

Каждый объект класса User должен обладать следующими атрибутами и методами:
- Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)

Каждый объект класса Video должен обладать следующими атрибутами и методами:
- Атрибуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)),
adult_mode(ограничение по возрасту, bool (False по умолчанию))

Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
- Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
- Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с такими
же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните, что password
передаётся в виде строки, а сравнивается по хэшу.
- Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если
пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже
существует". После регистрации, вход выполняется автоматически.
- Метод log_out для сброса текущего пользователя на None.
- Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же
названием видео ещё не существует. В противном случае ничего не происходит.
- Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое
слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
- Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела), то
ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр. После текущее
время просмотра данного видео сбрасывается.

Для метода watch_video так же учитывайте следующие особенности:
- Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
- Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль
надпись: "Войдите в аккаунт, чтобы смотреть видео"
- Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
- После воспроизведения нужно выводить: "Конец видео"
'''


class User:
    def __init__(self, nickname: str, password: str, age: int):
        '''
        :param nickname: Логин пользователя, str
        :param password: Пароль пользователя в захешированном виде, str
        :param age: Возраст пользователя, int
        '''
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):
        '''
        :param title: Заголовок видео, строка, str
        :param duration: Продолжительность видео, секунды, int
        :param time_now: Секунда остановки, int
        :param adult_mode: Ограничение по возрасту, bool
        '''
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, login, psw):
        for user in self.users:
            if user.nickname == login and hash(psw) == user.password:
                self.current_user = user
                print(f'Успешная авторизация! Привет, {login}.')
                break
        else:
            print(f'Пользователь {login} не найден или неверный пароль')

    def register(self, new_nickname, new_password, new_age):
        for user in self.users:  # проверяем есть ли такие пользователи
            if user.nickname == new_nickname:
                print(f'Пользователь {new_nickname} уже существует. Авторизуйтесь.')
                break
        else:  # если break не сработал, то регистрируем нового пользователя
            new_user = User(new_nickname, new_password, new_age)
            self.users.append(new_user)
            self.current_user = new_user
            print(f'Пользователь {new_nickname} зарегистрирован и авторизован!')

    def log_out(self):
        self.current_user = None
        print('Вы вышли из системы')

    def add(self, *args: Video):
        for el in args:
            for video in self.videos:
                if el.title == video.title:
                    print('Такое видео уже есть в базе данных')
                    break
            self.videos.append(el)
            print(f'Видео "{el.title}" добавлено в каталог!')

    def get_videos(self, search_query):
        search_result = []
        for video in self.videos:
            if search_query.lower() in video.title.lower():
                search_result.append(video.title)
        if len(search_result) == 0:
            print(f'Ничего не найдено по запросу "{search_query}"')
        else:
            print(f'Вот что нашлось по запросу "{search_query}":')
            for i in range(1, (len(search_result) + 1)):
                print(f'{i}. "{search_result[i - 1]}"')

    def watch_video(self, name_video):
        import time

        if self.current_user is None:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for video in self.videos:
                if name_video == video.title:
                    if not video.adult_mode or (self.current_user.age >= 18 and video.adult_mode):
                        for i in range(video.time_now, video.duration + 1):
                            print(i, end=' ')
                            time.sleep(0.2)
                            video.time_now = 0  # сброс времени просмотра на 0
                        print('Конец видео')
                    else:
                        print(f'{self.current_user.nickname}, Вам нет 18 лет, пожалуйста покиньте страницу')
                    break
            print(f'Видео "{name_video}" не существует')

    def name_current_user(self):
        # возвращает читабельное имя текущего пользователя
        if self.current_user is None:
            name = None
        else:
            name = self.current_user.nickname
        return name


ur = UrTube()

# Добавление видео
print('\nДобавление видео:')
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, 3, True)
v3 = Video('Смешные котики за январь 2024', 3500, 500)
v4 = Video('Как научиться кодить за 6 месяцев', 250)
ur.add(v1, v2, v3, v4)
print(f'Все видео: {ur.videos}')
v5 = Video('Смешные котики за январь 2024', 3500, 500)
ur.add(v5)
v6 = Video('Топ гаджетов 2024', 350)
ur.add(v6)
print(f'Все видео: {ur.videos}')

# регистрация
print('\nРегистрация:')
ur.register('looper', '7775lksahd67817', 13)
ur.register('king', '123546', 15)
ur.register('queen', '777777', 25)
ur.register('ace', '16591324', 35)
print(f'Все пользователи: {ur.users}')

# авторизация
print('\nАвторизация:')
ur.log_in('user', '123546')
print(f'Текущий пользователь: {ur.name_current_user()}')
ur.log_in('queen', '111111')
print(f'Текущий пользователь: {ur.name_current_user()}')
ur.log_in('queen', '777777')
print(f'Текущий пользователь: {ur.name_current_user()}')

# выход из личного кабинета
print('\nВыход из личного кабинета:')
ur.log_out()
print(f'Текущий пользователь: {ur.name_current_user()}')

# повторная авторизация
print('\nПовторная авторизация:')
ur.log_in('queen', '777777')
print(f'Текущий пользователь: {ur.name_current_user()}')

# поиск видео
print('\nПоиск видео:')
ur.get_videos('wdtnjr')
ur.get_videos('Програм')

# просмотр видео
print('\nПросмотр видео:')
print(f'Текущий пользователь: {ur.name_current_user()}')
ur.watch_video('Для чего девушкам парень программист?')
ur.log_out()
print(f'Текущий пользователь: {ur.name_current_user()}')
ur.watch_video('Для чего девушкам парень программист?')

# Проверка на вход пользователя и возрастное ограничение
print('\nПроверка на вход пользователя и возрастное ограничение:')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
print('\nПроверка входа в другой аккаунт:')
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(f'Текущий пользователь: {ur.name_current_user()}')

# Попытка воспроизведения несуществующего видео
print('\nПопытка воспроизведения несуществующего видео:')
ur.watch_video('Лучший язык программирования 2024 года!')
ur.watch_video('Занимательные флаги. Выпуск 24')
