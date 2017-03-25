from random import *

print(random())  # 生成一个[0,1.0]之间的随机小数
# 0.6147838817304846

print(uniform(0, 1))  # uniform(a,b) 生成一个a到b之间的随机小数
# 0.8195755503199231

print(randint(0, 10))  # randint(a,b) 生成一个a到b之间的随机整数
# 10

for i in range(10):
    print(randint(0, 10), end=',')
# 6,2,3,0,5,1,1,2,5,9,
# 有重复.

# 实际上,还有一种方法可以实现生成随机整数

print()
for k in range(10):
    print(int(10 * random() + 1), end=',')
    #  2,1,9,2,6,10,5,9,6,3,
print()
for j in range(10):
    print(randrange(1, 10, 3), end=',')  # 随机生成一个从a开始到b以c递增的数
    # 7,1,7,1,7,7,1,4,4,4,
print()
listOne = [1, 3, 5, 1, 'a', 56]
print(type(listOne))  # <class 'list'>
print(listOne)  # [1, 3, 5, 1, 'a', 56]

print(choice(listOne))  # choice(<list>) 从列表中随机返回一个元素
# 1

shuffle(listOne)  # shuffle(<list>) 将列表中的元素随机打乱
print(listOne)  # [5, 3, 1, 56, 'a', 1]

print(sample(listOne, 3))  # sample(<list>,k)  # 从指定的列表中随机获取k个元素
# [5, 56, 1]

