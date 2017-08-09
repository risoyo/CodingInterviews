#coding=utf-8
def fibonacci1(num1):
    if num1 == 0:
        return 0
    elif num1 == 1:
        return 1
    else:
        return fibonacci1(num1 - 1)+fibonacci1(num1 - 2)


def fibonacci2(num1):
    result = [0, 1]
    if num1 < 2:
        return result[num1]
    fib1 = 1
    fib2 = 0
    fibn = 0
    for i in range(1, num1):
        fibn = fib1 + fib2
        fib2 = fib1
        fib1 = fibn
    return fibn


if __name__ == '__main__':
    print fibonacci1(100)
