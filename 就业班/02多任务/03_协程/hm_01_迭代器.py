# 用迭代器计算并显示斐波那切数列


class Fiblist(object):
    def __init__(self,num):
        self.num = num
        self.a = 0
        self.b = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.num:
            num = self.a
            self.a, self.b = self.b, self.a+self.b
            self.count += 1
            return num
        else:
            raise StopIteration


def main():
    myfiblist = Fiblist(100)
    for num in myfiblist:
        print(num)


if __name__ == '__main__':
    main()