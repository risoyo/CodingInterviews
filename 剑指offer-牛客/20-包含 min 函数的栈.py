# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):  # 初始化栈,将items初始化为一个list
        self.items = []

    def push(self, node):
        self.items.append(node)

    def size(self):
        return len(self.items)

    def pop(self):
        item = self.items[-1]
        del self.items[-1]
        return item

    def top(self):
        return self.items[-1]

    def min(self):
        min_num = self.items[0]
        for i in self.items:
            if i < min_num:
                min_num = i
        return min_num
            

if __name__ == '__main__':
    bat = Solution()
    bat.push('1')
    bat.push('2')
    bat.push('5')
    bat.push('3')
    bat.push('7')
    bat.push('4')
    print bat.min()
