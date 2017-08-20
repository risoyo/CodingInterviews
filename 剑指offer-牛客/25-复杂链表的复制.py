# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        if not pHead:
            return None
        cur = pHead
        while cur:
            next = cur.next
            cpy = RandomListNode(cur.label)
            cur.next = cpy
            cpy.next = next
            cur = next
        cur = pHead
        while cur:
            next = cur.next.next
            cpy = cur.next
            if cur.random:
                cpy.random = cur.random.next
            else:
                cpy.random = None
            cur = next
        newHead = pHead.next
        cur = pHead
        while cur:
            next = cur.next.next
            cpy = cur.next
            cur.next = next
            if next:
                cpy.next = next.next
            else:
                cpy.next = None
            cur = next
        return newHead


if __name__ == '__main__':
    bat = Solution()
    head = RandomListNode('2')
    bat.Clone(head)
