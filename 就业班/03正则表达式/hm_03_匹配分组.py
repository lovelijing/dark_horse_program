import re


def main():
    data = '''    
    <body>
        <h1>
            Hello world!   
        </h1>
    </body>    
    '''

    ret1 = re.match(r'^[\s\S]*<(\w*)>[\s\S]*<(\w*)>[\s\S]*</\2>[\s\S]*</\1>[\s\s]*$', data)
    ret2 = re.match(r'^[\s\S]*<(?P<p1>\w*)>[\s\S]*<(?P<p2>\w*)>[\s\S]*</(?P=p2)>[\s\S]*</(?P=p1)>[\s\S]*', data)
    if ret1:
        print(ret1.group())
    print()
    if ret2:
        print(ret2.group())


if __name__ == '__main__':
    main()