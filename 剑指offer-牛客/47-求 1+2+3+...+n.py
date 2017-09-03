# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.sum = 0

    def Sum_Solution(self, n):
        # write code here
        def qiusum(n):
            self.sum += n
            n -= 1
            return n > 0 and self.Sum_Solution(n)

        qiusum(n)
        return self.sum

if __name__ == '__main__':
    bat = Solution()
    print bat.Sum_Solution(10)