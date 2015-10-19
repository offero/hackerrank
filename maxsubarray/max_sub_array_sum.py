#!/usr/bin/env python3

import sys
from itertools import chain
import numpy as np

def max_sub_array_sum_dp(arr):
    """
    T(n) = max sum of array of n elements.
    T(n) = max{
                ...
                T(n-1)
                a_n
            }
    [a b]
    [a b c]
    """
    max_neg = float("-inf")
    sum_pos = 0
    n = len(arr)
    sums = np.zeros((n, n))
    sums[0,0] = arr[0]
    B = [float("-inf")] * n
    B[0] = arr[0]  # best score for array of size i (index)

    # non-contiguous
    if arr[0] >= 0:
        sum_pos += arr[0]
    else:
        max_neg = arr[0]

    for i in range(1, n):
        # non-contiguous
        if arr[i] >= 0:
            sum_pos += arr[i]
        else:
            max_neg = max(max_neg, arr[i])

        # contiguous
        # either the existing best or the best including the new element
        for j in range(i+1):
            sums[j, i] = sums[j, i-1] + arr[i]
            B[i] = max(B[i-1], B[i], sums[j, i])

    return B[-1], sum_pos if (sum_pos > 0 or max_neg == float("-inf")) else max_neg

def max_sub_array_sum(arr):
    """
    Runs in ((n+1)*n)/2 addition and comparison operations.
    One for each possible sub array sum.
    Way better than the exponential brute force solution,
    but it still can take some time on large input.
    """

    # print("Arr size: %d" % len(arr))

    if len(arr) == 0:
        return 0

    op_ct = 0
    max_sum = arr[-1]
    n = len(arr)
    prev = None
    for i in range(n-1, -1, -1):
        cur = arr[i]
        for j in range(i-1, -1, -1):
            prev = cur
            cur = arr[j] + prev
            op_ct += 1
            if cur > max_sum:
                max_sum = cur

            # 2362490691
            # 1000000
            if op_ct % 1000000 == 0:
                print("Op Ct: %d" % op_ct)

    # print("Op Ct: %d" % op_ct)
    return max_sum

def find_examples():
    import random
    from max_sub_array_sum_n import max_sub_array_sum_n
    for i in range(20):
        arr = list([random.randint(-10, 10) for _ in range(14)])
        a = max_sub_array_sum_n(arr)
        b = max_sub_array_sum_dp(arr)
        if a != b:
            print(arr, a, b)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        # print(max_sub_array_sum(arr))
        a, b = max_sub_array_sum_dp(arr)
        print("%d %d" % (a, b))  # print integers

if __name__ == "__main__":
    main()
    # find_examples()
