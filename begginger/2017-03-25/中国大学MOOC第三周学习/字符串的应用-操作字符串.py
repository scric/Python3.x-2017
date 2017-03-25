# 讲解如何操作字符串


day = "25"
month = "Mar"
weekday = "星期六"
print(month+day+"是"+weekday)  # +号表连接
# 三月25是星期六
print(month*3)  # *号表重复
# 三月三月三月

days = month+day+"是"+weekday  # 创建一个新的变量,并给它赋值为 "Mar25是星期六"
print(days[6])     # <string>[] 表索引. 需要注意的是下标是从0开始的 ,这句话的意思是输出字符串中第6个字符(从0开始数)
# 星

print(len(days))  # len() 用来计算字符串长度,注意是长度
# 9

print(days[6:len(days)])  # <string>[a:b] 输出a-b间的字符串
# 星期六

print(days.upper())  # 字符串中字母大写
# MAR25是星期六
# 是不是也可以像<string>[a:b] 一样输出a-b间的字母大写字符串?
# print(days.upper[1:2])  # TypeError: 'builtin_function_or_method' object is not subscriptable
# 那么如何实现呢?

print(days.lower())  # 字符串中字母小写
# mar25是星期六

print(days.strip('a'))  # 为什么结果还是没有变?
# Mar25是星期六

a = "我很帅啊123abs"
print(a.strip('123'))
# 我很帅啊123abs
b = "123abs"
print(b.strip('123'))
# abs
print(b.strip('abs'))
# 123

# 所以能看出来是中文字符惹的祸.那么如何修正呢?如果一定要中文字符呢?

print(days.split("25"))  # 按指定字符分割字符串为数组
# ['Mar', '是星期六']

print("-".join(days))
# M-a-r-2-5-是-星-期-六
# 怎么不是 按 'Mar' '25' '是' '星期六' 来连接的?

rel = ['Mar', '25', '是', '星期六']
print(type(rel))
# <class 'list'>
print("-".join(rel))
# Mar-25-是-星期六

rel1 = 'Mar' + '25' + '是' + '星期六'
print(type(rel1))
# <class 'str'>
print("+".join(rel1))
# M+a+r+2+5+是+星+期+六

# 懂了吗?

print(days.find('星'))  # 搜索指定的字符串
# 6
print(days.find("25"))
# 3
print(days.find("Mar"))
# 0
print(days.find("六"))
# 8
print(days[6:8])
# 星期
print(days[6:len(days)])
# 星期六
print(days[days.find("星"):days.find("六")])
# 星期

# 通过上面的结果你能得出什么结论吗?试着总结一下.

print(days.replace("25", "32"))  # 字符串替换
# 语法 : <string>.replace("old","new",max)  max指替换多少个.max是可选参数
# Mar32是星期六









