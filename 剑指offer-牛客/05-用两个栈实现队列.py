# -*- coding:utf-8 -*-
from Functions import Stack


class Solution:
    def __init__(self):
        self.items = Stack.Stack()

    def push(self, node):
        self.items.push(node)

    def pop(self):
        self.items.pop()


if __name__ == '__main__':
    dic = Stack.Stack()
    dic.push('111')
    print dic.size()
    print dic.pop()
