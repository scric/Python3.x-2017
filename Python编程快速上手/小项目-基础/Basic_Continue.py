# 用 continue 写一个循环 , 要求输入正确的名字和口令

while True:
    print("Who are you ?(张鑫)")
    name = input()
    if name != "张鑫":
        continue
    while True:
        print("Hello ,张鑫, Who are you ?(Superman)")
        keywords = input()
        if keywords != "Superman":
            continue
        else:
            break
    break
print("Access granted.")  # 授予访问权限(笑)


# 这个程序有点问题, 因为你名字输入正确以后, 就算 keyword 输入错误, 也不应该要求你重新输入一遍名字.
# 所以应该重新修改一下
# 还能再精简吗?