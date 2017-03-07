
# 尝试打开一个不存在的文件

# try:
#     data=open('missing.txt')
#     print(data.readline(),end='')
# except IOError:
#     print('File error')
# finally:
#     data.close()

'''
出现错误
Traceback (most recent call last):
File error
  File "D:/Python/python-git/begginger/2017-03-07/missingFile.py", line 12, in <module>
    data.close()
NameError: name 'data' is not defined

'''

# 修正方法，在finally上添加一个判断语句。
# try:
#     data=open('missing.txt')
#     print(data.readline(),end='')
# except IOError as err:
#     print('File error'+str(err))
# finally:
#     if 'data' in locals():   # locals() BIF 会返回当前作用域中定义的所有名的集合
#         data.close()

# 不过还是不清楚什么导致了错误

# 使用with

try:
    with open('missing.txt',"w") as data:
      print("It's...",file=data)
except IOError as err:
    print('File error'+str(err))
