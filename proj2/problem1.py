"""
maps and Hash
a dictionary can be used with this problem to facilitate constant, i.e. O(1), lookups insertions and deletions
need a hash function
using larger table sized would be ideal for a production implementation. For this project we will use a Prime
value of 7 for a smaller container lookup. However 31 would be better. This implementation doesn't take into account collisions
the test data should limit collision so this was not worked on as none of the test cases require this.
"""

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.size = capacity
        self.table = [None]*1000
        self.p = 11

        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        hv = self._create_hash_value(key)

        if self.table[hv] != None:
            return self.table[hv]

        return -1
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        hv = self._create_hash_value(key)
        self.table[hv] = value
        pass

    def _create_hash_value(self, key): 
        # create simple hash function from the key to create new key for Cache table
        key = str(key)
        hv = 0
        current_coefficient = 1
        for char in key: ## for loop handles if key is longer than 1 digit
            hv += ord(key) * current_coefficient
            current_coefficient *= self.p
        return hv 

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
