# python3
import sys


class Node:
	def __init__(self):
		self.next = {}
		self.is_pattern = False


def build_trie_rec(trie, pat):
	if len(pat) == 0:
		trie.is_pattern = True
		return
	c = pat[0]
	if c in trie.next:
		build_trie_rec(trie.next[c], pat[1:])
	else:
		cur_node = trie
		for c in pat:
			n = Node()
			cur_node.next[c] = n
			cur_node = n
		cur_node.is_pattern = True


def build_trie(patterns):
	tree = Node()
	for pat in patterns:
		max_ind = build_trie_rec(tree, pat)
	return tree


def trie_match(text, node):
	for c in text:
		if node.is_pattern:
			break
		if c in node.next:
			node = node.next[c]
		else:
			break
	if node.is_pattern:
		return True
	return False


def solve (text, patterns):
	result = []

	# write your code here
	trie = build_trie(patterns)
	for i in range(len(text)):
		if trie_match(text[i:], trie):
			result.append(i)
	return result

text = sys.stdin.readline ().strip ()
n = int (sys.stdin.readline ().strip ())
patterns = []
for i in range (n):
	patterns += [sys.stdin.readline ().strip ()]

ans = solve (text, patterns)

sys.stdout.write (' '.join (map (str, ans)) + '\n')
