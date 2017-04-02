# 猜数字, 引入random库 , 利用 循环
import random

# random 库的使用
# for i in range(10):
#     print(int(random.randint(0, 99)))

# 随机产生一个 0 - 99数 ,赋值给 num
keynums = random.randint(0, 100)

count = 0  # 创建一个计数器, 用于记录用户猜的次数
while True:
    usernum = int(input("请输入你要猜的数字(0,99):"))
    if usernum != keynums:
        count += 1
        if usernum > keynums:
            print("你猜的数字大了,"+"这是第" + str(count)+"次")
        else:
            print("你猜的数字小了,"+"这是第" + str(count)+"次")
        continue
    else:
        print("恭喜你, 你猜对了, 共猜了" + str(count) + "次")
        break

# 你是否还想到了别的什么方法来实现这个?
# 如果让你实现 在 N 次里面猜数字的游戏, 你要如何实现？
# 用函数如何实现?




