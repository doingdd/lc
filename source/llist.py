#!/usr/bin/python

class LNode():
    def __init__(self,val=None):
        self.val = val
        self.next = None

class LList():
    def __init__(self):
        self.head = None

    def traverse_list(self):
        if self.head is None:
            print "List has no element"
            return

        p = self.head
        while p is not None:
            print p.val,
            p = p.next
        
        print ''

    def append(self,val):
        node = LNode(val)
        if not self.head:
            self.head = node
            return

        p = self.head
        while p.next:
            p = p.next
        p.next = node

    def insert(self,index,val):
        node = LNode(val)
        if index == 0:
            node.next = self.head
            self.head = node
            return

        if not self.head:
            self.head = node
            return

        p = self.head
        while index > 1:
            if not p.next:
                p.next = node
                return 
            
            index -= 1
            p = p.next

        node.next = p.next
        p.next = node

    def insert_after_item(self,data,val):
        p = self.head
        while p:
            if p.val == data:
                node = LNode(val)
                node.next = p.next
                p.next = node
                return

            p = p.next

        
    def insert_before_item(self,data,val):
        if not self.head:
            return
        p = self.head
        if p.val == data:
            node = LNode(val)
            node.next = self.head
            self.head = node

        while p.next:
            if p.next.val == data:
                node = LNode(val)
                node.next = p.next
                p.next = node
                return

            p = p.next

    def get_count(self):
        count = 0
        if not self.head:
            return count
        
        p = self.head
        while p is not None:
            count += 1
            p = p.next

        return count

    def delete_item(self,val):
        if not self.head:
            return

        if self.head.val == val:
            if self.head.next:
                self.head = self.head.next
            else:
                self.head = None

            return
        p = self.head
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
                return

            p = p.next


if __name__ == '__main__':

    my_list =  LList()
    for i in range(10):
        my_list.append(i)
    
    my_list.insert(100,'d')
    my_list.insert_after_item(21321,'c')
    my_list.insert_before_item(9,'c')
    my_list.delete_item(0)
    my_list.delete_item('d')
    my_list.traverse_list()
    print my_list.get_count()
