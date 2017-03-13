import sanitize


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return sorted(set([sanitize.sanitize(t) for t in self]))[0:3]

# 新类代码的使用

# vera = AthleteList('vera vi')  # 为vera创建一个新的对象实例
# vera.append('1.31')   # 增加一个计时值
# print(vera.top3())
#
# vera.extend(['2.22', '1-21', '2:22'])
# print(vera.top3())

# 让我们使用最终版的readFile吧

