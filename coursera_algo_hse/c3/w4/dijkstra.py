#Uses python3

import sys
import heapq


def distance(adj, cost, s, t):
    #write your code here
    finished, q, visited_costs = set(), [], [10**9 for i in range(len(adj))]
    visited_costs[s] = 0
    heapq.heappush(q, (0, s))
    while len(q):
        node_cost, node = heapq.heappop(q)
        if node in finished:
            continue
        finished.add(node)
        if node == t:
            return visited_costs[node]
        for target_node, edge_cost in zip(adj[node], cost[node]):
            if target_node in finished:
                continue
            target_cost = node_cost + edge_cost
            if target_cost < visited_costs[target_node]:
                visited_costs[target_node] = target_cost
                heapq.heappush(q, (target_cost, target_node))
    return -1


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
