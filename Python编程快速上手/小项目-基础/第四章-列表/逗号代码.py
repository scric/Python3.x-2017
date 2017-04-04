# 逗号代码
# 编写一个函数, 它以一个列表值作为参数, 返回一个字符串. 该字符串包含所有表项, 表项之间以逗号和空格分隔, 并在最后一个表项之前插入 and
# 比如


# string = ''
# print(type(string))
# for i in spam:
#     if i == spam[0]:
#         string = i + ', '
#     elif i != spam[-1]:
#         string = string + i + ', '
#     else:
#         string = string + 'and ' + i
# print(string)


# def changeList(spam):
#     string = ''
#     for i in spam:
#         if i != spam[-1]:
#             string = string + i + ', '
#         else:
#             string = string + 'and ' + i
#     return string
#


# print(changeList(spam))
#
# copyee = ['A', 'B', 'C', 'D']
# print(changeList(copyee))

# 改进



# def changeList2(spam):
#     i = 0
#     while i <= len(spam):
#         if i % 2 == 1:
#             spam.insert(spam.index(spam[i])-1, ', ')
#         elif i == len(spam):
#             spam.insert(spam.index(spam[len(spam)]), 'and ')
#         else:
#             print(spam[i])
#         i += 1
#     string = ''
#     for z in spam:
#         string += z
#     return string
# print(changeList2(spam))

print("4.10.1 answer:")


def chlist_str(spam):
    spam[-1] = 'and ' + spam[-1]
    str_list = ', '.join(spam)
    return str_list

new_str = ['apple', 'banana', 'tofu', 'cats']
new_str = chlist_str(new_str)
print("convert str is:")
print(new_str)