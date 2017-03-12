import turtle
import random
# import randomCol

# 谢谢Q群 569990730 Radial 的贡献
# 代码大部分来自于他


def ranColor():
   # 该模块使用16进制 来随机产生颜色
 setcolor=['A','B','C','D','E','F',1,2,3,4,5,6,7,8,9,0]
 for i in range(3):
  color=random.sample(setcolor,6)
  a="#"
  for j in color:
    a=a+str(j)
 return a


turtle.speed("fastest")  # 更改画笔速度，参数有'fast'，'slow'...
turtle.bgcolor(ranColor())   # 随机更改背景颜色，默认为白色

# colors=["red","blue","yellow","green"]  # 颜色模板，从其中选择颜色

sides=3

for x in range(100):
   # turtle.pencolor(colors[x%sides])
   # turtle.pencolor(randomCol.ranColor())
   turtle.pencolor(ranColor())
   turtle.forward(x*3/sides+x)
   turtle.left(360/sides+1)
   turtle.width(x*sides/200)

turtle.done()