import athletemodel
import yate
import glob
# import os
# os.chdir('D:/Python/python-git/begginger/2017-03-13/Program')

data_files = glob.glob("data/*.txt")
athletes = athletemodel.put_to_store(data_files)

print(yate.start_response()) # 总是从一个content-type行开始
print(yate.include_header("Coach Kelly's List of Athletes"))  # 开始生成Web页面，提供一个合适的标题
print(yate.start_form("generate_timing_data.py"))  # 开始生成表单，提供要连接的服务器端程序的名。
print(yate.para("Select an athlete from the list to work with:"))  # 这是一个段落，告诉用户做什么

# 为每个选手分别生成一个单选钮
for each_athlete in athletes:
    print(yate.radio_button("which_athlete", athletes[each_athlete].name))
print(yate.end_form("Select")) # 定制一个"提交"按钮

print(yate.include_footer({"Home": "/index.html"}))