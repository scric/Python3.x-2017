# draw star of David
import turtle
import math

turtle.penup()
turtle.seth(30)
vertex = []
for i in range(6):
    turtle.fd(200)
    vertex.append(turtle.pos())
    turtle.left(60)
print(vertex)

len_of_side = math.sqrt((vertex[0][0] - vertex[2][0]) ** 2 + (vertex[0][1] - vertex[2][1]) ** 2)

turtle.goto(vertex[4])
turtle.pendown()
for x in range(0, 6, 2):
    turtle.seth(turtle.towards(vertex[x]))
    turtle.fd(len_of_side)

turtle.penup()
turtle.goto(vertex[5])
turtle.pendown()
for x in range(1, 6, 2):
    turtle.seth(turtle.towards(vertex[x]))
    turtle.fd(len_of_side)

turtle.done()