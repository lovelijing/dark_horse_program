# 类的类属性、静态函数、类函数和成员函数练习
class Game:

    __top_scop=0

    def __init__(self,player_name):
        self.player_name=player_name

    @staticmethod
    def show_game_help():
        print("帮助信息：让僵尸进入大门！")

    @classmethod
    def show_top_scop(cls):
        print(f"历史最高分为：{Game.__top_scop}")

    def start_game(self):
        print(f"{self.player_name}游戏开始啦......")


Game.show_game_help()

Game.show_top_scop()

player1=Game("小明")

player1.start_game()