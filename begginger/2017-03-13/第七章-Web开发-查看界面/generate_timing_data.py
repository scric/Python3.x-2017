import cgi  # 导入cgi库
import athletemodel
import yate


athletes = athletemodel.get_from_store()

form_data = cgi.FieldStorage() # 获取所有表单数据并放在一个字典中
athlete_name = form_data['which_athlete'.value]

print(yate.start_response())  # 总是从一个content-type行开始
print(yate.include_header("Coach Kelly's Timing Data"))  # 开始生成Web页面，提供一个合适的标题
print(yate.header("Athlete:" + athlete_name + ",DOB: " + athletes[athlete_name].dob + "."))
print(yate.para("The top times for this athlete are:"))
print(yate.u_list(athletes[athlete_name].top3()))
print(yate.include_footer({"Home": "/index.html","Select another athlete": "generate_list.py"}))