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

def build_tree(inorder,postorder):
    def recur(left,right):
        print left,right
        if left > right:
            return 

        val = postorder.pop()
        root = TreeNode(val)
        idx = dict_inorder[val]
        root.right = recur(idx+1,right)
        root.left = recur(left,idx-1)
        return root

    dict_inorder = {v:i for i,v in enumerate(inorder)}
    root = recur(0,len(inorder)-1) 
    return root

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
root = build_tree(inorder,postorder)
preorder(root)

