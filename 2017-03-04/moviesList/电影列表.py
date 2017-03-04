
# 建立列表

movies = ["The Holy Grail","The Life of Brian","The Meaning of Life"]

# Python 在建立列表时，解释器会在内存中创建一个类似数组的数据结构，数据项自下而上推放。
# 第一项的编号为 0

# 访问列表数据

print(movies[0])

# 在电影名称列表中 插入年份

movies.insert(1,1975)
movies.insert(3,1979)
movies.insert(5,1986)

print(movies)