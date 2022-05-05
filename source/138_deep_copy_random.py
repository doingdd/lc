#!/usr/bin/python
class Node(object):
    def __init__(self,val=None):
        self.val = val
        self.random = None
        self.next = None


def construct_list(l):
    if not l:
        return ''

    node_dict = {}
    head = Node(l[0][0])
    random = Node(l[0][1])
    head.random = random

    p = head
    for i in l[1:]:
        node = Node(i)
        p.next = node
        p = p.next

    return head

def deepCopy(head):
    if not head:
        return head
    p = head
    while p:
        p.next = p
        p = p.next.next

    new_head = p

    return new_head

def transfer(head):
    if not head:
        return []

    p = head
    l = []
    while p:
        l.append([p.val,p.random.val])

    return l

case = [
        [[7,None],[13,0],[11,4],[10,2],[1,0]],
        [[1,1],[2,1]],
        [[3,None],[3,0],[3,None]],
        [],
        [[3,3]]
        ]

for i in case:
    head = construct_list(i)
    print transfer(head)
    #new_head = deepCopy(head)
    #new_i = transfer(new_head)
    #assert i == new_i
