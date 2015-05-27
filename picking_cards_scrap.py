"""
N = set of cards from which to choose
# ways to choose a card = |N|!
the next card you can choose is any card
with val <= the number picked so far
"""

import itertools


def nlte(n, L, sorted=False):
    it = iter(lte(n, L, sorted))
    c = 0
    try:
        while True:
            next(it)
            c += 1
    except StopIteration:
        pass

    return c


def lte(n, L, sorted=False):
    """Return the list of all elements in L <= n
    """
    it = iter(L)
    while True:
        x = next(it)
        if x <= n:
            yield x
        elif sorted:
            raise StopIteration("Done")


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


def count_perms(vals):
    vals = sorted(vals)
    nvals = len(vals)
    total = 1
    picked = 0
    while picked < nvals:
        # choices = list(lte(picked, vals[picked:], sorted=True))
        # print(val, choices)
        # total = (total * len(choices)) % 1000000007
        c = nlte(picked, vals[picked:], sorted=True)
        total = (total * c) % 1000000007
        # We encountered a value that we can't pick
        if c <= 0:
            break

        picked += 1

    return total


def main():
    n = int(input().strip())
    for picked in range(n):
        nvals = int(input())
        vals = map(int, input().strip().split())
        print(count_perms2(vals))


def pickperm(x):
    ct = 0
    for c in itertools.permutations(x):
        if all(n <= i for i, n in enumerate(c)):
            ct += 1
    return ct


def test_pick():
    tests = [([0, 0, 0], 3),
             ([0, 0, 1], 2),
             ([0, 0, 1, 1, 4], 12)
             ]

    for test in tests:
        a = pickperm(test[0])
        b = count_perms2(test[0])
        if not a == b:
            print("ERROR: pickperm: %s, count_perms: %s" % (a, b))


if __name__ == "__main__":
    test_pick()
    main()
