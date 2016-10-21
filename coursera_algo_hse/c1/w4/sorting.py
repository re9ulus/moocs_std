# Uses python2
import sys
import random


def partition3(a, l, r):
    x = a[l]
    j = l
    k = l
    for i in range(l + 1, r + 1):
        if a[i] == x and i != l+1:
            k += 1
            a[i], a[k] = a[k], a[i]
        elif a[i] < x:
            k += 1
            j += 1
            if j != k:
                a[i], a[j], a[k] = a[k], a[i], a[j]
            else:
                a[j], a[i] = a[i], a[j]
    a[l], a[j] = a[j], a[l]
    return j, k


def partition2(a, l, r):
    x = a[l]
    j = l;
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    m_left, m_right = partition3(a, l, r)
    randomized_quick_sort(a, l, m_left - 1);
    randomized_quick_sort(a, m_right + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, a = data[0], data[1:]
    randomized_quick_sort(a, 0, n - 1)
    print(' '.join(map(str, a)))
