### Request库的学习和使用

+ 如何安装request库?  

打开cmd - 输入pip install request ,等待即可 - 验证

验证: 

> r = requests.get("http://www.baidu.com")  
> print(r.status_code)  # 200 .安装成功