#!/usr/bin/python
from llist import LList,LNode

def add2list(l1,l2):
    new_list = LList()
    n_bit = 0
    while any([l1,l2]):
        c_bit = ((l1.val if l1 else 0) + (l2.val if l2 else 0) + n_bit)%10
        n_bit = ((l1.val if l1 else 0) + (l2.val if l2 else 0) + n_bit)/10
        new_list.append(c_bit)
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if n_bit:
        new_list.append(n_bit)

    return new_list.head
  
print '--'*20
l1 = LList()
l2 = LList()
for i in [2,4,3]:
    l1.append(i)

for i in [5,6,4]:
    l2.append(i)

new_head = add2list(l1.head,l2.head)
new_list = LList()
new_list.head = new_head
new_list.traverse_list()

print '--'*20
l1 = LList()
l2 = LList()
for i in [0,2]:
    l1.append(i)

for i in [0,1]:
    l2.append(i)

new_head = add2list(l1.head,l2.head)
new_list = LList()
new_list.head = new_head
new_list.traverse_list()
print '--'*20
l1 = LList()
l2 = LList()
for i in [9,9,9]:
    l1.append(i)

for i in [9,9]:
    l2.append(i)

new_head = add2list(l1.head,l2.head)
new_list = LList()
new_list.head = new_head
new_list.traverse_list()
