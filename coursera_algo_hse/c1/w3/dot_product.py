#Uses python2

import sys

def min_dot_product(a, b):
    #write your code here
    res = 0
    a = sorted(a)
    b = sorted(b, reverse=True)
    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(min_dot_product(a, b))
    
