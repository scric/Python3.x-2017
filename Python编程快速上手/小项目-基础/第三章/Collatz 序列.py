# 编写一个名为 collatz() 的函数, 它有一个名为 number 的参数 , 如果参数是偶数 , 那么 collatz()就打印出 number / 2 , 并返回该值;
# 如果 number 是奇数, collatz()就打印并返回 3 * number + 1
# 然后编写一个程序, 让用户输入一个整数, 并不断对这个数调用 collatz(), 知道函数返回值 1


def collatz(number):
    if number % 2 == 0:
        return number / 2
    elif number % 2 == 1:
        return 3 * number + 1
    # return number - 1

numbers = int(input("请输入一个整数: "))
count = 0  # 一个计数器, 用于统计调用 collatz()函数 的次数
while numbers != 1:
    count += 1
    numbers = collatz(numbers)
    print(int(numbers))
print("共调用 " + str(count) + ' 次')
# 在这个项目中需要注意的是:
# 返回值返回的 是 3 * number + 1 OR number / 2
# number 的值并未改变 , 所以我们应该将 collate(number) 的值 赋给 number 从而改变 number 的值, 否则打印的永远都是 原来 number 的值

# 修改版, 加入输入验证, 检测用户是否输入一个非整数的字符串, 如果在 int() 函数中传入一个非整数字符串, 则提示请重新输入一个 整数
countt = 0
while True:
    try:
        numberss = int(input("请输入一个整数 : "))
        while numberss != 1:
            countt += 1
            numberss = collatz(numberss)
            print(int(numberss))
        print("共调用 " + str(countt) + ' 次')
        break
    except ValueError as valError:
        continue




