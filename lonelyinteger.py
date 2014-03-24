#!/usr/bin/py
def lonelyinteger(b):
    #n = len(b)
    alone = {}
    for i in b:
        if i in alone:
            del alone[i]
        else:
            alone[i] = 1
    return alone.keys()[0]

if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
