# Uses python3

import sys

input = sys.stdin.read()
tokens = [int(i) for i in input.split()[1:]]

max_ind1 = 0
for i in range(len(tokens)):
	if tokens[i] >= tokens[max_ind1]:
		max_ind1 = i

max_ind2 = -1
for i in range(len(tokens)):
	if ((max_ind2==-1) or tokens[i] >= tokens[max_ind2]) and i != max_ind1:
		max_ind2 = i

print(tokens[max_ind1] * tokens[max_ind2])
