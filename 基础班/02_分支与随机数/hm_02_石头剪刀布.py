import random

computer=random.randint(1,3)
player=int(input("输入1石头、2剪刀、3布"))

d=["石头","剪刀","布"]

print(f"玩家出的是{d[player - 1]}，电脑出的是{d[computer - 1]}")

if((player==1 and computer==2)
            or(player==2 and computer==3)
            or(player==3 and computer==1)):
    print("玩家赢了！")
elif  player==computer:
        print("平局！")
else:
    print("电脑赢了！")
