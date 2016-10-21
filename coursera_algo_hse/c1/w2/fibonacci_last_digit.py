# Uses python3
import sys


def get_fibonacci_last_digit(n):
    if n <= 1:
    	return n
    n += 1
    ar = [0 for i in range(n)]
    ar[1] = 1
    for i in range(2, n):
    	ar[i] = (ar[i-1] + ar[i-2]) % 10
    return ar[-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit(n))
