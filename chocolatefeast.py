# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys

testcases = int(sys.stdin.readline().strip())

for i in range(testcases):
    # dollars, dollars per candy, wrappers per candy
    n, c, m = sys.stdin.readline().strip().split()
    n, c, m = float(n), float(c), float(m)
    totalcandies = int(n/c)

    # for every m wrappers, get an additional candy
    wrappers = totalcandies
    while wrappers >= m:
        candies = int(wrappers/m)
        wrappers = wrappers % m
        totalcandies += candies
        wrappers += candies

    print(totalcandies)
