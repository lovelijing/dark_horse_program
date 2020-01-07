import time


def task1():
    while True:
        print('-----1-----')
        time.sleep(0.1)
        yield


def task2():
    while True:
        print('-----2-----')
        time.sleep(0.1)
        yield


def main():
    y1 = task1()
    y2 = task2()
    while True:
        next(y1)
        next(y2)


if __name__ == '__main__':
    main()
