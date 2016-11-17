#Uses python3

import sys


visited = set()


def dfs(adj, x):
    visited.add(x)
    for node in adj[x]:
        if node not in visited:
            dfs(adj, node)


def number_of_components(adj):
    components = 0
    #write your code here
    for node in range(len(adj)):
        if node not in visited:
            dfs(adj, node)
            components += 1
    return components


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
