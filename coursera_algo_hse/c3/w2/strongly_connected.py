#Uses python3

import sys

sys.setrecursionlimit(200000)

def dfs(adj, times, visited, x):
    global time
    if visited[x]:
        return
    visited[x] = True
    for to in adj[x]:
        dfs(adj, times, visited, to)
    time += 1
    times.append((time, x))


def number_of_strongly_connected_components(adj):
    res = 0
    #write your code here
    rev_adj = [[] for i in range(len(adj))]
    for key in range(len(adj)):
        for node in adj[key]:
            rev_adj[node].append(key)
    times = []
    visited = [False] * n
    for i in range(len(adj)):
        dfs(rev_adj, times, visited, i)
    times = [y for x, y in sorted(times, reverse=True)]
    res = 0
    visited = [False] * n
    for node in times:
        if visited[node]:
            continue
        res += 1
        dfs(adj, [], visited, node)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    time = 0
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
