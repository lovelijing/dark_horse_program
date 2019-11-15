

def mul_table():
    """打印九九乘法表

    """
    row = 9
    i = 1
    while i <= row:
        col = 1
        while col <= i:
            print("{}*{}={}".format(col,i,col*i),end="\t")
            col = col+1
        print("")
        i = i+1
