# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):  # 初始化栈,将items初始化为一个list
        self.items = []

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

    def IsPopOrder(self, pushV, popV):
        num = 0
        while pushV[num] != popV[0]:
            if len(pushV) == len(popV) == 1:
                return False
            self.push(pushV[num])
            num += 1
        for i in range(num, len(pushV)):
            if pushV[i] == popV[0]:
                del popV[0]
            elif self.peek() == popV[0]:
                self.pop()
                del popV[0]
            else:
                self.push(pushV[i])
        for i in popV:
            if self.pop() == i:
                continue
            else:
                return False
        return True


if __name__ == '__main__':
    bat = Solution()
    push1 = [1]
    pop1 = [2]
    print bat.IsPopOrder(push1, pop1)