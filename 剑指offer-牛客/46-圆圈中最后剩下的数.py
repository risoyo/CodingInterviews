# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def LastRemaining_Solution_list_node(self, n, m):  # 链表解法,创建一个循环链表
        if n == 0:
            return -1
        num = []
        for i in range(n):
            num.append(i)
        circle_list = ListNode(num[0])
        last_node = circle_list
        for i in num[1:]:
            node = ListNode(i)
            last_node.next = node
            last_node = last_node.next
        last_node.next = circle_list
        while circle_list != circle_list.next:
            for i in range(0, m - 2):
                circle_list = circle_list.next
            print circle_list.next.val
            circle_list.next = circle_list.next.next
            circle_list = circle_list.next
        return circle_list.val


if __name__ == '__main__':
    bat = Solution()
    print bat.LastRemaining_Solution_list_node(0, 0)
