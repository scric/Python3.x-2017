# print输出格式的定制

# 先了解一下print的原型
#  def print(self, *args, sep=' ', end='\n', file=None):
# 发现它通常都是以 '\n' 也就是以换行符结尾

data = 6, 5, 1, 7, 0, 'o', "iad"

# 发现每输出一个元素都进行了换行,那么如何不换行输出呢?
for i in range(len(data)):
    print(data[i], end='')   # 65170oiad

print()

#  发现无法在同一行之间分开数据,我们可以:
for i in range(len(data)):
    print(data[i], end=',')  # 6,5,1,7,0,o,iad,

# 那么如何将末尾的','去掉呢?

