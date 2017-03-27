# 六芒星的绘制 法四

# 谢谢Q群 569990730 ★味★ 的贡献
# 代码来自于他
import turtle
import math


t1 = turtle.Pen()
t2 = turtle.Pen()

def draw(len):

    for i in range(3):
        t1.fd(len)
        t1.left(120)
        t2.fd(len)
        t2.right(120)


def main():

    len = 100
    l = float(len) * math.sqrt(3) / 3
    turtle.setup(1300, 800, 0, 0)
    t2.up()
    t2.goto(0, l)
    t2.down()
    draw(len)

main()
turtle.done()


