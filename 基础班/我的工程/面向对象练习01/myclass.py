#学习定义class的语法

class Person:

    def __init__(self):
        self.__name=""
        self.__age=0

    def setname(self,new_name):
        self.__name=new_name

    def setage(self,new_age):
        self.__age=new_age

    def getname(self):
        return self.__name

    def getage(self):
        return self.__age

    def __del__(self):
        print("{}对象已被销毁！".format(self.__name))

    def __str__(self):
        return "\n我是一个人，名字叫： {} \n".format(self.__name)
p1=Person()
p1.setname("SunShine")
p1.setage(25)
print("\n第一个人\n姓名：{}，年龄：{}".format(p1.getname(),p1.getage()))
p2=Person()
p2.setname('tom')
p2.setage('20')
if p2.getname()=='' or p2.getage()==0:
    print("没有设置姓名或年龄！")
else:
    print("\n第二个人\n姓名：{}，年龄：{}".format(p2.getname(),p2.getage()))

print(p1)
print(p2)
