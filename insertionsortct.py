# coding: utf-8

'''
a b c d e f

The i'th insertion will have to, at max, have i-1 shifts.

(n-1) + (n-2) + (n-3) ... (n-(n-1))
1 + 2 + 3 ... + n-1

n*(n-1)/2

The number of shifts for each i:
If sorted, the number of shifts is the number of elements to the left of i that
are greater than the i'th.

More generally, it is the number of places up until there are no elements
less than or equal to the i'th in the left sub-array.

Ref:
http://www.cs.umd.edu/class/fall2009/cmsc451/lectures/Lec08-inversions.pdf
http://www.programminggeek.in/2013/07/c-and-java-program-for-counting-number-of-inversion-in-an-array-using-naive-approach-and-divide-and-conquer-approach.html#.UwyYuNt6RxA
http://pine.cs.yale.edu/pinewiki/OrderStatisticsTree
'''


def insertionSortCount1(ar, l):
    shiftct = 0
    for i in range(1, l):
        v = ar[i]
        for j in range(i, -1, -1):
            if j == 0:
                ar[j] = v
                #print(" ".join(map(str, ar)))
            elif v >= ar[j-1]:
                ar[j] = v
                #print(" ".join(map(str, ar)))
                break
            else:
                ar[j] = ar[j-1]
                shiftct += 1

    print(shiftct)


def insertionSortCount2(ar, l):
    shiftct = 0
    gtct = {}
    for i in xrange(1, l):
        if ar[i-1] > ar[i]:
            gtct[i] = 1

        for j in xrange(i, -1, -1):
            if ar[j] > ar[i]:
                shiftct += 1
    print(shiftct)
    return shiftct


def insertionSortCount3(ar, l):
    #l = len(ar)
    shiftct = 0
    for i in xrange(1, l):
        v = ar[i]
        x = ar[i-1]
        shiftct += sum((x > v for x in ar[:i]))  # too slow!

    print(shiftct)
    return shiftct

from time import sleep
def mergeCount(l, nl, r, nr):
    i = 0
    j = 0
    ct = 0

    # every time we take from the right side while there is a valid i, count up

    sortedl = []
    while i < nl and j < nr:
        #print("i: {i} j: {j}".format(i=i, j=j))
        #print("sortedl: {0}".format(sortedl))

        n = min(l[i], r[j])
        sortedl.append(n)

        if n == r[j]:
            j += 1
            ct += nl - i
        else:
            i += 1

        #sleep(1)

    if i < nl:
        sortedl.extend(l[i:])
    if j < nr:
        sortedl.extend(r[j:])

    return ct, sortedl


def merge(l, nl, r, nr):
    i = 0
    j = 0
    ct = 0
    res = []

    while i < nl:
        while j < nr and r[j] < l[i]:
            res.append(r[j])
            ct += nl-i
            j += 1

        res.append(l[i])
        i += 1

    res.extend(r[j:])
    return ct, res


def inversionCount(ar, l):
    """
    Uses a merge-sort like inversion count to get the number of shifts.
    """
    if l == 1:
        return 0, ar

    if l == 2:
        return (1, ar[::-1]) if ar[1] < ar[0] else (0, ar)

    m = l//2
    left, right = ar[:m], ar[m:]
    ct = 0

    ctl, leftsorted  = inversionCount(left, m)
    ctr, rightsorted = inversionCount(right, m + l%2)

    ctm, merged = merge(leftsorted, m, rightsorted, m + l%2)

    ct += ctl + ctr + ctm
    #print("%d %d %d" % (ctl, ctr, ctm))

    return ct, merged


def main():
    T = input()
    for t in range(T):
        m = input()
        ar = [int(i) for i in raw_input().strip().split()]
        #insertionSortCount3(ar, m)
        ct, res = inversionCount(ar, m)
        print(ct)
        #print(res)

if __name__ == "__main__":
    main()


def test_data():
    import random
    ar = [random.randint(0, 99) for _ in xrange(200)]
    l = 200
    return ar, l

