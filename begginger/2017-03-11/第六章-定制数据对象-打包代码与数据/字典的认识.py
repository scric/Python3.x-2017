'''
字典是一个内置的数据结构，
运行将数据和键值而不是与数字关联。
这样可以使内存中的数据与实际数据的结构一致
'''

# 如何创建字典

cleese={}  # 大括号
palin=dict()  # 小括号

# print(type(cleese))
# print(type(palin))

# 通过将值与键关联，向这两个字典分别增加一些数据
# 注意：palin字典是一次性同时创建

cleese['Name']='John Cleese'
cleese['Occupations']=['actor','comedian','writer','film producer']
palin={'Name':'Michael Palin','Occupations':['comedian','actot','writer','tv']}

# 数据与键关联后，可以使用一种类似列表的方法 访问单个数据项

# print(palin['Name'])   # 使用中括号指定字典中的索引来访问数据项。
# print(cleese['Occupations'][-1])   # 使用数字来访问存储在一个特定字典键位置上的列表项、

# 字典也可以动态扩展来存储额外的键/值对、

palin['Birthplace']="Broomhill,Sheffield,England"
cleese['Birthplace']="Weston-super-Mare,North Somerset,England"

# 与列表不同，字典不会维持插入的顺序。它主要维护关联关系，而不是顺序

print(palin)
print(cleese)
