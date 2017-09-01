# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        if len(data) == 0 or k is "":
            return 0
        first_k = self.get_first_k(data, k, 0, len(data) - 1)
        last_k = self.get_last_k(data, k, 0, len(data) - 1)
        if first_k == -1 and last_k == -1:
            return 0
        return last_k - first_k +1

    def get_first_k(self, data, k, start, end):
        if start > end:
            return -1
        middle_index = (start + end) / 2
        middle_val = data[middle_index]
        if k == middle_val:
            if (middle_index > 0 and data[middle_index - 1] != k) or middle_index == 0:
                return middle_index
            else:
                end = middle_index - 1
        elif k < middle_val:
            end = middle_index - 1
        else:
            start = middle_index + 1
        return self.get_first_k(data, k, start, end)

    def get_last_k(self, data, k, start, end):
        if start > end:
            return -1
        middle_index = (start + end) / 2
        middle_val = data[middle_index]
        if k == middle_val:
            if (middle_index < len(data) - 1 and data[middle_index + 1] != k) or middle_index == len(data) - 1:
                return middle_index
            else:
                start = middle_index + 1
        elif k < middle_val:
            end = middle_index - 1
        else:
            start = middle_index + 1
        return self.get_last_k(data, k, start, end)


if __name__ == '__main__':
    bat = Solution()
    num = [1,2,3,3,3,3]
    print bat.GetNumberOfK(num, 3)
