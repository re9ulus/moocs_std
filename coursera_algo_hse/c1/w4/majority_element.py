# Uses python2
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    mid = left + (right - left) / 2
    maj_left = get_majority_element(a, left, mid-1)
    maj_right = get_majority_element(a, mid, right)
    cnt_left, cnt_right = 0, 0
    if maj_left != -1 or maj_right != -1:
        for i in a[left: right+1]:
            if i == maj_left:
                cnt_left+=1
            elif i == maj_right:
                cnt_right+=1
    fall = (right - left + 1) / 2 + 1
    if cnt_left >= fall:
        return maj_left
    if cnt_right >= fall:
        return maj_right
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, a = data[0], data[1:]
    if get_majority_element(a, 0, n-1) != -1:
        print(1)
    else:
        print(0)
