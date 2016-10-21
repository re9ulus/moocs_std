# Uses python2
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #write your code here
    segments = sorted(segments, key=lambda it: it[1])
    points.append(segments[0][1])
    for s in segments[1:]:
        if s[0] <= points[-1]:
            continue
        else:
            points.append(s[1])
    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    tmp = map(int, input.split())
    n, data = tmp[0], tmp[1:]
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(' '.join(map(str, points)))
