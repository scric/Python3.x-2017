import turtle
# import time

# 绘制等边三角形
# 法一 直接绘图法：

# t=turtle.Pen()
# len=60
# angle=120

# t.fd(len)
# t.seth(angle)
# t.fd(len)
# t.seth(-angle)
# t.fd(len)

# 法二 参数构造法

# def drawET(len,angle):
#   turtle.fd(len)
#   turtle.seth(angle)
#   turtle.fd(len)
#   turtle.seth(2*angle)
#   turtle.fd(len)
#
# def main():
#     drawET(120,120)
#
# main()

# 法三，改进版

def drawET2(len,angle):
    for i in range(3):
        turtle.seth(i*angle)
        turtle.fd(len)

def main():
    drawET2(120,120)

main()
# time.sleep(55)




