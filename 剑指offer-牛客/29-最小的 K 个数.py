# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        if len(tinput) == 0 or k is None or k == 0:
            return []
        elif k > len(tinput):
            return []
        num = []
        for i in tinput[0:k]:
            num.append(i)
        num.sort()
        for i in tinput[k:]:
            if i < num[k - 1]:
                del num[k - 1]
                num.append(i)
                num.sort()
        return num


if __name__ == '__main__':
    bat = Solution()
    num = [4, 5, 1, 6, 2, 7, 3, 8]
    print bat.GetLeastNumbers_Solution(num, 4)
