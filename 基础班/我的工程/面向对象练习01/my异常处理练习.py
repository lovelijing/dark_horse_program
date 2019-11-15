def demo1():
    return int(input("请输入一个整数（不可以为0）："))


def demo2():
    return 8 / demo1()


while True:
    try:
        print(demo2())
    except ValueError:
        print("请输入一个整数，而不是字母！")
    except ZeroDivisionError:
        print('除零错误！')
    except Exception as resuate:
        print(f'未知错误！{resuate}')
    else:
        print("尝试成功！")
        break
    finally:
        print("必须执行的代码！")
    continue

print("-" * 50)
