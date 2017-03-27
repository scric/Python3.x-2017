import random

def ranColor():
 setcolor=['A','B','C','D','E','F',1,2,3,4,5,6,7,8,9,0]
 for i in range(3):
  color=random.sample(setcolor,6)
  a="#"
  for j in color:
    a=a+str(j)
 return a