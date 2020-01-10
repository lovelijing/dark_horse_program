import re


def main():
    email = input('请输入电子邮箱地址:')
    ret = re.match(r'^[a-zA-Z0-9]{4,20}@(163|126|qq|139|sina|189)\.([Cc][Oo][Mm]|[Cc)][Nn])$', email)
    if ret:
        print(email,f'：  符合条件。是{ret.group(1)}邮箱')
    else:
        print(email, '：  不符合条件。')


if __name__ == '__main__':
    main()