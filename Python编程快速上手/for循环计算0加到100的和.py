# range 的用法
# for 循环计算 0 到 100 的和

total = 0
count = 0  # 设立一个计数器, 用来记录 for 循环执行了多少次
for i in range(100):
    count += 1
    total += i
print(total)  # 4950
print(count)  # 100

total2 = 0
count2 = 0
for i in range(101):
    count2 += 1
    total2 += i
print(total2)
print(count2)  # 101

# 需要注意的是 .第一次运行时, 变量 i 被设为 0.
# 在完成一次迭代后, 执行返回循环的顶部, for 语句让 i 增加 1
# 也就是说 range(5) 导致子句的五次迭代, i 分别被设置为 0, 1, 2, 3, 4.
# 变量 i 将递增到(但不包括)传递给 range()函数的整数


# range() 的开始, 停止和步长参数
# 两个参数
for i in range(12, 16):  # 第一个参数是 for 循环变量开始的值, 第二个参数是上限, 但不包括它.
    print(i, end=',')  # 12,13,14,15,

print()
# 三个参数
for i in range(0, 10, 2):  # 前两个参数分别是起始值和终止值, 第三个参数是 "步长" , 步长是每次迭代后循环变量增加的值
    print(i, end=',')  # 0,2,4,6,8,

print()
for i in range(10, -1, -2):  # 可以使用负数作为 步长参数, 让循环计数逐渐减少
    print(i, sep=',', end=',')  # 10,8,6,4,2,0,

# 在上面你可以看到, print 里面多了一些数据 , 比如 end = ','
# 其中 end 可选变元, 是什么意思呢 ? 意味着它是可选择的 ,我们可以看下 print 函数的源码
# def print(self, *args, sep=' ', end='\n', file=None): # known special case of print
# 它默认为 以 '\n' 结尾 , 所以我们如果想更改 print 的输出形式的话, 只需将 end 中的关键字参数(\n)改成其他的字符

