#!/usr/bin/python
from tree import Tree


def in_order(root):
    if root:
        in_order(root.left)
        print root.val
        in_order(root.right)

root = [1,None,2,3]
tr = Tree(root)
tr.inOrder(tr.root)
#in_order(tr.root)
#root = [1,None,2]
#root = [1]
#root = [1,2]

