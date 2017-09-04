# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        if num1 == 0:
            return num2
        if num2 == 0:
            return num1
        sum = 0
        carry = 0
        while num2 != 0:
            sum = num1 ^ num2
            carry = (num1 & num2) << 1
            num1 = sum
            num2 = carry
        return num1


if __name__ == '__main__':
    bat = Solution()
    print bat.Add(1111, 1211)