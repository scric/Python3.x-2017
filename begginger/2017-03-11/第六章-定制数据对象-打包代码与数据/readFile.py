import sanitize
import getCoachData
import os
os.chdir('D:/Python/python-git/begginger/2017-03-11/Program')

sarah=getCoachData.get_coach_data('sarah.txt')  # 使用get_coach_data()函数将sarah的数据文件转化为一个列表，然后把它赋值给“sarah”变量

(sarah_name,saran_dob)=sarah.pop(0),sarah.pop(0) # pop()调用将删除并返回列表最前面的数据项。
print(sarah_name+"'s fastest times are:"+str(sorted(set([sanitize.sanitize(t) for t in sarah]))[0:3]))

'''
以上程序确实能正常工作，但必须指定并创建sarah的三个变量，以便表示哪个名字，
出生日期和计时数据与sarah关联。如果再增加代码来处理james等的数据，则需要多达12个变量

所以我们应该改进代码
'''

# 使用字典关联数据

