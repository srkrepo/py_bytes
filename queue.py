# -*- coding: utf-8 -*-
# - - - - - - - - - - - Sri Pandi - - - - - - - - - - - - - -

__author__ = 'Satheesh R'


# Defanged version of IP address.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


q = Queue()
for i in range(1, 11):
    q.enqueue(i)
    print(q.items)

for i in range(1, 11):
    q.dequeue()
    print(q.items)
