#!/usr/bin/python
class Node():
    def __init__(self,k=None,val=None):
        self.k = k
        self.val = val
        self.pre = None
        self.next = None


class LRUCache():
    def __init__(self,cap):
        self.cap = cap
        self.cache = {}
        self.size = 0
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self,k):
        if k in self.cache:
            node = self.cache[k]
            self.move_to_head(node)
            return node.val
        else:
            return -1

    def put(self,k,v):
        if k in self.cache:
            node = self.cache[k]
            node.val = v
            self.move_to_head(node)
        else:
            node = Node(k,v)
            self.add_to_head(node)
            self.cache[k] = node
            self.size += 1
            if self.size > self.cap:
                self.delete_tail()

    def move_to_head(self,node):
        self.delete(node)
        self.add_to_head(node)

    def delete(self,node):
        node.next.pre = node.pre
        node.pre.next = node.next
  
    def add_to_head(self,node):
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node
        node.pre = self.head
    def delete_tail(self):
        node = self.tail.pre
        self.delete(node)
        self.cache.pop(node.k)

    def traverse(self):
        if not self.head.next.val:
            print 'empty'
            return

        p = self.head.next
        while p.val:
            print p.k,
            p = p.next

        print ''


l = LRUCache(2)
l.put(1,1)
print l.get(1)
l.put(2,2)
print l.get(1)
#l.traverse()
l.put(3,3)
print l.get(2)
#l.traverse()
l.put(4,4)
#l.traverse()
#l.traverse()
print l.get(1)
print l.get(3)
print l.get(4)
#
