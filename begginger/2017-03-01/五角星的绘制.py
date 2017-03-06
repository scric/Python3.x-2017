from turtle import *
fillcolor("blue")
begin_fill()
while True:
    forward(400)
    right(100)
    if abs(pos()) <1:
        break
end_fill()
done()


#为什么会出现警告

