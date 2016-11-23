#Uses python3

import sys
from queue import Queue


inf = float('inf')


def bfs(adj, s, t):
    q = Queue()
    dist = [inf for i in range(len(adj))]
    dist[s] = 0
    q.put(s)
    while not q.empty():
        curr = q.get()
        for node in adj[curr]:
            if dist[node] != inf:
                continue
            dist[node] = dist[curr] + 1
            if node == t:
                return dist[node]
            q.put(node)
    return -1


def distance(adj, s, t):
    #write your code here
    return bfs(adj, s, t)


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
