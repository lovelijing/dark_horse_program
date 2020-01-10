import re


def main():
    names = ['age', 'age1', 'age_', '_age', 'age_2', '_________', '2age', 'age!', 'age_&']
    for name in names:
        ret = re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name)
        if ret:
            print(f'{name}：  符合要求。')
        else:
            print(f'{name}:   不符合要求')


if __name__ == '__main__':
    main()