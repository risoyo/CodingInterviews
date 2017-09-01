# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if pHead1 is None or pHead2 is None:
            return
        count1 = 0
        count2 = 0
        count_phead1 = pHead1
        count_phead2 = pHead2
        while count_phead1 is not None:
            count1 += 1
            count_phead1 = count_phead1.next
        while count_phead2 is not None:
            count2 += 1
            count_phead2 = count_phead2.next
        while count1 > count2:
            pHead1 = pHead1.next
            count1 -= 1
        while count1 < count2:
            pHead2 = pHead2.next
            count2 -= 1

        while pHead1 != pHead2:
            print pHead1.val
            pHead1 = pHead1.next
            print pHead2.val
            pHead2 = pHead2.next

        return pHead1


if __name__ == '__main__':
    bat = Solution()
    num1 = [1, 2, 3, 6, 7]
    ln1 = ListNode(num1[0])
    ln1_head = ln1
    for i in num1[1:]:
        temp = ListNode(i)
        ln1_head.next = temp
        ln1_head = ln1_head.next
    num2 = [4, 5, 6, 7]
    ln2 = ListNode(num2[0])
    ln2_head = ln2
    for i in num2[1:]:
        temp = ListNode(i)
        ln2_head.next = temp
        ln2_head = ln2_head.next
    print bat.FindFirstCommonNode(ln1, ln2)
