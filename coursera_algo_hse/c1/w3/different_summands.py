# Uses python2
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    i = 1
    while n > 0:
    	if n - i <= i:
    		summands.append(n)
    		break
    	else:
    		summands.append(i)
    		n -= i
    		i += 1
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    print(' '.join(map(str, summands)))
