from greenlet import greenlet
import time

def tesk1():
    while True:
        print("---A--")
        gr2.switch()
        time.sleep(0.5)

def tesk2():
    while True:
        print("---B--")
        gr1.switch()
        time.sleep(0.5)

gr1 = greenlet(tesk1)
gr2 = greenlet(tesk2)

#切换到gr1中运行
gr1.switch()