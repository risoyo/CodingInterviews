# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum == 0:
            return [[0]]
        possible_num = []
        for i in range(1, tsum):
            possible_num.append(i)
        list_number = []
        number = []
        num1 = 0
        num2 = 1
        total = 0
        while num1 < len(possible_num):
            total += possible_num[num1]
            number.append(possible_num[num1])
            if num2 >= len(possible_num):
                break
            while total != tsum and num2 < len(possible_num):
                total += possible_num[num2]
                number.append(possible_num[num2])
                num2 += 1
                if total == tsum:
                    list_number.append(number)
                    number = []
                    num1 += 1
                    num2 = num1 + 1
                    total = 0
                    break
                elif total > tsum:
                    number = []
                    num1 += 1
                    num2 = num1 + 1
                    total = 0
                    break

        return list_number


if __name__ == '__main__':
    bat = Solution()
    print bat.FindContinuousSequence(0)
