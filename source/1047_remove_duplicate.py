#!/usr/bin/python
case = [
  "abbaca",
  "aa",
  "abc",
  "abccba",
  "",
  "a",
  "abcabc"
]
def removeDuplicates(s):
    """
    :type s: str
    :rtype: str
    """
    stack = []
    for i in s:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    return ''.join(stack)

for i in case:
    print "case is {0},result is {1}".format(i,removeDuplicates(i))
