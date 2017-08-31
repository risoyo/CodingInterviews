# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        if len(numbers) == 0:
            return ""
        num = list()   # 新建数组用于存储最小数的序列
        num.append(numbers[0])
        for i in range(1, len(numbers)):  # 遍历numbers中的元素
            for j in range(len(num)):  # 遍历新数组num中的元素
                if self.compare(num[-1], numbers[i]):  # 若
                    num.append(numbers[i])
                    break
                if self.compare(numbers[i], num[j]):
                    num.insert(j, numbers[i])
                    break
                else:
                    continue
        num = map(str, num)
        total = ""
        for i in num:
            total += i
        return int(total)

    def compare(self, num1, num2):  # num1 < num2
        num1 = str(num1)
        num2 = str(num2)
        if len(num2) > len(num1):
            lenth = len(num2)
        else:
            lenth = len(num1)
        for i in range(lenth):
            if i >= len(num1):
                sec1 = num1[0]
                sec2 = num2[i]
            elif i >= len(num2):
                sec2 = num2[0]
                sec1 = num1[i]
            else:
                sec1 = num1[i]
                sec2 = num2[i]
            if int(sec1) > int(sec2):  # 第一个数较大
                return False
            elif int(sec1) < int(sec2):  # 第二个数较大
                return True
        return True  # 两个数相等


if __name__ == '__main__':
    bat = Solution()
    num = [3, 32, 321]
    num2 = [3, 5, 1, 4, 2]
    num3 = [1, 11, 111]
    num4 = []
    number = bat.PrintMinNumber(num)
    print number
