# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        right = None
        if len(sequence) == 0:
            return False
        for i in range(len(sequence)):
            if sequence[i] > sequence[-1]:
                right = i
                break
        if right is None:
            return True
        for i in range(right, len(sequence)-1):
            if sequence[i] < sequence[-1]:
                return False
        return True


if __name__ == '__main__':
    bat = Solution()
    tree1 = [5, 7, 6, 9, 11, 10, 8]
    tree2 = [7, 4, 6, 5]
    tree3 = []
    tree4 = [1, 2, 3, 6]
    print bat.VerifySquenceOfBST(tree1)
