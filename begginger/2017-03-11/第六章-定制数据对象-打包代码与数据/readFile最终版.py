import os
os.chdir('D:/Python/python-git/begginger/2017-03-11/Program')


def sanitize(time_string):
    if '-'in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return time_string
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]


def get_coach_data3(filename):
    try:
        with open(filename)as f:
            data = f.readline()
        templ = data.strip().split(',')
        return AthleteList(templ.pop(0), templ.pop(0), templ)  # 删除字典创建代码，替换成Athlete对象创建代码

    except IOError as ioerr:
        print('File error:'+str(ioerr))
        return None

# 获取数据
james = get_coach_data3('james.txt')
julie = get_coach_data3('julie.txt')
mikey = get_coach_data3('mikey.txt')
sarah = get_coach_data3('sarah.txt')
# 输出数据
print(james.name+"'s fastest times are: " + str(james.top3()))
print(julie.name+"'s fastest times are: " + str(julie.top3()))
print(mikey.name+"'s fastest times are: " + str(mikey.top3()))
print(sarah.name+"'s fastest times are: " + str(sarah.top3()))