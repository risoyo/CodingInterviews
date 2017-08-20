# -*- coding:utf-8 -*-
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if pHead is None:
            return
        head = pHead
        while head is not None:
            node = RandomListNode(head.label)
            node.next = head.next
            node.random = None
            head.next = node
            head = node.next
        head = pHead
        node = head.next
        while head is not None:
            if head.random is not None:
                node.random = head.random.next
            head = node.next
        head = pHead
        clone_head = clone_node = head.next
        head.next = clone_node.next
        node = node.next
        while node is not None:
            clone_node.next = head.next
            node = node.next
            head.next = node.next
            head = head.next
        return clone_head

    def Clone_2(self, pHead):
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
