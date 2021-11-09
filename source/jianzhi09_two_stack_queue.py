#!/usr/bin/python
class CQueue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def appendTail(self,v):
        self.stack1.append(v)

    def deleteHead(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        if not self.stack2:
            return -1

        return self.stack2.pop()

a = CQueue()
print a.appendTail(5)
print a.deleteHead()
print a.deleteHead()
print '---'*10
a = CQueue()
print a.deleteHead()
print a.appendTail(5)
print a.appendTail(2)
print a.deleteHead()
print a.deleteHead()
print a.deleteHead()
