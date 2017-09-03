# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if len(array) == 0:
            return []
        head = 0
        tail = len(array) - 1
        while head < tail:
            if array[head] + array[tail] < tsum:
                head += 1
            elif array[head] + array[tail] > tsum:
                tail -= 1
            else:
                return array[head], array[tail]
        return []


if __name__ == '__main__':
    bat = Solution()
    num = [1,2,4,7,11,15]
    num2 = [1,2,4,7,11,16]
    print bat.FindNumbersWithSum(num2, 10)