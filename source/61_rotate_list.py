#!/usr/bin/python
from llist import LList,LNode
def rotate_list(l1,k):
    n = 1
    head = l1
    while l1.next:
        n+=1
        l1 = l1.next

    l1.next = head
    for i in range(n-k%n):
        l1 = l1.next
        

    new_head = l1.next
    l1.next = None

    return new_head

print '---'*10
l1 = [1,2,3,4,5]
k = 2
ll1 = LList()
l3 = LList()
for i in l1:
    ll1.append(i)

l3.head = rotate_list(ll1.head,k)
l3.traverse_list()

print '---'*10
l1 = [2,0,1]
k = 5
ll1 = LList()
l3 = LList()
for i in l1:
    ll1.append(i)

l3.head = rotate_list(ll1.head,k)
l3.traverse_list()

