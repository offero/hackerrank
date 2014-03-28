#!/usr/bin/env python
# coding: utf-8

'''
Given a N row x M columns board:

D R U
R U D
* U U

Get to the * in exactly k moves with the minimum number of changes.
Changes only happen once per round.
Start in the upper left corner.
Output -1 if impossible.
'''

right = lambda x: (x[0],   x[1]+1)
left  = lambda x: (x[0],   x[1]-1)
up    = lambda x: (x[0]-1, x[1])
down  = lambda x: (x[0]+1, x[1])


movefns = {"L": left, "R": right, "U": up, "D": down}
fnmoves = dict([(v, k) for k, v in movefns.items()])


def findStar(B):
    for i in range(len(B)):
        for j in range(len(B[0])):
            if B[i][j] == "*":
                return (i, j)

    raise Exception("No * character found.")


def sameDirection(x, y, B):
    return movefns[val(x, B)](x) == y


def neighbors(x, n, m):
    cells = left(x), right(x), up(x), down(x)
    valid_cell = lambda x: x[0] < n and x[1] < m and x[0] >= 0 and x[1] >= 0
    return [x for x in cells if valid_cell(x)]


def val(x, B):
    return B[x[0]][x[1]]


def manhattanDist(x, star):
    rdist = star[0] - x[0]
    cdist = star[1] - x[1]
    return abs(rdist)+abs(cdist), rdist, cdist


def reachableInPMods(x, visited, star, p, k, B, n, m):
    if p < 0 or k < 0:
        return False

    if manhattanDist(x, star)[0] > k:
        return False

    if x == star:
        return True

    res = False
    visited.add(x)
    for y in neighbors(x, n, m):
        if y not in visited:
            res = reachableInPMods(y, visited, star,
                                    p if sameDirection(x, y, B) else p-1,
                                    k-1, B, n, m)
        if res:
            break

    visited.remove(x)

    return res

        #if sameDirection(x, y, B):
            #res = reachableInPMods(y, visited | set((x,)), star, p, k-1, B)
        #else:
            #res = reachableInPMods(y, visited | set((x,)), star, p-1, k-1, B)


def minChanges2(x, B, k):
    star = findStar(B)

    n, m = len(B), len(B[0])
    res = reachableInPMods(x, set(), star, k, k, B, n, m)
    if not res:
        return -1

    p = k

    start = 0
    end = p
    n = end-start+1
    while n > 1:
        p2 = start + n//2
        res = reachableInPMods(x, set(), star, p2, k, B, n, m)
        if res:
            p = p2
            end = p2
        else:
            start = p2+1
        n = end-start+1

    return p


def minChanges1(x, B, k):
    star = findStar(B)
    n, m = len(B), len(B[0])
    for i in range(k+1):
        res = reachableInPMods(x, set(), star, i, k, B, n, m)
        if res:
            return i
    return -1


#     row  col
#  L  -1    0
#  R  +1    0
#  U   0   -1
#  D   0   +1


def testBoard1():
    B = [
            ["D", "R", "U"],
            ["R", "U", "D"],
            ["*", "U", "U"],
        ]
    return B

def testBoard2():
    return [
        [c for c in "DDDDDDD*"],
        [c for c in "DDDDDDDU"],
        [c for c in "RRDLLLLU"],
        [c for c in "UUUUUUUD"],
        [c for c in "UUDUUUUU"],
        [c for c in "UURRRRRU"],
        ]

def testBoard3():
    return [["R", "D"],
            ["*", "L"]]

minChanges = minChanges1

def test1():
    B = testBoard1()
    k = 8
    return minChanges((0, 0), B, k)

def test2():
    B = testBoard2()
    k = 34
    return minChanges((0, 0), B, k)

def test3():
    B = testBoard3()
    k = 4
    return minChanges((0, 0), B, k)


def main():
    n, m, k = map(int, raw_input().strip().split())
    B = []
    for i in range(n):
        B.append([c for c in raw_input().strip()])

    x = (0, 0)
    mc = minChanges(x, B, k)
    if mc is None:
        print("-1")
    else:
        print(mc)


if __name__ == "__main__":
    main()


