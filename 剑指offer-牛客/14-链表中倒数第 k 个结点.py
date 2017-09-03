# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):  # 使用两个指针来指向倒数第k个节点
        if k == 0 or head is None:  # 当k为0或者head不存在时,直接返回
            return

        li = head  # 定义两个指针
        la = head

        for x in range(k - 1):
            if li.next is None:  # 当链表中只有一个节点时,直接返回
                return
            if li.next is None and x is k - 1:  # 当链表中只有一个节点且要求返回倒数第一个节点时,head即为要找的节点
                return head
            li = li.next  # li前进k个节点

        while li.next is not None:  # li与la同时向前,直到li到达尾节点,此时la即为要找的节点
            li = li.next
            la = la.next

        return la


if __name__ == '__main__':
    bat = Solution()
    num = [1, 2, 3, 4, 5, 6]

