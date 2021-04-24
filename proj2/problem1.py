"""
maps and double linked list
a double linked list can be used as a LRU cache
a dictionary can be used to map the keys to the nodes to facilitate constant, i.e. O(1), lookups insertions and deletions
added print lines to the cache lookups to see value in console.

"""

class Node():
    def __init__(self, key=0, value=0):
        self.next = None
        self.prev = None
        self.value = value
        self.key = key

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.maxsize = capacity
        self.map = dict() #should be a map of the key and the node for the value
        self.head = None
        self.tail = None

        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        cache_map = self.map
        cache_node = cache_map.get(key)
        if self.head == cache_node:
            return cache_node.value
        if cache_node != None:
            if self.tail != cache_node:
                nxt = cache_node.next
                if nxt.prev != None:
                    nxt.prev = cache_node.prev
            elif self.tail == cache_node:
                self.tail = cache_node.prev
            prev = cache_node.prev
            if prev.next != None:
                prev.next = cache_node.next
            head = self.head
            head.prev = cache_node            
            cache_node.next = head
            cache_node.prev = None
            self.head = cache_node

            return cache_node.value

        return -1
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        cache_map = self.map
        cache_item = Node(key, value)
        if self.head == None:
            self.head = cache_item
            self.tail = cache_item
        else:
            if len(cache_map) == self.maxsize:
                tail = self.tail
                cache_map.pop(tail.key)
                self.tail = tail.prev

            cache_item.next = self.head
            head = self.head
            head.prev = cache_item
            self.head = cache_item

        cache_map[key] = cache_item
        print(cache_item)
        print(cache_item.value)
        print(cache_item.next)
        print(cache_item.prev)
        
        pass

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))     # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(6))
print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
