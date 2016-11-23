#Uses python3

import sys
from queue import Queue


def bipartite(adj):
    #write your code here
    q = Queue()
    q.put(0)
    colors = [-1 for i in range(len(adj))]
    colors[0] = 0
    while not q.empty():
        curr = q.get()
        for node in adj[curr]:
            if colors[node] == colors[curr]:
                return 0
            elif colors[node] != -1:
                continue
            colors[node] = not colors[curr]
            q.put(node)
    return 1


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
    print(bipartite(adj))
