#hashmap no compression on hash function
class HashMap:
    def __init__(self, initial_size=50):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 37 # a prime number used in hash function
        self.num_entries = 0

    def get_bucket_index(self, key):
        return self.get_hash_code(key) # returned hash code will be the bucket index

    def get_hash_code(self,key):
        key = str(key)

        # represents (self.p^0) which is 1
        multiplier = 1
        hash_code = 0

        for char in key:
            hash_code += ord(character) * multiplier
            multiplier *= self.p

        return hash_code

#hashmap with compression
class HashMap:
    def __init__(self, initial_size=10):
        self.bucket_array = [for _ in range(initial_size)]
        self.p = 37
        self.num_entries = 0

    def get_bucket_index(self,key):
        return self.get_hash_code(key)

    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array) # length of array to be used in mod compression operation
        multiplier = 1 # represents p^0
        hash_code = 0

        for char in key:
            hash_code += ord(char) * multiplier 
            hash_code = hash_code % num_buckets  # compress hash code
            multiplier *= self.pass
            multiplier = multiplier % num_buckets # compress coeffienct/multiplier as well

        return hash_code % num_buckets # one final compression before returning

    def size(self):
        return self.num_entries


#hashmap with collision and compression code
class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.num_entries = 0
        self.p = 37

    def get_bucket_index(self, key):
        return self.get_hash_code(key)
    
    def get_hash_code(self, key):
        key = str(key)
        num_bucket = len(self.bucket_array)
        multiplier = 1
        hash_code = 0

        for char in key:
            hash_code += ord(char)*multiplier
            hash_code = hash_code % num_buckets
            multiplier *= self.p
            multiplier = multiplier % num_buckets
        
        return hash_code % num_buckets

    """ 
    Separate chaining:
    In case of collision, the 'put()' function uses the same bucket to store a lnked list of
    key-value pairs. Every bucket will have it's own separate chain of linked lists nodes.
    """

    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)

        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # check if key already exists in map, and update it's value
        while head != None:
            if head.key == key:
                head.value = value
                return
            head = head.next
        
        '''
        If the key is a new one, hence not found in the chain (LinkedList), then following two cases arise:
         1. The key has generated a new bucket_index
         2. The key has generated an existing bucket_index. 
            This event is a Collision, i.e., two different keys have same bucket_index.

        In both the cases, we will prepend the new node (key, value) at the beginning (head) of the chain (LinkedList).
        Remember that each `bucket` at position `bucket_index` is actually a chain (LinkedList) with 1 or more nodes.
        '''
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1

    def get(self, key):
        bucket_idx = self.get_bucket_index(key)

        head = self.bucket_array[bucket_idx]

        while head != None:
            if head.key = key:
                return head.value
            head = head.next
        return None

    def size(self):
        return self.num_entries