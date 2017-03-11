
import getCoachData
import os
os.chdir('D:/Python/python-git/begginger/2017-03-11/Program')


# 能否用循环替代下列的代码？
james=getCoachData.get_coach_data2('james.txt')
julie=getCoachData.get_coach_data2('julie.txt')
mikey=getCoachData.get_coach_data2('mikey.txt')
sarah=getCoachData.get_coach_data2('sarah.txt')


# 用循环替代掉下列代码
# print(sarah['Name']+"'s fastest times are: "+ sarah['Times'])
# print(james['Name']+"'s fastest times are: "+ james['Times'])
# print(sarah['Name']+"'s fastest times are: "+ sarah['Times'])
# print(julie['Name']+"'s fastest times are: "+ julie['Times'])

# 创建一个列表
name=[james,julie,mikey,sarah]

# print(name)
# print(type(name))

for i in name:
    # i=getCoachData.get_coach_data2('i.txt')
    print(i['Name']+"'s fastest times are: "+i['Times'])

#  'NoneType' object is not iterable