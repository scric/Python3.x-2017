def reduceNum(n):
    print('{} = '.format(n),end='')
    if not isinstance(n, int) or n <= 0 :
        print('请输入一个正确的数字 !')
        exit(0)
    elif n in [1]:
        print('{}'.format(n),end='')
    while n not in [1]:  # 循环保证递归
        for index in range(2, n + 1):
            if n % index == 0:
                n /= index  # n 等于 n/index
                n = int(n)
                if n == 1:
                    print(index,end='')
                else:  # index 一定是素数
                    print('{} *'.format(index),end='')
                break
s = input("请输入一个数字")
reduceNum(int(s))
