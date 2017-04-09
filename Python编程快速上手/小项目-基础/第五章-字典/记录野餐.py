allGuests = {'Alice': dict(apples=5, pretzels=12), 'Bob': dict(hamsandwiches=3, apples=2),
             'Carol': dict(cups=3, applepies=1)}


# 定义一个函数, 用来计算所有客人带来的食物的总数
def totalBrought(guest, item):
    numBrought = 0  # 初始化食物总数
    for k, v in guest.items():  # 建立一个 for 循环来读取字典的键值对 , k 读取键 , v 获取值( key & value )
        numBrought = numBrought + v.get(item, 0)  # 对 v 调用 get() 方法, 如果食物参数 item 是字典中存在的键, 它的值(数量)就添加到 numBrought.
        # 如果它不是键, get() 方法就返回 0 ,添加到 numBrought
    return numBrought


print('Number of things being brought: ')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'hamsandwiches')))
print(' - Apple Pies ' + str(totalBrought(allGuests, 'applepies')))

# 尽管这是一个简单的模型, 但是这个 totalBrought() 函数能够轻易处理一个包含数千名客人的字典, 只要它符合这种数据形式
