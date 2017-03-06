import os # 从标准库中导入"os"

# os.chdir('D:/Python/firstProgram/begginger/2017-03-06/Program/chapter3') # 切换成包含数据文件的文件夹
# data = open('paper2.txt') # 打开一个命名的文件，将文件赋至一个名为"data"的文件对象
# for each_line in data:
#     print(each_line,end='')

"""
进一步查看数据
"""
# split() 会根据特定符号来将字符串分割开来

os.chdir('D:/Python/python-git/begginger/2017-03-06/Program/chapter3') # 切换成包含数据文件的文件夹
# data = open('paper2.txt') # 打开一个命名的文件，将文件赋至一个名为"data"的文件对象


# for each_line in data:
#     (role,line_spoken)=each_line.split(":")  # split() 会根据特定符号来将字符串分割开来
#     print(role,end='')
#     print(' said :',end='')
#     print(line_spoken,end='')

# 此时出现一个错误：too many values to unpack (expected 2)
# 因为我在后面多添加了一个冒号
# 事实上，split() 有可选参数。

# for each_line in data:
#     (role,line_spoken)=each_line.split(":",1)  # split() 会根据特定符号来将字符串分割开来，在后面调用了可选参数，使得错误消失
#     # 将可选参数设置为1，数据行只会分解成两部分。
#     print(role,end='')
#     print(' said :',end='')
#     print(line_spoken,end='')

"""

此时并无问题。
但如果要求多分割一段呢？
又或者，某段并不符合我们要求的格式呢（没有冒号）？
此时split方法在查找冒号时就会出错 ,ValueError: not enough values to unpack

这时有两个处理办法，
一个是增加额外逻辑来确定是否可以再数据行上调用split
一个是让错误出现，监视它的发生，然后从运行时错误恢复
"""

# 增加额外逻辑

# 使用find()来寻找所需要的字符

# for each_line in data:
#     if not each_line.find(':')==-1:   # not 关键字会将条件的值取反
#       (role,line_spoken)=each_line.split(":",1)
#       print(role,end='')
#       print(' said :',end='')
#       print(line_spoken,end='')


# 处理异常

"""
Python 允许在异常发生时捕获异常。
在异常控制流期间，Python 先尝试运行你的代码,如果发现有问题，就会执行恢复代码，然后继续正常执行你的代码。
"""

# try/except机制 和 pass
# 用 pass 忽略错误

# for each_line in data:
#     try:
#       (role,line_spoken)=each_line.split(":")  # split() 会根据特定符号来将字符串分割开来
#       print(role,end='')
#       print(' said :',end='')
#       print(line_spoken,end='')
#     except:
#         pass

# 如果文件缺少，会发生什么？FileNotFoundError: [Errno 2] No such file or directory: 'paper2.txt'

# 增加额外逻辑的做法:

# if os.path.exists('paper2.txt'):
#     data = open('paper2.txt')
#     for each_line in data:
#         if not each_line.find(':')==-1:   # not 关键字会将条件的值取反
#           (role,line_spoken)=each_line.split(":",1)
#           print(role,end='')
#           print(' said :',end='')
#           print(line_spoken,end='')
# else:
#     print('The data file is missing!')


# 处理异常做法

# try:
#     data = open('paper2.txt')
#     for each_line in data:
#       try:
#        (role,line_spoken)=each_line.split(":")  # split() 会根据特定符号来将字符串分割开来
#        print(role,end='')
#        print(' said :',end='')
#        print(line_spoken,end='')
#       except:
#          pass
# except:
#     print('The data file is missing!')

# 代码还有一个小问题：过于一般性。
# 出现的任何运行时错误都会由某个 except 组处理。代码会悄无声息地忽略运行时错误

# 指定异常

#   如果异常代码设置为处理一种特定类型的错误，一定要在except代码行上指定错误类型.

try:
    data = open('paper3.txt')
    for each_line in data:
      try:
       (role,line_spoken)=each_line.split(":")  # split() 会根据特定符号来将字符串分割开来
       print(role,end='')
       print(' said :',end='')
       print(line_spoken,end='')
      except ValueError:
         pass
except IOError:
    print('The data file is missing!')