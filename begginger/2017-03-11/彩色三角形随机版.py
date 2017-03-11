import turtle
import randomCol

# 谢谢Q群 569990730 Radial 的贡献
# 代码大部分来自于他

# import random
#
# def ranColor():
#  setcolor=['A','B','C','D','E','F',1,2,3,4,5,6,7,8,9,0]
#  for i in range(3):
#   color=random.sample(setcolor,6)
#   a="#"
#   for j in color:
#     a=a+str(j)
#  return a

colors=["red","blue","yellow","green"]
turtle.speed("fastest")
turtle.bgcolor(randomCol.ranColor())

sides=3

for x in range(100):
   # turtle.pencolor(colors[x%sides])
   turtle.pencolor(randomCol.ranColor())
   turtle.forward(x*3/sides+x)
   turtle.left(360/sides+1)
   turtle.width(x*sides/200)

turtle.done()