from nester import print_lol
movies = ["The Holy Grail",1975,"Terry Jones & Terry Gilliam",91,
          ["Graham Chapman",
           ["Michael Palin","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]

print_lol(movies)

"""
   如何导入自定义的模块？
法一:
   将 module 和 测试代码放到同一个目录下
   import module
使用时应该注意将功能带上。
   比如 module 名称是 nester
   功能是 print_lol()
   则使用该功能应该是
   nester.print_lol(*)

法二：
   将 module 和 测试代码放到同一个目录下
   from module import foundation
   比如 module 名称是 nester
   功能是 print_lol()
   则使用该功能可以是
   print_lol(*)

需要注意的是：
   如果你的当前命名空间已经定义了一个print_lol()的函数，
   这个特定import语句会用导入的函数覆盖掉你自己定义的函数，
   而这并不是你原来所期望的行为

"""