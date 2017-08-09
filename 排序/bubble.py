def bubble_sort(arry):
    n = len(arry)
    for i in range(n):
        for j in range(0, n-i-1):
            if arry[j] > arry[j+1]:
                arry[j], arry[j + 1] = arry[j + 1], arry[j]
    return arry


if __name__ == '__main__':
    numbers = [15, 2, 35, 8, 24, 9, 43]
    print bubble_sort(numbers)

