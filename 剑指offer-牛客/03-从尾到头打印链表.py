# -*- coding:utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def printListFromTailToHead(self, listNode):
        l = []
        while listNode:
            l.insert(0, listNode.val)
            listNode = listNode.next
        return l


if __name__ == '__main__':
    bat = Solution()
    num = [5, 6, 7, 8]
    list = ListNode(num)
    bat.printListFromTailToHead(list)
