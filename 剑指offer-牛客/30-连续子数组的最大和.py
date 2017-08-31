# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        if len(array) == 0:
            return 0
        max_sum = maxi = array[0]
        for i in range(1, len(array)):
            if maxi <= 0:
                maxi = array[i]
            else:
                maxi += array[i]
            if maxi > max_sum:
                max_sum = maxi
        return max_sum


if __name__ == '__main__':
    bat = Solution()
    num = [6, -3, -2, 7, -15, 1, 2, 2]
    print bat.FindGreatestSumOfSubArray(num)
