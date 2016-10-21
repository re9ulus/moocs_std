# Uses python2
import sys

def get_change(m):
    #write your code here
    ans = m / 10
    m %= 10
    ans += m / 5
    m %= 5
    ans += m
    return ans

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
