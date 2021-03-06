# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        if base == 0:  # 若底数为0,返回0
            return 0
        if exponent == 0:  # 若幂为0,返回1
            return 1
        number = base
        for i in range(1, abs(exponent)):  # 乘exponent次
            base *= number
        if exponent < 0:  # 若幂小于0,则返回乘积分之一
            return 1 / float(base)  # 在计算除法时,分子分母中的一个为float型则结果为float型,否则为int型,不加float(base)的话除得的结果为0
        return base


if __name__ == '__main__':
    bat = Solution()
    print bat.Power(2, 0)
