#!/usr/bin/python
class Node():
    def __init__(self,val=None):
        self.val = val
        self.next = None

class ListNode():
    def __init__(self):
        self.head = None

    def traverse(self):
        if not self.head:
            print "None"
            return
        p = self.head
        while p:
            print p.val,
            p = p.next

        print ''

    def append(self,val):
        node = Node(val)
        if not self.head:
            self.head = node
            return

        p = self.head
        while p.next:
            p = p.next

        p.next = node

    def cycle(self,idx):
        if not self.head:
            return

        p = self.head
        while idx > 0:
            p = p.next
            idx -= 1

        cycle_in = p
        while p.next:
            p = p.next

        p.next = cycle_in

def find_cycle(head):
    '''input:node
       rt: node
    '''
    if (not head) or (not head.next):
        return -1

    fast = head.next.next
    slow = head.next
    while fast != slow:
        if not fast:
            return -1

        fast = fast.next.next
        slow = slow.next

    fast = head

    while fast != slow:
        fast = fast.next
        slow = slow.next

    return slow

case = [
        ([3,2,0,-4],1),
        ([1,2],0),
        ([1],-1),
        ([1,2,3,4],-1),
        ]
for i in case:
    l = ListNode()
    for j in i[0]:
        l.append(j)

    #l.traverse()
    if i[1] >= 0:
        l.cycle(i[1])

    #l.traverse()
    in_cycle = find_cycle(l.head)
    rt = in_cycle
    if isinstance(rt,int):
        print i,rt
    else:
        print i,rt.val

   
