# Uses python3
import sys

def get_fibonaccihuge(n, m):
    if n <= 1:
    	return n
    ar = [0, 1, 1]
    while not(ar[-1] == 1 and ar[-2] == 0):
    	ar.append((ar[-1] + ar[-2]) % m)
    period = len(ar) - 2
    return ar[n % period]

if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonaccihuge(n, m))
