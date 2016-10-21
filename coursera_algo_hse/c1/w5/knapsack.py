# Uses python2
import sys

def optimal_weight(W, w):
    # write your code here
    n = len(w)
    ar = [[0 for i in range(W + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for k in range(1, W + 1):
            cur_weight = k
            prev_val = 0
            if w[i-1] <= cur_weight:
                prev_val = ar[i-1][k-w[i-1]] + w[i-1]
            ar[i][k] = max([ar[i][k], prev_val, ar[i-1][k]])

    # for row in ar:
    #     print row
    return ar[n][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    W, n, w = data[0], data[1], data[2:]
    print(optimal_weight(W, w))
