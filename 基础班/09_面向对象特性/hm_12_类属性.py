class Tool(object):

    # 使用赋值语句定义类属性，记录所有工具对象的数量
    __count = 0

    def __init__(self, name):
        self.name = name

        # 让类属性的值+1
        Tool.__count += 1

    def __del__(self):
        Tool.__count -= 1

    @classmethod
    def show_tools_count(cls):
        print(f"共有{cls.__count}个工具。")


# 1. 创建工具对象
tool1 = Tool("斧头")
tool2 = Tool("榔头")
tool3 = Tool("水桶")
tool3.__del__()
# 2. 输出工具对象的总数
print(dir(Tool))
Tool.show_tools_count()
