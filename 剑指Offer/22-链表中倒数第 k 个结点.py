# -*- coding:utf-8 -*-
from Functions import ListNode

class Solution:
    def FindKthToTail(self, head, k):
        p2 = head.head
        for i in range(k):
            if p2.next is not None:
                p2 = p2.next
            else:
                return 0
        while p2 is not None:
            p2 = p2.next
            head.head = head.head.next
        print head.head.data


if __name__ == '__main__':
    bat = Solution()
    num = [1, 2, 3, 4, 5, 6]
    list = ListNode.LinkedList()
    for i in num:
        list.append(i)
    bat.FindKthToTail(list, 3)
