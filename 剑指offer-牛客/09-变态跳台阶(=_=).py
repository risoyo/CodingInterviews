# -*- coding:utf-8 -*-


class Solution:  # 写是写出来了,但是并不懂为什么青蛙最多跳n阶的时候,跳法是2的n-1次方
    def jumpFloorII(self, number):
        if number == 1:
            return 1
        j = 2
        for i in range(1, number-1):
            j = j * 2
        return j


if __name__ == '__main__':
    bat = Solution()
    print bat.jumpFloorII(9)