# python2

def read_input():
    return (raw_input().rstrip(), raw_input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def poly_hash(s, prime, x):
	h = 0
	for c in reversed(s):
		h = (h * x + ord(c)) % prime
	return h


def precompute_hashes(text, pattern_length, p, x):
	size = len(text) - pattern_length
	H = [0 for i in range(size + 1)]
	S = text[size:]
	H[-1] = poly_hash(S, p, x)
	y = 1
	for i in range(pattern_length):
		y = (y * x) % p
	for i in reversed(range(0, size)):
		H[i] = (x * H[i+1] + ord(text[i]) - y * ord(text[i + pattern_length])) % p
	return H


def rabin_karp(text, pattern):
	p = 15487457
	x = 100 #absolutly random
	result = []
	p_hash = poly_hash(pattern, p, x)
	H = precompute_hashes(text, len(pattern), p, x)
	for i in range(len(text) - len(pattern) + 1):
		if p_hash != H[i]:
			continue
		if text[i:i+len(pattern)] == pattern:
			result.append(i)
	return result


def get_occurrences(pattern, text):
	return rabin_karp(text, pattern)


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
