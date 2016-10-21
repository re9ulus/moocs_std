# Uses python2

def edit_distance(s, t):
	ar = [[0 for j in range(len(s) + 1)] for i in range(len(t) + 1)]

	for i in range(1, len(t) + 1):
		ar[i][0] = i
	for j in range(1, len(s) + 1):
		ar[0][j] = j

	for i in range(1, len(t) + 1):
		for j in range(1, len(s) + 1):
			diag = ar[i-1][j-1]
			if t[i-1] != s[j-1]:
				diag += 1
			ar[i][j] = min(ar[i-1][j] + 1, ar[i][j-1] + 1, diag)
	return ar[len(t)][len(s)]

if __name__ == "__main__":
	s1 = raw_input()
	s2 = raw_input()
	print(edit_distance(s1, s2))
