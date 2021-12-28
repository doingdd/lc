#!/usr/bin/python
case = [
  ["push",-2],
  ["push",0],
  ["push",-3],
  ["getMin"],
  ["pop"],
  ["top"],
  ["getMin"]
]
result = [None,None,None,-3,None,0,-2]

class MinStack():
    def __init__(self):
        self.stack = []
        self.min_stack = [float('inf')]

    def push(self,val):
        self.stack.append(val)
        self.min_value = min(self.min_stack[-1],val)
        self.min_stack.append(self.min_value)

        return

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()

        return

    def top(self):

        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None

def stack_option(option):
    if len(option) > 1:
        return getattr(stack,option[0])(option[1])
    else:
        return getattr(stack,option[0])()

stack = MinStack()
for i,case in enumerate(case):
    output = stack_option(case)
    print case,result[i],output
    assert output == result[i]
