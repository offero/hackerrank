"""
https://www.hackerrank.com/challenges/strange-grid

A strange grid has been recovered from an old book. It has 5 columns and infinite number of rows. The bottom row is considered as the first row. First few rows of the grid are like this:
..............
..............
20 22 24 26 28
11 13 15 17 19
10 12 14 16 18
 1  3  5  7  9
 0  2  4  6  8

The grid grows upwards forever!
Your task is to find the integer in cth column in rth row of the grid.

Input Format
There will be two integers r and c separated by a single space.
Constraints
1≤r≤2 * 109
1≤c≤5


Rows are indexed from bottom to top and columns are indexed from left to right.
Output Format
Output the answer in a single line.
Sample Input
6 3
Sample Output
25
Explanation

The number in the 6th row and 3rd column is 25.

In [42]: [[start(r) + addtl(c) for c in range(1,6)] for r in range(1,11)]
Out[42]:
[[0, 2, 4, 6, 8],
 [1, 3, 5, 7, 9],
 [10, 12, 14, 16, 18],
 [11, 13, 15, 17, 19],
 [20, 22, 24, 26, 28],
 [21, 23, 25, 27, 29],
 [30, 32, 34, 36, 38],
 [31, 33, 35, 37, 39],
 [40, 42, 44, 46, 48],
 [41, 43, 45, 47, 49]]
"""

start = lambda r: 5 * (r-1-((r+1)%2))
addtl = lambda r,c: (c-1)*2 + ((r-1)%2)

ans = lambda r, c: 2*(c-1) + 10*((r-1)//2) + (r-1)%2

def main():
    r, c = map(int, input().strip().split())
    print(start(r) + addtl(r, c))
    # print(ans(r, c))


if __name__ == "__main__":
    main()
