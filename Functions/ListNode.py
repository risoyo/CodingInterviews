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
        if link_list.head.next is None and link_list.head.data == list_delete:
            link_list.head = None
        elif link_list.tail.data == list_delete:
            while link_list.head.next is not link_list.tail:
                link_list.head = link_list.head.next
            link_list.head.next = None
        else:
            while link_list.head.next is not None:
                if link_list.head.data == list_delete:
                    link_list.head.data = link_list.head.next.data
                    link_list.head.next = link_list.head.next.next
                    break
                link_list.head = link_list.head.next


if __name__ == '__main__':
    list_number = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    link_list = LinkedList()
    for i in list_number:
        link_list.append(i)
    link_start = link_list.head
    link_list.delete_node(link_list, 48)
    while link_start is not None:
        print link_start.data,
        link_start = link_start.next
