"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string.

Create a HashTable class, with the following functions:

store() - a function that takes a string as input, and stores it into the hash table.
lookup() - a function that checks if a string is already available in the hash table. If yes, return the hash value, else return -1.
calculate_hash_value() - a helper function to calculate a hash value of a given string.

"""

class HashMap:
    def __init__(self, initail_size=1000):
        self.bucket_array = [None for _ in range(initial_size)]

    def store(self, word):
        lookup = self.lookup(word)
        if lookup == -1: #not there already
            hv = self.calculate_hash_value(word)
            self.bucket_array[hv] = [word]
        else:
            self.bucket_array[lookup].append(word)

    def lookup(self,word):
        idx = self.calculate_hash_value(word)

        if idx < len(self.bucket_array) and self.bucket_array[idx] == word:
            return idx
        else:
            return -1
    
    def calculate_hash_value(self, word):
        hash_key = (ord(word[0]) * 100) + ord(word[1])
        return hash_key


#Setup

hash_table = HashTable()

# Test calculate_hash_value
print(hash_table.calculate_hash_value('UDACITY'))   # should be 8568

# Test Lookup edge case
print(hash_table.lookup('UDACITY')) # should be -1

# Test store
hash_table.store('UDACITY')
print(hash_table.lookup('UDACITY')) # should be 8568

# Test store edge case
hash_table.store('UDACIOUS')
print(hash_table.lookup('UDACIOUS'))    # should be 8568
