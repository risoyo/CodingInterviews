# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):  # 44ms
        if len(s) == 0:
            return -1
        dict_unique = {}
        for i in s:
            if i in dict_unique:
                dict_unique[i] += 1
            else:
                dict_unique.update({i: 1})
        for i in range(len(s)):
            if dict_unique[s[i]] == 1:
                return i


if __name__ == '__main__':
    bat = Solution()
    string = "abaccdeff"
    print bat.FirstNotRepeatingChar(string)
