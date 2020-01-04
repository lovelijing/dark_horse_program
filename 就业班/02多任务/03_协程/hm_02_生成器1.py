# 用生成器实现斐波那切数列


def fib(nums):
    a, b = 0, 1
    count = 0
    while count < nums:
        yield a     # 函数中有yield就变成生成器模板。
        a, b = b, a+b
        count += 1
    return 'done'


def main():
    obj = fib(10)
    c = 0
    for num in obj:
        print(num)


if __name__ == '__main__':
    main()