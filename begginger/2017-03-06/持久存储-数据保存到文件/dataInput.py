import os
man=[]
other=[]
os.chdir('D:/Python/python-git/begginger/2017-03-06/Program/chapter3')
try:
    data=open('paper3.txt')
    for each_line in data:
        try:
           (role,line_spoken)=each_line.split(":")
           line_spoken=line_spoken.strip() # strip() 可以从字符串中去除不想要的空白符
           if role =='Man':
               man.append(line_spoken)
           elif role=='Other Man':
               other.append(line_spoken)
        except ValueError:
            pass
except IOError:
    print('The data file is missing!')

# print(man)
# print(other)

# Python 的open() BIF 除了可以打开文件来读文件，也可以写文件。
# 使用open() BIF打开磁盘文件时，可以指定使用什么访问模式，默认使用r表示读
# 要打开一个文件完成写，需要使用模式w
# 同样的，print()BIF 显示数据时会使用标准输出。要把数据写至一个文件，需要使用file参数来指定所使用的数据文件对象。


# try:
#     man_file=open('man_data.txt','w')
#     other_file=open('other_data.txt','w')
#
#     print(man,file=man_file)
#     print(other,file=other_file)
#
#     man_file.close()
#     other_file.close()
#
# except IOError:
#     print('File error.')
#
# print("Man said：{}".format(man))
# print("Other Man said: {}".format(other))

# 如果第二个print()调用导致一个IOError，文件数据会怎么样？

# 用 finally 保证不论是否出现一个IOError都会运行某些代码

try:
    man_file=open('man_data.txt','w')
    other_file=open('other_data.txt','w')

    print(man,file=man_file)
    print(other,file=other_file)

except IOError:
    print('File error.')

finally:
    man_file.close()
    other_file.close()

print("Man said：{}".format(man))
print("Other Man said: {}".format(other))
