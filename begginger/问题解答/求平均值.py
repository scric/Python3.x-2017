# 求平均值 ,问题来自讨论区

# 法一
# zum = 0
# count = 0
# moredata = "y"
# while moredata == "y":  # 记得上下条件一致,否则进不了循环,就会得到错误的结果
#     x = int(input("Enter a number >>"))
#     zum += x
#     count += 1
#     moredata = input("Do you have more numbers(yes or no)?>>")
# print("The average of the number is", zum / count)
# print(type(zum / count))  # <class 'float'>

# 一个疑问是 : sum/count 都是int类型,为什么得到的结果却是float类型?
# 如何在输入错误的值后,重新返回循环?


# 法二 哨兵循环

sum1 = 0
count = 0
xStr = input("Enter a number (<Enter> to quit) >> ")
while xStr != "":
    x = eval(xStr)
    sum1 += x
    count += 1
    xStr = input("Enter a number (<Enter> to quit) >> ")
print("The average of the number is", sum1 / count)


