#!/usr/bin/python
class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None

class ListNode():
    def __init__(self):
        self.head = None

    def pprint(self):
        if not self.head:
            print "Empty"
        p = self.head
        while p:
            print p.val,
            p = p.next

        print ""

    def construct(self,l):
        if not l:
            return
        p = self.head
        for i,v in enumerate(l):
            node = Node(v)
            if not p:
                self.head = p = node
            else:
                p.next = node
                p = p.next
def reverse(head,k):
    hair = Node()
    hair.next = head
    cur = hair
    fast = hair
    while fast:
        for i in range(k):
            fast = fast.next
            if not fast:
                return hair.next
        for i in range(k):
            tmp = cur.next
            cur.next = fast
            tmp.next = fast.next
            fast.next = tmp


case = [
    ([1,2,3,4,5],2),
    ([1,2,3,4,5],3),
    ([1,2,3,4,5,6],3),
    ([1],1)
]
for i in case:
    listnode = ListNode()
    listnode.construct(i[0])
    listnode.pprint()
    listnode.head = reverse(listnode.head,i[1])