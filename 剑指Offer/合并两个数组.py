#coding=utf-8


def combine1(l1, l2):  # 空间换时间,创建了另一个字符串存储比较后的数字
    len1 = len(l1)
    len2 = len(l2)
    i = 0
    num1 = 0
    num2 = 0
    listshow = []
    while num1 < len1 and num2 < len2:
        if l1[num1] < l2[num2]:
            listshow.append(l1[num1])
            num1 = num1 + 1
        elif l1[num1] == l2[num2]:
            listshow.append(l1[num1])
            num1 = num1 + 1
            num2 = num2 + 1
        elif l1[num1] > l2[num2]:
            listshow.append(l2[num2])
            num2 = num2 + 1
    if num1 != len1:
        for i in l1[num1:]:
            listshow.append(i)
    if num2 != len2:
        for i in l2[num2:]:
            listshow.append(i)
    return listshow


def combine2(l1, l2):  # 时间换空间,直接在l1中进行插入操作
    num1 = 0
    while len(l2) > 0:
        n = len(l2)
        if l1[-1] < l2[0]:
            for i in l2:
                l1.append(i)
            break
        if l1[num1] < l2[0]:
            num1 = num1 + 1
        elif l1[num1] == l2[0]:
            l2.pop(0)
            num1 = num1 + 1
        elif l1[num1] > l2[0]:
            l1.insert(num1, l2[0])
            l2.pop(0)
            num1 = num1 + 1
        else:
            print ('woops')
    return l1

if __name__ == '__main__':
    list1 = [1, 3, 6, 7, 9, 10, 12]
    list2 = [2, 4, 5, 6, 8, 14, 16, 19, 20]
    list1 = combine1(list1, list2)
    for i in list1:
        print i
