#coding=utf-8
# col 列 row 行


def find(num1, alpha):
    row = len(alpha)  # 获取总行数
    col = len(alpha[1])  # 获取总列数
    rows = 0  # 从第0行开始
    cols = col - 1  # 从最后一列开始
    while rows < row and cols >= 0:
        if num1 == alpha[rows][cols]:
            print ("found")
            break
        elif alpha[rows][cols] > num1:
            cols = cols - 1
        else:
            rows = rows + 1


if __name__ == '__main__':

    numbers = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    for num in numbers:
        for nu in num:
            print nu,
            print ' ',
        print " "

    catch = int(raw_input("输入要找的数"))
    find(catch, numbers)
