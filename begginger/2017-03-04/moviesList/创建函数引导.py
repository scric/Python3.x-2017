movies = ["The Holy Grail",1975,"Terry Jones & Terry Gilliam",91,
          ["Graham Chapman",
           ["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]
# print(movies[4][1][3])
#
# for each_item in movies:
#     if isinstance(each_item,list):
#         for nested_item in each_item:
#             print(nested_item)
#     else:
#         print(each_item)

# 如果需要继续将方括号中的数据项读取出来 不可能继续往下面添加 for 语句 和 if 语句来读取
# 更好的办法应该是构建一个函数来将重复代码替代掉。
# 如何建立函数呢？

# 使用 def 来创建函数 def 函数名 （参数）:
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)

print_lol(movies)



