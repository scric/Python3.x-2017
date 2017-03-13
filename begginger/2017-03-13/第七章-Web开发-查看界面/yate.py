from string import Template

'''
从标准库中的“string” 模块导入“Template”类。它
支持简单的字符串替换模板
'''


def start_response(resp = "text/html"):
    return 'Content-type: ' + resp + '\n\n'

# 这个函数需要一个可选的字符串作为参数，用它来创建一个CGI “Content-type:” 行，参数缺省值是"text/html"


def include_header(the_title):
    with open('templates/header.html') as headf:  # 打开模板文件(HTML)。
        head_text = headf.read()  # 读入文件
    header = Template(head_text)  # 换入所提供的"标题"
    return header.substitute(title=the_title)  # 换入所提供的"标题"

# 这个函数需要一个字符串作为参数，用在HTML页面最前面的标题中。页面本身存储在一个单独的文件"templates/header.html"中，可以根据需要替换标题。


def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()
    link_string = ''
    # 打开模板文件，读入文件，换入"the_links"中提供的HTML链接字典
    for key in the_links:
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp'  # 将链接字典转换为一个字符串，然后换入模板
    footer = Template(foot_text)
    return footer.substitute(links=link_string)
# 与"include_header"函数类似，这个函数使用一个字符串作为参数，来创建一个HTML页面的尾部。页面本身存储在一个单独的文件"templas/footer.html"中，参数用于动态地创建一组HTML链接标记，从这些标记的使用来看，应该是一个字典，。


def start_from(the_url, form_type="POST"): # form_type 的缺省值一般为POST或GET
    return '<form action="' + the_url + '" method="' + form_type + '">'
# 这个函数返回表单最前面的HTML，允许调用者制定url（表单数据将发送到这个url），还可以指定所要使用的方法


def end_form(submit_msg="Submit"):
    return '<p></p><input type=submit value="' + submit_msg + '"><form>'

# 这个函数返回表单末尾的HTML标记，同时还允许调用老定制表单"submit"(提交)按钮的文本


def radio_button(rb_name, rb_value):
    return '<input type="radio" name="' + rb_name + '"value="' + rb_value + '">' + rb_value + '<br />'

# 给定一个单选按钮名和值，创建一个 HTML单选钮(通常包括在一个HTML表单中)。注意，两个参数都是必要的


def u_list(items):
    u_string = '<u1>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return u_string

# 给定一个列表项，这个函数会把该列表转换为一个HTML无序列表。一个简单的'for'循环就可以完成全部工作，每次迭代回想ul元素增加一个li元素。


def header(header_text, header_level=2):
    return '<h' + str(header_level) + '>' + header_text + '</h' + str(header_level) + '>'

# 创建一个并返回一个HTML标题标记（H1,H2,H3等） 默认为2级标题。“header_text”参数是必要的


def para(para_text):
    return '<p>' + para_text + '</p>'

# 用HTML段落标记包围一个文本段(一个字符串)。

# print(start_response())
# print(start_response("text/plain"))
# print(start_response("application/json"))

