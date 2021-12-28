#!/usr/bin/python
class Node(object):
    def __init__(self,val=None,random=None):
        self.val = val
        self.random = random
        sef.next = None


def construct_list(l):
    if not l:
        return ''

    head = Node(*l[0])
    p = head
    for i in l[1:]:
        node = Node(*i)
        p.next = node
        p = p.next

    return head

def deepCopy(head):
    if not head:
        return head

    return new_head

def transfer(head):
    if not head:
        return []

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
    new_head = deepCopy(head)
    new_i = transfer(new_head)
    assert i == new_i
