#Uses python2

import sys

def dfs(adj, used, order, x):
    #write your code here
    global time
    if used[x]:
        return
    used[x] = True
    for to in adj[x]:
        dfs(adj, used, order, to)
    time = time + 1
    order.append((time, x))


def toposort(adj):
    used = [False] * len(adj)
    order = []
    #write your code here
    for i in range(len(adj)):
        dfs(adj, used, order, i)
    order = [y + 1 for x, y in sorted(order, reverse=True)]
    return order


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
    order = toposort(adj)
    print(' '.join(map(str ,order)))
    # for x in order:
        # print(x + 1, end=' ')

