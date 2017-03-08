import pickle
import nester
import os



# 制作数据

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


# 腌制数据
new_man=[]
try:
    with open('man_data.txt','wb') as man_file,open('other_data.txt','wb') as other_file:
        pickle.dump(man,man_file)
        pickle.dump(other,other_file)
except IOError as err:
    print('File error.' + str(err))
except pickle.PickleError as perr:
    print('Pickling error:'+str(perr))



# 读取数据

try:
    with open('man_data.txt','rb') as man_file:
        new_man =pickle.load(man_file)
except IOError as err:
    print('File error:'+str(err))
except pickle.PickleError as perr:
    print('Pickling error:' + str(perr))


# 代码输出


# nester.print_lol(new_man)
# print(new_man)
print(new_man[0])
print(new_man[-1])