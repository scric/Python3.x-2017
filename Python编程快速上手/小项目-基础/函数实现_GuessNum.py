import random


def guessNum(userNum):
    keynums = random.randint(0, 100)
    print(keynums)
    while True:
        if userNum != keynums:
            if userNum > keynums:
                return 0
                # print("你猜的数字大了," + "这是第" + str(count) + "次")
            else:
                return -1
                # print("你猜的数字小了," + "这是第" + str(count) + "次")
        else:
            return 1


count = 0  # 创建一个计数器, 用于记录用户猜的次数
while True:
    userNum = int(input("请输入你的数字:"))
    count += 1
    if guessNum(userNum) != 1:
        if guessNum(userNum) == 0:
            print("你猜的数字大了," + "这是第" + str(count) + "次")
        else:
            print("你猜的数字小了," + "这是第" + str(count) + "次")
        continue
    else:
        print("恭喜你, 你猜对了, 共猜了" + str(count) + "次")
        break


# 这是一个失败的实现
# 因为