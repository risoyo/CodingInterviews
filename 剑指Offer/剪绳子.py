# coding=utf-8
def max_product(num):
    d = [0 for i in range(num + 1)]
    d[0] = 1
    d[1] = 1
    for i in range(2, num + 1):
        product = 1
        d[i] = 1
        for j in range(1, i + 1):
            if d[i] < d[i - j] * j:
                d[i] = d[i - j] * j
    return d[num]


if __name__ == '__main__':
    num = 8
    print max_product(num)
