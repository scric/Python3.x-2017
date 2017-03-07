# from turtle import *
import turtle
turtle.fillcolor("blue")
turtle.begin_fill()
while True:
    turtle.forward(400)
    turtle.right(100)
    if abs(turtle.pos()) <1:
        break
turtle.end_fill()
turtle.done()


#为什么会出现警告
# 可以通过

