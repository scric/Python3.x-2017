diet=['西红柿','花椰菜','黄瓜','牛排','虾仁']
count=0
for x in range(0,5):
    for y in range(0,5):  #改为for y in range(int(x),5)，结果会怎么样
        if not(x==y):
            print("{}{}".format(diet[x],diet[y]))
            count=count+1
print('')
print("排列总数有{}个".format(count))
