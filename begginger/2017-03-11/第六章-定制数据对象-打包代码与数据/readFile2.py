import sanitize
import getCoachData
import os
os.chdir('D:/Python/python-git/begginger/2017-03-11/Program')

sarah=getCoachData.get_coach_data('sarah.txt')

# 使用字典关联

# 创建字典

sarah_data={} # 创建一个空字典
sarah_data['Name']=sarah.pop(0)
sarah_data['DOB']=sarah.pop(0)
sarah_data['Time']=sarah

print(sarah_data['Name']+"'s fastrst times are:"+str(sorted(set([sanitize.sanitize(t) for t in sarah_data['Time']]))[0:3]))

#  在 get_coach_data() 函数中，我们先读取数据再创建字典，为什么不一次性完成呢？

# 修改 get_coach_data() 函数 或者在 getCoachData 模块中再添加一个函数为 get_coach_data2()

