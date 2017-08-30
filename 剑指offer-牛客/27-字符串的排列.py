# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        self.vis = [0 for i in range(len(ss))]
        self.ans = []
        self.temp = ""
        self.DFS(0, ss)
        return sorted([i for i in set(self.ans)])

    def DFS(self, sum, ss):
        if sum == len(ss):
            self.ans.append(self.temp)
            return
        for idx in range(len(ss)):
            if self.vis[idx] == 0:
                self.vis[idx] = 1
                self.temp += ss[idx]
                self.DFS(sum + 1, ss)
                self.temp = self.temp[:-1]
                self.vis[idx] = 0

    # def Permutation(self, ss):
    #     if ss is "":
    #         return []
    #     string_per = []
    #     for i in itertools.permutations(ss,len(ss)):
    #         ele = None
    #         i = str(i)
    #         for num in i:
    #             if 'a' <= num <= 'z' or 'A' <= num <= 'Z':
    #                 if ele is None:
    #                     ele = num
    #                 else:
    #                     ele += num
    #         string_per.append(ele)
    #     string_per = list(set(string_per))
    #     string_per.sort()
    #     return string_per




if __name__ == '__main__':
    bat = Solution()
    string_raw = "aab"
    string_raw = str(string_raw)
    string_compelete = bat.Permutation(string_raw)
    for i in string_compelete:
        print i,
