#coding=utf-8
coin_total = 20
min_coin = [None for i in range(20)]
min_coin[0] = 0
coin = [1, 3, 5]
plan = []
result = []
for i in range(1, 12):
    for j in coin:
        if i >= j:
            plan.append(i - j)
    plan.sort()
    min_coin[i] = min_coin[plan[0]] + 1
    result.append([i, min_coin[i]])
    plan = []
print 'sum',
print '  ',
print 'min coin'
for i in result:
    print i[0],
    print '    ',
    print i[1]

