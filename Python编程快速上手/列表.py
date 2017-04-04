# 列表

spam = ['dog', 'cat', 'pig', 'rat', 1]

print(spam)  # ['dog', 'cat', 'pig', 'rat' , 1]
print(type(spam))  # <class 'list'>

print(spam[0])  # dog
print(type(spam[0]))  # <class 'str'>

# 知道列表的性质了吗?
# spam 变量 只被赋予一个值 : 列表值. 所以在打印 spam 变量的类型时, 输出了 <class 'list'>
# 但是 列表值本身包含多个值, 所以当我们 通过 [] 提取值时, 打印 spam[0] 变量的类型时, 输出了<class 'str'>

# 我们可以使用 len() 函数获取列表的长度
print(spam[len(spam)-1])  # 1
print(type(spam[len(spam)-1]))  # <class 'int'>

# 用下标改变列表中的值

spam[1] = 'rabbit'
print(spam)  # ['dog', 'rabbit', 'pig', 'rat', 1]

spam[-1] = 'elephant'
print(spam)  # ['dog', 'rabbit', 'pig', 'rat', 'elephant']

# 列表连接和复制

humanbing = ['man','woman']
animal = humanbing + spam  # 可以使用 + 操作符来连接两个列表, 得到一个新列表
print(animal)  # ['man', 'woman', 'dog', 'rabbit', 'pig', 'rat', 'elephant']

animal *= 2  # 实现列表的复制
print(animal)
# ['man', 'woman', 'dog', 'rabbit', 'pig', 'rat', 'elephant', 'man', 'woman', 'dog', 'rabbit', 'pig', 'rat', 'elephant']

# 用 del 语句从列表中删除值
del spam[2]  # 删除下标为 2 的值
print(spam)  # ['dog', 'rabbit', 'rat', 'elephant']

# 多重赋值技巧

cat = ['fat', 'black', 'load']
size, color, disposition = cat
print(size, color, disposition, sep=',')  # fat,black,load

# in 和 not in 操作符
# 利用 in 和 not in 操作符 , 可以确定一个值是否在列表中; 同样 , 它们两个用于连接两个值

# spam = ['dog', 'rabbit', 'rat', 'elephant']

print('cat' in spam)  # False
print('dog' in spam)  # True

print('cat' not in spam)  # True

# 利用 index() 方法在列表中查找值(返回值的下标)

print(spam.index('dog'))  # 0
print(spam.index('rat'))  #

# 用 append() 和 insert() 方法在列表中添加值

print(spam)  # ['dog', 'rabbit', 'rat', 'elephant']
spam.append('cat')
spam.append('moose')  # 注意, 以上两个语句都没有赋给新值
print(spam)  # ['dog', 'rabbit', 'rat', 'elephant', 'cat', 'moose']
# 我们可以看到, 参数被添加到列表末尾,
# 而且列表被 "当场" 修改了, 它并没有将旧值赋给新值, 实际上, append() 的返回值是 None

# 如果你想在列表中任意位置插入一个值, 应该调用 insert() 方法
spam.insert(2, 'lion')
print(spam)  # ['dog', 'rabbit', 'lion', 'rat', 'elephant', 'cat', 'moose']
# 需要注意的是 , 这两个方法都是列表方法, 只能在列表上调用, 不能在其他值上调用

# 用 remove() 方法从列表中删除值
print(spam)  # ['dog', 'rabbit', 'lion', 'rat', 'elephant', 'cat', 'moose']

spam.remove('lion')
# 给 remove() 方法传入一个值, 它将从被调用的列表中删除. 不要求给出下标
print(spam)  # ['dog', 'rabbit', 'rat', 'elephant', 'cat', 'moose']
# 需要注意的是它只会删除重复值第一次出现的值.
spam.append('cat')
print(spam)  # ['dog', 'rabbit', 'rat', 'elephant', 'cat', 'moose', 'cat']
spam.remove('cat')
print(spam)  # ['dog', 'rabbit', 'rat', 'elephant', 'moose', 'cat']

# 如果想全部删除怎么办?

# 字符串和元组
# 字符串和列表实际上是很相似的, 只是字符串是单个文本字符的列表, 和它是不可变的数据类型, 它不能被修改.

eggs = [1, 2, 3]
eggs = [4, 5, 6]
print(eggs)  # [4, 5, 6]
# 这里 eggs 中的列表值并没有改变, 而是整个新的不同的列表值([4, 5, 6]), 覆写了老的列表值
# 我们可以这样认为, t = [1, 2, 3] , eggs = t ; f = [4, 5, 6] , eggs = f . 实际上 t , f 就是它的列表值, 其包含的列表数并未改变.
# 如果你要修改 eggs 中原来的列表, 让它包含[4, 5, 6], 你就要将列表值包含的列表数修改掉, 使用 del 和 append 来删除和添加
# 这样, eggs 最后的列表值与它开始的列表值是一样的, 只是这个列表被改变了, 而不是被覆写

# 元组
# 元组输入时用圆括号() , 而不是用方括号[], 元组与列表的主要叙别在, 元组和字符串一样, 是不可变的. 元组不能让它们的值被修改, 添加或删除 .
# 如果元组中只有一个值, 可以在括号内该值的后面跟上一个逗号表明是元组.

# 需要注意的是:
# 变量包含对列表值的引用, 而不是列表值本身.(列表)
# 对于字符串和整数值, 变量就包含了字符串或整数值. 在变量必须保存可变数据类型的值时, 例如列表或字典, Python 就使用引用
# 对于不可变的数据类型的值, 例如字符串, 整型或元组 , Python 就保存值本身.

# copy 模块
# 如果不希望函数修改传入的列表或字典影响原来的列表或字典, 我们应该使用 copy 模块 .

# copy.copy() , 可以用来复制列表或字典这样的可变值, 而不只是复制引用.

import copy

copyee = ['A', 'B', 'C', 'D']
cheese = copy.copy(copyee)  # 浅拷贝
cheese[1] = 42
print('copyee: ' + str(copyee))  # copyee: ['A', 'B', 'C', 'D']
print('cheese: ' + str(cheese))  # cheese: ['A', 42, 'C', 'D']

# 我们可以看到, 尽管你将 42 赋给 下标 1 时, 只有 cheese 中的列表被改变. 因为现在 copyee 和 cheese 分别指向了独立的列表, 它们的引用ID 数字不再一样

# 如果要复制的列表中包含了列表, 那就使用 copy.deepcopy() 函数来代替(深拷贝)


