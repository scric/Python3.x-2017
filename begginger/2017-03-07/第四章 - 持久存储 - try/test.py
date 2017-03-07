# 导入库和文件
import os
import nester3
os.chdir('D:/Python/python-git/begginger/2017-03-06/Program/chapter3')
# 打开文件
with open('man_data.txt')as mdf:
    nester3.print_lol(mdf.readline())

'''
['Is this the right room for an argument?', "No you haven't!", 'When?', "No you didn't!", "You didn't!", 'You did not!', 'Ah! (taking out his wallet and paying) Just the five minutes.', 'You most certainly did not!', "Oh no you d
'''

# 发现被python处理成一整串字符串。
# 这时我们可以修改print_lol()来处理