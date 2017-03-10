# 删除重复项

# 引入readFile中的代码
import os
import sanitize
os.chdir('D:/Python/python-git/begginger/2017-03-09/Program')

# with open('james.txt')as jaf:
#     data=jaf.readline()  # 读取数据行
# james=data.strip().split(',') # 将数据转换为一个列表
# with open('julie.txt')as juf:
#     data=juf.readline()
# julie=data.strip().split(',')
# with open('mikey.txt')as mif:
#     data=mif.readline()
# mikey=data.strip().split(',')
# with open('sarah.txt')as saf:
#     data=saf.readline()
# sarah=data.strip().split(',')


# clean_james=[]
# clean_julie=[]
# clean_mikey=[]
# clean_sarah=[]
#
# clean_james=[sanitize.sanitize(each_t) for each_t in  james]
# clean_julie=[sanitize.sanitize(each_t) for each_t in  julie]
# clean_mikey=[sanitize.sanitize(each_t) for each_t in  mikey]
# clean_sarah=[sanitize.sanitize(each_t) for each_t in  sarah]

# print(sorted(clean_james))
# print(sorted(clean_julie))
# print(sorted(clean_mikey))
# print(sorted(clean_sarah))

# 修改程序

# james=sorted([sanitize.sanitize(t) for t in james])
# julie=sorted([sanitize.sanitize(t) for t in julie])
# mikey=sorted([sanitize.sanitize(t) for t in mikey])
# sarah=sorted([sanitize.sanitize(t) for t in sarah])

# unique_james=[]
# for each_t in james:
#     if each_t not in unique_james:
#         unique_james.append(each_t)
# print(unique_james[0:3])   # 访问列表中从第0项到（但不包括）第三项的数据
#
# unique_julie=[]
# for each_t in julie:
#     if each_t not in unique_julie:
#         unique_julie.append(each_t)
# print(unique_julie[0:3])
#
# unique_mikey=[]
# for each_t in mikey:
#     if each_t not in unique_mikey:
#         unique_mikey.append(each_t)
# print(unique_mikey[0:3])
#
# unique_sarah=[]
# for each_t in sarah:
#     if each_t not in unique_sarah:
#         unique_sarah.append(each_t)
# print(unique_sarah[0:3])

# 用集合来改造

# print(sorted(set([sanitize.sanitize(t) for t in james]))[0:3])
# print(sorted(set([sanitize.sanitize(t) for t in julie]))[0:3])
# print(sorted(set([sanitize.sanitize(t) for t in mikey]))[0:3])
# print(sorted(set([sanitize.sanitize(t) for t in sarah]))[0:3])

# 将上述4个with语句改为一个函数

def get_coach_data(filename):
  try:
      with open(filename)as f:
          data=f.readline()
      return (data.strip().split(','))

  except IOError as ioerr:
      print('File error:'+str(ioerr))
      return (None)


james=get_coach_data('james.txt')
julie=get_coach_data('julie.txt')
mikey=get_coach_data('mikey.txt')
sarah=get_coach_data('sarah.txt')


print(sorted(set([sanitize.sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize.sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize.sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize.sanitize(t) for t in sarah]))[0:3])
