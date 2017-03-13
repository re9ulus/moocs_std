# python3
import sys

sys.setrecursionlimit(10000)

class Node():

    def __init__(self):
        self.next = {}


def build_tree_rec(tree, text):
    if len(text) == 0:
        return
    splited = False
    for edge in tree.next:
        if edge[0] == text[0]:
            splited = True
            i = 1
            while i < len(text) and i < len(edge):
                if text[i] != edge[i]:
                    break
                i += 1
            if i < len(edge):
                pref, suf = edge[:i], edge[i:]
                tree.next[pref] = Node()
                tree.next[pref].next[suf] = tree.next[edge]
                del tree.next[edge]
            build_tree_rec(tree.next[text[:i]], text[i:])
            break
    if not splited:
        tree.next[text] = Node()


def travers(tree, res, depth=1):
    for key in tree.next:
        # print(depth * '_' + key)
        travers(tree.next[key], res, depth+1)
        res.append(key)


def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding
    substrings of the text) in any order.
    """
    result = []
    tree = Node()
    for i in range(len(text)):
        build_tree_rec(tree, text[i:])
    travers(tree, result)
    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))
