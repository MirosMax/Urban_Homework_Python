'''
Симуляция общепита.
Приготовление булок и котлет. Первый сотрудник бесконечно жарит булки, второй готовит котлеты. В 20% случаев булки будут
подгорать.
'''

import time
from threading import Thread
import random
import queue


class Bulka(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            time.sleep(1)
            if random.random() > 0.8:
                self.queue.put('подгорелая булка')
            else:
                self.queue.put('хорошая булка')


class Kotleta(Thread):
    def __init__(self, queue, count):
        super().__init__()
        self.queue = queue
        self.count = count

    def run(self):
        count_burger = 0
        while self.count:
            count_burger += 1
            print(self.queue.qsize())
            bulka = self.queue.get()
            if bulka == 'хорошая булка':
                time.sleep(random.randint(1, 3))
                self.count -= 1
                print(f'Бургер № {count_burger} готов!')
            print(f'Булок в запасе: {self.count}')


q = queue.Queue(maxsize=20)

t1 = Bulka(q)
t2 = Kotleta(q, 20)

t1.start()
t2.start()
t1.join()
t2.join()