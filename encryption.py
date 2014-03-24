# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import floor, ceil, sqrt

def main():
    sent = raw_input()
    n = len(sent)
    sqrtn = sqrt(n)

    r = int(floor(sqrtn))
    c = int(ceil(sqrtn))

    res = [[] for x in range(n)]
    for i, ch in enumerate(sent):
        #print i%c
        res[i%c].append(ch)

    print " ".join(["".join(s) for s in res])


if __name__ == "__main__":
    main()
