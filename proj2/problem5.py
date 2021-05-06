""" timestamp examples from python do not include how to remove seconds and microseconds. found example on stackoverflow: https://stackoverflow.com/questions/3183707/stripping-off-the-seconds-in-datetime-python/3183720 """

import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash=None):
      self.timestamp = self.__createTimeStamp(timestamp)
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.__calc_hash(timestamp,data)
      self.prev = None
      self.next = None


    def __createTimeStamp(self, currentTime):
        now_time = currentTime.replace(second=0, microsecond=0)
        return now_time

    def __calc_hash(self, timestamp, data):
      sha = hashlib.sha256()
      hash_str = data.encode('utf-8')
      hash_str += str(timestamp).encode('utf-8')
      sha.update(hash_str)

      return sha.hexdigest()
    

class BlockChain:
    def __init__(self, block=None):
        self.first = None
        self.last = None

    def addBlock(self, blockdata):
        head = self.first
        tail = self.last

        if head == None:
            new_block = Block(datetime.now(), blockdata)
            self.first = new_block
            self.last = new_block
        else:
            new_block = Block(datetime.now(), blockdata, tail.hash)
            tail.next = new_block
            new_block.prev = tail
            self.last = new_block
    
    def append(self, block):
        head = self.first
        tail = self.last

        if head == None:
            self.first = block
            self.last = block
        else:
            tail.next = block
            block.prev = tail
            block.previous_hash = tail.hash
            self.tail = block

        

data_to_hash = "This is the data to hash"
startBlock = Block(datetime.now(),data_to_hash, 0)
"Hash me please"

print(startBlock.hash)

chain1 = BlockChain()
chain1.append(startBlock)
print(chain1)
print(chain1.first)
chain1.addBlock("Hash me please")
print(chain1.last)