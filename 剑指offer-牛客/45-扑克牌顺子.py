# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        if len(numbers) == 0:
            return False
        numbers.sort()
        count_0 = 0
        for i in numbers:
            if i == 0:
                count_0 += 1
            else:
                break
        num1 = count_0
        num2 = num1 + 1
        while num2 < 5:
            if numbers[num2] - numbers[num1] == 1:
                num1 += 1
                num2 += 1
                continue
            elif numbers[num2] == numbers[num1]:
                return False
            else:
                if count_0 + 1 == numbers[num2] - numbers[num1]:
                    count_0 = 0
                    num1 += 1
                    num2 += 1
                    continue
                elif count_0 + 1 < numbers[num2] - numbers[num1]:
                    return False
                else:
                    count_0 -= numbers[num2] - numbers[num1] - 1
                    num1 += 1
                    num2 += 1
                    continue
        return True


if __name__ == '__main__':
    bat = Solution()
    num = [0, 0, 2, 2, 3]
    num2 = []
    print bat.IsContinuous(num2)
