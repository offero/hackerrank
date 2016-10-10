"""
https://www.hackerrank.com/challenges/candies

Alice is a kindergarden teacher. She wants to give some candies to the children in her class.  All the children sit in a
line ( their positions are fixed), and each  of them has a rating score according to his or her performance in the
class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with
the higher rating must get more candies. Alice wants to save money, so she needs to minimize the total number of candies
given to the children.

Input Format: The first line of the input is an integer N, the number of children in Alice's class. Each of the
following N lines contains an integer that indicates the rating of each child.

Output Format: Output a single line containing the minimum number of candies Alice must buy.
"""

class Scores(object):
    def __init__(self, scores):
        self.scores = scores
        self.candies = [1 for _ in range(len(scores))]

    def compareAndAssignCandies(self, i):
        j = i+1
        si, sj = self.scores[i], self.scores[j]
        ci, cj = self.candies[i], self.candies[j]

        if si > sj and not (ci > cj):
            ci = cj + 1

        elif si < sj and not (ci < cj):
            cj = ci + 1

        self.candies[i], self.candies[j] = ci, cj

    def assignCandies2xBy2(self):
        """
        O(N) solution. 2N. Scan forwards, then backwards.
        """
        i = 0
        while i < (len(self.scores)-1):
            self.compareAndAssignCandies(i)
            i += 1

        i = len(self.scores)-2
        while i >= 0:
            self.compareAndAssignCandies(i)
            i -= 1

TEST_CASES = [
    ( [5, 4, 3, 1, 1], [4, 3, 2, 1, 1] ),
    ( [1, 2, 3, 2, 1], [1, 2, 3, 2, 1] ),
    ( [1, 2, 3, 4, 3, 2, 1], [1, 2, 3, 4, 3, 2, 1] ),
    ( [1, 4, 4, 4, 1], [1, 2, 1, 2, 1] ),
    ( [1, 4, 1, 1], [1, 2, 1, 1] ),
    ( [5, 4, 1, 1], [3, 2, 1, 1] ),
    ( [1, 4, 5, 1], [1, 2, 3, 1] ),
    ( [1, 4, 5, 1], [1, 2, 3, 1] ),
    ( [2, 3, 4, 5], [1, 2, 3, 4] ),
    ( [5, 4, 3, 2], [4, 3, 2, 1] ),
    ( [5, 4, 3, 3], [3, 2, 1, 1] ),
    ( [5, 4, 3, 3, 2, 2], [3, 2, 1, 2, 1, 1] ),
    ( [1, 1], [1, 1] ),
    ( [1], [1] ),
    ( [], []),
    ( [2, 4, 2, 6, 1, 7, 8, 9, 2, 1],
      [1, 2, 1, 2, 1, 2, 3, 4, 2, 1] ),  # 19
    ( [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1],
      [1, 2, 3, 2, 1, 2, 3, 2, 1, 2, 3, 2, 1]),
    ( [1, 2, 3, 2, 1, 3, 3, 3, 1, 2, 3, 2, 1],
      [1, 2, 3, 2, 1, 2, 1, 2, 1, 2, 3, 2, 1])
]

def checkContstrints(scores, candies):
    assert len(scores) == len(candies)
    i = 1
    while i < len(scores)-1:
        j = i + 1
        if scores[i] > scores[j]:
            assert candies[i] > candies[j]
        if scores[i] < scores[j]:
            assert candies[i] < candies[j]
        i += 1

def main():
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(int(input().strip()))

    scores = Scores(arr)
    scores.assignCandies2xBy2()
    print(sum(scores.candies))

    checkContstrints(arr, scores.candies)

    # with open('out.txt', 'w+') as fp:
    #     for a, b in zip(arr, scores.candies):
    #         fp.write('%s\t%s\n' % (a, b))

def testAssignCandies():
    for input, output in TEST_CASES:
        scores = Scores(input)
        scores.assignCandies2xBy2()
        if output != scores.candies:
            print("Failed example:", input, scores.candies, "expected", output)
        # else:
        #     print("Successful exmaple:", input, scores.candies)

if __name__ == "__main__":
    # testAssignCandies()
    main()
