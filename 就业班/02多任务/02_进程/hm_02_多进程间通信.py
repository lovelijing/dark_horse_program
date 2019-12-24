import multiprocessing


def putdata(q):
    data = [11,22,33,44,55,66]
    for tempdata in data:
        q.put(tempdata)


def getdata(q):
    datalist = list()
    while True:
        if q.empty():
            break
        tempdata = q.get()
        datalist.append(tempdata)
    print(datalist)


def main():
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=putdata, args=(q,))
    p2 = multiprocessing.Process(target=getdata, args=(q,))
    p1.start()
    p2.start()


if __name__ == '__main__':
    main()
