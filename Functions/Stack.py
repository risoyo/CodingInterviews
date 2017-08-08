#coding=utf-8
class Stack:
    def __init__(self):  # 初始化栈,将items初始化为一个list
        self.items = []

    def isEmpty(self):  # 判断栈是否为空,为空则返回1
        return len(self.items) == 0

    def push(self, item):  # 入栈
        self.items.append(item)

    def pop(self):  # 出栈
        item = self.items[-1]
        del self.items[-1]
        return item

    def peek(self):  # 返回栈顶元素且不删除
        return self.items[-1]

    def size(self):  # 返回栈中元素个数
        return len(self.items)

