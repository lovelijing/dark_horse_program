# 一个含有yield的函数可以生成多个生成器。
# 用生成器.send(返回值)也有和next一样的功能，只是传递了参数作为返回值。


def fib(nums):
    num1, num2 = 0, 1
    count = 0
    while count < nums:
        ret = yield num1
        num1, num2 = num2, num1 + num2
        count += 1
        if ret != None:
            print(ret+f'值为{num1}')
    return 'done'


def main():
    obj1 = fib(10)  # 生成第一个生成器。
    obj2 = fib(10)  # 生成第二个生成器。
                    # 两个生成器互不相关。
    for n in obj1:
        print(n)
    count = 0
    print('-------------------------')
    while count<10:
        if count == 0:
            data = obj2.send(None)     # 第一次用send不能传参数（也可以用next（））。
            print(f"第{count}次取值，值为{data}")
        else:
            data = obj2.send(f'第{count}次取值')

        count += 1


if __name__ == '__main__':
    main()