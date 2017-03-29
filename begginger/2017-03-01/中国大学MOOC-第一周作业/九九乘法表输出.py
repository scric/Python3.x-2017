for i in range(1, 10):
    for j in range(1, i+1):
        print('{}*{}={:2} '.format(j, i, i*j), end='')  # 第三个大括号里的":2" 可以去除掉或者将数字改成其他。应该只是起到位宽的作用。
    print('')

print()

for i in range(1, 10):
    for j in range(1, i+1):
        print('{}*{}={:2} '.format(i, j, i*j), end='')
    print('')


for i in range(1, 10):
    for j in range(1, i+1):
        print('{}*{}={:2} '.format(j, i, i*j), end='\n')

    print('')