
# 建立名字列表
cast = ["Cless","Palin","Jones","Idle"]
# 输出列表数据
print(cast[1])
# 得到列表数据数量
print("列表总共有{}个数据".format(len(cast)))

# 添加列表数据项 append
cast.append("Gilliam")
print(cast)

cast.pop() # pop() 从列表末尾删除数据
print(cast)

cast.extend(["Gilliam","Chapman"]) # extend() 从列表末尾添加数据
print(cast)

cast.remove("Chapman")  # remove() 从列表删除某个特定数据项
print(cast)

cast.insert(0,"Chapman") # insert(a,b) 在列表 a 位置上 添加 b 数据项
print(cast)