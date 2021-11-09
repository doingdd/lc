#!/usr/bin/python

from llist import LList
def removeNthFromEnd(head,n):
    if not head:
        return head

    ## delete last one
    if n == 1:
        p = head
        if not p.next:
            head = None
            return head

        while p.next.next:
            p = p.next

        p.next = None

        return head

    ## two points,p is fast point
    p = head
    q = head
    while n > 0:
        ## n >= length of LList, just delete head
        if not p.next:
            return head.next

        p = p.next
        n -= 1

    while p.next:
        p = p.next
        q = q.next

    q.next = q.next.next


    return head


### two node, delete last 1
print '---'*10
my_list = LList()
for i in range(10):
    my_list.append(i)

my_list.traverse_list()
new_list = LList()
new_list.head = removeNthFromEnd(my_list.head,1)
new_list.traverse_list()

## one node, delete last 1
print '---'*10
my_list = LList()
for i in range(1):
    my_list.append(i)

my_list.traverse_list()
new_list = LList()
new_list.head = removeNthFromEnd(my_list.head,1)
new_list.traverse_list()

## delete head
print '---'*10
my_list = LList()
for i in range(10):
    my_list.append(i)

my_list.traverse_list()
new_list = LList()
new_list.head = removeNthFromEnd(my_list.head,10)
new_list.traverse_list()

## delete 2th from end 
print '---'*10
my_list = LList()
for i in range(10):
    my_list.append(i)

my_list.traverse_list()
new_list = LList()
new_list.head = removeNthFromEnd(my_list.head,3)
new_list.traverse_list()

## two node, delete head
print '---'*10
my_list = LList()
for i in range(2):
    my_list.append(i)

my_list.traverse_list()
new_list = LList()
new_list.head = removeNthFromEnd(my_list.head,2)
new_list.traverse_list()

## two node, delete last
print '---'*10
my_list = LList()
for i in range(2):
    my_list.append(i)

my_list.traverse_list()
new_list = LList()
new_list.head = removeNthFromEnd(my_list.head,1)
new_list.traverse_list()
