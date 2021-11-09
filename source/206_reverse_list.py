#!/usr/bin/python

from llist import LList
def reverse_list(head):
    pre = None
    cur = head
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp

    head = pre
    return head

def recursive_reverse(head):
    if not head or not head.next:
        return head
    cur = recursive_reverse(head.next)
    head.next.next = head
    head.next = None

    return cur


## two node, delete head
print '---'*10
my_list = LList()
for i in range(5):
    my_list.append(i)

my_list.traverse_list()
#my_reverse = reverse_list(my_list.head)
my_reverse = recursive_reverse(my_list.head)
my_list.head = my_reverse
my_list.traverse_list()
print '---'*10
my_list = LList()
for i in range(2):
    my_list.append(i)

my_list.traverse_list()
my_reverse = reverse_list(my_list.head)
my_list.head = my_reverse
my_list.traverse_list()
print '---'*10
my_list = LList()
for i in range(1):
    my_list.append(i)

my_list.traverse_list()
my_reverse = reverse_list(my_list.head)
my_list.head = my_reverse
my_list.traverse_list()
print '---'*10
my_list = LList()
my_list.traverse_list()
my_reverse = reverse_list(my_list.head)
my_list.head = my_reverse
my_list.traverse_list()
