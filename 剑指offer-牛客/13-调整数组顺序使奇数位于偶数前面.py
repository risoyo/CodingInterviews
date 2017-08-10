# -*- coding:utf-8 -*-

class Solution:
    def reOrderArray(self, array):
        re_order = []  # 新建一个数组用于保存调整后的数
        odd = 0  # 保存当前奇数的位置
        for i in range(len(array)):  # 遍历array中的元素
            if array[i] % 2 == 0:  # 当i为偶数时,append到新数组最后面
                re_order.append(array[i])
            else:  # 当i为奇数时,在新数组的odd位置插入i
                re_order.insert(odd, array[i])
                odd += 1
        return re_order


if __name__ == '__main__':
    bat = Solution()
    number_list = [1, 2, 3, 4, 5, 6, 7]
    number_list = bat.reOrderArray(number_list)
    print number_list
