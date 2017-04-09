# 计算一个字符串中每个字符出现的次数.

# 定义一个字符串 string
string = 'It was a bright cold day in April , and the clocks were striking thirteen.'
# 定义一个空字典
count = {}

for words in string:  # 循环迭代 string 字符串中的每个字符串
    count.setdefault(words, 0)  # setdefault() 方法的调用确保了键存在于 count 字典中(默认值为0)
    count[words] += 1  # 为字符 + 1
print(count)

# 修改
# "漂亮打印"一个字典的字

import pprint
# 键排过序
pprint.pprint(count)
# 将漂亮打印的文本作为字符串, 而不是显示在屏幕上.

print(type(pprint.pformat(count)))  # <class 'str'>
print(pprint.pformat(count))

