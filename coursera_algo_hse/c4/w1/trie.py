#Uses python3
import sys


def build_trie_rec(trie, node, pattern, max_ind):
    if len(pattern) == 0:
        return max_ind
    c = pattern[0]
    if c in trie[node]:
        return build_trie_rec(trie, trie[node][c], pattern[1:], max_ind)
    else:
        current_node = node
        for it in pattern:
            max_ind += 1
            trie[max_ind] = {}
            trie[current_node][it] = max_ind
            current_node = max_ind
        return max_ind


# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = {0: {}}
    # write your code here
    max_ind = 0
    for pat in patterns:
        max_ind = build_trie_rec(tree, 0, pat, max_ind)
    return tree

if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
