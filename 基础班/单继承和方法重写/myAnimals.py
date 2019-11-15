class Animal:

    def chi(self):
        print('吃---')

    def  he(self):
        print('喝---')

    def pao(self):
        print('跑---')

    def shui(self):
        print('睡---')


class Dog(Animal):

    def jiao(self):
        print('汪汪叫')


class XiaoTianQuan(Dog):

    def fei(self):
        print('我会飞。')

    def jiao(self):
        print('叫得像神一样...')
        super().jiao()
        print('#$%^*((())()')


class  Cat(Animal):

    def zhuaLaoShu(self):
        print('我是一只会抓老鼠的猫！')


xtq = XiaoTianQuan()
xtq.jiao()
xtq.chi()

tom = Cat()
tom.zhuaLaoShu()