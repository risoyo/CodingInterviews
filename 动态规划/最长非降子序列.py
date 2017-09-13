# coding=utf-8
num = [5, 3, 4, 8, 6, 7]
d = [0 for i in range(len(num))]
d[0] = 1
result = []
numbers = []
result.append([0, d[0]])
numbers.append([num[0]])
for i in range(1, len(num)):  # 将num[i]的值加入某个子序列,使其变为num[i]下的最长子序列
    d[i] = 1
    for j in range(0, i):  # 遍历num[i]之前的数,查找每个数的最长子序列
        if num[i] >= num[j] and d[j] + 1 > d[i]:  # 当前num[i]的值大于num[j]的值且d[j] + 1大于当前的d[i],证明该子序列更长
            d[i] = d[j] + 1
    result.append([i, d[i]])
for i in result:
    print i[0],
    print '    ',
    print i[1]
