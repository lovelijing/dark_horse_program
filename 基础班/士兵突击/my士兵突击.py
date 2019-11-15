class Qiang:
    def __init__(self, xinghao):
        self.xinghao = xinghao
        self.zidanshu = 0

    def __str__(self):
        return f'[{self.xinghao}]有{self.zidanshu}发子弹。'

    def shangzidan(self, num):
        self.zidanshu=num

    def kaiqing(self):
        self.zidanshu -= 1
        print(f'[{self.xinghao}]突突突......[{self.zidanshu}]')


class ShiBing:
    def __init__(self, name):
        self.name = name
        self.qiang = None

    def __str__(self):
        return f'我是士兵[{self. name}]'

    def kaihuo(self):
        if self.qiang is None:
            print(f'[{self.name}]还没有枪！')
            return
        if self.qiang.zidanshu == 0:
            self.qiang.shangzidan(50)
        print(f'冲啊......[{self.name}]')
        self.qiang.kaiqing()


if __name__=='__main__':
    ak47 = Qiang('AK47突击步枪')
    #ak47.shangzidan(50)
    #ak47.kaiqing()
    #print(ak47)
    xusanduo = ShiBing('许三多')
    print(xusanduo)
    xusanduo.qiang = ak47
    xusanduo.kaihuo()
