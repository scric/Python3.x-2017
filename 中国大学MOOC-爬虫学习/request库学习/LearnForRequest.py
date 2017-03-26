import requests

r = requests.get("http://www.baidu.com")  # requests.get(url)

print(type(r))  # <class 'requests.models.Response'>
print(r.status_code)  # HTTP请求的返回状态.
# 200 .如果返回的结果是200,则连接成功,.如果是404或其他某些原因出错将产生异常

print(r.encoding)  # r.encoding : 从HTTP header中猜测的响应内容编码方式
# ISO-8859-1
# 如果r.encoding = 'ISO-8859-1' ,则网页中的中文字符为乱码,所以我们应该赋值为utf-8的形式

r.encoding = 'UTF-8'   # 将url中的响应内容编码方式重新赋值为 'utf-8'

# r.encoding = 'GBK'  # 仍然乱码.
# GBK

print(r.encoding)
# utf-8/UTF-8

# 还有一种方式可以得到响应内容编码方式, r.apparent_encoding(备选编码方式)
print(r.apparent_encoding)  # 从内容中分析出的响应内容编码方式
# utf-8
print(r.text)  # HTTP响应内容的字符串形式,即url对应的页面内容
print(type(r.text))  # <class 'str'>

# 其他测试

zx = requests.get("http://www.zxabs.xyz")
print(zx.status_code)  # 200
print(zx.encoding)  # utf-8
print(zx.text)

# 发现我的网站格式和百度的格式不一样....为什么?再爬一个

zh = requests.get("https://www.zhihu.com")
print(zh.status_code)  # 500
print(zh.encoding)  # ISO-8859-1
zh.encoding = 'utf-8'
print(zh.text)  # 出现异常.



