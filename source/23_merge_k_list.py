#!/usr/bin/python

case = [
	[[1,4,5],[1,3,4],[2,6]],
        [],
  	[[]],
  	[[1],[1],[1],[1]],[[],[1],[2,3]],
        [[2,3,4],[5,6,7],[1],[2,3]]
       ]

class Node():
    def __init__(self,val=None):
        self.val = val
        self.next = None

class ListNode():
    def __init__(self):
        self.head = None

    def pprint(self):
        if not self.head:
            print "Empty"
        p = self.head
        while p:
            print p.val,
            p = p.next
        print ''

def construct(l):
    ''' transfer list to listnode
    '''
    listnode = ListNode()
    if not l:
        return listnode

    listnode.head = Node(l[0])
    p = listnode.head
    for i in l[1:]:
        node = Node(i)
        p.next = node
        p = p.next

    return listnode

def merge(c):
    lists = []
    rt_list = []
    for i in c:
        lists.append(construct(i).head)

    new_head = merge_list(lists)
    if not new_head:
        return rt_list
    p = new_head
    while p:
        rt_list.append(p.val)
        p = p.next

    return rt_list
    
def merge_list(lists):
    '''
    type lists: List(Node)
    type rt: Node
    '''
    k = len(lists)
    if k == 0:
        return None
    if k == 1:
        return lists[0]

    rt = ListNode()
    p = rt.head = Node()
    i = 0
    while True:
        for i in range(k):
            if not lists[i]:
                continue

            min_i,min_v = find_min(lists)
            lists[min_i] = lists[min_i].next
            node = Node(min_v)
            p.next = node
            p = p.next
            break

        else:
            break

    return rt.head.next

def find_min(lists):
    min_i = 0
    min_v = float('inf')
    for i,l in enumerate(lists):
        if not l:
            continue
        if l.val < min_v:
            min_v = l.val
            min_i = i

    #print min_i,min_v
    return min_i,min_v


for i in case:
    print "case is {0},result is {1}".format(i,merge(i))









