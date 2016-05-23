"""
https://www.hackerrank.com/challenges/even-tree

You are given a tree (a simple connected graph with no cycles). You have to remove as many edges from the tree as possible to obtain a forest with the condition that : Each connected component of the forest should contain an even number of vertices.

To accomplish this, you will remove some edges from the tree. Find out the number of removed edges.

Input Format
The first line of input contains two integers N and M. N is the number of vertices and M is the number of edges.
The next M lines contain two integers ui and vi which specifies an edge of the tree. (1-based index)

Output Format
Print the answer, a single integer.

Constraints
2 <= N <= 100.

Note: The tree in the input will be such that it can always be decomposed into components containing even number of nodes.
"""

def subGraph(G, nodes):
    nodes = set(nodes)
    subG = {}

    for node in nodes:
        subG[node] = G[node] & nodes

    return subG

def bfsNodes(G, node):
    "Perfrom a bfs on G starting from node and return the nodes in a list"
    visited = set()
    tovisit = [node]

    while tovisit:
        node = tovisit.pop()
        if node not in visited:
            visited.add(node)
            tovisit.extend(G[node])

    return visited

def graphCut(G, a, b):
    "Return the Graph's obtained by cutting the edge between a and b"
    if b not in G[a] or a not in G[b]:
        raise Exception('wtf')

    # unlink
    G[a].remove(b)
    G[b].remove(a)

    nodesA = bfsNodes(G, a)
    nodesB = bfsNodes(G, b)

    compA = subGraph(G, nodesA)
    compB = subGraph(G, nodesB)

    # relink
    G[a].add(b)
    G[b].add(a)

    return compA, compB

def isEven(n):
    return n % 2 == 0

def isOdd(n):
    return not isEven(n)

def isLeaf(G, node):
    return len(G[node]) == 1

def shouldCut(G, a, b):
    if len(G) <= 2:
        return False, G, {}

    compA, compB = graphCut(G, a, b)

    if isOdd(len(compA)) or isOdd(len(compB)):
        return False, compA, compB

    return True, compA, compB

def edges(G):
    for a in G:
        for b in G[a]:
            yield (a, b)

def findGraphCuts(G):
    components = [G]
    cuts = 0

    while components:
        C = components.pop()

        for a, b in edges(C):
            yn, compA, compB = shouldCut(C, a, b)
            if yn:
                cuts += 1
                components.append(compA)
                components.append(compB)
                break

    return cuts

def main():
    G = {}

    n, m = map(int, raw_input().strip().split(" "))
    for _ in range(m):
        a, b = map(int, raw_input().strip().split(" "))
        if a not in G:
            G[a] = set()
        if b not in G:
            G[b] = set()

        G[a].add(b)
        G[b].add(a)

    print (findGraphCuts(G))

if __name__ == "__main__":
    main()
