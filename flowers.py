#!/bin/python

def nextj(row):
    j = 0
    while row[j] > 0:
        j += 1
    return j


def lowtrip((a1, b1, c1), (a2, b2, c2)):
    if a2 is not None and a2 <= a1:
        return (a2, b2, c2)
    return (a1, b1, c1)

cost = lambda ci, x: (x+1)*ci

def generateA(N):
    A = []
    for _ in range(N):
        A.append([0]*N)
    return A

def generateX(N, K):
    X = []
    for j in range(N):
        X.append([(j//K) + 1]*N)
    return X

def generateXC(N, X, C):
    XC = []
    for i in range(N):
        tmp = []
        for j in range(N):
            tmp.append(X[i][j] * C[j])
            #tmp.append( cost(C[j], X[i][j]) ) # X already 1 based
        XC.append(tmp)
    return XC


def make_purchases(N, K, C):
    # i for rows
    # j for columns
    # x = j//K

    A = generateA(N)
    X = generateX(N, K)
    XC = generateXC(N, X, C)

    purchases = []  # list of individual flower purchases
    while len(purchases) < N:
        # if i and j both exceed N, bad data
        # always put a 1 in the next adjacecnt spot in A with the least cost

        low = None, None, None
        for i in range(1, N):
            j1 = nextj(A[i-1])  # next available spot in the row
            j2 = nextj(A[i])
            tmp = lowtrip((XC[i][j1], i, j1), (XC[i][j2], i, j2))
            low = lowtrip(tmp, low)

        v, _i, _j = low
        A[_i][_j] = 1
        purchases.append(v)

    print sum(purchases)


def main():
    # code snippet illustrating input/output methods
    N, K = map(int, raw_input().split())
    C = map(int, raw_input().split())
    #i = len(C)
    make_purchases(N, K, C)


if __name__ == "__main__":
    main()

        #if XC[i][j1] <= XC[i][j2]:
            #low = XC[i][j1], i, j1
        #else:
            #low = XC[i][j2], i, j2

