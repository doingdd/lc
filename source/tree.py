#!/usr/bin/python

class TreeNode():
    def __init__(self,val=None):
        self.val = val
        self.left = None
        self.right = None

class Tree():
    def __init__(self,arr):
        print arr
        #self.root = self.construct_tree(arr,None,0)
        self.root = self.insertLevelOrder(arr,None,0,len(arr))

    def height(self,root):
        if not root:
            return 0

        l_height = self.height(root.left) + 1 
        r_height = self.height(root.right) + 1

        return l_height if l_height > r_height else r_height

    def construct_tree(self,arr,root,i):
        if i >= len(arr):
            return root

        if arr[i] is None:
            return None

        root = TreeNode(arr[i])
        root.left = self.construct_tree(arr,root.left,2*i+1)
        root.right = self.construct_tree(arr,root.right,2*i+2)

        return root

    def insertLevelOrder(self,arr, root, i, n): 
          
        # Base case for recursion  
        if i >= n or arr[i] is None:
            return None

        if i < n: 
            temp = TreeNode(arr[i])  
            root = temp  
      
            # insert left child  
            root.left = self.insertLevelOrder(arr, root.left, 
                                         2 * i + 1, n)  
      
            # insert right child  
            root.right = self.insertLevelOrder(arr, root.right, 
                                          2 * i + 2, n) 
        return root 

    def inOrder(self,root):
        if root:
            self.inOrder(root.left)
            print root.val,
            self.inOrder(root.right)
    
    def preOrder(self,root):
        if root:
            print root.val,
            self.preOrder(root.left)
            self.preOrder(root.right)

    def postOrder(self,root):
        if root:
            self.postOrder(root.left)
            self.postOrder(root.right)
            print root.val,

if __name__ == "__main__":
    #arr = [1,2,3,4,5,6,7,8,9,10]
    ##arr = [1,2,3]
    #tree = Tree(arr)
    #tree.inOrder(tree.root)
    #print ''
    #tree.preOrder(tree.root)
    #print ''
    #tree.postOrder(tree.root)
    #print ''
    #print tree.height(tree.root)
    arr = [1,None,3,4,5]
    tree = Tree(arr)
    #print tree.root.val,tree.root.right.val
    tree.inOrder(tree.root)
