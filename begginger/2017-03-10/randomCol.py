import random
# import math
def ranColor():
 setcolor=['A','B','C','D','E','F',1,2,3,4,5,6,7,8,9,0]
 for i in range(3):
  color=random.sample(setcolor,6)
  a="#"
  for j in color:
    a=a+str(j)
 return a

# def randomColor():
#     colorStr=math.floor(math.random()*0xFFFFFF).toString(16).toUpperCase()
#     return "#"+"000000".substring(0,6-corStr)+colorStr

