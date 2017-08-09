# coding=utf-8
from Functions import ListNode


def delete_node(link_list, list_delete):
    if link_list.head.next is None and link_list.head.data == list_delete:  # 当需要删除的为头节点且链表中只有一个节点时,直接将其置为None
        link_list.head = None
    elif link_list.tail.data == list_delete:  # 当需要删除的节点为尾节点时,遍历链表,找到链表倒数第二个节点,然后使其next为next.next
        while link_list.head.next is not link_list.tail:
            link_list.head = link_list.head.next
        link_list.head.next = None
    else:  # 正常删除,只对链表遍历一遍,时间复杂度趋近于o(1)
        while link_list.head.next is not None:
            if link_list.head.data == list_delete:  # 当找到需要删除的节点时
                link_list.head.data = link_list.head.next.data  # 将下一个节点的值赋给当前节点
                link_list.head.next = link_list.head.next.next  # 然后使其next为next.next,删除下一个节点
                break
            link_list.head = link_list.head.next


if __name__ == '__main__':
    list_number = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    link_list = ListNode.LinkedList()
    for i in list_number:
        link_list.append(i)
    link_list.delete_node(link_list, 48)
    if link_list.head is None:
        print "链表已空,删除了唯一的个节点"
    else:
        while link_list.head is not None:
            print link_list.head.data,
            link_list.head = link_list.head.next
