# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        reversed_string = self.reverse_string(s[:n], s[n:])
        return reversed_string

    def reverse_string(self, s1, s2):
        return s2 + s1


if __name__ == '__main__':
    bat = Solution()
    string = "abcdefg"
    num = 2
    print bat.LeftRotateString(string, num)
