# 使用class 定义类

class Athlete:
    def __init__(self,a_name,a_dob=None,a_times=[]):
     self.name=a_name
     self.dob=a_dob
     self.times=a_times

# 添加数据
# sarah=Athlete('Sarah Sweeney','2002-6-17',['2:58','2.58','1.56'])
# james=Athlete('James Jones')

# print(type(sarah))
# print(type(james))

# 存储在不同的内存地址上
# print(sarah) # <__main__.Athlete object at 0x000000000290E828>
# print(james) # <__main__.Athlete object at 0x000000000290E898>


# print(sarah.name)
# print(james.name)
# print(sarah.times)
# print(james.dob)  # None
# print(james.times) # []

'''
定义一个新方法，来返回最快的三个时间。
'''

  def top3(self):
      return

