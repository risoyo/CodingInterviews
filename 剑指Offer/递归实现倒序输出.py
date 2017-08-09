# coding = utf-8
# 递归的方法实现倒序输出

def offorder(list1):
    i = 0
    if i <= len(list1):
        offorder(list1)


if __name__ == '__main__':
    list1 = [1, 3, 6, 7, 9, 10, 12]
    offorder(list1)
    