# 基础知识一码过
# 输出 HelloWorld
print("HelloWorld")  # HelloWorld (运行以后的结果, 以后的格式均为这样, 同行注释结果, 另行解释)
# 在屏幕上打印出 "*"(双引号) 里的内容 ,即 HelloWorld . ""里的内容可任意修改, print() 功能就是将内容打印到屏幕上

# 输出表达式

print(2 + 2)  # 4
# 在屏幕上打印出 表达式的结果, 即 2+2 的值. + 号为操作符, 在这里的作用和数学上的意义相同
# 请问 print(8+8) 运行后会输出什么?
# print(8 + 8)
# print(2 * 2)

# 认识 "+" 操作符的另一个作用

print("Hello"+"World")  # HelloWorld
# "+" 号操作符的作用在这里为连接两个字符串, 将它们"无缝"打印在屏幕上

t = 2 + 2
print(t)  # 4
# 同上, t = 2 + 2 这个表达式的意思是 将 2+2 的值 赋值给 t , "=" (等号) 操作符的作用 就是将 右边的"值" 赋值给左边的 变量
# 请问print(2 * t) 运行后的结果是什么?
# print(2 * t)

# 再认识一下 * 号操作符的另一个作用

print(2*"Hello")  # HelloHello
# 将字符串重复 n 次 , 需要注意的是, 倍数需要是整数.

# 认识一下数据类型

print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>

print(type("Hello"))  # <class 'str'>
print(type('a'))  # <class 'str'>

# 在上面我们认识到了一个赋值语句, t = 2 + 2
# t 在这里作为一个变量, 用于存储一个值, 如果你的程序稍后将用到一个已求值的表达式, 就可以将它保存在一个变量中

a = 8  # 第一次存入一个值, 就说该变量(a) 被初始化了, 此后就可以在表达式使用它,

print(a + t)  # 12
# 与其他变量
print(a + 2)  # 10
# 与其他值
print(a)  # 8
# 我们发现 a 的值并没有改变, 我们可以这样改变它
a += 2   # a = a + 2 也是被允许的, 它的意思是 a + 2 的值被赋值给 a , 也就是说 旧值在操作后 被新值给替代掉了.
print(a)  # 10
# 我们可以发现 a 的值被改变了 .

# 变量名规范
# 你可以给变量名取任何名字, 只要它遵守下面三个规则
# 1) 只能是一个词(不能用空格隔开)
# 2) 只能包含字母, 数字, 和下划线(其他特殊符号都是不被允许的)
# 3) 不能以数字开头

# 变量名是区分大小写的 , 也就意味着 spam , Spam ,SPAM....是不同的变量, 变量用小写字母开头是 python 的惯例, 最好使用驼峰形式

spam = 2
Spam = 2
SPAM = 2
# 运行后没有报错信息.


# 函数应用

print("路飞才是世界上最帅的男人")  # 路飞才是世界上最帅的男人
# print() 函数将括号内的字符串显示在屏幕上

# name = input("请输入你的名字")  # 函数等待用户在键盘上输入一些文本, 并按下回车/ 这个函数求值为一个字符串, 即用户输入的文本
# 等号 将这个字符串赋给变量 name
# print(type(name))  # <class 'str'> 说明变量 name 被声明为字符串类型
# print(name)  # 张鑫. 打印出你输入的文本

# 可以更加有趣一点

# yourName = input("请输入你的名字(zhangxin):")  # 将在屏幕上打印出 "请输入你的名字:" ,后面接着输入你的文本
# print("你的名字是" + yourName)  # 你的名字是zhangxin

# len()函数
# print("The length of your name is : " + len(yourName))  # 该语句会报错,   TypeError: must be str, not int
# 虽然 print() 函数允许传入一个整型值或字符串, 但错误的根本不在这里, 而是你试图传递给 print() 的表达式
# 报错是因为, 只能用 + 操作符加两个整数, 或连接两个字符串
# 所以我们应该将 len(yourName) 转换为 字符串类型
# print("The length of your name is : " + str(len(yourName)))   # The length of your name is : 8
# len() 函数要求你传递一个字符串(或者包含字符串的变量) , 然后 len()函数会返回这个字符串中字符的个数
# 所以如果想连接一个整数和一个字符串, 在传递给 print , 就可以使用 str()函数传入一个整数值, 并求值为它的字符串形式 /


# 字符串下标和切片
'''字符串像列表一样, 使用下标和切片.
可以将字符串 "Hello world" 看成是一个列表, 字符串中的每个字符都是一个表项, 有相应的下标
'''
spam1 = 'Hello world'
print(spam1[0])
print(spam1[4])
print(spam1[-1])
print(spam1[0:5])  # 开始下标将被包含, 结束下标则不包含
print(spam1[:5])
# 需要注意的是, 字符串切片并没有修改原来的字符串.

# 字符串也可以用 in 和 not in 操作符

# 有用的字符串方法 upper(), lower(), isupper(), islower()
# spam1 = 'Hello world'
spam1 = spam1.upper()
print(spam1)  # HELLO WORLD
spam1 = spam1.lower()
print(spam1)  # hello world
# 懂怎么用了吧. 还是需要注意的是, 这些方法还是没有改变字符串本身, 之所以字符串改变是因为被赋了新值

print(spam1.islower())  # True
print(spam1.isupper())  # False
print('123456'.isupper())  # False
print('abs123456'.islower())  # True

# 还有其他的方法
'''
isalpha(), 如果字符串只包含字母, 并且非空
isalnum(), 如果字符串只包含字母和数字, 并且非空
isdecimal(), 如果字符串只包含数字字符, 并且非空
isspace(), 如果字符串只包含空格, 制表符和换行, 并且非空
istitle(), 如果字符串仅包含以大写字母, 后面都是小写字母的单词
以上都可以用于验证用户输入
'''
# 验证字符串的开头和结束 startswith() 和 endswith()
print('Hello world'.startswith('Hello'))  # True
print('Hello world'.endswith('world'))  # True

# join() 和 split()
# 如果有一个字符串列表, 需要将它们连接起来称为一个单独的字符串, 你可以使用 join

spam2 = ','.join(['cats', 'rats', 'bats'])
print(spam2)
spam2 = ' - '.join(['cats', 'rats', 'bats'])
print(spam2)  # cats - rats - bats
print(type(spam2))  # <class 'str'>
# 实际上可以把上面的代码改一下
spam2 = '````'.join(spam2)
print(spam2)  # 有点问题 . ..因为 spam2 的类型从字符串列表变成了字符串 . 表项从 'cats' 变成了 'c'
# 换个试试
spam3 = ['cats', 'dragon', 'house']
spam3 = '('.join(spam3)
print(spam3)  # cats(dragon(house

# split() 方法做的事情正好和 join() 方法相反. 它针对字符串而调用, 按照传入的字符来将字符串分割
spam3 = spam3.split('(')
print(spam3)  # ['cats', 'dragon', 'house']
# 默认情况下, 还是按空白字符分割
# 一个常见的用法, 按照换行符来分割多行的字符串

spam4 = '''
isalpha(), 如果字符串只包含字母, 并且非空
isalnum(), 如果字符串只包含字母和数字, 并且非空
isdecimal(), 如果字符串只包含数字字符, 并且非空
isspace(), 如果字符串只包含空格, 制表符和换行, 并且非空
istitle(), 如果字符串仅包含以大写字母, 后面都是小写字母的单词
以上都可以用于验证用户输入
'''
spam4 = spam4.split('\n')
print(spam4)

# 用 rjust(), ljust() 和 center() 方法对齐文本
#  rjust(), ljust() 方法调用它们的字符串的填充版本, 通过插入空格来对齐文本 . 这两个方法的第一个参数都是一个整数长度






