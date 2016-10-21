# Uses python2
import sys

def get_optimal_value(capacity, weights, values):
	value = 0.
	val_for_cap = [float(values[i]) / weights[i] \
					for i in range(len(weights))]
	items = sorted(zip(val_for_cap, values, weights), reverse=True)
	current_item = 0
	while capacity > 0 and current_item < len(weights):
		if items[current_item][2] <= capacity:
			capacity -= items[current_item][2]
			value += items[current_item][1]
			current_item += 1
		else:
			value += items[current_item][1] * \
				float(capacity) / items[current_item][2]
			break
	return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
