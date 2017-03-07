
"""
 这是 "nester.py" 模块。提供了一个名为print_lol()的函数，这个函数的
 作用是打印列表，其中可能包含嵌套列表。
 第二个参数（命名为"level"）用来在遇到嵌套列表时插入制表符。

"""
import sys
def print_lol(the_list,indent=False,level=0,fh=sys.stdout): # 增加一个缺省值使得‘level’变成一个可选参数
    """
    这个函数取一个位置参数，名为“the_list”，这可以是任何Python列表。
    #     所指定的列表中的每个数据项会输出到屏幕上，各数据项各占一行。
    """
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1,fh)
        else:
            if indent:
             for tab_stop in range(level):
                print("\t",end='',file=fh)
            print(each_item,file=fh)