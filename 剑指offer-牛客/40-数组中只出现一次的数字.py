# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if len(array) == 0:
            return []
        num_onece = {}
        for i in array:
            if num_onece.get(i):
                num_onece.pop(i)
            else:
                num_onece[i] = 1
        num = []
        for i, j in num_onece.iteritems():
            num.append(i)
        return num


if __name__ == '__main__':
    bat = Solution()
    num = [2, 4, 3, 6, 3, 2, 5, 5]
    bat.FindNumsAppearOnce(num)
