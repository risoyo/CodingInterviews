# -*- coding:utf-8 -*-
from Functions import Partition
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):  # 中分法,数字如果超过一半的话,中位数一定为该数
        if len(numbers) == 0:
            return 0
        middle = len(numbers) >> 1
        start = 0
        end = len(numbers) - 1
        parti = Partition.Partition()
        index = parti.partition_core(numbers, start, end)
        while index != middle:
            if index > middle:
                end = index - 1
                index = parti.partition_core(numbers, start, end)
            else:
                start = index + 1
                index = parti.partition_core(numbers, start, end)
        result = numbers[middle]
        if self.check_more_than_half(numbers, result):
            return result
        else:
            return 0

    def MoreThanHalfNum_Solution_2(self, numbers):  # 计数法,数字出现的次数比其他数字出现次数和还大,所以遇到其他的数次数自减1,遇到自己自加1
        if len(numbers) == 0:  # 最后的count一定大于0
            return 0
        count = 1
        num = numbers[0]
        for i in range(1, len(numbers)):
            if num == numbers[i]:
                count += 1
            else:
                count -= 1
            if count == 0:
                num = numbers[i]
                count = 1
        if self.check_more_than_half(numbers, num):
            return num
        else:
            return 0

    def check_more_than_half(self, numbers, number):
        times = 0
        for i in numbers:
            if i == number:
                times += 1
        if times * 2 <= len(numbers):
            return False
        else:
            return True


if __name__ == '__main__':
    bat = Solution()
    num = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    num2 = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    print bat.MoreThanHalfNum_Solution_2(num2)
