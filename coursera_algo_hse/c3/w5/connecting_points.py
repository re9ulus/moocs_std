#Uses python3
import sys
import math
from queue import PriorityQueue


def build_graph(x_coord, y_coord):
    G = {}
    counter = 0
    for i in range(len(x_coord)):
        for j in range(i+1, len(x_coord)):
            if i == j:
                continue
            node = ((x_coord[i], y_coord[i]), (x_coord[j], y_coord[j]))
            G[node] = math.sqrt((x_coord[i] - x_coord[j])**2 +
                (y_coord[i] - y_coord[j])**2)
    return G


def parent(disj_set, v):
    if disj_set[v] == v:
        return v
    disj_set[v] = parent(disj_set, disj_set[v])
    return disj_set[v]


def kruscal(G):
    disj_set = {}
    added_edges = set()
    edges = []
    for edge, val in G.items():
        edges.append((val,edge))
        if edge[0] not in disj_set:
            disj_set[edge[0]] = edge[0]
        if edge[1] not in disj_set:
            disj_set[edge[1]] = edge[1]
    edges = sorted(edges)
    for edge in edges:
        __, nodes = edge
        if parent(disj_set, nodes[0]) != parent(disj_set, nodes[1]):
            added_edges.add(edge)
            disj_set[parent(disj_set, nodes[0])] = parent(disj_set, nodes[1])
    return added_edges


def minimum_distance(x, y):
    result = 0.
    #write your code here
    g = build_graph(x, y)
    edges = kruscal(g)
    for cost, edge in edges:
        result += cost
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
