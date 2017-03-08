# TempConvert.py
# val = input("请输入带温度表示符号的温度值(例如: 32C): ")
# if val[-1] in['C','c']:
#      f = 1.8 * float(val[0:-1]) + 32
#      print("转换后的温度为: %.2fF"%f)
# elif val[-1] in['F','f']:   #[]中可添加其他符号。比如如果想添加 a 或 A ，则只需在括号中添加 'a','A' 即可。
#      c = (float(val[0:-1]) - 32) / 1.8
#      print("转换后的温度为: %.2fC"%c)
# else:
#     print("输入有误")

#注意：if 和 elif 还有 if之间要注意缩进。否则会出现 invalid syntax（语法错误）

# 改进版

val = input("请输入带温度表示符号的温度值(例如: 32C): ")
if val[-1] in['C','c']:
     f = 1.8 * eval(val[0:-1]) + 32
     print("转换后的温度为: %.2fF"%f)
elif val[-1] in['F','f']:   # []中可添加其他符号。比如如果想添加 a 或 A ，则只需在括号中添加 'a','A' 即可。
     c = (eval(val[0:-1]) - 32) / 1.8
     print("转换后的温度为: %.2fC"%c)
else:
    print("输入有误")

# eval(str [,globals [,locals]]) 函数将字符串 str 当成有效 Python 表达式来求值, 并返回计算结果。