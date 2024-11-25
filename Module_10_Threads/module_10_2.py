import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.counter = 100

    def run(self):
        print(f'{self.name}, на нас напали!')
        days_war = 0
        while self.counter > 0:
            time.sleep(1)
            self.counter -= self.power
            days_war += 1
            if self.counter >= 0:
                print(f'{self.name} сражается {days_war} дней, осталось {self.counter} воинов.')
            else:
                print(f'{self.name} сражается {days_war} дней, осталось 0 воинов.')
        print(f'{self.name} одержал победу спустя {days_war} дней!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
