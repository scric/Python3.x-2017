"""
首先派生内置list类创建一个定制列表，有一个名为name的属性
"""


class NamedList(list):  # 提供一个list的类名,新类将派生这个类.
    def __init__(self, a_name):
        list.__init__([])  # 初始化所派生的类
        self.name = a_name  # 将参数赋值给属性


johnny = NamedList('John Paul Jones')  # 创建一个新的"namedList"对象实例
# print(type(johnny))  # <class '__main__.NamedList'>
# print(dir(johnny))    # 看看它会提供什么内容

# 使用list类提供的功能补充johnny中存储的数据
johnny.append("Bass Player")
johnny.extend(['Composer', "Arranger", "Musician"])
# print(johnny)
# print(johnny.name)

# 列表处理

for attr in johnny:
    print(johnny.name + "is a " + attr + ".")


# OK ,认识了继承类的使用后，我们尝试一下如何修改前面所用的Athlete类的代码

