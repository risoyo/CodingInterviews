# coding=utf-8
class Partition:
    def __init__(self):
        self.num_complete = []

    def partition(self, num, start, end):
        if num is "" or start is None or end is None:
            return False
        self.num_complete = num
        self.partition_core(self.num_complete, 0, len(num))

    def partition_core(self, num, start, end):
        if num is "" or start is None or end is None:
            return False
        index = 0
        if len(self.num_complete) == 0:
            self.num_complete = num
        self.num_complete[index], self.num_complete[end] = self.num_complete[end], self.num_complete[index]
        small = start - 1
        for index in range(start, end):
            if self.num_complete[index] < self.num_complete[end]:
                small += 1
                if small != index:
                    self.num_complete[index], self.num_complete[small] = self.num_complete[small], \
                                                                           self.num_complete[index]
        small += 1
        self.num_complete[end], self.num_complete[small] = self.num_complete[small], self.num_complete[end]
        return small


if __name__ == '__main__':
    num = [3, 1, 5, 7, 2, 4, 9, 6]
    bat = Partition()
    bat.partition_core(num, 0, len(num))
