# 如何画出六芒星？

'''

画图前应该想到什么呢？

六芒星的基本性质
+ 角度
+ 边长

更重要的是，如何一笔画出来。

不如先在纸上试试。
'''

import turtle
# import time

# 设置画笔
t=turtle.Pen()
# 设置参数
len=60
angle=120

# 画图开始
t.fd(len)
t.seth(angle)
t.fd(len)
t.seth(2*angle)
t.fd(len/3)
t.seth(0)
t.fd(2*len/3)
t.seth(2*angle)
t.fd(len)
t.seth(120)
t.fd(len)
t.seth(0)
t.fd(len/3)
t.seth(2*angle)
t.fd(2*len/3)


# time.sleep(5)

# 如何再对代码进行改进呢？？