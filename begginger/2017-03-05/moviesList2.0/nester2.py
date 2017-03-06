# 使用一个三重引号 来建立多行注释
# 这是 2.0 版本

"""
 这是 "nester.py" 模块。提供了一个名为print_lol()的函数，这个函数的
 作用是打印列表，其中可能包含嵌套列表。
 第二个参数（命名为"level"）用来在遇到嵌套列表时插入制表符。

"""

# def print_lol(the_list,level):
#     """这个函数取一个位置参数，名为“the_list”，这可以是任何Python列表。
#     所指定的列表中的每个数据项会输出到屏幕上，各数据项各占一行。"""
#     for each_item in the_list:
#         if isinstance(each_item,list):
#             # print_lol(each_item) 只输入这句会引起错误。新代码中引入了两个参数，而这只使用了一个参数
#             # 所以在调用函数新版本时 ， 要提供数目正确的参数。
#             print_lol(each_item,level+1)
#             # 如果仅仅添加level 并不会对结果产生影响，数值并未改变
#             # 增加 level 参数的目的是为了 能够控制嵌套输出。
#             # 问 ，如何知道嵌套的层数呢 ？
#         else:
#             for tab_stop in range(level):
#                 print("\t",end='')
#             print(each_item)

"""
   使用可选参数
   为了向函数参数提供一个缺省值，需要在参数后面指定这个缺省值
"""

# def print_lol(the_list,level=0): # 增加一个缺省值使得‘level’变成一个可选参数
#     for each_item in the_list:
#         if isinstance(each_item,list):
#             print_lol(each_item,level+1)
#         else:
#             for tab_stop in range(level):
#                 print("\t",end='')
#             print(each_item)


"""
控制默认行为：是否缩进

"""

def print_lol(the_list,indent=False,level=0): # 增加一个缺省值使得‘level’变成一个可选参数
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1)
        else:
            if indent:
             for tab_stop in range(level):
                print("\t",end='')
            print(each_item)