'''
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
'''

# 将上述代码用 with 重写

import os
import sys
import nester3
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

# 法一
try:
    with open('man_data.txt','w') as man_file:
        nester3.print_lol(man,fh=man_file)
    with open('other_data.txt','w') as other_file:
        nester3.print_lol(other,fh=other_file)

except IOError as err:
    print('File error.'+str(err))
