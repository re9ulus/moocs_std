# python2

import sys

class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == '[' and c == ']':
            return True
        if self.bracket_type == '{' and c == '}':
            return True
        if self.bracket_type == '(' and c == ')':
            return True
        return False

if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets_stack = []
    missmatch_position = -1
    for i, next in enumerate(text):
        if next == '(' or next == '[' or next == '{':
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i))

        if next == ')' or next == ']' or next == '}':
            # Process closing bracket, write your code here
            if len(opening_brackets_stack) == 0:
                missmatch_position = i + 1
                break
            if not opening_brackets_stack.pop().Match(next):
                missmatch_position = i + 1
                break
    # Printing answer, write your code here
    if missmatch_position > -1:
        print(missmatch_position)
    elif len(opening_brackets_stack) > 0:
        print(opening_brackets_stack.pop().position + 1)
    else:
        print('Success')
