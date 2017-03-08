import pickle # 导入pickle库
import os
os.chdir('D:/Python/python-git/begginger/2017-03-06/Program/chapter3')
# 该语法错误。
# man=str(open('man_data.txt','w'))
# other=str(open('other_man.txt','w'))

# 腌制数据
try:
    with open('man_data.txt','wb') as man_file,open('other_data.txt','wb') as other_file:
        pickle.dump(man,man_file)
        pickle.dump(other,other_file)
except IOError as err:
    print('File error.' + str(err))
except pickle.PickleError as perr:
    print('Pickling error:'+str(perr))

# 运行发现man_data和other_data中的文件都是乱码形式。如何解决呢？
#

