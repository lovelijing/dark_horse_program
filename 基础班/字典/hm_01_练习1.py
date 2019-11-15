mydict = {"name": "小明"}
tempdict = {}
print(type(mydict))
print(type(tempdict))
print(mydict["name"])
mydict["age"] = 18

tempdict["hight"] = 1.75
tempdict["phone"] = '13595582167'
mydict.update(tempdict)

mydict["age"] = 15
# tempdict.pop("hight")
print(len(mydict))
# tempdict.clear()
print(tempdict)
print(mydict)

for k in mydict:
    print('{}--{}'.format(k,mydict[k]))

card_list=[
    mydict,
    {"name":"张三",
     "age":16,
     "hight": 1.7,
     "phone":"10086"}
]

for card_info in card_list:
    print(card_info)
