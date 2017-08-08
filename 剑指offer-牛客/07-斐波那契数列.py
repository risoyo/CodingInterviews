# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        result = [0, 1]
        if n < 2:
            return result[n]
        fib1 = 1
        fib2 = 0
        fibn = 0
        for i in range(1, n):
            fibn = fib1 + fib2
            fib2 = fib1
            fib1 = fibn
        return fibn