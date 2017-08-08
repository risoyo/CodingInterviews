# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray2(self, rotateArray):
        if rotateArray:
            left = 0
            right = len(rotateArray)-1
            middle = (left + right)/2
            while middle != right and middle != left:
                if rotateArray[middle] < rotateArray[left]:
                    right = middle
                    middle = (left + middle) / 2
                if rotateArray[middle] > rotateArray[right]:
                    left = middle
                    middle = (right + middle) / 2
            return rotateArray[right]
        else:
            return 0


if __name__ == '__main__':
    bat = Solution()
    num = [1727, 1870, 1943, 2383, 2392, 2996, 3282, 3812, 3903, 4465, 4605, 4665, 4772, 4828, 5142, 5437, 5448, 5668,
           5706, 5725, 6300, 6335, 6501, 6828, 6963, 7036, 7422, 7674, 8146, 8468, 8704, 8717, 9170, 9359, 9719, 9895,
           9896, 9913, 9962, 154, 293, 334, 492, 1323, 1479, 1539]
    print bat.minNumberInRotateArray2(num)
