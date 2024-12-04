import time
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(line)


if __name__ == '__main__':

    files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']

    start = time.time()
    for file in files:
        read_info(file)
    stop = time.time()
    print(f'Затраченное время на ЛИНЕЙНЫЙ: {stop - start} сек.')

    start = time.time()
    with multiprocessing.Pool(4) as pool:
        pool.map(read_info, files)
    stop = time.time()
    print(f'Затраченное время на МНОГОПРОЦЕССНЫЙ: {stop - start} сек.')


