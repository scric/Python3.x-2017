# 错误出现在 第二章-控制流  P37

name = ''
while not name:
    print("Enter your name: ")
    name = input()
print("How many guests will you have? ")
numeOfGuests = int(input())
if numeOfGuests:
    print("Be sure to have enough room for all your guests.")
    print('done')