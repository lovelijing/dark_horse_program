import threading
import time



def sing():
    for i in range(5):
        print('------正在唱歌---------')
        time.sleep(1)


def dance():
   for i in range(5):
       print('--------正在跳舞---------')
       time.sleep(1)


def main():
    t1 = threading.Thread(target = sing)
    t2 = threading.Thread(target = dance)
    t1.start()
    t2.start()

    print(threading.enumerate())




if __name__ == '__main__':
    main()
