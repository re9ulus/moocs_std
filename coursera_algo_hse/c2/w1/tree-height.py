# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))
        self.g = {}
        for child in range(len(self.parent)):
            p = self.parent[child]
            if p in self.g:
                self.g[p].append(child)
            else:
                self.g[p] = [child]

    def compute_height_recursive(self, elem, h=0):
        if elem not in self.g:
            return h
        heights = []
        for node in self.g[elem]:
            heights.append(self.compute_height_recursive(node, h+1))
        return max(heights)

    def compute_height(self):
        return self.compute_height_recursive(-1)


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())

threading.Thread(target=main).start()
