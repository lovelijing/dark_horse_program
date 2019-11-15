

def print_line(char,times):
    """打印单行分隔符
    :param char: 要打印的分隔符字符
    :param times: 打印的个数
    """
    print(char*times)


def  print_lines(char,times,lines):
    """打印lines行分隔符
    :param char: 要打印的分隔符字符
    :param times: 打印的个数
    :param lines: 打印的行数
    """
    i=0
    while i<lines:
        print_line(char,times)
        i = i + 1


print_lines("-",20,8)