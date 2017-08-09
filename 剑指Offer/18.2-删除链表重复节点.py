# coding=utf-8
from Functions import ListNode


def delete_duplication(link_list):
    pre_node = None
    node = link_list.head
    while node is not None:
        next_node = node.next
        need_delete = False
        if next_node is not None and next_node.data == node.data:
            need_delete = True
        if need_delete is not True:
            pre_node = node
            node = node.next
        else:
            value = node.data
            to_be_del = node
            while to_be_del is not None and to_be_del.data == value:
                next_node = to_be_del.next
                link_list.delete_node(link_list, value)
                to_be_del = None
                to_be_del = next_node
            if pre_node is None:
                link_list.head = next_node
            else:
                pre_node.next = next_node
            node = next_node

if __name__ == '__main__':
    list_number = [1, 2, 3, 3, 4, 4, 5]  # 1,2,5
    link_list = ListNode.LinkedList()
    for i in list_number:
        link_list.append(i)
    delete_duplication(link_list)
    while link_list.head is not None:
        print link_list.head.data,
        link_list.head = link_list.head.next