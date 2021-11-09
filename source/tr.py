#!/usr/bin/python
# -*- coding:utf-8 -*-
from collections import deque

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


data = [3,5,2,1,4,6,7,8,9,10,11,12,13,14]
data = [1,None,2,3]
n = iter(data)
tree = Node(next(n))
fringe = deque([tree])
while True:
    head = fringe.popleft()
    try:
        head.left = Node(next(n))
        fringe.append(head.left)
        head.right = Node(next(n))
        fringe.append(head.right)
    except StopIteration:
        break

def in_order(root):
    if root:
        in_order(root.left)
        print(root.val),
        in_order(root.right)

#print(tree.left.val)
print data
in_order(tree)
