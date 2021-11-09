#!/usr/bin/python
class LNode():
    def __init__(self,val=None):
        self.val = val
        self.next = None

class LList():
    def __init__(self):
        self.head = None

    def append(self,val):
        node = LNode(val)
        if not self.head:
            self.head = node
            return

        p = self.head
        while p.next:
            p = p.next

        p.next = node

    def lprint():
        if self.head is None:
            print "None"
            return

        while p:
            print p.val,
            p = p.next

        print ''

def middle_in_list(head):
    ## head : ListNode, middle: ListNode
    if not head:
        return None
    fast,slow = head,head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    middle = slow
    return middle


case = [[1,2,3,4,5],
        [1,2,3,4,5,6],
        [],
        [1,2,3,2,1]
        ]

for i in case:
    my_list = LList()
    for j in i:
        my_list.append(j)

    middle = middle_in_list(my_list.head)
    print middle.val if middle else ''
