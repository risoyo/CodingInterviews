#coding=utf-8
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def delete_node(self, link_list, list_delete):
        list_start = link_list.head
        if list_start.next is None and list_start.data == list_delete:  # 当需要删除的为头节点且链表中只有一个节点时,直接将其置为None
            list_start = None
        elif link_list.tail.data == list_delete:  # 当需要删除的节点为尾节点时,遍历链表,找到链表倒数第二个节点,然后使其next为next.next
            while list_start.next is not link_list.tail:
                list_start = list_start.next
            list_start.next = None
        else:  # 正常删除,只对链表遍历一遍,时间复杂度趋近于o(1);另一种删除方法是使用两个指针,一个指向需要删除节点,另一个指向前一个节点,然后删除
            while list_start.next is not None:
                if list_start.data == list_delete:  # 当找到需要删除的节点时
                    list_start.data = list_start.next.data  # 将下一个节点的值赋给当前节点
                    list_start.next = list_start.next.next  # 然后使其next为next.next,删除下一个节点
                    break
                list_start = list_start.next


if __name__ == '__main__':
    list_number = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    link_list = LinkedList()
    for i in list_number:
        link_list.append(i)
    link_list.delete_node(link_list, 48)
    while link_list.head is not None:
        print link_list.head.data,
        link_list.head = link_list.head.next
