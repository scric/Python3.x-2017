import os
import sanitize
os.chdir('D:/Python/python-git/begginger/2017-03-11/Program')

# 使用类处理数据


class Athlete:

 def __init__(self,a_name, a_dob=None, a_times=[]):
     self.name=a_name
     self.dob=a_dob
     self.times=a_times

 def top3(self):
   return (sorted(set([sanitize.sanitize(t) for t in self.times]))[0:3]) # 记得self


def get_coach_data3(filename):
  try:
      with open(filename)as f:
          data = f.readline()
      templ = data.strip().split(',')
      return Athlete(templ.pop(0), templ.pop(0), templ) # 删除字典创建代码，替换成Athlete对象创建代码

  except IOError as ioerr:
      print('File error:'+str(ioerr))
      return (None)

# 获取数据
james = get_coach_data3('james.txt')
julie = get_coach_data3('julie.txt')
mikey = get_coach_data3('mikey.txt')
sarah = get_coach_data3('sarah.txt')
# 输出数据
print(james.name+"'s fastest times are: " + str(james.top3()))
print(julie.name+"'s fastest times are: " + str(julie.top3()))
print(mikey.name+"'s fastest times are: " + str(mikey.top3()))
print(james.name+"'s fastest times are: " + str(james.top3()))