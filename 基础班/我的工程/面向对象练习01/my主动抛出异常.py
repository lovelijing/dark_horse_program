def input_password():
    pwd = input("请输入密码：")
    if len(pwd)>=8:
        return pwd
    ex=Exception("密码长度小于8个字符")
    raise ex


while True:
    try:
        print(f"你输入的密码为：{input_password()}")
    except Exception as result:
        print(f"发现错误：{result}")
    else:
        break
    finally:
        pass
    continue


print("-"*50)



