birthdays = {'张鑫': 'Apr 1', 'Bigboss': 'Jul 2', '连小璐': 'Feb 3', '陈一': 'Oct 4'}

while True:
    name = input("请输入要查询的名字(直接回车则退出): ")
    if name == '':
        break
    if name in birthdays:
        print('<' + name + '> 的生日是 ' + birthdays[name])
    else:
        print("没有 <" + name + "> 的生日信息")
        bday = input("请输入 <"+name+"> 的生日: ")
        birthdays[name] = bday
        print("生日信息更新完毕")
print(birthdays)

# 在程序终止时, 程序的数据都会丢失