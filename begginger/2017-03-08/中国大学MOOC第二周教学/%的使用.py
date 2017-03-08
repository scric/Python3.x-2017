n = 9806.22222  # 实数类型

# %f的测试
print("My number is %.2f" %n)
print("%f is My number "%n)

print('')



print('')

# %s的测试  # 字符串类型

f = "我"
print("最帅的人是%s"%f)
print("%s是最帅的人"%f)

'''
%后的字母有特定含义
%s 是指str 也就是替代字符串类型
%f 是float 取代的类型应该是 real number
%d 是整数型

'''

print('')


# 高级应用 - 将多个变量放进字符串

print('')
e="世界上最帅的人的电话号码是"
w=123456789
print("%s %d %f"%(e,w,n))


print('')

# 其他应用 - 求余

print(5%2)



