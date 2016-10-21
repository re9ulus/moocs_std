# Uses python2
import sys


def merge(a, left, mid, right):
    ar_left = a[left:mid+1]
    ar_right = a[mid+1:right+1]
    inv = 0
    i = left
    i_left, i_right = 0, 0
    while i_left < len(ar_left) and i_right < len(ar_right):
        if ar_left[i_left] <= ar_right[i_right]:
            a[i] = ar_left[i_left]
            i_left += 1
        else:
            a[i] = ar_right[i_right]
            i_right += 1
            inv += len(ar_left) - i_left
        i += 1
    while i_left < len(ar_left):
        a[i] = ar_left[i_left]
        i += 1
        i_left += 1
    while i_right < len(ar_right):
        a[i] = ar_right[i_right]
        i += 1
        i_right += 1
    return inv


def get_number_of_inversions(a, left, right):
    if left >= right:
        return 0
    mid = left + (right - left) / 2
    inv = get_number_of_inversions(a, left, mid)
    inv += get_number_of_inversions(a, mid+1, right)
    inv += merge(a, left, mid, right)
    return inv


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, a = data[0], data[1:]
    print(get_number_of_inversions(a, 0, len(a)-1))
