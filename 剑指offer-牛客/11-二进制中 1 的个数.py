# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        count = 0
        for i in range(0, 32):
            num = n >> i  # 将num右移i位,逐个将num中的数移到最左边
            num2 = num & 1  # 将右移后的数,与1做按位与,1即为0000(31个0)1,除了最右其他位全为0,将num与1做按位与的时候,若num最右为1,则num2为1,若num最右为0,则num2为0
            count += num2  # 统计num2为0的次数,即为二进制数中1的个数
        return count


if __name__ == '__main__':
    bat = Solution()
    print bat.NumberOf1(0)
