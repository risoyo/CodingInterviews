# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        reverse_head = pHead
        node = pHead
        node_pre = None
        while node is not None:
            node_next = node.next
            if node.next is None:
                reverse_head = node
            node.next = node_pre
            node_pre = node
            node = node_next
        return reverse_head


if __name__ == '__main__':
    bat = Solution()
    num = [1, 2, 3, 4, 5]
    link_list = ListNode(num[0])
    link_head = link_list
    for i in range(1, len(num)):
        node = ListNode(num[i])
        link_head.next = node
        link_head = link_head.next
    link_reverse = bat.ReverseList(link_list)
    while link_reverse is not None:
        print link_reverse.val,
        link_reverse = link_reverse.next
