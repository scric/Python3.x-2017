weight = eval(input("请输入您的体重(weight):"))
height = eval(input("请输入您的身高(height):"))
BMI = weight / height
print(BMI)

# 法一
# 发现python没有switch case 语句... 我们可以使用字典映射方式来实现
# switch = {
#     BMI < 18.5: "偏瘦",
#     BMI < 25: "正常",
#     BMI < 30: "偏胖",
#     BMI >= 30: "肥胖"
# }
#
# print(switch)

# 该方法实现失败 .

# 使用判断

if BMI < 18.5:
    print("您的体质偏瘦")
elif (BMI < 25) & (BMI < 24):
    print("您的体质正常")
elif (BMI < 30) & (BMI < 28):
    print("您的体质偏胖")
elif (BMI >= 30) & (BMI >= 28):
    print("您的体质过于肥胖")





