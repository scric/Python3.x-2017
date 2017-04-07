# 建立一个井字棋
# 用 top, mid, low 分别表示棋盘的上中下,
# 用 L, M, R 分别表示棋盘的左中右 .
# 用字符 'O', 'X' 表示黑白棋子

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


# 这样我们就表示了一个井字棋
# 如何输出棋盘呢?
def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

# printBoard(theBoard)

# 接下来我们要获取用户的输入,
# 棋盘总共能下九个子, 所以下完之后就要重新开始
count = 0
turn = 'X'
while True:
    printBoard(theBoard)
    print(' Turn for ' + turn + '. Move on which space')
    move = input()
    if move not in theBoard:
        print("别淘气, 请重新下一次吧")
        continue
    else:
        if 'X' in theBoard[move]:
            print("傻了吧你, 请重新落子吧")
            continue
        elif 'O' in theBoard[move]:
            print("傻了吧你, 请重新落子吧")
            continue
        else:
            theBoard[move] = turn
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'
            if count != 9:
                count += 1
            else:
                print("游戏结束")
                break
        print(count)
printBoard(theBoard)

# 还可以改进吗?
