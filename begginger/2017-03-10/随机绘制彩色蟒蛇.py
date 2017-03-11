import random
import turtle
import randomCol

# 随机生成颜色的代码块
# setcolor=['A','B','C','D','E','F',1,2,3,4,5,6,7,8,9,0]
# for i in range(2):
#     color=random.sample(setcolor,6)
#     a="#"
#     for j in color:
#         a=a+str(j)

# print(a)

#    setcolor = ['A', 'B', 'C', 'D', 'E', 'F', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# # 先选取好颜色
#    for i in range(len):
#        a = "#"
#        color = random.sample(setcolor, 6)
#        for j in color:
#             a = a + str(j)

def drawSnake(rad,angle,len,neckrad):
    # setcolor = ['A', 'B', 'C', 'D', 'E', 'F', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    for i in range(len):
      # a = "#"
      # color= random.sample(setcolor, 6)
      # for j in color:
      #   a = a + str(j)
      turtle.pencolor(randomCol.ranColor())
      turtle.circle(rad,angle) # circle() ，画圆：rad描述轨迹半径位置，angle为推挤沿圆形爬行的弧度值。
      turtle.circle(-rad, angle)
    turtle.circle(angle / 2, rad)
    turtle.fd(rad) # fd()表示轨迹要运动的距离
    turtle.circle(neckrad+1,180)
    turtle.fd(rad*2/3)

def main():
    turtle.setup(1300,800,0,0)
    # setup()用于启动一个图形窗口，参数分别是（width,height,startX,startY）
    pythonsize = 30
    turtle.pensize(pythonsize) # pensize()表示运动轨迹的宽度
    turtle.seth(-30) # 表示启动时轨迹要运动的方向，参数是角度值
    drawSnake(20,80,8,pythonsize/2)

# 运行程序
main()
turtle.done()

