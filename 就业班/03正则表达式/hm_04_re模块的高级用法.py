import re
# 本程序运用的函数只有Python的re模块才具备。


def add(temp):
    strNum = temp.group()
    num = int(strNum) + 1
    return str(num)


def main():
    # re.search()函数
    ret = re.search(r"\d+", "阅读次数为 9999")
    print(ret.group())

    # re.findall()函数
    ret = re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
    print(print(ret))

    # re.sub()函数的两种用法
    ret = re.sub(r"\d+", '998', "python = 997")
    print(ret)

    ret = re.sub(r"\d+", add, "python = 997")
    print(ret)

    ret = re.sub(r"\d+", add, "python = 99")
    print(ret)

    # re.split()函数
    ret = re.split(r":| ", "info:xiaoZhang 33 shandong")
    print(ret)


if __name__ == '__main__':
    main()