from time import sleep, time
import threading


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            sleep(0.1)
            file.write(f'Какое-то слово № {i + 1}\n')
    print('Завершилась запись в файл', file_name)


time_start = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_stop = time()
time_spent = round(time_stop - time_start, 3)
print(f'Работа функций заняла {time_spent} секунд')

thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

time_start = time()
thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread3.join()  # так как поток 3 самый объемный, то применяем join только к нему
time_stop = time()
time_spent = round(time_stop - time_start, 3)
print(f'Работа потоков заняла {time_spent} секунд')
