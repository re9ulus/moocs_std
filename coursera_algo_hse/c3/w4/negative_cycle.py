#Uses python3

import sys

def bellman_ford(G, cost, visited, start):
    size = len(G)
    visited_costs = [float('inf') for i in range(size)]
    visited_costs[start] = 0
    was_relaxed = True

    for i in range(size):
        if not was_relaxed:
            break
        was_relaxed = False
        for node_from in range(size):
            for ind_to, node_to in enumerate(G[node_from]):
                if visited_costs[node_to] > visited_costs[node_from] + cost[node_from][ind_to]:
                    visited_costs[node_to] = visited_costs[node_from] + cost[node_from][ind_to]
                    visited[node_from] = True
                    was_relaxed = True
                    if i == size - 1:
                        return 1
    return 0


def negative_cycle(adj, cost):
    visited = [False for i in range(len(adj))]
    res = 0
    for start in range(len(adj)):
        if not visited[start]:
            res = bellman_ford(adj, cost, visited, start)
            if res:
                break
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
