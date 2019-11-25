import threading
# 多线程共有两种方式使用全局变量
# 1、为直接使用如myname和mytemp两个全局变量
# 2、用参数的方法使用全局变量，如mystr，注意26,27行的args，args必须等于元祖
myname = [1,2]
mytemp = 126
mystr = ('ab','cd','efg')


def demo1(s1):
    global  mytemp      # 因为改变了mytemp的指向，所有这里要加global指明mytemp是全局变量
    mytemp = mytemp + 1
    myname.append(3)    # 因为没有改变myname的指向，因此不用global
    print(myname, s1[1])
    print(mytemp)


def demo2(s1):
    global mytemp   # 因为改变了mytemp的指向，所有这里要加global指明mytemp是全局变量
    mytemp += 100
    myname.append(5)    # 因为没有改变myname的指向，因此不用global
    print(myname, s1)
    print(mytemp)

def main():
    t1 = threading.Thread(target = demo1, args = (mystr,))
    t2 = threading.Thread(target = demo2, args = (mystr,))
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()

