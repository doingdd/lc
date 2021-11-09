#!/usr/bin/python
from llist import LList,LNode
def merge_list(l1,l2):
    l3 = LNode()
    head = l3
    if (not l1) and (not l2):
        return head

    while (l1 and l2):
        if (l1.val < l2.val):
            l3.next = l1
            l1 = l1.next

        elif (l1.val >= l2.val):
            l3.next = l2
            l2 = l2.next

        l3 = l3.next

    l3.next = l1 if l1 else l2
    return head.next

def rec_merge_list(l1,l2):
    if not l1:
        return l2
    elif not l2:
        return l1
    elif l1.val < l2.val:
        l1.next = rec_merge_list(l1.next,l2)
        return l1
    else:
        l2.next = rec_merge_list(l1,l2.next)
        return l2


        

print '---'*10
l1 = [1,2,4]
l2 = [1,3,4]
ll1 = LList()
ll2 = LList()
l3 = LList()
for i in l1:
    ll1.append(i)

for i in l2:
    ll2.append(i)
l3.head = merge_list(ll1.head,ll2.head)
l3.traverse_list()


print '---'*10
l1 = []
l2 = []
ll1 = LList()
ll2 = LList()
l3 = LList()
for i in l1:
    ll1.append(i)

for i in l2:
    ll2.append(i)
l3.head = merge_list(ll1.head,ll2.head)
l3.traverse_list()


print '---'*10
l1 = []
l2 = [0]
ll1 = LList()
ll2 = LList()
l3 = LList()
for i in l1:
    ll1.append(i)

for i in l2:
    ll2.append(i)
l3.head = merge_list(ll1.head,ll2.head)
l3.traverse_list()


print '---'*10
l1 = [1,2,7]
l2 = [3]
ll1 = LList()
ll2 = LList()
l3 = LList()
for i in l1:
    ll1.append(i)

for i in l2:
    ll2.append(i)
l3.head = rec_merge_list(ll1.head,ll2.head)
l3.traverse_list()


