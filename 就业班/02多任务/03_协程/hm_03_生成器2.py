# 生成器可以用next函数获取下一个元素


def fib(nums):
    num1, num2 = 0, 1
    count = 0
    while count < nums:
        yield num1
        num1, num2 = num2, num1 + num2
        count += 1
    return 'done'


def main():
    obj = fib(10)
    count = 0
    while count < 10:
        print(next(obj))
        count += 1


if __name__ == '__main__':
    main()