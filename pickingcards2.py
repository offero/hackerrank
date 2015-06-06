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

from collections import Counter

def count_perms3(vals):
    cntr = Counter(vals)
    cards = 0
    total = 1
    for i in range(len(vals)):
        cards += cntr[i]
        if cards <= i:
            return 0
        total = (total * (cards-i)) % 1000000007
    return total


def main():
    n = int(input().strip())
    for _ in range(n):
        nvals = int(input())
        vals = list(map(int, input().strip().split()))
        print(count_perms3(vals))


if __name__ == "__main__":
    main()
