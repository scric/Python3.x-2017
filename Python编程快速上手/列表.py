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
print(size, color, disposition, sep=',')
