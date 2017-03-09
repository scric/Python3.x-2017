# 列表推导 list comprehension

# 将分钟列表转换成秒列表
mins=[1,2,3]
secs=[m*60 for m in mins]
print(secs)

# 将混合大小写和小写字符串的列表，转换成全大写字符串

lower=["I","don't","like","spam"]
upper=[s.upper() for s in lower]
print(upper)

# 用sanitize转换格式
import sanitize
mess=['2-22','2:22','2.22']
clean=[sanitize.sanitize(t) for t in mess]
print(clean)