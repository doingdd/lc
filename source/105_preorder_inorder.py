#!/usr/bin/python
class TreeNode():
    def __init__(self,val=None):
        self.left = None
        self.right = None
        self.val = val
    
def preorder(root):
    if root:
        print root.val,
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print root.val,

def build_tree(preorder,inorder):

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
root = build_tree(preorder,inorder)
postorder(root)

