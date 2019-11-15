# 单例练习，让类创建的对象，在系统中只有唯一的一个实例。
# 请比较老师写的单例播放器程序！！！


class MusicPlayer:
    __instance = None         # 定义为类的私有属性！！！
    __init_flag = False       # 定义为类的私有属性！！！

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance=super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if self.__init_flag==True:
            return
        print("现在在这里运行初始化播放器的所有代码！")
        self.__init_flag = True


player1 = MusicPlayer()
print(id(player1))

# MusicPlayer.__instance = None      外部不能修改类属性！！！
# MusicPlayer.__init_flag = False    外部不能修改类属性！！！

player2 = MusicPlayer()
print(id(player2))

# MusicPlayer.__instance = None      外部不能修改类属性！！！
# MusicPlayer.__init_flag = False    外部不能修改类属性！！！


player3=MusicPlayer()
print(id(player3))
