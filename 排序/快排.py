#coding=utf-8


def quick_sort(ary):
    return qsort(ary, 0, len(ary)-1)


def qsort(ary, left, right):
    mark = ary[left]
    lp = left
    rp = right
    if lp >= rp:
        return ary
    while lp < rp:
        while ary[rp] >= mark and lp < rp:
            rp = rp - 1
        while ary[lp] <= mark and lp < rp:
            lp = lp + 1
        ary[lp], ary[rp] = ary[rp], ary[lp]
    ary[left], ary[lp] = ary[lp], ary[left]
    qsort(ary, left, lp-1)
    qsort(ary, lp+1, right)
    return ary

if __name__ == '__main__':
    num = [3, 1, 5, 7, 2, 4, 9, 6]
    num = quick_sort(num)
    for i in num:
        print i,
