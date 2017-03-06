import os # 从标准库中导入"os"

# os.chdir('D:/Python/firstProgram/begginger/2017-03-06/Program/chapter3') # 切换成包含数据文件的文件夹
# data = open('paper2.txt') # 打开一个命名的文件，将文件赋至一个名为"data"的文件对象
# for each_line in data:
#     print(each_line,end='')

"""
进一步查看数据
"""
# split() 会根据特定符号来将字符串分割开来

os.chdir('D:/Python/firstProgram/begginger/2017-03-06/Program/chapter3') # 切换成包含数据文件的文件夹
data = open('paper2.txt') # 打开一个命名的文件，将文件赋至一个名为"data"的文件对象
for each_line in data:
    (role,line_spoken)=each_line.split(":")
    print(role,end='')
    print(' said :',end='')
    print(line_spoken,end='')


