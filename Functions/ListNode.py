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


if __name__ == '__main__':
    list_number = [3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    link_list = LinkedList()
    for i in list_number:
        link_list.append(i)
    while link_list.head is not None:
        print link_list.head.data,
        link_list.head = link_list.head.next
