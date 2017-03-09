import os
import sanitize
os.chdir('D:/Python/python-git/begginger/2017-03-09/Program')

# 和前几天内容不同，不需要制作数据导入到文件中，只需要从文件中读取数据，并导入到列表中即可
# 所以使用 with open 来打开 james.txt文件，用jaf来指代该内容地址，再用readline()来读取地址代表内容
with open('james.txt')as jaf:
    data=jaf.readline()  # 读取数据行
james=data.strip().split(',') # 将数据转换为一个列表
with open('julie.txt')as juf:
    data=juf.readline()
julie=data.strip().split(',')
with open('mikey.txt')as mif:
    data=mif.readline()
mikey=data.strip().split(',')
with open('sarah.txt')as saf:
    data=saf.readline()
sarah=data.strip().split(',')

# print(james)
# print(julie)
# print(mikey)
# print(sarah)
# print(jaf) # 试试看这个代码输出了什么，
# print('-------------')
# 使用排序，按从小到大排序

# print(sorted(james))
# print(sorted(julie))
# print(sorted(mikey))
# print(sorted(sarah))

# 发现数据很奇怪，因为数据本身格式不统一，所以不好排序。
# 所以我们应该把数据处理成统一的格式再来进行排序

# 创建一个函数来处理该问题

# 创建4个新列表来保存清理后的数据

clean_james=[]
clean_julie=[]
clean_mikey=[]
clean_sarah=[]

# for each_t in james:   # 迭代
#     clean_james.append(sanitize.sanitize(each_t))  # 先转换，再添加
# for each_t in julie:
#     clean_julie.append(sanitize.sanitize(each_t))
# for each_t in mikey:
#     clean_mikey.append(sanitize.sanitize(each_t))
# for each_t in sarah:
#     clean_sarah.append(sanitize.sanitize(each_t))

# print(sorted(clean_james))
# print(sorted(clean_julie))
# print(sorted(clean_mikey))
# print(sorted(clean_sarah))

# 正常运行


# 第二部分


# 有个问题是：代码很多都在重复...

# 我们可以做出的改进是：

clean_james=[sanitize.sanitize(each_t) for each_t in  james]
clean_julie=[sanitize.sanitize(each_t) for each_t in  julie]
clean_mikey=[sanitize.sanitize(each_t) for each_t in  mikey]
clean_sarah=[sanitize.sanitize(each_t) for each_t in  sarah]

print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_mikey))
print(sorted(clean_sarah))