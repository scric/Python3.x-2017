# draw star of David
# 来自于慕课网
# 六芒星的绘制 法 三
from turtle import *
lenofside = 20

for x in range(12):
    if x % 2 == 0:
        left(60)
    else:
        right(2 * 60)
    fd(lenofside)

for x in range(6):
    fd(lenofside)
    right(60)
done()