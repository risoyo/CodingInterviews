#coding= utf-8
import time;


def sinsert1(num):  # 方法一,新建一个数组插入
    lenth = len(num)
    listc = []
    for i in range(lenth):
        if i == 0:
            listc.append(num[0])
            continue
        if listc[-1] < num[i]:
            listc.append(num[i])
        elif listc[-1] == num[i]:
            continue
        elif listc[-1] > num[i]:
            x = len(listc)
            while listc[x-1] > num[i]:
                x = x - 1
            listc.insert(x, num[i])
    return listc


def sinsert2(num):  # 方法二,不新建数组插入,使用insert
    for i in range(1, len(num)):  # 遍历数组
        if num[i-1] > num[i]:  # 如果当前num[i]的前一个数,比现在的大,那么把当前num[i]插入前面排序完成的部分中
            for j in range(0, i):  # 遍历排序完成的部分,找到num[i]应该属于的位置
                if num[j] > num[i]:  # 寻找刚好比num[i]大的数,将num[i]插入这个数之前
                    temp = num[i]
                    del num[i]  # 将num[i]保存到temp之后,先删除num[i]再插入
                    num.insert(j, temp)
    return num


def sinsert3(num):  # 方法三.不新建数组插入,不使用insert
    for i in range(1, len(num)):  # 遍历数组
        if num[i-1] > num[i]:  # 如果当前num[i]的前一个数,比现在的大,那么把当前num[i]插入前面排序完成的部分中
            j = i
            temp = num[i]
            while j >= 0:
                j = j - 1
                if num[j] > temp and j >= 0:
                    num[j+1] = num[j]
                    continue
                num[j+1] = temp
                break

    return num


def insert1_sort2(ary):
    n = len(ary)
    for i in range(1, n):
        if ary[i-1] > ary[i]:
            temp = ary[i]
            for j in range(i-1, -1, -1):
                if temp < ary[j]:
                    ary[j+1] = ary[j]
                    if j == 0:
                        ary[j] = temp
                        break
                    continue
                ary[j+1] = temp
                break
    return ary


def sort(ary):
    return insert1_sort2(ary)


def insert_sort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists


def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


if __name__ == '__main__':
    num = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    num2 = [3, 1, 5, 7, 2, 4, 9, 6]
    num3 = [3, 4, 1, 2, 5, 6]
    num4 = ['b', 'c', 'a', 'd']
    fake = raw_input()
    num5 = raw_input()
    listd = num5.split()
    listc = sinsert3(listd)
    for i in listc:
        print i,
    print listc
