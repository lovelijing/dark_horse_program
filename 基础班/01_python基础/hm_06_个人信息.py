"""

- 姓名：小明
- 年龄：18 岁
- 性别：是男生
- 身高：1.75 米
- 体重：75.0 公斤

"""
fgf='-'*10
print('\n'+fgf+'\n 个人信息\n'+fgf)
print()

name="小明"
age=18
gender=True
hight=1.75
weigt=75.0

print(type(name))
print(type(age))
print(type(gender))
print(type(hight))
print(type(weigt))
print()
print(name)
print(age)
print(gender)
print(hight)
print(weigt)

# 试探一下complex类型
s=1+7j
print(type(s))
print(s*(3+9j))