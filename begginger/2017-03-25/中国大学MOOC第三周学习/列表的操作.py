# 列表的操作.

listOne = ["red", "blue", "#qwe", 123, "abc"]

print(type(listOne))  # <class 'list'>
print(listOne)  # ['red', 'blue', '#qwe', 123, 'abc']

listOne.append("123")  # <list>.append(x) , 将元素x增加到列表的最后
print(listOne)
# ['red', 'blue', '#qwe', 123, 'abc', '123']
# 如果直接print(listOne.append("123")) 会输出什么?为什么
# 如果想在任意位置插入一个新元素,又该如何做呢?

listOne.insert(2, "234")  # <list>.insert<i,x> ,将元素x插入到索引为i处
print(listOne)
# ['red', 'blue', '234', '#qwe', 123, 'abc', '123']

# 删除呢?
# listOne.remove(2)
# print(listOne)  # ValueError: list.remove(x): x not in list

listOne.remove(123)  # <list>.remove(x) 删除列表中第一次出现的x元素
print(listOne)
# ['red', 'blue', '234', '#qwe', 'abc', '123']

listOne.pop(0)  # <list>.pop(i) ,删除列表位置为i的元素
print(listOne)
# ['blue', '234', '#qwe', 123, 'abc', '123']

listOne.sort()  # 将列表元素排序
print(listOne)
# ['#qwe', '123', '234', 'abc', 'blue']

# 你发现什么了吗?？ 整型元素123 没了,只剩下字符串元素'123'

listOne.reverse()  # 将列表元素反序
print(listOne)
# ['blue', 'abc', '234', '123', '#qwe']

print(listOne.index(123))  # 返回第一次出现元素x的索引值
# ValueError: 123 is not in list
# 为什么? 再详细看下listOne 有什么变化

print(listOne.count('123'))  # 返回元素x在列表中的数量








