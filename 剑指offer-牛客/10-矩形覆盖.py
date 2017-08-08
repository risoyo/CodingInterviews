# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        if number == 1:
            return 1
        elif number == 0:
            return 0
        elif number == 2:
            return 2
        jt = 0
        j1 = 1
        j2 = 2
        for i in range(1, number - 1):
            jt = j1 + j2
            j1 = j2
            j2 = jt
        return jt

if __name__ == '__main__':
    bat = Solution()
    print bat.rectCover(4)