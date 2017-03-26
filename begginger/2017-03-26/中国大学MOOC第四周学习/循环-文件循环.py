import os
# os.chdir('D:/Python\python-git/begginger/2017-03-26/中国大学MOOC第四周学习')  # 切换为包含数据文件的文件夹
# 不使用os.chdir也可以追踪到 numList.txt ,因为代码文件和数据文件在同一个文件夹下

data = open('numList.txt', 'r')  # 打开文件并将数据赋值给data

# 试试在另一个包外的文件夹里的数据
# data = open('paper.txt', 'r') # FileNotFoundError: [Errno 2] No such file or directory: 'paper.txt'

# 试试在同一个包下的另一个文件夹内的数据
# data = open('numList1.txt', 'r') # FileNotFoundError: [Errno 2] No such file or directory: 'numList1.txt'

print(data)   # 输出地址值,说明数据还需进一步处理
# <_io.TextIOWrapper name='numList.txt' mode='r' encoding='cp936'>
line = data.readline()  # 读取文件数据的下一行
print(line)
# 2

# 测试完毕,下面来试一试如何输出文件数据中的平均值
# 这里的文件数据是以一行一个数据存在的
sum1 = 0
count = 0
while line != '':
    sum1 += eval(line)
    count += 1
    line = data.readline()
print("The average of the number is:", sum1/count)   # 20/6

# The average of the number is: 3.3333333333333335

# 接下来测试数据在同一行并以逗号隔开的形式
data1 = open('numList2', 'r')
line1 = data1.readline()
print(type(line1))  # <class 'str'>
print(line1)  # 2,2,3,4,5,20
sum12 = 0
index = 0
while line1 != '':
    for xStr in line1.split(","):
        sum12 += eval(xStr)
        index += 1
    line1 = data1.readline()
print("The average of the number is:", sum12/index)
# The average of the number is: 6.0  