# 使用class 定义类
import sanitize


class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

# 添加数据
# sarah=Athlete('Sarah Sweeney','2002-6-17',['2:58','2.58','1.56'])
# james=Athlete('James Jones')

# print(type(sarah))
# print(type(james))

# 存储在不同的内存地址上
# print(sarah) # <__main__.Athlete object at 0x000000000290E828>
# print(james) # <__main__.Athlete object at 0x000000000290E898>


# print(sarah.name)
# print(james.name)
# print(sarah.times)
# print(james.dob)  # None
# print(james.times) # []


# 定义一个新方法，来返回最快的三个时间。

# 该方法能够返回文件数据中最快的三个时间

    def top3(self):
        return sorted(set([sanitize.sanitize(t) for t in self.times]))[0:3]


# 该方法能够将一个额外的计时值追加到选手的计时数据

    def add_time(self, time_value):
        self.times.append(time_value)

# 该方法会用一个或多个计时值（提供为一个列表）来扩展选手的计时数据

    def add_times(self, list_of_times):
        self.times.extend(list_of_times)


# 测试

vera = Athlete('vera vi')  # 为vera创建一个新的对象实例
vera.add_time('1.31')   # 增加一个计时值
print(vera.top3())

vera.add_times(['2.22', '1-21', '2:22'])
print(vera.top3())

# 我们重新创建一个Athlete类在Athlete中
