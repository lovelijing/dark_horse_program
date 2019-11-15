class HouseItem:
    def __init__(self,name,area):
        self.name=name
        self.area=area

    def __str__(self):
        return f"家具[{self.name}]占地面积：{self.area:.2f}平方米"


class House:
    def __init__(self,house_type,area):
        self.house_type=house_type
        self.area=area
        self.free_area=area
        self.item_list=[]

    def __str__(self):
        return f"\n房子户型：{self.house_type}\n总面积:{self.area:.2f}\n"

    def AddItem(self,item):
        if self.free_area>=item.area:
            self.item_list.append(item)
            self.free_area=self.area-item.area
        else:
            print("家具面积太大，放不下了！")

    def ShowItem(self):
        print(f"\n家里共有家具{len(self.item_list)}件,它们是：")
        for item in  self.item_list:
            print(f"[{item.name}]占地：{item.area:.2f}平方米。")
        print(f"\n家里还剩面积：{self.free_area}平方米。")


bed=HouseItem("席梦思床",4)
chest=HouseItem("大衣柜",2)
table=HouseItem("餐桌",1.5)

my_home=House("两室一厅", 80)
my_home.AddItem(bed)
my_home.AddItem(chest)
my_home.AddItem(table)

print(my_home)
my_home.ShowItem()