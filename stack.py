# -*- coding: utf-8 -*-
# - - - - - - - - - - - Sri Pandi - - - - - - - - - - - - - -

__author__ = 'Satheesh R'


# Defanged version of IP address.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        l = len(self.items) - 1
        return self.items[l]

    def size(self):
        return len(self.items)


s = Stack()
for i in range(1, 11):
    s.push(i)
    print(s.items)

for i in range(1, 11):
    s.pop()
    print(s.items)
