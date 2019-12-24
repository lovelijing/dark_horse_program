import multiprocessing


def process1():
    while True:
        print('----------1------------')


def process2():
    while True:
        print('-----------2------------')


def main():
    p1 = multiprocessing.Process(target=process1)
    p2 = multiprocessing.Process(target=process2)

    p1.start()
    p2.start()


if __name__ == '__main__':
    main()