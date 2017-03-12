# 介绍turtle库里circle()的使用

import turtle

# circle(rad,angle)
# rad 控制的是轨迹半径
# angle 控制的是轨迹沿圆心运动的弧度


# T1  简单认识
for i in range(1):  # range() ：迭代一个数字序列。在这里指运行下列代码几次
    turtle.circle(80,120)    # 轨迹半径为80，弧度为120

# T1 的圆心在轨迹的哪一侧？轨迹半径是多少？

# # T2   range 的使用
# for i in range(2):   # 运行下列代码2次
#     turtle.circle(80,120)

# #  T2 的弧度是多少？半径是多少？


# # T3 rad的使用
# for i in range(1):
#     turtle.circle(-80, 120)

# T3 的圆心在哪里？它的圆心在半径的哪一侧？


turtle.done()