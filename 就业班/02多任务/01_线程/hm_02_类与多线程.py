import threading
import time


class mythread(threading.Thread):
    def run(self):
        for i in range(3):
            print('类和线程' + str(time.time()))
            time.sleep(1)


if __name__ == '__main__':
    m1 = mythread()
    m2 = mythread()
    m1.start()
    m2.start()
