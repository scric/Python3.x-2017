print('Test One')
print('空字典的代码是怎样的 ?  ' + str('dict = {}   ') + str(type(dict)))  # <class 'dict'>
print()
print('Test Two')
print('一个字典包含键 fow 和值 42 , 看起来是怎么样的？  ' + str('dict = {"fow": 42}'))
print()
print('Test Three')
print("如果 spam 是 {'bar':100}, 你试图访问 spam['foo'], 会发生什么?")
try:
    spam = {'bar': 100}
    print(spam['foo'])  # KeyError: 'foo'
except KeyError as kerr:
    print("会报出错误 : " + "  KeyError: 'foo'")
print()
print('Test Four')
print("字典和列表的主要区别是什么. ")
print("字典不是只能使用整数下标, 而是可以用各种数据类型作为键; 它也不像列表, 只包含一系列有序的值.")
print()
print('Test Five')
print("如果一个字典保存在span中, 表达式 'cat' in spam 和 'cat' in spam.keys() 之间的区别是什么 ")
span = {'cat': 2}
print('cat' in span)  # True
print('cat' in span.keys())  # True
print('cat' in span.values())  # False
print("我们可以看到 'cat' in spam 是 'cat' in spam.keys() 的简写版本 ")
print(" 这种情况总是对的 : 如果想要检查一个值是否为字典中的键, 就可以使用关键字 in (Or not in ), 作用该字典本身")

print()
print("Test Six")
print("什么模块和函数可以用于 '漂亮打印' 字典值")
print(" pprint 模块 和 pprint() 函数可以用于漂亮打印")
