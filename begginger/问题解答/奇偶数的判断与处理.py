# 奇偶数的判断与处理

# 从键盘输入一个整数(正数.负数,0) ,判断其奇偶性, 如果是奇数, 输出其立方值. 如果是偶数, 则输出其绝对值的平方根 .

import math  # 导入math库

num = eval(input("请输入一个整数:"))  # 获得从键盘输入的值, eval()是将输入的字符串转换为数值

# 判断语句
if num % 2 == 0:  # 判断是否为偶数 ,如果是, 则执行下一条语句, 即 if num > 0: .如果不是偶数, 则执行与它对齐的 else 语句
    if num > 0:   # 在 num 是 偶数的情况下 进行判断 ; 如果 num 大于0 ,则执行下一条语句, 也就是 print 语句 .否则执行 else 语句
        print(math.sqrt(num))   # sqrt() 语句是求 num 的平方根函数 .
    else:
        print(math.sqrt(-num))
else:
    print(num * num * num)
