#!/usr/bin/python
class Node():
    def __init__(self,val=None):
        self.val = val
        self.next = None

class ListNode():
    def __init__(self):
        self.head = None

    def append(self,val):
        node = Node(val)
        if not self.head:
            self.head = node
            return
        p = self.head
        while p.next:
            p = p.next

        p.next = node

    def traverse(self):
        if not self.head:
            print "None"
            return
        p = self.head
        while p:
            print p.val,
            p = p.next

        print ''
def find_mid(head):
    if not head.next:
        return head

    fast = slow = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow  = slow.next

    return slow
def reverse_list(head):
    if not head:
        return head
    pre = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp

    return pre

def merge_list(l1_head,l2_head):
    p1,p2 = l1_head,l2_head
    while p2:
        tmp1 = p1.next
        tmp2 = p2.next
        p1.next = p2
        p2.next = tmp1
        p1 = tmp1
        p2 = tmp2

    return l1_head

def re_sort(head):
    if not head or not head.next or not head.next.next:
        return head

    l1_head = head
    mid = find_mid(l1_head)
    l2_head = reverse_list(mid.next)
    mid.next = None
    l3 = ListNode()
    l3.head = merge_list(l1_head,l2_head)
    
    return head


case = [(1,2,3,4,5),
       (1,2,3,4)
       ]
for i in case:
    l = ListNode()
    for j in i:
        l.append(j)

    l.traverse()
    l.head = re_sort(l.head)
    l.traverse()

