

import turtle
# import time
def drawSnake(rad,angle,len,neckrad):
    for i in range(len):
        turtle.circle(rad,angle)
        turtle.circle(-rad,angle)

    turtle.circle(rad,angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)



def main():
    turtle.setup(1300,800,0,0)
    pythonsize=30
    turtle.pensize(pythonsize)
    turtle.seth(-30)
    colors = ["blue", "yellow", "red"]
    for i in range(len(colors)):
        turtle.pencolor(colors[i])
        drawSnake(20,80,10,pythonsize/2)

main()

# time.sleep(55)