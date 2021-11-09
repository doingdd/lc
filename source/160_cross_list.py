#!/usr/bin/python
class Node():
    def __init__(self,val=None):
        self.val = val
        self.next = None

class ListNode():
    def __init__(self):
        self.head = None
 
    def traverse(self):
        if self.head:
            p = self.head
            while p:
                print p.val,
                p = p.next

        print ''

    def append(self,val):
        node = Node(val)
        if self.head:
            p = self.head
            while p.next:
                p = p.next
            p.next = node
        else:
            self.head = node


def find_cross(headA,headB):
    A = headA
    B = headB
    while A != B:
        A = A.next if A else headB
        B = B.next if B else headA

    return A

a = [4,1,8,4,5]
b = [5,0,1,8,4,5]
