name_list=["张三","李四","王五"]

# 显示列表长度:
print(len(name_list))

# 获取列表中的元素：
print(name_list[0])

#  获取列表中元素的索引：
print(name_list.index("李四"))

# 向列表中增加数据的方法有以下三种：
name_list.append("赵六")
name_list.insert(2,"小明")
temp_list=["孙悟空","猪八戒","沙和尚"]
name_list.extend(temp_list)

print(name_list)

# 删除列表中的元素有以下三种方法：
name_list.remove("小明")
print(name_list)

# pop方法默认弹出列表最后一个元素
print(name_list.pop())
print(name_list)

# pop方法可以弹出指定序号的元素
print(name_list.pop(3))
print(name_list)

# clear方法可以清空列表
name_list.clear()
print(name_list)



