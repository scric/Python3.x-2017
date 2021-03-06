# def sanitize(time_string):
#     if '-' in time_string:
#         splitter='-'
#         (mins,secs)=time_string.split(splitter)
#         return time_string
#     elif ':' in time_string:
#         splitter=':'
#         (mins, secs) = time_string.split(splitter)
#         return time_string
#     else:
#         return (mins+ '.' + secs)

# 创建一个函数
def sanitize(time_string):
    if '-'in time_string:   # 使用"in"操作符检查字符串中是否包含内容
        splitter='-'
    elif ':' in time_string:
        splitter=':'
    else:
        return (time_string)
    (mins,secs)=time_string.split(splitter)  # 分解字符串，抽出分钟和秒
    return (mins+'.'+secs)