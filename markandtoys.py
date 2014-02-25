# coding: utf-8
'''
Mark and Toys

Mark and Jane are very happy after having their first kid. Their son is very
fond of toys. Therefore, Mark wants to buy some toys for his son. But he has a
limited amount of money. But he wants to buy as many toys as he can. So, he is
in a dilemma and is wondering how he can maximize the number of toys he can buy.

He has N items in front of him, tagged with their prices and he has only K
rupees.

Now, you being Mark's best friend have the task to help him buy as many toys for
his son as possible.

Input Format
The first line will contain two inputs N and K, followed by a line containing N
integers separated by a single space indicating the products’ prices.

Output Format
Maximum number of toys Mark can buy for his son.

Constraints
1<=N<=105
1<=K<=109
1<=price of any toy<=109

Sample Input

7 50
1 12 5 111 200 1000 10

Sample Output

4
'''

'''
Maximize the number of toys purchased.
'''

n, k = map(float, raw_input().strip().split())
prices = map(int, raw_input().strip().split())

prices = sorted(prices)
toys = 0
cost = 0.0
for p in prices:
    if k - (p + cost) >= 0:
        cost += p
        toys += 1
    else:
        break

print toys

