import turtle
import randomCol

colors=["red","blue","yellow","green"]
# turtle.speed("fastest")
turtle.bgcolor(randomCol.ranColor())

sides=3

for x in range(100):
   turtle.pencolor(colors[x%sides])
   turtle.forward(x*3/sides+x)
   turtle.left(360/sides+1)
   turtle.width(x*sides/200)

turtle.done()