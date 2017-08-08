# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        row = len(array)  # 获取总行数
        col = len(array[0])  # 获取总列数
        rows = 0  # 从第0行开始
        cols = col - 1  # 从最后一列开始
        while rows < row and cols >= 0:
            if target == array[rows][cols]:
                return True
            elif array[rows][cols] > target:
                cols = cols - 1
            else:
                rows = rows + 1
        return False

if __name__ == '__main__':
    bart = Solution()
    numbers = [[]]
    catch = 16
    if bart.Find(catch, numbers):
        print "found"
    else:
        print "none"
