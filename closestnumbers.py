#!/usr/bin/env python
# coding: utf-8

from itertools import chain

def main():
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split())
    arr.sort()
    lowest = None
    pairs = []
    for i in range(1, n):
        b, a = arr[i], arr[i-1]
        diff = b - a
        if diff <= lowest or lowest is None:
            if diff < lowest:
                pairs = []

            pairs.append((a, b))
            lowest = diff

    # sorted(set(chain(*pairs)))
    print " ".join(map(str, chain(*pairs)))

if __name__ == "__main__":
    main()
