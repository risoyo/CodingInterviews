# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        if pHead1 is None and pHead2 is not None:  # 若pHead1空,pHead2非空,直接返回pHead2
            return pHead2
        elif pHead2 is None and pHead1 is not None:  # 若pHead2空,pHead1非空,直接返回pHead1
            return pHead1
        elif pHead1 is None and pHead2 is  None:  # 若pHead1,pHead2都为空,返回None
            return None
        if pHead1.val < pHead2.val:  # 初始化头节点,将pHead1和pHead2头节点中较小的一个初始化为新链表的头节点
            link_list = ListNode(pHead1.val)
            pHead1 = pHead1.next
        else:
            link_list = ListNode(pHead2.val)
            pHead2 = pHead2.next
        list_tail = link_list  # 新建一个指针,总是指向新链表的末尾,现在链表中只有一个节点,所以头节点即为尾节点
        while pHead1 is not None and pHead2 is not None:  # 当pHead1与pHead2均非空时,循环遍历它俩
            if pHead1.val < pHead2.val:  # 若pHead1当前节点的值值小于pHead2当前节点的值
                node = ListNode(pHead1.val)  # 初始化一个节点node,保存pHead1的值,将node接在新链表末尾
                list_tail.next = node
                list_tail = list_tail.next
                pHead1 = pHead1.next
            elif pHead1.val == pHead2.val:  # 两个值相等时,将两个值都接在链表末尾
                node = ListNode(pHead1.val)
                list_tail.next = node
                list_tail = list_tail.next
                pHead1 = pHead1.next
                node = ListNode(pHead2.val)
                list_tail.next = node
                list_tail = list_tail.next
                pHead2 = pHead2.next
            else:
                node = ListNode(pHead2.val)
                list_tail.next = node
                list_tail = list_tail.next
                pHead2 = pHead2.next
        if pHead1 is not None:  # 若循环结束后pHead1非空,将pHead1剩余的节点接在链表后面
            list_tail.next = pHead1
        if pHead2 is not None:
            list_tail.next = pHead2
        return link_list


if __name__ == '__main__':
    bat = Solution()
    num = []
    num2 = []
    if len(num) != 0:
        link_list1 = ListNode(num[0])
        link_head1 = link_list1
    else:
        link_list1 = None
    if len(num2) != 0:
        link_list2 = ListNode(num2[0])
        link_head2 = link_list2
    else:
        link_list2 = None
    for i in range(1, len(num)):
        node = ListNode(num[i])
        link_head1.next = node
        link_head1 = link_head1.next
    for i in range(1, len(num2)):
        node = ListNode(num2[i])
        link_head2.next = node
        link_head2 = link_head2.next
    list_merge = bat.Merge(link_list1, link_list2)
    # while link_list1 is not None:
    #     print link_list1.val,
    #     link_list1 = link_list1.next
    # while link_list2 is not None:
    #     print link_list2.val,
    #     link_list2 = link_list2.next
    while list_merge is not None:
        print list_merge.val,
        list_merge = list_merge.next
