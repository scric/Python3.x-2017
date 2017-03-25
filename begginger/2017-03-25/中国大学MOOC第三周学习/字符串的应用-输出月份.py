# 输入 1 - 12 来输出一到十二月的英文缩写(三个单词)

months = "JanFebMarAprMayJunJulAugSepOctNovDec"
count = 0
while True:
    n = eval(input("请输入月份数(1-12):"))
# 如果不强制转换 n为int类型,则会报错,因为index不能被确定为 int类型或是string类型
# TypeError: unsupported operand type(s) for -: 'str' and 'int'
    if n > 0 & n <= 12:
        index = (n-1)*3
        monthAbbrev = months[index:index+3]
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















