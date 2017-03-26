import requests
zh = requests.get("https://www.zhihu.com")
print(zh.status_code)  # 500
print(zh.encoding)  # ISO-8859-1
zh.encoding = 'utf-8'
print(zh.text)   # 出现异常.