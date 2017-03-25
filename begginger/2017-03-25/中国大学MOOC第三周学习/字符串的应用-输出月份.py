# 输入 1 - 12 来输出一到十二月的英文缩写(三个单词)
# 涉及到了字符串的操作,条件语句和循环语句的使用,还有如何控制流程.

months = "JanFebMarAprMayJunJulAugSepOctNovDec"
count = 0   # 定义一个计数器 ,一定要放在外面.
while True:  # 设置一个while循环
    n = eval(input("请输入月份数(1-12):"))
# 如果不强制转换 n为int类型,则会报错,因为index不能被确定为 int类型或是string类型
# TypeError: unsupported operand type(s) for -: 'str' and 'int'
    if n > 0 & n <= 12:  # 设置一个进入条件
        index = (n-1)*3
        monthAbbrev = months[index:index+3]  # 用到了<string>[:] 的知识,不懂请看操作字符串
        if monthAbbrev != '':
            print("所输入的月份简写是:" + monthAbbrev + ",")
        elif count != 2:
            count += 1
            print("你还有%d次机会" % (3-count))
            continue
        else:
            print("你太皮了")
            break

# 还能再精简吗?不能省略掉循环和判断语句
# 如果不加if monthAbbrev != '': 这句, 会怎么样.















