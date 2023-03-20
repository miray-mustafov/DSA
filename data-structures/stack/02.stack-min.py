'''
Design a stack that beside pop and push, has min method that returns the
el with min value with 0(1) runtime.
'''
import sys


class MyStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, el):
        self.stack.append(el)
        if len(self.min_stack) == 0 or el < self.min():
            self.min_stack.append(el)

    def pop(self):
        last_el = self.stack.pop()
        if last_el is self.min():
            self.min_stack.pop()
        return last_el

    def peek(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]

    def __repr__(self):
        return str(self.stack)


my_stack = MyStack()
my_stack.push(2)
my_stack.push(2)
my_stack.push(-2)
my_stack.push(-1)
my_stack.push(4)
my_stack.pop()
my_stack.pop()
my_stack.pop()
print(my_stack)
print(my_stack.min())
