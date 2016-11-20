#Uses python3

import sys

def dfs(adj, node):
    if color[node] == 2:
        return False
    elif color[node] == 1:
        return True
    color[node] = 1
    res = False
    for to in adj[node]:
        res |= dfs(adj, to)
    color[node] = 2
    return res

def acyclic(adj):
    res = False
    for i in range(n):
        res |= dfs(adj, i)
    return 1 if res else 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)

    color = [0 for i in range(n)]
    print(acyclic(adj))
