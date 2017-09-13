#coding=utf-8
coin_total = 20
min_coin = [None for i in range(20)]  # 依次存入i元需要几个硬币
min_coin[0] = 0  # 设置初始值,凑齐0元需要0个硬币
coin = [1, 3, 5]  # 硬币有1,3,5三种
plan = []  # 递推过程中分别将当前的金额减去coin中存在的面值,存入相减后的金额
result = []  # 保存结果
for i in range(1, 12):  # 递推过程,从初始值下一个开始,i表示金额,从1到11
    for j in coin:  # 遍历coin中硬币的值
        if i >= j:  # 若金额大于当前币值
            plan.append(min_coin[i - j])  # 当前币值减去每个硬币值之后的值即为增加一个硬币之后,还需要的剩余值,在min_coin中查找剩余值对应的最少硬币数
    plan.sort()  # 对plan进行排序,寻找到最小的需要的硬币数,这几步对应方程应为d(i)=min{d(i-Vj)+1}
    min_coin[i] = min_coin[plan[0]] + 1  # 当前金额所需最小硬币数即为plan中最小值加一
    result.append([i, min_coin[i]])  # 在result中添加金额-硬币数的对应关系
    plan = []  # 清空plan
print 'sum',
print '  ',
print 'min coin'
for i in result:
    print i[0],
    print '    ',
    print i[1]

