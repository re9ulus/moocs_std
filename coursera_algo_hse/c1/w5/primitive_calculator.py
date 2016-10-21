# Uses python2
import sys


def optimal_sequence(n):
	ar = [n+1 for i in range(n+1)]
	ar[0], ar[1] = 1, 1
	for i in range(1, n+1):
		if i * 3 <= n:
			ar[i * 3] = min(ar[i * 3], ar[i] + 1)
		if i * 2 <= n:
			ar[i * 2] = min(ar[i * 2], ar[i] + 1)
		if i + 1 <= n:
			ar[i + 1] = min(ar[i + 1], ar[i] + 1)
	i = n
	seq = []
	while i >= 1:
		seq.append(i)
		min_val, next_i = ar[i - 1], i - 1
		if i % 3 == 0 and ar[i / 3] < min_val:
			min_val, next_i = ar[i / 3], i / 3
		if i % 2 == 0 and ar[i / 2] < min_val:
			min_val, next_i = ar[i / 2], i / 2
		i = next_i
	return list(reversed(seq))


input = sys.stdin.read()
n = int(input)
sequence = optimal_sequence(n)
print(len(sequence) - 1)
ans = ' '.join(map(str, sequence))
print ans
