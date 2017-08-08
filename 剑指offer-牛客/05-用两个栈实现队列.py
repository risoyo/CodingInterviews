#coding=utf-8
from Functions import Stack


class Solution:
    def __init__(self):
        self.items1 = Stack.Stack()
        self.items2 = Stack.Stack()

    def push(self, node):
        self.items1.push(node)

    def pop(self):
        if self.items2.isEmpty():
            while self.items1.size() > 0:
                self.items2.push(self.items1.pop())
        return self.items2.pop()

    def isEmpty(self):
        if self.items1.size() > 0 or self.items2.size() > 0:
            return 1
        else:
            return 0


if __name__ == '__main__':
    dic = Solution()
    dic.push('a')
    dic.push('b')
    print dic.pop()
    dic.push('c')
    dic.push('d')
    print dic.pop()
    print dic.pop()
    dic.push('e')
    print dic.pop()
    print dic.pop()

