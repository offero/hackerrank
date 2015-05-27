"""
# picking-cards

## Problem Statement
There are N cards on the table and each has a number between 0 and N. Let us denote the number on the ith card by ci. You want to pick up all the cards. The ith card can be picked up only if at least ci cards have been picked up before it. (As an example, if a card has a value of 3 on it, you can't pick that card up unless you've already picked up 3 cards previously) In how many ways can all the cards be picked up?
The first line contains the number of test cases T. T test cases follow. Each case contains an integer N on the first line, followed by integers c1,..ci,...,cN on the second line.
Output T lines one corresponding to each test case containing the required answer for the corresponding test case. As the answers can be very big, output them modulo 1000000007.

## Constraints:
1 <= T <= 10
1 <= N <= 50000
0 <= ci <= N

## Sample Input:
3
3
0 0 0
3
0 0 1
3
0 3 3

Sample Output:
6
4
0
"""

'''
## Strategy:

Implement naive version, test.
Implement nlogn version with sorting and sliding window.
Test against naive version.
Sort vals ascending (nlogn)
i is the array positon signifying the number of cards chosen so far.
j is the array position representing the max card that can be chosen.
j-i is the number of cards that can be chosen.
Seek both i and j forward until i reaches the end.
j stops at the end of the array.
At any given point, multiply the total by the number of cards that can
be chosen. The next card that you can choose is any card whose value
is <= the number picked so var (i).
'''


def count_perms2(vals):
    vals = sorted(vals)
    nvals = len(vals)
    total = 1
    i = j = 0
    while i < nvals:
        while j < nvals and vals[j] <= i:
            j += 1

        total = (total * (j-i)) % 1000000007
        i += 1
    return total


def main():
    n = int(input().strip())
    for picked in range(n):
        nvals = int(input())
        vals = map(int, input().strip().split())
        print(count_perms2(vals))


if __name__ == "__main__":
    main()
