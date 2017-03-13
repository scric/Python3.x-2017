from yate import *
import os
os.chdir('D:/Python/python-git/begginger/2017-03-13/Program/yate')

# start_response()
# start_response("text/plain")
# start_response("application/json")


# include_header()函数生成一个Web页面的开始部分，允许定制页面的标题。
# print(include_header("Welcome to my home on the web!"))


# include_footer()函数会生成一个Web页面末尾的HTML，并提供链接。若字典为空，则不会包含链接HTML
# print(include_footer({'Home': '/index.html', 'Select': '/cgi-bin/select.py'}))
# print(include_footer({})) # 不包含链接


# start_form()和end_form()函数会建立HTML表单，并用参数来调整所生成的HTML的内容
# print(start_from("/cgi-bin/process-athlete.py"))  # POST 允许指定服务器上的程序名，表单数据将发送到这个程序
# print(end_form())
# print(end_form("Click to Confirm Your Order"))


# 创建HTML单选钮 radio_button()
# for fab in ['John', 'Paul', 'George', 'Ringo']:
#     print(radio_button(fab, fab))  # 从单选列表中选取


# 创建无序列表 u_list()
# print(u_list(['Life of Brian', 'Holy Grail']))


# 快速建立选定级别的HTML标题 header() 默认级别为2
# print(header("Welcome to my home on the web"))
# print(header("This is a sub-sub-sub-sub heading", 5))


# 把文本块包围在HTML段落标记中间 para()
print(para("Was ot worth the wait? We hope it was..."))