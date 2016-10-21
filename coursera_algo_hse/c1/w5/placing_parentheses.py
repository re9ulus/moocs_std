# Uses python2
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    #write your code here
    digits = []
    operators = []
    for i in range(len(dataset)):
        if i % 2 == 0:
            digits.append(int(dataset[i]))
        else:
            operators.append(dataset[i])
    return 0


if __name__ == "__main__":
    print(get_maximum_value(raw_input()))
