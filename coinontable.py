#!/usr/bin/env python
# coding: utf-8

'''
Given a N row x M columns board:

D R U
R U D
* U U

Get to the * in exactly k moves with the minimum number of changes.
Changed only happen once per round.
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


def manhattanDist(x, star):
    rdist = star[0] - x[0]
    cdist = star[1] - x[1]
    return abs(rdist)+abs(cdist), rdist, cdist


#def reachableWithPMods(x, star, p, B):
    #pass

def reachableInK(x, star, k, B):
    """
    Is `star` reachable by `x` in <= `k` moves on board `B`.
    Returns k - the minimum number of moves to get to star from x.
    """
    m, r, c = manhattanDist(x, star)
    return m <= k


def val(x, B):
    return B[x[0]][x[1]]


#     row  col
#  L  -1    0
#  R  +1    0
#  U   0   -1
#  D   0   +1


def minchanges(x, star, B, path_so_far, k):
    # bounds check first
    n, m = len(B), len(B[0])
    if x[0] >= n or x[1] >= m or x[0] < 0 or x[1] < 0:
        return None

    # TODO: Try all reachable paths in order (BFS)
    # What condition allows me to forgo larger paths?
    # Condition: If each path from this point is reachable in a larger number
    # of moves and not less modifications.

    if not reachableInK(x, star, k, B):
        return None

    md, rd, cd = manhattanDist(x, star)
    path = path_so_far[:] + [x]

    if md == 0:
        return 0, path

    # try other neighboring spaces
    # all moves except the one that takes us back to where we came from
    movefns2 = {m: fn for m, fn in movefns.items()
                if fn(x) not in path_so_far}

    res = []
    for m, movefn in movefns2.items():
        # record the minimum number of changes and the move to take

        mc = minchanges(movefn(x), star, B, path, k-1)
        if mc is not None:
            res.append(
                ((0 if val(x, B) == m else 1) + mc[0], mc[1])
            )

    return min(res) if len(res) > 0 else None


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

def test1():
    B = testBoard1()
    k = 8
    return minchanges((0, 0), findStar(B), B, [], k)

def test2():
    B = testBoard2()
    k = 34
    return minchanges((0, 0), findStar(B), B, [], k)

def test3():
    B = [["R", "D"],
         ["*", "L"]]
    x = (0, 0)
    k = 4
    print(minchanges(x, findStar(B), B, [], k)[0])


def main():
    n, m, k = map(int, raw_input().strip().split())
    B = []
    for i in range(n):
        B.append([c for c in raw_input().strip()])

    x = (0, 0)
    mc = minchanges(x, findStar(B), B, [], k)[0]
    if mc is None:
        print("-1")
    else:
        print(mc)


if __name__ == "__main__":
    main()

