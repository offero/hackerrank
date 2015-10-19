#!/usr/bin/env python3

def max_sub_array_sum_n(arr):
    """
    A O(n) solution to the max sub array sum problem.
    (Without hints!).
    """
    if len(arr) == 0:
        return 0, 0

    # remember the max elt for the all negative case
    _max = max(enumerate(arr), key=lambda a: a[1])
    _max = (_max[0], _max[0], _max[1])
    if _max[2] < 0:
        return _max

    # Prune left negatives
    while arr[0] < 0:
        arr = arr[1:]

    # Prune right negatives
    while arr[-1] < 0:
        arr = arr[:-1]

    n = len(arr)
    isums = [arr[0]] * n   # Running sum from the left
    jsums = [arr[-1]] * n  # Running sum from the right
    inegs = []             # Indices of ranges of negatives
                           # as tuples with inclusive range [a, b] and a >= b

    # O(n) Running sums in both directions, keep track of negative indices,
    # and sum all positives
    sum_pos = arr[0] if arr[0] > 0 else 0
    for i in range(1, n):
        j = n-i-1
        isums[i] = isums[i-1] + arr[i]
        jsums[j] = jsums[j+1] + arr[j]

        if arr[i] < 0:
            if not inegs or inegs[-1][1] is not None:
                inegs.append([i, None])
        elif inegs and inegs[-1][1] is None:
            inegs[-1][1] = i-1

        if arr[i] > 0:
            sum_pos += arr[i]

    i = 0              # start i at the beginning
    j = n-1            # and j at the end
    total = isums[-1]  # sum of the total array

    # O(1) Function to sum between any i, j leveraging our running sum arrays
    sumij = lambda _i,_j: total \
                        - (isums[_i-1] if _i > 0 else 0) \
                        - (jsums[_j+1] if _j < n-1 else 0)

    # Which index ranges (inclusive [a, b]) should we consider for max sum?
    indices_to_consider = [(i, j)]

    # O(n) For each negative segment, determine if it over-powers
    # the sub-arrays to the left or right of it.
    while inegs:
        ni, nj = inegs.pop(0)
        neg = sumij(ni, nj)

        # if it over-powers the left size
        if  neg + sumij(i, ni-1) < 0:
            indices_to_consider.append((i, ni-1))
            # Keep solving for the right side
            i = nj+1

        # if it over-powers the right side
        elif neg + sumij(nj+1, j) < 0:
            # Add range of left side to indices_to_consider
            indices_to_consider.append((i, ni-1))

    # Add the tail
    if i <= j:
        indices_to_consider.append((i, j))

    i, j = max(indices_to_consider, key=lambda args: sumij(*args))

    # return i, j, sumij(i, j)
    # print(i, j, sumij(i, j))
    return sumij(i, j), sum_pos if sum_pos > 0 else _max


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        # print(max_sub_array_sum(arr))
        a, b = max_sub_array_sum_n(arr)
        print("%d %d" % (a, b))  # print integers

examples = [
    #   arr,                                   (i, j), max_sub_sum, max_sum
    ([-2, -2, 1, 2, -6, -6, 1, 4, -7, 1, 3,
                                    -10, -20], (4, 5), 5, 12),
    ([1, 2, -6, 1, 4, -7, 1, 3],               (3, 4), 5, 12),
    ([1, 2, -6, 1, 4, -7, 1, 2, 3],            (6, 8), 6, 14),
    ([1, 2, -6, 1, 4, -7, 8, -8, 10],          (6, 8), 10, 26),
    ([1, 2, -6, 14, -7, 8, -8, 10],            (3, 7), 17, 35)
]

def test():
    for arr, (i, j), max_sub_sum, max_tot_sum in examples:
        ans_sub_sum, ans_tot_sum = max_sub_array_sum_n(arr)
        # print(arr, "=>", ansi, ansj, ans_sum, "==?", i, j, max_sum)
        print(arr, "=>", ans_sub_sum, ans_tot_sum, "==?", max_sub_sum, max_tot_sum)

if __name__ == "__main__":
    main()
    # test()
