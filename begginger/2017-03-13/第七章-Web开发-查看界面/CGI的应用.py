# 导入HTTP服务器和CGI模块
from http.server import HTTPServer,CGIHTTPRequestHandler

port = 8080 # 指定一个端口
httpd = HTTPServer(('',port), CGIHTTPRequestHandler)   # 创建一个HTTP服务器

# 显示一个友好的消息，并启动服务器
print("Starting simple_httpd on port: ") + str(httpd.server_port)
httpd.serve_forever()

# 以上是用Python来构建一个Web服务器所必须的。

