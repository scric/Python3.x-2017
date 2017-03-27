
# 方法一
try:
    a, b, c = eval(input("请分别输入三个数值来比较大小:"))
    if a > b & b > c:
        print("a>b>c")
    elif a > c & c > b:
        print("a>c>b")
    elif b > a & a > c:
        print("b>a>c")
    elif b > c & c > b:
        print("b>c>a")
    elif c > b & b > a:
         print("c>b>a")
    else:
        print("c>a>b")
except ValueError as valerr:
    print(valerr)
except TypeError as typerr:
    print(typerr)
except NameError as namerr:
    print(namerr)

# 方法二

try:
    a, b, c = eval(input("请分别输入三个数值来比较大小:"))
    if a>b:
        if a>c:
            if c>b:
                print("a>c>b")
            else:
                print("a>b>c")
        else:
            print("c>a>b")
    elif a<b:
        if b>c:
            if c>a:
                print("b>c>a")
            else:
                print("b>a>c")
        else:
            print("c>b>a")
    else:
        print("c>b>a")
except NameError as namerr1:
    print(namerr1)
except SyntaxError as synerr:
    print(synerr)

# 吐血,不玩了.

# 求三个数中的最大值
a, b, c = eval(input("请分别输入三个数值来比较大小:"))
print("The largest number is :" ,max(a,b,c))

