# Uses python2
import sys

def points_cmp(a, b):
    if a[0] != b[0]:
        return cmp(a[0], b[0])
    else:
        return cmp(a[1], b[1])

def naive_count_segments(starts, ends, points):
    items = []
    S, P, E = 0, 1, 2
    for p in starts:
        items.append((p, S))
    for p in points:
        items.append((p, P))
    for p in ends:
        items.append((p, E))
    items = sorted(items, cmp=points_cmp)
    cnt = 0
    points_cnt = {}
    for p in items:
        if p[1] == S:
            cnt += 1
        elif p[1] == P:
            points_cnt[p[0]] = cnt
        elif p[1] == E:
            cnt -= 1
    ans = []
    for p in points:
        ans.append(points_cnt[p])
    return ans


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = naive_count_segments(starts, ends, points)
    print(' '.join(map(str, cnt)))
