# Uses python3


def calc_fib(n):
    if (n <= 1):
        return n
    n += 1
    ar = [0 for i in range(n)]
    ar[1] = 1
    for i in range(2, n):
    	ar[i] = ar[i-1] + ar[i-2]
    return ar[-1]


n = int(input())
print(calc_fib(n))
