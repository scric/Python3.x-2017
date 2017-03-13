

import pickle
# import Athlete
import os
os.chdir('D:/Python/python-git/begginger/2017-03-11/Program')

from Athlete import AthleteList


def get_coach_data3(filename):
    try:
        with open(filename)as f:
            data = f.readline()
        templ = data.strip().split(',')
        return AthleteList(templ.pop(0), templ.pop(0), templ)  # 删除字典创建代码，替换成Athlete对象创建代码

    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return None


def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data3(each_file)
        all_athletes[ath.name] = ath    # 每个选手的名字作为字典的键， 值是AthleteList对象实例
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error(put_and_store):'+str(ioerr))
    return all_athletes


def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error(get_from_store):' + str(ioerr))
    return all_athletes

#  print(dir()) # 查看该函数的功能

# 测试

the_files = ['sarah.txt', 'james.txt', 'mikey.txt', 'julie.txt']  # 创建一个要处理的文件列表

data = put_to_store(the_files) # 调用put_to_store()函数将文件列表中的数据转化为一个字典

# print(data)

# 在2017-03-11的Program中我们可以看到athletes.pickle 的文件。
# 要访问这个数据，需要使用put_to_store(files_list)和get_from_store()函数放回的字典

# 使用数据字典中现有的数据来显示各个选手的名字和出生日期:

for each_athlete in data:
    print(data[each_athlete].name + ' ' + data[each_athlete].dob)

# 使用
