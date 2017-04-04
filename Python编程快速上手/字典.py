# 字典和结构化数据
# 像列表一样,"字典" 是许多值的集合, 但不像列表的下标, 字典的索引可以使用许多不同数据类型, 不只是整数.
# 字典的索引被称为 "键", 键以其关联的值称为 "键值" 对
# 字典的输入带花括号{}

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'load'}
# 这将一个字典赋给 myCat 变量. 这个字典的键是冒号前面的字串 'size', 'color', 'disposition'.键值相对应的值是 'fat', 'gray', 'load'
print(myCat['color'])  # gray
# 可以通过它们的键来访问键值
# 字典也可以使用整数值作为键

spam = {12345: '中国消防权益维护协会', 67890: '中国共产党人民基会'}
print(spam[12345])  # 中国消防权益维护协会

# 字典与列表
# 字典中的表项是不排序的, 键值对输入的顺序并不重要

# key(), values(), items()方法
# 分别对应返回字典的键, 值, 和键值对

for i in myCat.keys():
    print(i, end=', ')  # size, color, disposition,
print()

for i in myCat.values():
    print(i, end=', ')  # fat, gray, load,
print()

for i in myCat.items():
    print(i, end=', ')  # ('size', 'fat'), ('color', 'gray'), ('disposition', 'load'),
print()
# 多重赋值技巧

# myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'load'}

for k, v in myCat.items():
    print('Key: ' + k + ' Value: ' + str(v))

# 检查字典中是否存在键或值  in , not in

print('size' in myCat)  # True
print('size' in myCat.keys())
print('size' in myCat.values())  # False

# 在访问一个键的值之前, 检查该键是否存在字典中, 这很麻烦 . 因为你要在 in 和 not in 的基础上再增加一些代码来增加键值
# 我们可以使用 get() 方法来直接达到目的: 要取得其值的键, 以及如果该键不存在时, 返回备用值

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')  # I am bringing 2 cups.
print('I am bringing ' + str(picnicItems.get('egg', 0)) + ' eggs')  # I am bringing 0 eggs
print(picnicItems)  # {'apples': 5, 'cups': 2}
# 可以看到, 'egg' 的值并未被添加到 picnicItems 中

# setdefault() 方法

# 为字典中的某个键设置一个默认值. 如果该键不存在, 则将默认值赋给该键.
# 查看 setdefault() 源码
# def setdefault(self, k, d=None):  # real signature unknown; restored from __doc__
#     """ D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D """
#     pass

# 方法的第一个参数是要检查的键, 第二个参数, 是



