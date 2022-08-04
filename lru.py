# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
"""
    Copyright(c) VMware, Inc.
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import collections


class SimpleLRUCache:
    def __init__(self, size):
        self.size = size
        self.lru_cache = collections.OrderedDict()

    def get(self, key):
        try:
            value = self.lru_cache.pop(key)
            self.lru_cache[key] = value
            return value
        except KeyError:
            return -1

    def put(self, key, value):
        try:
            self.lru_cache.pop(key)
        except KeyError:
            if len(self.lru_cache) >= self.size:
                self.lru_cache.popitem(last=False)
        self.lru_cache[key] = value

    def show_entries(self):
        print(self.lru_cache)


# Create an LRU Cache with a size of 3
cache = SimpleLRUCache(3)

cache.put("1", "1")
cache.put("2", "2")
cache.put("3", "3")

cache.get("1")
cache.get("3")

cache.put("4", "4")  # This will replace 2
cache.show_entries()  # shows 1,3,4
cache.put("5", "5")  # This will replace 1
cache.show_entries()  # shows 3,4,5